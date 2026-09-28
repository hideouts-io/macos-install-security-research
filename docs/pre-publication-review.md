---
layout: default
title: Pre-publication review
---

# Pre-publication review

[Home](../README.md) · [Readiness](repository-readiness.md) · [License](licensing-review.md)

This is a local pre-push review of the build-25G83 research snapshot. It does not approve publication or assert that the entire installer dataset is semantically audited.

The recommended publication layout is a standalone `hideouts-io/macos-install-security-research` repository, followed by a short link from `hideouts-io/Apple-Infrastructure-Research`. The latter currently has an MIT license and a networking/cloud-log focus; keeping this CC BY 4.0 investigation separate avoids mixing license scopes and gives the partial-audit status its own landing page.

## READY

- The original 100 finding IDs and their claim, evidence, and limit fields remain in the byte-identical public CSV copy. Every grouped record has a source location and a relevant analysis link. The [source narrative map](source-coverage.md) assigns all 37 substantive sections of the retained publication draft to public pages.
- The local repository validator checks IDs, grouped records, source crosswalk, authored links, anchors, public file types, privacy markers, measurement arithmetic, and public checksums. A separate verifier checks retained source hashes and CSV copies. The rendered-site validator checks built HTML navigation, fragments, and image assets.
- GitHub Pages' `github-pages` dependency set builds locally with Ruby 3.4. The root README renders as the Jekyll homepage; eleven SVG diagrams render with their Mermaid sources retained. The CI workflow runs validation and a site build without deployment.
- The public set contains derived tables, hashes, bounded analysis, and diagrams. It excludes Apple binaries, original disk images, full decoder output, host logs, raw NVRAM, protected files, and the private evidence tree.
- The owner selected [CC BY 4.0](../LICENSE) for original material. The [scope note](licensing-review.md) excludes any claim to relicense Apple or other third-party work.

## PARTIAL

- Stage 6F.7 is still partial: 147,253 registered objects, 72 bounded semantic paths, 147,181 pending, and zero whole-object closures. The [audit status](audit-status.md) gives the exact next trace. Static reachability does not establish execution, authorization, a persistent NVRAM change, firmware flashing, or compromise.
- Source-document hashes and three CSV copies were checked against the retained local audit, but readers without the private original evidence cannot reproduce every reverse-engineering result from the public repository alone.
- At this local pre-push checkpoint, GitHub-hosted Pages and the GitHub Actions workflow had not run. Local build and rendered checks are complete for the configured project path; later hosted results must be checked on GitHub.
- The external-reference probe returned 70 HTTP 200 responses and one HTTP 403 for Microchip's PM40100 product page. The latter is a server denial to this client, not a confirmed dead link; the page is indexed by search. No confirmed 404s remained after three malformed parenthesized Markdown URLs were repaired.

## REQUIRES DECISION

- The owner has requested publication as an explicitly partial snapshot. Confirm the GitHub repository location: the recommended standalone name is `hideouts-io/macos-install-security-research`. If the name differs, update `_config.yml`'s `baseurl` and rerun the rendered-site validator first.
- Review the most consequential security interpretations and third-party attributions against the privately retained evidence before authorizing a public push.

## BLOCKERS

No additional technical blocker was found in the local build, authored links, public-file boundary, or checksum validation. The exact repository location is the remaining publication-routing decision.

## OPTIONAL IMPROVEMENTS

- Run the prepared workflow on GitHub after the first authorized push and verify the real Pages URL after Pages is explicitly enabled.
- Add more publication-safe per-finding raw-byte excerpts where rights and privacy permit, and extend the private Stage 6F.7 investigation without weakening the present evidence boundaries.
