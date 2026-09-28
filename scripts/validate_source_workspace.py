"""Verify the public draft against its retained, private audit source."""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path


class SourceValidationError(Exception):
    """A retained source file differs from the declared audit snapshot."""


def main(repository_argument: str, source_argument: str) -> None:
    """Check source document hashes and byte-identical public CSV copies."""
    repository: Path = Path(repository_argument).resolve()
    source: Path = Path(source_argument).resolve()
    provenance: object = json.loads((repository / "evidence/publication-provenance.json").read_text())
    if not isinstance(provenance, dict) or not isinstance(provenance.get("source_publication_sha256"), dict):
        raise SourceValidationError("publication-provenance.json lacks source_publication_sha256")
    source_hashes: dict[str, str] = provenance["source_publication_sha256"]
    for relative, expected in source_hashes.items():
        if not isinstance(relative, str) or not isinstance(expected, str) or len(expected) != 64:
            raise SourceValidationError(f"invalid source hash entry: {relative}")
        target: Path = (source / relative).resolve()
        if not target.is_relative_to(source) or not target.is_file():
            raise SourceValidationError(f"missing retained source document: {relative}")
        actual: str = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            raise SourceValidationError(f"source SHA-256 mismatch: {relative}: expected {expected}; measured {actual}")
    csv_pairs: tuple[tuple[str, str], ...] = (
        ("tables/findings.csv", "publication/FINDINGS.csv"),
        ("tables/efi-converter-branches.csv", "publication/EFI_CONVERTER_BRANCHES.csv"),
        ("tables/firmware-helpers.csv", "publication/FIRMWARE_HELPERS.csv"),
    )
    for public_relative, source_relative in csv_pairs:
        if (repository / public_relative).read_bytes() != (source / source_relative).read_bytes():
            raise SourceValidationError(f"CSV differs from retained source: {public_relative} versus {source_relative}")
    with (repository / "tables/finding-provenance.csv").open(newline="") as file:
        locations: list[dict[str, str]] = list(csv.DictReader(file))
    for record in locations:
        relative, separator, line_text = record["source_audit_location"].rpartition(":")
        if not separator or not line_text.isdigit():
            raise SourceValidationError(f"invalid source location for {record['id']}")
        document: Path = (source / relative).resolve()
        if not document.is_relative_to(source) or not document.is_file():
            raise SourceValidationError(f"missing finding source document for {record['id']}: {relative}")
        lines: list[str] = document.read_text(errors="replace").splitlines()
        line_number: int = int(line_text)
        if line_number < 1 or line_number > len(lines):
            raise SourceValidationError(f"source line out of range for {record['id']}: {relative}:{line_number}")
        if record["source_match"] == "explicit ID in source narrative" and record["id"] not in lines[line_number - 1]:
            raise SourceValidationError(f"source ID absent at declared line: {record['id']} in {relative}:{line_number}")
        if record["source_match"] == "relevant source section; ID absent from narrative" and not lines[line_number - 1].startswith(("## ", "### ")):
            raise SourceValidationError(f"section-context line is not a heading: {record['id']} in {relative}:{line_number}")
    print(json.dumps({"status": "passed", "source_hashes_verified": len(source_hashes), "byte_identical_csv_copies": len(csv_pairs), "finding_source_locations_verified": len(locations)}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SourceValidationError("usage: python3 scripts/validate_source_workspace.py REPOSITORY_ROOT SOURCE_AUDIT_ROOT")
    main(sys.argv[1], sys.argv[2])
