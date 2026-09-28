---
layout: default
title: Reverse-engineering map and reproducibility bounds
---

# Reverse-engineering map and reproducibility bounds

[Home](../README.md) · [Methods](methodology.md) · [Evidence](../evidence/README.md)

Analysis used symbol tables, Mach-O fileset structure, code-signature metadata, imports, chained fixups, original-byte-checked disassembly, strings with offsets, Objective-C selectors, launch configuration, and cross-artifact consumers. A function name or string was treated as a lead. The published claims depend on a checked branch, binding, data structure, or measured content. The full instruction streams remain in private evidence because they include copied Apple code and machine-specific data.

| Artifact or code family | Exact scope reached | Detailed page |
| --- | --- | --- |
| `ramrod`, `libramrod.dylib`, patch plugin | Sealing call binding, arguments, root-hash validation, selected errors and skip control | [RAMDisk/ramrod](ramdisk-ramrod.md) |
| `softwareupdated`, `UpdateBrainLibrary` | 27-command and seven-command tables, selected entitlement gates, writer/reader, receiver and context guards | [Installer workflow](installer-workflow.md) |
| `remoted`, RemoteServiceDiscovery, Security/CTK/AKS | Selected service policy, TLS, attestation, identity token and signing routes | [USB/services](usb-and-services.md) |
| Restore libraries and PFX | URL/TLS/FDR/AP-ticket gates, PFX staging and IOKit selector routes | [Restore](restore-network.md), [PFX](firmware-personalization.md) |
| PSFFlasher, MultiUpdater, `bless`, FirmwareUpdateLauncher | Input selection, PCI mailbox, EFI boot handoff, result/error and helper mappings | [Flashers/updaters](firmware-flashers.md) |
| Intel `BootKernelExtensions.kc` | 204-member fileset indexed; selected `AppleEFINVRAM`, `AppleEFIRuntime`, `AppleACPIPlatform`, sandbox and AMFI functions decoded | [Stage 6F.7](nvram-efi-paths.md), [sandbox](sandbox-policy.md), [AMFI](amfi-entitlements.md) |
| EFI/Option ROMs and Image4 | Bounded PE signature, wrapper, certificate-role, payload-region and cache representation checks | [Firmware](firmware-catalog.md), [Secure Boot](secure-boot.md) |

For Stage 6F.7 the x86_64 KC is **67,584,000 bytes**, SHA-256 `c80161fa3065883753fc285339281361a8469cbb6fb27653c88e2a22eb4807a4`. Its 204 fileset entries were indexed, not all analyzed. The published [EFI branch table](../tables/efi-converter-branches.csv) records 22 typed-node branches with required/optional fields, widths and node bytes. The [helper table](../tables/firmware-helpers.csv) records 11 Mach-O helper paths and 15 EFI flasher paths, but a located/signed path is not proof of invocation.

Selected original-byte-checked ranges include `AppleEFINVRAM::verifyPermission` at `0xffffff800195f221`, EFI path conversion at `0xffffff8001486574` and typed-array converter at `0xffffff80014866a0..0xffffff8001488c94`, registry builder at `0xffffff80014890b2..0xffffff800148ae65`, `AppleEFIRuntime::callEFIRuntime` at `0xffffff800195a1f8`, and the EFI indirect call at `0xffffff80002ea041`. Sandbox operation `0x76` maps to `nvram-set`; the current continuation begins at `_sb_evaluate_internal` `0xffffff8003034156`. These are **artifact-specific virtual addresses** and must not be transplanted to another KC/build.

The retained analysis cross-checked selected decoded ranges against original KC bytes and original chained pointer links. Disassembly still has limitations: whole-section decoders may cross padding or misidentify function starts, and inferred Objective-C receivers can be wrong without register/callsite proof. The [reproduction guide](reproduction.md) identifies checks possible with legally obtained matching artifacts. The [findings index](findings-index.md) retains per-finding claims and limits.
