"""Check local links, image assets, and fragment targets in a Jekyll build."""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class SiteValidationError(Exception):
    """A rendered site link or asset is missing."""


class PageParser(HTMLParser):
    """Collect rendered IDs and navigation targets."""

    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.images: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values: dict[str, str | None] = dict(attrs)
        identifier: str | None = values.get("id")
        if identifier is not None:
            self.ids.add(identifier)
        if tag == "a" and values.get("href") is not None:
            self.links.append(str(values["href"]))
        if tag == "img" and values.get("src") is not None:
            self.images.append(str(values["src"]))


def parse_page(path: Path) -> PageParser:
    """Parse one generated HTML page."""
    parser: PageParser = PageParser()
    parser.feed(path.read_text())
    return parser


def local_target(site: Path, source: Path, url: str, baseurl: str) -> tuple[Path, str] | None:
    """Resolve one site-local URL and fragment beneath the output directory."""
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or url.startswith(("mailto:", "tel:", "javascript:")):
        return None
    path_text: str = unquote(parsed.path)
    if path_text.startswith("/"):
        if path_text != baseurl and not path_text.startswith(baseurl + "/"):
            raise SiteValidationError(f"link lacks configured baseurl: {source}: {url}")
        relative: str = path_text[len(baseurl):].lstrip("/")
        target: Path = site / relative
    elif path_text:
        target = source.parent / path_text
    else:
        target = source
    if target.is_dir():
        target /= "index.html"
    target = target.resolve()
    if not target.is_relative_to(site):
        raise SiteValidationError(f"link escapes built site: {source}: {url}")
    return target, unquote(parsed.fragment)


def main(site_argument: str, baseurl: str) -> None:
    """Validate every generated HTML page without external network requests."""
    site: Path = Path(site_argument).resolve()
    if not site.is_dir() or not (site / "index.html").is_file():
        raise SiteValidationError(f"missing Jekyll build at {site}")
    pages: dict[Path, PageParser] = {path.resolve(): parse_page(path) for path in site.rglob("*.html")}
    counts: dict[str, int] = {"html_pages": len(pages), "local_links": 0, "anchors": 0, "images": 0}
    for source, parsed in pages.items():
        for url, is_image in [(url, False) for url in parsed.links] + [(url, True) for url in parsed.images]:
            resolved = local_target(site, source, url, baseurl)
            if resolved is None:
                continue
            target, fragment = resolved
            if not target.is_file():
                raise SiteValidationError(f"missing rendered target: {source}: {url}")
            counts["images" if is_image else "local_links"] += 1
            if fragment:
                if target not in pages or fragment not in pages[target].ids:
                    raise SiteValidationError(f"missing rendered anchor: {source}: {url}")
                counts["anchors"] += 1
    print(json.dumps({"status": "passed", **counts}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SiteValidationError("usage: python3 scripts/validate_rendered_site.py SITE_ROOT BASEURL")
    main(sys.argv[1], sys.argv[2])
