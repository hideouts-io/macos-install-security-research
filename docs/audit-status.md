---
layout: default
title: "Current audit status and remaining work"
---

# Current audit status and remaining work

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

**Current checkpoint, September 30, 2026:** Stage 6F.7 is **partial**; Stage 6F.6 is the last completed major pass. The register contains 147,253 objects, 85 bounded paths (43 detailed and 42 other bounded), 147,168 pending, eight separately bounded embedded components, and zero whole-object closures. The publication ledger contains 100 findings. The [coverage page](coverage.md) defines these terms.

<a id="exact-next-investigative-action"></a>
## Exact next investigative action

Trace the `AppleEFINVRAM` `+0xe0/+0xe8` path-property producers and `flattenPathProperties` stale-tail/append-error routes. The matching Intel cache routine establishes a conditional `NoCacheGuids` input and three built-in GUIDs; its [ordinary driver-local write gate](nvram-efi-paths.md#nocacheguids-ordinary-write-gate-and-producer-limit) is bounded to root privilege success or the NVRAM write entitlement. A readable-file search found no concrete writer, runtime value or effective authorization. A [matching Intel hibernation call chain](nvram-efi-paths.md#a-hibernation-consumer-of-the-registry-derived-path) identifies one registry-derived EFI path consumer and a conditional `boot-image` NVRAM handoff; MBR fallback use and firmware acceptance remain unobserved. The matching ARM cache's 781 program prebuilt-loader sets and 117,753 bind targets add no Brain/trust-cache path-option bind, while 69 binds to other Bootability exports identify ten static client paths. No path-value sender, accepted BootabilityService peer, successful mount or actual framework choice is observed. A standalone ARM kernel collection for AMFI selector-2 analysis is absent from the seven retained inventories. The separate operation-118 NVRAM question remains conditional: its real caller profile, active policy, resync request and firmware-error reachability are unknown.

<a id="ranked-review-checkpoint"></a>
## Ranked review checkpoint

Seven bounded review passes revisited the highest-value open questions without changing any finding severity. A byte-checked NVRAM modifier trace narrowed its direct status writes but did not establish an accepted caller or FW-021 runtime impact. An Apple-signed Intel `usbcupdater` independently constructs the helper dictionary keys and `efi-apple-payload%u-data` form consumed by the launcher; the PSF-specific `psfupdater` is still absent from the enumerated paths. A retained entitlement census identified candidate Apple update clients, but no observed `DoNotSeal` sender or runtime `Update.plist` permissions. Packaged remoted/SSH declarations and USB-mux policy do not establish an accepted remote or USB session. Five paired trust caches have equal parsed entries but distinct Image4 container digests; active loader choice and SSV/LocalPolicy enforcement remain unmeasured. BootabilityBrain entry points and operation-queue construction now have a bounded trace; `apfs_sealvolume` and the arm64e `efiupdater` remain high-priority unreviewed objects. The earlier 76-path count included the Intel BaseSystem `nvram` command, BootabilityBrain and arm64e BootabilityService; the current count is 85 bounded paths as stated above.

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
| Firmware semantics | PFX/PSF layout/CRC, PCI mailbox, PSF inputs/error paths, launcher-to-bless/MultiUpdater handoff and one USB-C helper producer bounded | PSF-specific helper and launcher authority, actual loader/device trust, signed-message/device keys and inner firmware; remaining families |
| SSV / kernel / cryptex | Image properties and selected code examined | Full relevant seal/policy path and embedded kernel/cache components |
| Services / USB | 477 launch-directory plists parsed; 19 socket groups and 16 remote-service declarations classified; selected local guards, policy producers, AKS/APFS gates and USB policy reviewed | Trace transport identity, description provenance, backend verification and target selection, complete policy composition and ARM paths; resolve deployment and protected-file gaps |
| Identity token and certificate-query consumer | Token dispatch/object lookup and null-result-string TLS callback traced | Operation-block callers, local/remote backend rights, adverse reply producer, endpoint access, cache-hit authority and accepted transport; bounded Stage5T complete |
| Restore network and FDR trust | URL/TLS-option producers, selected digest gates, ticket exceptions, client challenge and selected Image4 backend traced | Resolve cross-binary option authority, required ticket/certificate constraints, conditional RSA reachability and PFX user-client/device validation; other dynamic/cache references remain |
| Historical events | No corroborated execution timeline | Bounded acquisition of relevant staging, installer, boot and update logs |
| Publication | Partial CC BY 4.0 snapshot, 100 finding records, and GitHub Pages site published; validation passed at the publication checkpoint | Validate and publish later evidence-backed revisions without implying completion |

An exhaustive inventory cannot establish when ramrod ran, whether firmware was flashed, which USB profile was active, who connected, or whether a skip path was used. Those questions require corroborating runtime evidence. No live experiment has been performed to force a sealing skip or test a firmware update.

The current bounded continuation checks the Intel `nvram` assignment parser (353 original-byte instructions, 23 independent anchors) and specializes the compiled platform rule for the corrected resync name (12 name misses; 28 unknown-filter paths to an **intermediate** terminal value). Final process-profile/MAC/approval state and any historical request remain unknown. BootabilityBrain's original and copy have matching corresponding bytes; selected entry/controller ranges (725 original-byte instructions, 20 independently corroborated named calls) show operation-queue construction, not completed boot-policy changes. Full-bundle `codesign` reports an obsolete omit-rule envelope on both copies; code-only verification passes with resources expressly unverified. The runner, XPC route, `bputil`, Startup Disk helper client paths and `mount_apfs` request chain are bounded; actual framework selection, accepted peer, effective mount authorization and LocalPolicy effects remain open. See [NVRAM authority](nvram-efi-paths.md#resync-parser-platform-specialization) and [boot trust](secure-boot.md#bootabilitybrain-bounded-trace).
