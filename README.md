# macOS Install Security Research

> **PARTIAL RESEARCH SNAPSHOT — build 25G83.** This repository publishes completed bounded findings while Stage 6F.7 and the wider object-by-object audit remain unfinished. It does not certify an installed Mac, firmware state, or historical execution. [Current coverage and next step](docs/audit-status.md).

**Installer, recovery RAMDisk, firmware, EFI, and platform-security forensics for macOS 26.6.2 build 25G83.** Research snapshot: September 30, 2026.

The research began with a retained `macOS Install Data` staging tree. It compares that tree with the matching Apple distribution, reconstructs update and recovery images, and traces selected privileged paths from launch configuration through update services, ramrod, firmware helpers, EFI device paths, NVRAM, and trust checks. It also records what the collection cannot prove. The [audit overview](docs/audit-overview.md) gives the concise assessment; the pages below contain the evidence and limits.

The partial snapshot is available as a [GitHub Pages research site](https://hideouts-io.github.io/macos-install-security-research/). The site and repository publish derived findings, not the private source evidence.

> **Current boundary:** 147,253 inventory objects are registered across seven scopes. Eighty-five paths have bounded semantic review, 147,168 remain pending, and **zero whole objects have been declared completely reverse engineered**. Stage 6F.7 is partial. Same-build Bootability client, Startup Disk helper, and BootabilityBrain-to-`mount_apfs` request paths are statically bounded alongside the NVRAM resync route. No accepted resync or BootabilityService request, Brain/trust-cache path override, successful mount, final authorization or runtime boot-policy effect is established. The inventory is extensive; the semantic audit is not complete.

**Latest static bound:** The matching ARM dyld cache contains 781 program prebuilt-loader sets with 117,753 bind targets. Sixty-nine bind to Bootability exports across ten program paths; none binds to the Brain or trust-cache path-option constants. This narrows one optimized-linking route, without identifying a path-value sender or a runtime service decision. See [boot trust](docs/secure-boot.md#bootability-dispatch-and-xpc-service-continuation).

**Intel EFI-path continuation:** A same-build hibernation call chain requests a registry-derived EFI device path and offers its returned data as the `boot-image` NVRAM property. The path-construction result is checked; the later property setter's Boolean result is not propagated by its local helper. This is [a bounded static workflow](docs/nvram-efi-paths.md#a-hibernation-consumer-of-the-registry-derived-path), not evidence of a failed write or observed resume.

**NVRAM cache continuation:** The matching driver constructs its immediate-write GUID list from a conditional `NoCacheGuids` firmware value and three built-in GUIDs. This [static input and cache-selection trace](docs/nvram-efi-paths.md#nvram-deletion-internal-writes-and-the-userspace-boundary) does not establish the value's actual contents, writer authority or a permission bypass.

**NVRAM policy correction:** A previously described forced sandbox fallback has selector `0x100000000` and conditionally writes low status `1`, rather than leaving it zero. This corrects a static branch interpretation; whether a real caller took that branch remains unknown. See [sandbox policy and NVRAM authorization](docs/sandbox-policy.md).

## Read the research

| Start here | What it contains |
| --- | --- |
| [Documentation map](docs/index.md) | All subsystem pages and reading paths |
| [Findings index](docs/findings-index.md) | All 100 stable finding IDs, status, evidence level, and linked records |
| [Architecture](docs/architecture.md) | Source, images, update brain, RAMDisk, ramrod, and firmware relationships |
| [Evidence and provenance](evidence/README.md) | Public measurements, source-document hashes, excluded raw evidence |
| [Methodology](docs/methodology.md) | Acquisition, static analysis, claim classes, and evidence boundaries |
| [Reproduction](docs/reproduction.md) | Read-only checks, exact-build assumptions, and local validation |
| [Audit status](docs/audit-status.md) | Coverage, current Stage 6F.7 handoff, and incomplete work |
| [Open questions](docs/open-questions.md) | The unresolved question register |
| [References](docs/references.md) | Apple and third-party sources with their proper evidentiary role |

### Subsystem pages

- [Artifact provenance and exact Apple comparison](docs/artifact-provenance.md) · [inventory and images](docs/inventory-images.md)
- [RAMDisk and ramrod](docs/ramdisk-ramrod.md) · [installer/update-brain workflow](docs/installer-workflow.md) · [sealed system volume](docs/sealed-system-volume.md)
- [USB, launch services, remote identity, and TLS](docs/usb-and-services.md) · [mobile-device components](docs/mobile-device-components.md) · [restore networking and FDR](docs/restore-network.md)
- [Firmware catalog and Option ROMs](docs/firmware-catalog.md) · [PFX personalization](docs/firmware-personalization.md) · [PSF, flashers, bless, and MultiUpdater](docs/firmware-flashers.md)
- [Stage 6F.7 NVRAM and EFI paths](docs/nvram-efi-paths.md) · [sandbox policy](docs/sandbox-policy.md) · [AMFI and entitlements](docs/amfi-entitlements.md) · [APFS and Device Tree paths](docs/apfs-device-tree.md)
- [Code signing and kernel collections](docs/code-signing-kernel.md) · [Secure Boot, Image4, and trust caches](docs/secure-boot.md) · [reverse-engineering map](docs/reverse-engineering.md)
- [OpenCore assessment](docs/opencore.md) · [resolved anomalies](docs/corrections.md) · [limitations](docs/limitations.md)

## What the evidence establishes

The retained update files with exact Apple reference counterparts match: **1,186 regular files and three symlinks**. A separately matched installer-integrity file brings exact official-byte coverage to **1,187 of 1,191 original regular files**. Four presentation/index files lack exact counterparts and remain outside that claim. All 1,191 original regular-file hashes matched the readable working copy at acquisition. See [provenance](docs/artifact-provenance.md) and the [public measurements](evidence/measurements.json).

Reconstruction and read-only inspection cover the Intel Software Update RAMDisk, AppleDiagnostics, ARM and Intel BaseSystems, Intel Preboot, and an Intel system cryptex. Selected code-page, Image4, trust-cache, and EFI signature checks have passed with their stated scopes. These checks do not authenticate every downstream policy decision or prove any component ran. The [image inventory](docs/inventory-images.md), [signing analysis](docs/code-signing-kernel.md), and [Secure Boot page](docs/secure-boot.md) separate those layers.

The RAMDisk contains a configured ramrod launch path and a bounded sealing call chain. The official-reference update brain can serialize a `DoNotSeal` option into `skip-sealing`; the investigated command gates and callers do **not** establish that an unauthorized caller could set it or that the option was historically used. Firmware staging, `bless`, MultiUpdater, kernel EFI-path conversion, and NVRAM writes likewise form a static request chain with distinct authorization and firmware-acceptance boundaries. See [ramrod](docs/ramdisk-ramrod.md), [installer workflow](docs/installer-workflow.md), and [Stage 6F.7](docs/nvram-efi-paths.md).

The update includes USB configuration and remote-service components, including a proxy launch declaration whose executable is absent in the examined RAMDisk. One declared control socket lacks an explicit loopback node. Neither observation establishes an active listener, external reachability, a USB session, or compromise. [USB and services](docs/usb-and-services.md) traces the configuration and selected authentication paths.

**OpenCore is a third-party bootloader, not a normal Apple update component.** Its source was used only as an external format cross-check. This dataset has not established OpenCore installation or execution on the examined Mac. [Read the full OpenCore assessment](docs/opencore.md).

## How to interpret a finding

The [100 finding records](docs/findings-index.md) preserve their original IDs, evidence, limits, and follow-up questions; the [source crosswalk](tables/finding-provenance.csv) identifies a retained audit location for each. **VERIFIED** means a measured or byte-checked fact within its stated artifact and path. **SUPPORTED INFERENCE** explains what those facts imply without turning an unobserved step into an event. **HYPOTHESIS** is a testable explanation. **UNKNOWN** marks missing evidence. A code path, string, entitlement, signature, or launch declaration is not proof of runtime authorization, execution, network traffic, firmware mutation, bypass, exploitability, or compromise.

Raw Apple binaries, full disassembly, machine-specific evidence, and private working files are not in this repository. Public material includes the [finding ledger](tables/findings.csv), [firmware-helper table](tables/firmware-helpers.csv), [EFI converter branch table](tables/efi-converter-branches.csv), small derived measurements, diagrams, and safe validation scripts. The [evidence index](evidence/README.md) explains the retention boundary. This repository does not certify the installed system or firmware as clean.

## Reproduce and review

Run `python3 scripts/validate_repository.py .` to check the finding IDs, local links, anchors, checksums, and public-file boundary. `python3 scripts/verify_artifact.py PATH EXPECTED_SHA256` verifies a locally obtained artifact without uploading it. The [reproduction guide](docs/reproduction.md) includes the local Jekyll build and rendered-link check and identifies which research results require privately held source artifacts or hardware.

The original research and scripts are licensed under [CC BY 4.0](LICENSE) to the extent stated in the [license scope](docs/licensing-review.md); cited third-party material is not relicensed. The [readiness report](docs/repository-readiness.md) and [publication review](docs/pre-publication-review.md) record the validation and evidence limits.
