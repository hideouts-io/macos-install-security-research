---
layout: default
title: "Current audit status and remaining work"
---

# Current audit status and remaining work

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

**Current checkpoint, September 27, 2026:** Stage 6F.7 is **partial**; Stage 6F.6 is the last finalized bounded pass. The register contains 147,253 objects, 72 bounded paths (30 detailed and 42 other bounded), 147,181 pending, eight separately bounded embedded components, and zero whole-object closures. The publication ledger contains 100 findings. The [coverage page](coverage.md) defines these terms.

<a id="exact-next-investigative-action"></a>
## Exact next investigative action

Continue `_sb_evaluate_internal` in the matching Intel `BootKernelExtensions.kc` from `0xffffff8003034156` through the indirect process-profile `_eval_op` call, the second `_action_combine` at `0xffffff80030342b0`, and the approval modifier branch through `0xffffff8003034364`. Bound final low-status semantics without inventing a caller profile or runtime decision. The twelve `nvram-set` FSA records, 39 normalized name conditions, initial terminal combination, and static MAC registration route are already bounded and should not be repeated. Then return to caller-context and remaining converter/helper dependencies. See [sandbox policy](sandbox-policy.md) and [Stage 6F.7](nvram-efi-paths.md).

<a id="remaining-work"></a>
## Remaining work

| Workstream | Current state | Next work |
| --- | --- | --- |
| Official comparison | Completed for corresponding retained update paths | Maintain explicit four-file reference gap and explain history only with evidence |
| Full path coverage | All 147,253 recorded objects reconciled to seven catalog path sets | Complete per-path semantic dispositions; extend metadata capture and curate public tables |
| Ramrod / brain | Bounded traces through 4I; receiver, selected guards, local saved flags and handle registration traced | Finish failed-context lifecycle, handle ownership/expiry, endpoint forwarding, client origin and DoNotSeal authorization |
| Verification state | Early flag timing and two direct false-result paths traced | Stored-context flag provenance, callback exclusions and failed-context persistence/retry |
| Firmware trust | Signatures and several measurement formats resolved | Runtime root/cache selection, full hardware policy, rollback and personalization |
| Product.efi | Wrapper and runtime dependency traced | Cipher/padding/trailer and plaintext only if suitable evidence becomes available |
| Firmware semantics | PFX/PSF layout/CRC, PCI mailbox, PSF inputs/error paths and generic launcher-to-bless staging traced | Exact bless/MultiUpdater handoff, helper authority, signed-message/device keys and inner firmware; remaining families |
| SSV / kernel / cryptex | Image properties and selected code examined | Full relevant seal/policy path and embedded kernel/cache components |
| Services / USB | 477 launch-directory plists parsed; 19 socket groups and 16 remote-service declarations classified; selected local guards, policy producers, AKS/APFS gates and USB policy reviewed | Trace transport identity, description provenance, backend verification and target selection, complete policy composition and ARM paths; resolve deployment and protected-file gaps |
| Identity token and certificate-query consumer | Token dispatch/object lookup and null-result-string TLS callback traced | Operation-block callers, local/remote backend rights, adverse reply producer, endpoint access, cache-hit authority and accepted transport; bounded Stage5T complete |
| Restore network and FDR trust | URL/TLS-option producers, selected digest gates, ticket exceptions, client challenge and selected Image4 backend traced | Resolve cross-binary option authority, required ticket/certificate constraints, conditional RSA reachability and PFX user-client/device validation; other dynamic/cache references remain |
| Historical events | No corroborated execution timeline | Bounded acquisition of relevant staging, installer, boot and update logs |
| Publication | Structured local repository, 100 finding records, public tables and safe validation scripts assembled | Complete user review, license choice, spot checks and optional local Pages render before any push |

An exhaustive inventory cannot establish when ramrod ran, whether firmware was flashed, which USB profile was active, who connected, or whether a skip path was used. Those questions require corroborating runtime evidence. No live experiment has been performed to force a sealing skip or test a firmware update.
