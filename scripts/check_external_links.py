"""Record bounded HTTP status checks for Markdown reference URLs."""

from __future__ import annotations

import concurrent.futures
import json
import subprocess
import sys
from pathlib import Path


class ExternalLinkError(Exception):
    """External-link check could not be run."""


def page_urls(content: str) -> set[str]:
    """Extract Markdown HTTP destinations, including balanced URL parentheses."""
    urls: set[str] = set()
    for scheme in ("](https://", "](http://"):
        start: int = 0
        while (position := content.find(scheme, start)) >= 0:
            begin: int = position + 2
            depth: int = 1
            end: int = begin
            while end < len(content) and depth:
                if content[end] == "(":
                    depth += 1
                elif content[end] == ")":
                    depth -= 1
                end += 1
            if depth != 0:
                raise ExternalLinkError(f"unbalanced Markdown URL beginning at character {position}")
            urls.add(content[begin:end - 1])
            start = end
    return urls


def markdown_urls(root: Path) -> list[str]:
    """Collect unique absolute HTTP links from authored Markdown."""
    pages: list[Path] = [root / "README.md", *sorted((root / "docs").glob("*.md")), *sorted((root / "findings").glob("*.md")), *sorted((root / "diagrams").glob("*.md")), *sorted((root / "evidence").glob("*.md"))]
    return sorted({url for page in pages for url in page_urls(page.read_text())})


def request_status(url: str, method: str) -> tuple[int, str, str]:
    """Use bounded curl retries; return HTTP code and final URL host/path."""
    command: list[str] = ["curl", "--silent", "--show-error", "--location", "--max-time", "15", "--retry", "2", "--retry-delay", "1", "--output", "/dev/null", "--write-out", "%{http_code}\t%{url_effective}"]
    if method == "HEAD":
        command.append("--head")
    elif method != "GET":
        raise ExternalLinkError(f"unsupported HTTP method {method}")
    command.append(url)
    result: subprocess.CompletedProcess[str] = subprocess.run(command, capture_output=True, text=True, check=False)
    status_text, separator, final_url = result.stdout.partition("\t")
    if not separator or not status_text.isdigit():
        raise ExternalLinkError(f"curl output invalid for {url}: exit={result.returncode}, stderr={result.stderr.strip()}")
    return int(status_text), final_url.strip(), result.stderr.strip()


def inspect_url(url: str) -> dict[str, str | int]:
    """Check a URL with HEAD, then GET when HEAD cannot establish reachability."""
    head_status, head_final, head_warning = request_status(url, "HEAD")
    if 200 <= head_status < 400:
        return {"url": url, "method": "HEAD", "http_status": head_status, "final_url": head_final, "warning": head_warning}
    get_status, get_final, get_warning = request_status(url, "GET")
    warning: str = f"HEAD {head_status}: {head_warning}; GET: {get_warning}".strip()
    return {"url": url, "method": "GET after HEAD", "http_status": get_status, "final_url": get_final, "warning": warning}


def main(root_argument: str, output_argument: str) -> None:
    """Write a reproducible, bounded link-check record."""
    root: Path = Path(root_argument).resolve()
    output: Path = Path(output_argument).resolve()
    urls: list[str] = markdown_urls(root)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        results: list[dict[str, str | int]] = list(executor.map(inspect_url, urls))
    output.write_text(json.dumps({"checked_urls": len(urls), "results": results}, indent=2) + "\n")
    codes: dict[int, int] = {}
    for row in results:
        code: int = int(row["http_status"])
        codes[code] = codes.get(code, 0) + 1
    print(json.dumps({"checked_urls": len(urls), "http_status_counts": codes}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ExternalLinkError("usage: python3 scripts/check_external_links.py REPOSITORY_ROOT OUTPUT_JSON")
    main(sys.argv[1], sys.argv[2])
