---
layout: default
title: Local repository readiness review
---

# Local repository readiness review

[Home](../README.md) · [Documentation](index.md) · [Pre-publication review](pre-publication-review.md) · [Evidence](../evidence/README.md)

**Repository:** `macos-install-security-research`  
**Local review:** September 28, 2026  
**Git state at local review:** initialized on `main`, uncommitted; no remote, push, Pages deployment, release, or tag.  
**Research state, September 29 update:** Stage 6F.7 remains **partial**. The 147,253-object register has 76 bounded semantic paths, 147,177 pending paths, and zero whole-object closures. The local-review and first-publication checks below remain dated records; validate each subsequent revision independently.

**Published outcome:** [standalone repository](https://github.com/hideouts-io/macos-install-security-research) and [GitHub Pages site](https://hideouts-io.github.io/macos-install-security-research/) are public. The first corrected publication commit, `0da15ca`, passed [GitHub Actions validation](https://github.com/hideouts-io/macos-install-security-research/actions/runs/36400645630) and the [Pages deployment](https://github.com/hideouts-io/macos-install-security-research/actions/runs/36400821744). The hosted homepage, audit-status page, one finding page, one SVG diagram, and `LICENSE` each returned HTTP 200. The research coverage remains partial despite successful publication checks.

| Check | Local result |
| --- | --- |
| Public repository files | 91, excluding Git and ignored build/dependency/cache directories |
| Markdown pages | 46; 37 substantive source narrative sections assigned by the [source map](source-coverage.md) |
| Findings | 100 unique IDs; claim/evidence/limit text checked against the byte-identical source CSV; 100 source locations, including 72 explicit-ID narrative locations and 28 labeled section-context locations |
| Diagrams | 11 Mermaid sources and 11 rendered SVGs; 11 image references resolve in the built site |
| Public derived data | Four CSVs and three JSONs; one SHA-256 manifest with 30 verified entries for diagrams and public data |
| Validation utilities | Six: repository validator, retained-source verifier, rendered-site validator, external-reference probe, artifact SHA-256 verifier, diagram renderer |
| Authored links | 804 Markdown links parsed by the repository validator; local targets and supported anchors resolve |
| Rendered Pages links | 46 HTML pages; 688 local links, 158 fragments, and 11 images resolved under `/macos-install-security-research` |
| External URLs | 74 unique authored HTTP(S) URLs checked; 73 HTTP 200, one Microchip HTTP 403, zero confirmed broken URLs, zero final-URL redirects, zero plain HTTP links |
| Jekyll | `github-pages` 232 / Jekyll 3.10.0 built successfully with Ruby 3.4 and repository-local gems; local `jekyll serve` responded at the configured project path |
| Visual spot-check | Headless Chrome displayed the homepage and architecture SVG at desktop width and the findings index at mobile width; Cayman tables scroll within their container |
| Source integrity | Nine retained source-document SHA-256 values match the original audit workspace; three public CSVs remain byte-identical copies |
| Privacy and distribution | No local home-directory path, local username, private-key header, raw Apple binary, installer image, or private-evidence directory in the public file set. Twenty textual `private-evidence/` provenance pointers in two pages are intentional and do not promise public downloads. |
| License | [CC BY 4.0](../LICENSE) selected for original material; third-party scope documented in the [license note](licensing-review.md) |
| CI and Pages | Both succeeded on publication commit `0da15ca`; future commits require fresh validation |

The three initially malformed Apple documentation links with literal parentheses were repaired and rechecked. The remaining Microchip PM40100 URL returned HTTP 403 to the command-line probe; a search-indexed version of the same official product page was visible, so this is recorded as client-denied reachability rather than a dead reference. The external-link result is in [external-links.json](../evidence/external-links.json). External status can change after this snapshot.

The original pre-push Jekyll build used a placeholder repository name because no remote existed then. The published repository name now matches `_config.yml`'s `baseurl`; hosted Pages and the live page checks corroborate the local build. The early missing-HEAD message came from the intentionally commit-free preparation checkout and did not recur after the first commit.

The original 43-GB private evidence tree, Apple binaries and packages, reconstructed images, firmware and kernel collections, full decoder output, host identifiers/logs, raw NVRAM, and protected records remain outside this repository. The public checksums establish integrity of this draft's derived files; the source hashes establish which retained report versions informed it. Neither independently verifies original Apple signatures or historical execution for a reader who lacks the originals.

The [pre-publication review](pre-publication-review.md) separates locally validated items, unfinished research, owner decisions, and optional improvements. No commit or upload had been made at this local validation checkpoint; later GitHub state must be checked at the repository itself.
