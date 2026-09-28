"""Check an explicitly supplied local file against a published SHA-256 digest."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


class ArtifactError(Exception):
    """The local artifact cannot be verified."""


def sha256_file(path: Path) -> str:
    """Hash a file without loading it into memory or executing it."""
    digest = hashlib.sha256()
    with path.open("rb") as source:
        while chunk := source.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def main(path_argument: str, expected_argument: str) -> None:
    """Require an exact hexadecimal digest match for one regular file."""
    path: Path = Path(path_argument)
    expected: str = expected_argument.lower()
    if not path.is_file():
        raise ArtifactError(f"artifact is not a regular file: {path}")
    if len(expected) != 64 or any(character not in "0123456789abcdef" for character in expected):
        raise ArtifactError("expected SHA-256 must be exactly 64 hexadecimal characters")
    actual: str = sha256_file(path)
    if actual != expected:
        raise ArtifactError(f"SHA-256 mismatch for {path}: expected {expected}; measured {actual}")
    print(json.dumps({"path": str(path), "sha256": actual, "status": "match"}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ArtifactError("usage: python3 scripts/verify_artifact.py PATH EXPECTED_SHA256")
    main(sys.argv[1], sys.argv[2])
