"""Validate the public documentation graph and publication boundary."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


class ValidationError(Exception):
    """A public repository invariant failed."""


def heading_slug(heading: str) -> str:
    """Return the GitHub-style anchor used for ordinary Markdown headings."""
    without_markup: str = re.sub(r"<[^>]*>", "", heading).lower()
    without_punctuation: str = re.sub(r"[^\w\- ]", "", without_markup)
    return re.sub(r"\s+", "-", without_punctuation.strip())


def markdown_anchors(content: str) -> set[str]:
    """Collect explicit anchors and ordinary heading anchors."""
    anchors: set[str] = set(re.findall(r'<a id="([^"]+)"></a>', content))
    for heading in re.findall(r"^#{1,6} (.+)$", content, re.MULTILINE):
        anchors.add(heading_slug(heading))
    return anchors


def validate_link(root: Path, source: Path, target_text: str) -> None:
    """Require a relative Markdown target and its fragment to exist."""
    if target_text.startswith(("https://", "http://", "mailto:")):
        return
    path_text: str
    fragment: str
    path_text, separator, fragment = target_text.partition("#")
    relative: Path = Path(unquote(path_text)) if path_text else source.name
    target: Path = (source.parent / relative).resolve()
    try:
        target.relative_to(root)
    except ValueError as error:
        raise ValidationError(f"link escapes repository: {source}: {target_text}") from error
    if not target.is_file():
        raise ValidationError(f"missing local link target: {source}: {target_text}")
    if separator and target.suffix.lower() == ".md":
        anchors: set[str] = markdown_anchors(target.read_text())
        if unquote(fragment) not in anchors:
            raise ValidationError(f"missing anchor: {source}: {target_text}")


def validate_markdown(root: Path) -> tuple[int, int]:
    """Check every local Markdown link and code-fence balance."""
    ignored: set[str] = {".git", ".bundle", "node_modules", "_site", ".jekyll-cache"}
    pages: list[Path] = sorted(page for page in root.rglob("*.md") if not any(part in ignored for part in page.relative_to(root).parts))
    checked_links: int = 0
    for page in pages:
        content: str = page.read_text()
        if content.count("```") % 2 != 0:
            raise ValidationError(f"unbalanced code fence: {page}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
            validate_link(root, page, target)
            checked_links += 1
    return len(pages), checked_links


def validate_findings(root: Path) -> int:
    """Require one record, index row and grouped-page anchor per finding ID."""
    with (root / "tables/findings.csv").open(newline="") as source:
        records: list[dict[str, str]] = list(csv.DictReader(source))
    ids: list[str] = [record["id"] for record in records]
    if len(ids) != 100 or len(ids) != len(set(ids)):
        raise ValidationError(f"finding ledger must have 100 unique IDs; found {len(ids)} rows")
    index: str = (root / "docs/findings-index.md").read_text()
    indexed: list[str] = re.findall(r"^\| \[([A-Z]+-\d{3})\]", index, re.MULTILINE)
    if sorted(ids) != sorted(indexed):
        raise ValidationError("finding index IDs do not match the CSV ledger")
    for item_id in ids:
        prefix: str = item_id.split("-", 1)[0].lower()
        grouped: Path = root / "findings" / f"{prefix}.md"
        if item_id.lower() not in markdown_anchors(grouped.read_text()):
            raise ValidationError(f"finding has no grouped-page anchor: {item_id}")
    with (root / "tables/finding-provenance.csv").open(newline="") as source:
        provenance: list[dict[str, str]] = list(csv.DictReader(source))
    if sorted(row["id"] for row in provenance) != sorted(ids):
        raise ValidationError("finding provenance IDs do not match the CSV ledger")
    for record in records:
        item_id: str = record["id"]
        page: Path = root / "findings" / f"{item_id.split('-', 1)[0].lower()}.md"
        content: str = page.read_text()
        for field in ("claim", "evidence", "limit", "status", "observation", "interpretation", "security_relevance", "confidence", "follow_up"):
            if record[field] not in content:
                raise ValidationError(f"finding {item_id} {field} differs from grouped page")
    for row in provenance:
        if not re.fullmatch(r"(?:publication/README|REPORT|STAGE[2-5]_[A-Z]+)\.md:[1-9][0-9]*", row["source_audit_location"]):
            raise ValidationError(f"invalid source location for {row['id']}")
        if row["source_match"] not in {"explicit ID in source narrative", "relevant source section; ID absent from narrative"}:
            raise ValidationError(f"invalid source match class for {row['id']}")
        validate_link(root, root / "README.md", row["public_analysis"])
        if row["public_corrob"]:
            validate_link(root, root / "README.md", row["public_corrob"])
    return len(ids)


def validate_public_boundary(root: Path) -> int:
    """Reject obvious private paths, secrets and Apple-binary file types."""
    forbidden_suffixes: set[str] = {".dmg", ".ipsw", ".pkg", ".aea", ".kc", ".im4p", ".im4m", ".efi", ".dylib"}
    allowed_suffixes: set[str] = {".md", ".csv", ".json", ".py", ".yml", ".mmd", ".sha256", ".svg", ".lock", ".sh"}
    forbidden_text: tuple[str, ...] = ("/Us" + "ers/", "mac" + "bookpro", "-----BEGIN " + "PRIVATE KEY-----", "-----BEGIN " + "OPENSSH PRIVATE KEY-----")
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or any(part in {".git", "__pycache__", "_site", ".jekyll-cache", ".bundle", "node_modules"} for part in path.relative_to(root).parts):
            continue
        if any(part in {"private-evidence", "raw-evidence"} for part in path.relative_to(root).parts):
            raise ValidationError(f"private evidence directory present: {path}")
        if path.suffix.lower() in forbidden_suffixes:
            raise ValidationError(f"proprietary or raw artifact type present: {path}")
        if path.suffix.lower() not in allowed_suffixes and path.name not in {".gitignore", ".gitattributes", "Gemfile", "LICENSE"}:
            raise ValidationError(f"unreviewed public file type: {path}")
        if path.stat().st_size > 2_000_000:
            raise ValidationError(f"unexpectedly large public file: {path}")
        if path.suffix.lower() in {".md", ".csv", ".json", ".py", ".yml", ".mmd", ".lock", ".sh", ".svg"} or path.name == "Gemfile":
            content: str = path.read_text()
            for marker in forbidden_text:
                if marker in content:
                    raise ValidationError(f"private marker {marker!r} in {path}")
        files.append(path)
    return len(files)


def validate_measurements(root: Path) -> None:
    """Check arithmetic and declared active-stage boundary."""
    measurements: object = json.loads((root / "evidence/measurements.json").read_text())
    if not isinstance(measurements, dict):
        raise ValidationError("measurements.json must contain an object")
    coverage: object = measurements.get("coverage")
    if not isinstance(coverage, dict):
        raise ValidationError("measurements.json coverage must contain an object")
    numeric_keys: tuple[str, ...] = ("inventory_objects", "bounded_semantic_paths", "semantic_paths_pending", "whole_objects_closed")
    for key in numeric_keys:
        value: object = coverage.get(key)
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValidationError(f"measurements.json coverage.{key} must be an integer")
    objects: int = coverage["inventory_objects"]
    bounded: int = coverage["bounded_semantic_paths"]
    pending: int = coverage["semantic_paths_pending"]
    if bounded + pending != objects:
        raise ValidationError("coverage counts do not reconcile")
    if coverage["whole_objects_closed"] != 0 or coverage.get("active_stage") != "6F.7":
        raise ValidationError("active-stage or whole-object boundary changed")


def validate_checksums(root: Path) -> int:
    """Verify every SHA-256 entry in the public evidence manifest."""
    manifest: Path = root / "evidence/checksums.sha256"
    entries: int = 0
    for line in manifest.read_text().splitlines():
        expected, separator, relative = line.partition("  ")
        if not separator or len(expected) != 64:
            raise ValidationError(f"malformed public checksum entry: {line}")
        target: Path = (root / relative).resolve()
        if not target.is_file() or not target.is_relative_to(root):
            raise ValidationError(f"missing or escaping checksum target: {relative}")
        actual: str = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            raise ValidationError(f"public checksum mismatch: {relative}: expected {expected}; measured {actual}")
        entries += 1
    required: set[str] = {str(path.relative_to(root)) for folder in ("diagrams", "evidence", "tables") for path in (root / folder).iterdir() if path.is_file() and path.name not in {"README.md", "checksums.sha256"}}
    listed: set[str] = {line.partition("  ")[2] for line in manifest.read_text().splitlines()}
    if listed != required:
        raise ValidationError(f"checksum coverage differs from public data files: missing={sorted(required - listed)} extra={sorted(listed - required)}")
    return entries


def main(root_argument: str) -> None:
    """Run local publication checks and print structured counts."""
    root: Path = Path(root_argument).resolve()
    if not (root / ".git").is_dir():
        raise ValidationError(f"not an initialized local Git repository: {root}")
    pages, links = validate_markdown(root)
    findings: int = validate_findings(root)
    files: int = validate_public_boundary(root)
    validate_measurements(root)
    checksums: int = validate_checksums(root)
    print(json.dumps({"status": "passed", "public_files": files, "markdown_pages": pages, "markdown_links_parsed": links, "finding_ids": findings, "checksums_verified": checksums, "external_url_reachability_checked": False}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValidationError("usage: python3 scripts/validate_repository.py REPOSITORY_ROOT")
    main(sys.argv[1])
