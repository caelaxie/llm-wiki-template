#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import heapq
import json
import re
import sys
from collections import deque
from dataclasses import dataclass
from pathlib import Path


CONTENT_DIRS = ("sources", "entities", "concepts", "syntheses")
WIKILINK_RE = re.compile(r"^\[\[([^\]]+)\]\]$")
KEY_RE = re.compile(r"^([A-Za-z0-9_]+):(?:\s+(.*))?$")
LIST_RE = re.compile(r"^\s*-\s+(.*)$")


class RefreshError(Exception):
    """Raised when the wiki does not satisfy refresh invariants."""


@dataclass
class MarkdownPage:
    path: Path
    rel_path: str
    slug: str
    page_type: str
    frontmatter: dict[str, object]
    body: str


def parse_scalar(raw: str) -> str:
    value = raw.strip()
    if not value:
        return ""
    if value[0] == value[-1] == '"':
        return bytes(value[1:-1], "utf-8").decode("unicode_escape")
    return value


def quote_scalar(value: object) -> str:
    escaped = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, object], str]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise RefreshError(f"{path}: missing YAML frontmatter")

    end_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break
    if end_index is None:
        raise RefreshError(f"{path}: unterminated YAML frontmatter")

    frontmatter_lines = lines[1:end_index]
    body = "".join(lines[end_index + 1 :])
    frontmatter: dict[str, object] = {}
    index = 0
    while index < len(frontmatter_lines):
        raw_line = frontmatter_lines[index].rstrip("\n")
        if not raw_line.strip():
            index += 1
            continue

        key_match = KEY_RE.match(raw_line)
        if not key_match:
            raise RefreshError(f"{path}: unsupported frontmatter line: {raw_line}")

        key = key_match.group(1)
        inline_value = key_match.group(2)
        if inline_value is None:
            inline_value = ""

        if inline_value == "":
            items: list[str] = []
            index += 1
            while index < len(frontmatter_lines):
                list_line = frontmatter_lines[index].rstrip("\n")
                if not list_line.strip():
                    index += 1
                    continue
                list_match = LIST_RE.match(list_line)
                if not list_match:
                    break
                items.append(parse_scalar(list_match.group(1)))
                index += 1
            frontmatter[key] = items
            continue

        frontmatter[key] = parse_scalar(inline_value)
        index += 1

    return frontmatter, body


def serialize_page(page: MarkdownPage) -> str:
    frontmatter = page.frontmatter
    ordered_keys: list[str] = []
    for key in ("title", "type", "sources"):
        if key in frontmatter:
            ordered_keys.append(key)
    if page.page_type == "source" and "raw_sha256" in frontmatter:
        ordered_keys.append("raw_sha256")
    for key in ("created_at", "updated_at"):
        if key in frontmatter and key not in ordered_keys:
            ordered_keys.append(key)
    for key in frontmatter:
        if key not in ordered_keys:
            ordered_keys.append(key)

    lines = ["---\n"]
    for key in ordered_keys:
        value = frontmatter[key]
        if isinstance(value, list):
            lines.append(f"{key}:\n")
            for item in value:
                lines.append(f"  - {quote_scalar(item)}\n")
        else:
            lines.append(f"{key}: {quote_scalar(value)}\n")
    lines.append("---\n")
    return "".join(lines) + page.body


def read_page(path: Path, root: Path) -> MarkdownPage:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text, path)
    slug = path.stem
    page_type = str(frontmatter.get("type", ""))
    rel_path = path.relative_to(root).as_posix()
    return MarkdownPage(path=path, rel_path=rel_path, slug=slug, page_type=page_type, frontmatter=frontmatter, body=body)


def discover_pages(root: Path) -> list[MarkdownPage]:
    pages: list[MarkdownPage] = []
    wiki_root = root / "wiki"
    for directory in CONTENT_DIRS:
        content_dir = wiki_root / directory
        if not content_dir.exists():
            continue
        for path in sorted(content_dir.glob("*.md")):
            if path.name == ".gitkeep":
                continue
            pages.append(read_page(path, root))
    return pages


def split_wikilink(link: str) -> str | None:
    match = WIKILINK_RE.match(link.strip())
    if not match:
        return None
    target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
    return target or None


def raw_target(link: str) -> str | None:
    target = split_wikilink(link)
    if target and target.startswith("raw/"):
        return target
    return None


def wiki_target(link: str) -> str | None:
    target = split_wikilink(link)
    if target and not target.startswith("raw/"):
        return target
    return None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ensure_list(path: str, key: str, value: object) -> list[str]:
    if not isinstance(value, list):
        raise RefreshError(f"{path}: `{key}` must be a YAML list")
    normalized: list[str] = []
    for item in value:
        normalized.append(str(item))
    return normalized


def validate_pages(
    pages: list[MarkdownPage], root: Path
) -> tuple[
    dict[str, MarkdownPage],
    dict[str, str],
    dict[str, str],
    dict[str, set[str]],
    dict[str, set[str]],
]:
    slug_map: dict[str, MarkdownPage] = {}
    raw_refs: dict[str, str] = {}
    raw_paths: dict[str, str] = {}
    dependencies: dict[str, set[str]] = {}
    reverse_dependencies: dict[str, set[str]] = {}

    for page in pages:
        if page.slug in slug_map:
            raise RefreshError(
                f"duplicate slug `{page.slug}` at {slug_map[page.slug].rel_path} and {page.rel_path}"
            )
        slug_map[page.slug] = page

    for page in pages:
        dependencies[page.slug] = set()
        reverse_dependencies.setdefault(page.slug, set())

        if "raw_sha256" in page.frontmatter and page.page_type != "source":
            raise RefreshError(f"{page.rel_path}: `raw_sha256` is only valid on source pages")

        sources = ensure_list(page.rel_path, "sources", page.frontmatter.get("sources", []))
        page.frontmatter["sources"] = sources

        raw_links = [target for target in (raw_target(item) for item in sources) if target]
        if page.page_type == "source":
            if len(raw_links) != 1:
                raise RefreshError(
                    f"{page.rel_path}: source pages must contain exactly one canonical `[[raw/...]]` reference"
                )
            raw_ref = raw_links[0]
            raw_path = root / raw_ref
            if not raw_path.is_file():
                raise RefreshError(f"{page.rel_path}: referenced raw file does not exist: {raw_ref}")
            raw_refs[page.slug] = raw_ref
            raw_paths[page.slug] = raw_path.as_posix()

        for item in sources:
            target = wiki_target(item)
            if not target:
                continue
            if target not in slug_map:
                raise RefreshError(
                    f"{page.rel_path}: `sources` references missing wiki page `[[{target}]]`"
                )
            dependencies[page.slug].add(target)
            reverse_dependencies.setdefault(target, set()).add(page.slug)

    return slug_map, raw_refs, raw_paths, dependencies, reverse_dependencies


def write_page_if_changed(page: MarkdownPage) -> bool:
    new_text = serialize_page(page)
    old_text = page.path.read_text(encoding="utf-8")
    if new_text == old_text:
        return False
    page.path.write_text(new_text, encoding="utf-8")
    return True


def set_raw_sha256(page: MarkdownPage, digest: str) -> None:
    reordered: dict[str, object] = {}
    inserted = False
    for key, value in page.frontmatter.items():
        if key == "raw_sha256":
            continue
        reordered[key] = value
        if key == "sources":
            reordered["raw_sha256"] = digest
            inserted = True
    if not inserted:
        reordered["raw_sha256"] = digest
    page.frontmatter = reordered


def topo_sort(
    targets: set[str],
    dependencies: dict[str, set[str]],
    reverse_dependencies: dict[str, set[str]],
) -> list[str]:
    indegree = {
        slug: len([dep for dep in dependencies.get(slug, set()) if dep in targets])
        for slug in targets
    }
    ready = [slug for slug, count in indegree.items() if count == 0]
    heapq.heapify(ready)
    order: list[str] = []

    while ready:
        slug = heapq.heappop(ready)
        order.append(slug)
        for dependent in sorted(reverse_dependencies.get(slug, set())):
            if dependent not in indegree:
                continue
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                heapq.heappush(ready, dependent)

    if len(order) != len(targets):
        remaining = sorted(targets - set(order))
        raise RefreshError(
            "dependency cycle detected in `sources` frontmatter: " + ", ".join(remaining)
        )

    return order


def build_report(
    mode: str,
    root: Path,
    pages_by_slug: dict[str, MarkdownPage],
    dependencies: dict[str, set[str]],
    reverse_dependencies: dict[str, set[str]],
    roots: dict[str, list[str]],
    changed_files: list[dict[str, object]],
) -> dict[str, object]:
    if mode == "full-rebuild":
        targets = set(pages_by_slug)
    else:
        targets = set(roots)
        queue = deque(sorted(roots))
        while queue:
            slug = queue.popleft()
            for dependent in sorted(reverse_dependencies.get(slug, set())):
                if dependent in targets:
                    continue
                targets.add(dependent)
                queue.append(dependent)

    refresh_order = topo_sort(targets, dependencies, reverse_dependencies) if targets else []

    refresh_rows = []
    for slug in refresh_order:
        page = pages_by_slug[slug]
        if slug in roots:
            reasons = roots[slug]
        else:
            reasons = sorted(
                f"depends_on:{dep}"
                for dep in dependencies.get(slug, set())
                if dep in targets
            )
        refresh_rows.append(
            {
                "slug": slug,
                "type": page.page_type,
                "path": page.rel_path,
                "depends_on": sorted(dep for dep in dependencies.get(slug, set()) if dep in targets),
                "reasons": reasons,
            }
        )

    return {
        "mode": mode,
        "repo_root": root.as_posix(),
        "changed_raw_files": changed_files,
        "refresh_roots": [
            {
                "slug": slug,
                "path": pages_by_slug[slug].rel_path,
                "type": pages_by_slug[slug].page_type,
                "reasons": roots[slug],
            }
            for slug in sorted(roots)
        ],
        "refresh_order": refresh_rows,
    }


def run(root: Path, full_rebuild: bool) -> dict[str, object]:
    pages = discover_pages(root)
    slug_map, raw_refs, raw_paths, dependencies, reverse_dependencies = validate_pages(pages, root)

    mode = "full-rebuild" if full_rebuild else "changed-only"
    roots: dict[str, list[str]] = {}
    changed_files: list[dict[str, object]] = []

    for slug in sorted(raw_refs):
        page = slug_map[slug]
        old_digest = str(page.frontmatter.get("raw_sha256", "")).strip() or None
        new_digest = sha256_file(Path(raw_paths[slug]))

        reasons: list[str] = []
        if old_digest is None:
            reasons.append("missing_hash")
        elif old_digest != new_digest:
            reasons.append("hash_changed")
        if full_rebuild:
            reasons.append("full_rebuild")

        if old_digest != new_digest:
            set_raw_sha256(page, new_digest)
            write_page_if_changed(page)

        if old_digest != new_digest:
            changed_files.append(
                {
                    "raw_path": raw_refs[slug],
                    "source_slug": slug,
                    "source_path": page.rel_path,
                    "old_sha256": old_digest,
                    "new_sha256": new_digest,
                }
            )

        if reasons:
            roots[slug] = sorted(set(reasons))

    return build_report(mode, root, slug_map, dependencies, reverse_dependencies, roots, changed_files)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plan wiki page refresh work from raw-source drift."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root to scan. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--full-rebuild",
        action="store_true",
        help="Report the full wiki dependency graph regardless of hash drift.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    try:
        report = run(root=root, full_rebuild=args.full_rebuild)
    except RefreshError as exc:
        print(f"refresh failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
