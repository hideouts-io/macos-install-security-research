---
layout: default
title: "Reproduction and source evidence map"
---

# Reproduction and source evidence map

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

**Public-repository checks:** `python3 scripts/validate_repository.py .` verifies links, anchors, all 100 finding IDs, the publication boundary, and public checksums. `python3 scripts/verify_artifact.py PATH EXPECTED_SHA256` checks one reader-supplied file without executing it. The commands below that mention `analysis/tools` or `private-evidence` document the original audit workflow; those internal scripts and raw inputs are **not distributed** here. They cannot be run from this public repository alone. Use legally obtained, exact-build artifacts for independent reproduction.

An authorized holder of the retained source workspace can also run `python3 scripts/validate_source_workspace.py . SOURCE_AUDIT_ROOT` to check all declared source-document digests and the three byte-identical CSV copies. That path is supplied locally and is never uploaded or embedded in the public output.

### Local Pages preview

Use Ruby 3.4 and the checked-in `Gemfile.lock`. GitHub Pages' pinned dependency set did not resolve under Ruby 4.0 during the local review. Install gems into the repository and render with the published repository name:

```sh
bundle config set --local path .bundle/vendor
bundle install
python3 scripts/validate_repository.py .
PAGES_REPO_NWO=hideouts-io/macos-install-security-research bundle exec jekyll build --trace
python3 scripts/validate_rendered_site.py _site /macos-install-security-research
PAGES_REPO_NWO=hideouts-io/macos-install-security-research bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

The local preview URL is `http://127.0.0.1:4000/macos-install-security-research/`. The published [Pages site](https://hideouts-io.github.io/macos-install-security-research/) uses the same `baseurl`. If the repository is renamed, update `_config.yml` and rerun the rendered-link check. The workflow in `.github/workflows/validate.yml` builds and checks the site; branch-backed GitHub Pages performs the public deployment separately.

Eleven editable Mermaid sources are paired with checked-in SVGs, because GitHub Pages renders Mermaid code fences as code. To regenerate those SVGs, run `npm ci` with `PUPPETEER_SKIP_DOWNLOAD=1`, set `PUPPETEER_EXECUTABLE_PATH` to an existing Chrome or Chromium executable, and run `npm run render:diagrams`. Then update `evidence/checksums.sha256` and rerun the repository validator. The SVGs are publication assets; the `.mmd` files preserve the reviewable graph definitions.

<a id="reproduction-and-evidence-map"></a>
## Reproduction and evidence map

<a id="method"></a>
### Method

1. Inventory original and working-copy paths, kinds, metadata and hashes; compare symlinks without following them.
2. Identify exact product/build/target independently from Apple metadata.
3. Obtain the official package, verify reported package signature and integrity chunks, extract reference members without installation.
4. Stream and hash update ZIP members; classify exact matches, omitted official content and local exceptions.
5. Reconstruct replacement images into separate files, validate lengths/digests, mount read-only and catalog filesystems.
6. Separate ordinary Mach-O signing, resource verification, Image4, Apple EFI signatures, trust caches and device policy.
7. Trace call arguments, import bindings, metadata and branches; validate important bytes and format boundaries.
8. Record counterexamples, parser limits, derivatives and negative controls. Publish bounded conclusions.

<a id="read-only-inspection-examples"></a>
### Read-only inspection examples

These commands are examples for reference files acquired by the reader. The quoted paths are placeholders. They inspect files and do not launch the firmware or installer:

```sh
shasum -a 256 '/path/to/InstallAssistant.pkg'
pkgutil --check-signature '/path/to/InstallAssistant.pkg'
file '/path/to/UpdateBrainLibrary.dylib'
codesign --verify --strict --verbose=4 '/path/to/UpdateBrainLibrary.dylib'
otool -arch x86_64 -tvV '/path/to/UpdateBrainLibrary.dylib'
xcrun dyld_info -arch x86_64 -fixups '/path/to/UpdateBrainLibrary.dylib'
nm -arch x86_64 -m '/path/to/UpdateBrainLibrary.dylib'
```

For image examination, use a dedicated analysis mount root with read-only attachment and retain its attach plist. Determine detach identifiers from the current attachment, not a previous session. Reconstruction and firmware parsing need their format-specific validation, not a blanket “DMG verified” label.

<a id="private-audit-evidence-index"></a>
### Private audit evidence index

The names below identify retained local records. They are deliberately not broken repository links: the raw evidence and audit-specific scripts have **not** been included in this publication directory.

| Topic | Retained evidence / implementation |
| --- | --- |
| Inventory | `coverage.json`, seven catalog CSVs, original/copy hash ledgers |
| Official comparison | `official-zip-verification.json`, `staged-official-comparison.json`, `signature-failure-reconciliation.json`; compare_official.py / reconcile_stage2.py |
| Image reconstruction | Reconstruction outputs, chunk/size/digest checks, attach/verify/detach records |
| Executable integrity | binary-analysis.json, recovery-binary-analysis.json, CodeDirectory/CMS records |
| Firmware structures | firmware-analysis.json, ftab.json, UARP and DP855 measurement records |
| Ticket/root validation | im4m-signatures.json, certificate-signatures.json, root-extraction.json, bootability-signature.json |
| Certificate roles | image4-role-checks.json and summaries; stage3c_roles.py |
| Trust-cache reconciliation | architecture-counterparts.json, official-trust-caches.json, expanded-code-correlations.json; stage3d_trust_context.py |
| EFI / PCI | efi-signatures.json, efi-openssl-crosscheck.json, decompressed-roms.json, product-wrapper.json |
| Ramrod | Full disassemblies, fixups, metadata, gate/volume checks and numbered excerpts in stages 4A–4C |
| Recovery dispatch | producer-string-scan.json, dispatch-table.json; stage4d_dispatch.py |
| Brain producer | brain-provenance.json, producer-recheck.json; stage4e_producer.py |
| Brain authorization | brain-command-table.json, authorization-excerpts.txt; stage4f_dispatch.py |
| Receiver and verification | stage4g/stage4h symbol-aware listings, instruction JSON and trace-recheck.json; analysis/tools/trace_brain.py |
| Context and session lifecycle | stage4i symbol-aware listing, instruction JSON, loader register-reference queue and trace-recheck.json; analysis/tools/trace_context.py |
| Service authentication and policy | stage5c acquisitions, signing records, Intel byte-checked listings, artifact-review.json and public-reference provenance; analysis/tools/trace_service_guards.py |
| FileVault unlock gate | stage5d selector metadata, reviewed excerpts, function-start/LLDB evidence and trace-recheck.json; analysis/tools/trace_fvunlock.py |
| Remote-service policy | stage5e producer/caller metadata, RemoteServices declarations, reviewed excerpts and trace-recheck.json; analysis/tools/trace_remote_policy.py |
| TLS negotiation and callback | stage5f method map, selector metadata, refusal/callback excerpts and trace-recheck.json; analysis/tools/trace_remote_tls.py |
| Peer attestation and expiration | stage5g selector/excerpt records, embedded-roots.json, root self-signatures and pinned Apple source; analysis/tools/trace_remote_attestation.py |
| Required OIDs and chassis policy | stage5h required-oid-arrays.json, class-method map, policy/outer-branch excerpts and trace-recheck.json; analysis/tools/trace_remote_chassis.py |
| Identity matching and preferences | stage5i identity/parser/preferences excerpts, selector references, migration constants and host-scanner observations; analysis/tools/trace_remote_identity.py and probe_hex_scanner.swift |
| Backend TLS and identity lifecycle | stage5j resolver/dispatch/lifecycle excerpts, hardware-defaults.json, direct references and trace-recheck.json; analysis/tools/trace_remote_backend_policy.py |
| Identity generation and reload | stage5k key/OID constants, generator/reload/metadata excerpts, pinned Apple headers and trace-recheck.json; analysis/tools/trace_remote_generation.py |
| Identity reply and completion | stage5l local reply, token serialization, caller completion and OID handshake excerpts; analysis/tools/trace_remote_identity_callers.py |
| Later TLS and certificate queries | stage5m completion/certificate-query excerpts and framework attribution; analysis/tools/trace_remote_completion.py, scan_remote_consumers.py and capture_rsd_cache.py |
| Framework identity consumer | stage5n original symbols, byte checks, pointer pages, token attributes and client excerpts; analysis/tools/decode_rsd_cache.py, capture_rsd_symbols.py, capture_rsd_constants.py and trace_rsd_identity.py |
| Token-provider dispatch and query consumer | stage5o selected Security listings, data-in-code tables, slide-chain/string rechecks, RSD query/TLS excerpts and registered-token constant; analysis/tools/capture_cache_component.py, decode_cache_functions.py, capture_cache_references.py and trace_token_client.py |
| Concrete token provider selection | stage5p original class/selector/constants, locality gate and selected decode records; analysis/tools/trace_sep_provider.py |
| Configuration pass | stage5a per-scope plist JSONL, native-parser reconciliation, launch-service-map.json and read-only mount records; analysis/tools/index_plists.py |
| Restore network defaults and request options | stage6b byte-checked auth/FDR excerpts, original fixups/import proofs, observations and path reviews; analysis/tools/trace_restore_network.py |
| FDR object, ticket and callback policy | stage6c checked excerpts, raw dispatch/tag/block proofs, observations and bounded path review; analysis/tools/trace_fdr_trust.py |
| FDR ticket backend and input providers | stage6d acquired backend, attach/detach records, checked excerpts, policy/anchor/option proofs and observations; analysis/tools/trace_fdr_ticket.py and prove_fdr_ticket_policy.py |
| Restore transport and crypto dependencies | stage6e checked session/delegate/RSA excerpts, original bindings, SDK references, exact crypto acquisitions and strict signatures, object register and remaining checklist; analysis/tools/trace_ams_transport.py, trace_transport_crypto.py, prove_ams_transport.py and build_audit_register.py |
| Coverage ledger | 147,253 path rows in coverage-ledger/path-coverage.csv; metadata-field counts in summary.json; analysis/tools/coverage_ledger.py |

Scripts currently depend on the local evidence layout and, in some cases, audit-local Python 3.14/dependencies. They are not advertised here as a portable public toolkit. The public [finding ledger](../tables/findings.csv) gives stable identifiers and scope limitations for documented findings.

Disassembler output requires review: whole-section decoding can cross padding and misidentify function starts. Objective-C receiver comments may also overinterpret register state. Selected constants/selectors were resolved from original bytes and fixups; Stage 4B's 227 and Stage 4C's 174 references remained unchanged after the resolver was extended for observed UTF-16LE constants. Matching text dumps alone is not proof of correct disassembly.

The private master ledger tracks all 18 requested investigation phases, with separate unresolved-question and artifact maps. Saved inventories capture modification/change times and extended-attribute names; they do not contain creation-time, ACL or extended-attribute-value fields. `ctime` must not be relabeled as creation time. The new path queue records existing collection links and pending semantic reconciliation, not a claim that every path is fully reviewed.

Stage/report SHA-256 manifests are **current-state consistency manifests**. They are refreshed when reports change and are not immutable timestamped attestations. Original input hashes, provenance and named analysis derivatives preserve the relevant distinctions.
