#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "docs-main"
SOURCE_DIR = DOCS_ROOT / "reference" / "protobuf" / "packages"
OUTPUT_DIR = DOCS_ROOT / "reference" / "protocol" / "latest"
DOCS_JSON_PATH = DOCS_ROOT / "docs.json"
NAV_DROPDOWN = "API Reference"
PARENT_GROUP = "Ledger API"
PROTOBUF_GROUP = "Protobufs"
MARKDOWN_GROUP = "Latest Protocol Markdown"
CONTENTS_PATH = OUTPUT_DIR / "contents.md"
PROTOCOL_PAGE_ORDER = [
    "com-digitalasset-canton-protocol-v30",
    "com-digitalasset-canton-protocol-v31",
    "com-digitalasset-canton-participant-protocol-v30",
    "com-digitalasset-canton-synchronizer-protocol-v30",
]
TYPE_BLOCK_START_RE = re.compile(r"(?m)^<a id=\"[^\"]+\"></a>$")
SOURCE_LINE_RE = re.compile(r"- Source: \[([^\]]+)\]\(([^)]+)\)")
BLOCK_TITLE_RE = re.compile(r"^\*\*(Message|Enum|Service) `([^`]+)`\*\*$", re.MULTILINE)
TYPE_LINK_RE = re.compile(r"\((?P<path>[^)#]*)#(?P<anchor>type-[^)]+)\)")


@dataclass(frozen=True)
class SourceFileEntry:
    source_path: str
    source_url: str
    services: str
    messages: str
    enums: str
    slug: str
    output_path: Path
    output_ref: str


@dataclass(frozen=True)
class TypeBlock:
    anchor: str
    title: str
    source_path: str
    content: str


@dataclass
class PackageExport:
    slug: str
    title: str
    description: str
    source_page_ref: str
    source_files: list[SourceFileEntry]
    blocks_by_source: dict[str, list[TypeBlock]]


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("Expected YAML frontmatter")
    _, rest = text.split("---\n", 1)
    frontmatter, body = rest.split("\n---\n", 1)
    return frontmatter, body.lstrip("\n")


def frontmatter_value(frontmatter: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*\"?(.*?)\"?$", frontmatter, re.MULTILINE)
    if not match:
        raise ValueError(f"Missing frontmatter key: {key}")
    return match.group(1)


def page_ref(path: Path) -> str:
    relative = path.resolve().relative_to(DOCS_ROOT.resolve())
    return "/" + relative.with_suffix("").as_posix()


def docs_json_ref(path: Path) -> str:
    relative = path.resolve().relative_to(DOCS_ROOT.resolve())
    return relative.with_suffix("").as_posix()


def protocol_source_pages() -> list[Path]:
    pages = [path for path in SOURCE_DIR.glob("*protocol*.mdx") if path.is_file()]
    order = {slug: index for index, slug in enumerate(PROTOCOL_PAGE_ORDER)}
    return sorted(pages, key=lambda path: (order.get(path.stem, len(order)), path.stem))


def section_slug(source_path: str) -> str:
    return Path(source_path).stem.replace("_", "-")


def extract_section(body: str, heading: str, next_heading: str | None = None) -> str:
    marker = f"## {heading}\n"
    start = body.find(marker)
    if start == -1:
        raise ValueError(f"Missing section: {heading}")
    start += len(marker)
    if next_heading is None:
        return body[start:].strip()
    end_marker = f"## {next_heading}\n"
    end = body.find(end_marker, start)
    if end == -1:
        raise ValueError(f"Missing section boundary: {next_heading}")
    return body[start:end].strip()


def parse_source_files(body: str, *, package_slug: str) -> list[SourceFileEntry]:
    section = extract_section(body, "Source Files", "Type Reference")
    entries: list[SourceFileEntry] = []
    package_dir = OUTPUT_DIR / package_slug
    for raw_line in section.splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or line.startswith("| File") or line.startswith("| ---"):
            continue
        parts = [part.strip() for part in line.split("|")[1:-1]]
        if len(parts) != 5:
            continue
        source_path, services, messages, enums, source_cell = parts
        source_match = re.search(r"\(([^)]+)\)", source_cell)
        source_url = source_match.group(1) if source_match else ""
        slug = section_slug(source_path)
        output_path = package_dir / f"{slug}.md"
        entries.append(
            SourceFileEntry(
                source_path=source_path,
                source_url=source_url,
                services=services,
                messages=messages,
                enums=enums,
                slug=slug,
                output_path=output_path,
                output_ref=page_ref(output_path),
            )
        )
    if not entries:
        raise ValueError(f"No source files parsed for {package_slug}")
    return entries


def parse_type_blocks(body: str) -> list[TypeBlock]:
    section = extract_section(body, "Type Reference")
    starts = list(TYPE_BLOCK_START_RE.finditer(section))
    if not starts:
        return []
    blocks: list[TypeBlock] = []
    for index, match in enumerate(starts):
        start = match.start()
        end = starts[index + 1].start() if index + 1 < len(starts) else len(section)
        chunk = section[start:end].strip()
        anchor_match = re.search(r'^<a id="([^"]+)"></a>$', chunk, re.MULTILINE)
        source_match = SOURCE_LINE_RE.search(chunk)
        title_match = BLOCK_TITLE_RE.search(chunk)
        if not anchor_match or not source_match or not title_match:
            raise ValueError("Malformed type block in protocol protobuf page")
        blocks.append(
            TypeBlock(
                anchor=anchor_match.group(1),
                title=title_match.group(2),
                source_path=source_match.group(1),
                content=chunk,
            )
        )
    return blocks


def load_package_exports() -> list[PackageExport]:
    exports: list[PackageExport] = []
    for path in protocol_source_pages():
        frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
        source_files = parse_source_files(body, package_slug=path.stem)
        grouped_blocks: dict[str, list[TypeBlock]] = defaultdict(list)
        for block in parse_type_blocks(body):
            grouped_blocks[block.source_path].append(block)
        exports.append(
            PackageExport(
                slug=path.stem,
                title=frontmatter_value(frontmatter, "title"),
                description=frontmatter_value(frontmatter, "description"),
                source_page_ref=page_ref(path),
                source_files=source_files,
                blocks_by_source=dict(grouped_blocks),
            )
        )
    if not exports:
        raise ValueError("No protocol protobuf package pages found")
    return exports


def build_anchor_map(exports: Iterable[PackageExport]) -> dict[str, str]:
    anchor_map: dict[str, str] = {}
    for package_export in exports:
        file_map = {entry.source_path: entry.output_ref for entry in package_export.source_files}
        for source_path, blocks in package_export.blocks_by_source.items():
            output_ref = file_map.get(source_path)
            if output_ref is None:
                raise ValueError(f"Missing output mapping for {source_path}")
            for block in blocks:
                anchor_map[block.anchor] = output_ref
    return anchor_map


def rewrite_type_links(content: str, *, current_ref: str, anchor_map: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        anchor = match.group("anchor")
        output_ref = anchor_map.get(anchor)
        if output_ref is None:
            return match.group(0)
        if output_ref == current_ref and not match.group("path"):
            return f"(#{anchor})"
        return f"({output_ref}#{anchor})"

    return TYPE_LINK_RE.sub(replace, content)


def package_links(exports: list[PackageExport], *, current_slug: str | None = None) -> str:
    links: list[str] = []
    for package_export in exports:
        overview_ref = package_export.source_page_ref
        label = package_export.title
        if package_export.slug == current_slug:
            links.append(f"`{label}`")
        else:
            links.append(f"[{label}]({overview_ref})")
    return " | ".join(links)


def format_section_page(
    *,
    package_export: PackageExport,
    entry: SourceFileEntry,
    blocks: list[TypeBlock],
    anchor_map: dict[str, str],
    exports: list[PackageExport],
) -> str:
    related_sections = [
        f"[{candidate.source_path}]({candidate.output_ref})"
        for candidate in package_export.source_files
        if candidate.source_path != entry.source_path
    ]
    type_links = [f"- [{block.title}](#{block.anchor})" for block in blocks]
    rewritten_blocks = [
        rewrite_type_links(block.content, current_ref=entry.output_ref, anchor_map=anchor_map)
        for block in blocks
    ]
    if related_sections:
        related_lines = "\n".join(f"- {link}" for link in related_sections)
    else:
        related_lines = "- _No sibling sections in this package._"
    type_lines = "\n".join(type_links) if type_links else "- _No types exported from this source file._"
    source_link_line = f"[{entry.source_path}]({entry.source_url})" if entry.source_url else f"`{entry.source_path}`"
    return "\n".join(
        [
            "---",
            f'title: "{Path(entry.source_path).name}"',
            f'description: "Markdown extract for {package_export.title} / {entry.source_path}."',
            "---",
            "",
            f"# `{entry.source_path}`",
            "",
            "## Navigation",
            "",
            f"- [Protocol markdown contents]({page_ref(CONTENTS_PATH)})",
            f"- [Original protobuf package page]({package_export.source_page_ref})",
            f"- Package set: {package_links(exports, current_slug=package_export.slug)}",
            f"- Source file: {source_link_line}",
            "",
            "## Related sections in this package",
            "",
            related_lines,
            "",
            "## Types in this section",
            "",
            type_lines,
            "",
            "## Extracted reference",
            "",
            "\n\n".join(rewritten_blocks),
            "",
        ]
    )


def format_contents_page(exports: list[PackageExport]) -> str:
    lines = [
        "---",
        'title: "Latest Protocol Markdown"',
        'description: "Cross-linked Markdown export of the latest protocol protobuf reference sections."',
        "---",
        "",
        "# Latest Protocol Markdown",
        "",
        "This page extracts the latest checked-in protocol protobuf reference into Markdown section pages.",
        "",
        f"- [Original protobuf overview](/reference/protobuf/index)",
        "- Each section below links to a Markdown page generated from one protobuf source file.",
        "- The section pages keep type anchors and add cross-links between related protocol files.",
        "",
        "## Package contents",
        "",
    ]
    for package_export in exports:
        lines.extend(
            [
                f"### `{package_export.title}`",
                "",
                f"- [Original package page]({package_export.source_page_ref})",
                f"- Source files: `{len(package_export.source_files)}`",
                f"- Description: {package_export.description}",
                "",
            ]
        )
        for entry in package_export.source_files:
            block_count = len(package_export.blocks_by_source.get(entry.source_path, []))
            lines.append(
                f"- [{entry.source_path}]({entry.output_ref}) — {block_count} type{'s' if block_count != 1 else ''}"
            )
        lines.append("")
    return "\n".join(lines)


def write_markdown_exports(exports: list[PackageExport]) -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    anchor_map = build_anchor_map(exports)
    for package_export in exports:
        for entry in package_export.source_files:
            entry.output_path.parent.mkdir(parents=True, exist_ok=True)
            content = format_section_page(
                package_export=package_export,
                entry=entry,
                blocks=package_export.blocks_by_source.get(entry.source_path, []),
                anchor_map=anchor_map,
                exports=exports,
            )
            entry.output_path.write_text(content, encoding="utf-8")
    CONTENTS_PATH.write_text(format_contents_page(exports), encoding="utf-8")


def update_docs_navigation() -> None:
    docs = json.loads(DOCS_JSON_PATH.read_text(encoding="utf-8"))
    dropdowns = docs.get("navigation", {}).get("dropdowns")
    if not isinstance(dropdowns, list):
        raise ValueError(f"docs.json navigation.dropdowns must be a list: {DOCS_JSON_PATH}")
    dropdown = next(
        (item for item in dropdowns if isinstance(item, dict) and item.get("dropdown") == NAV_DROPDOWN),
        None,
    )
    if dropdown is None:
        raise ValueError(f"Dropdown not found: {NAV_DROPDOWN}")
    pages = dropdown.get("pages")
    if not isinstance(pages, list):
        raise ValueError(f"Dropdown pages must be a list: {NAV_DROPDOWN}")
    parent_group = next((item for item in pages if isinstance(item, dict) and item.get("group") == PARENT_GROUP), None)
    if parent_group is None:
        raise ValueError(f"Group not found: {PARENT_GROUP}")
    parent_pages = parent_group.get("pages")
    if not isinstance(parent_pages, list):
        raise ValueError(f"Group pages must be a list: {PARENT_GROUP}")
    protobuf_group = next((item for item in parent_pages if isinstance(item, dict) and item.get("group") == PROTOBUF_GROUP), None)
    if protobuf_group is None:
        raise ValueError(f"Group not found: {PROTOBUF_GROUP}")
    protobuf_pages = protobuf_group.get("pages")
    if not isinstance(protobuf_pages, list):
        raise ValueError(f"Group pages must be a list: {PROTOBUF_GROUP}")
    protobuf_group["pages"] = [
        item
        for item in protobuf_pages
        if not (isinstance(item, dict) and item.get("group") == MARKDOWN_GROUP)
    ]
    protobuf_group["pages"].append(
        {
            "group": MARKDOWN_GROUP,
            "pages": [docs_json_ref(CONTENTS_PATH)],
        }
    )
    DOCS_JSON_PATH.write_text(json.dumps(docs, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    exports = load_package_exports()
    write_markdown_exports(exports)
    update_docs_navigation()
    print(f"Wrote latest protocol markdown export to {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
