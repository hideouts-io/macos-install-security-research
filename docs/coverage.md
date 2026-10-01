---
layout: default
title: Coverage register
---

# Coverage register

[Home](../README.md) · [Findings](findings-index.md) · [Status](audit-status.md)

At the September 30, 2026 checkpoint, the audit register contains **147,253** objects across seven inventoried source/image scopes: **85** paths have bounded semantic records (**43** detailed, **42** other bounded), and **147,168** remain pending semantic reconciliation. Eight embedded components have separate bounded records. **Zero whole objects are closed.** These are coverage labels, not vulnerability or integrity scores.

The seven trees include **105,123 regular-file paths**. Repeated or hard-linked paths are not unique binary counts. Inventory enumeration and hashing are broader than instruction-level review. Stage 5A parsed 78,465 plists, and Stage 5B classified 19 launch socket groups, but these bulk passes do not make every plist or service semantically complete. The [inventory page](inventory-images.md) gives per-scope counts and image formats.

The 18-phase master checklist records work in progress on preservation/metadata, disk images, RAMDisk, ramrod, USB, firmware, Secure Boot, SSV, services, signatures, kernel/cryptex, network, provenance correlation, and independent validation. Bounded stage passes are documented; the whole investigation is **not complete**. The active continuation is [Stage 6F.7](nvram-efi-paths.md), with the [exact next static trace](audit-status.md#exact-next-investigative-action) recorded there.

| Coverage class | Meaning |
| --- | --- |
| Inventory observed | Path, type, and collected metadata are recorded; role may be inferred from packaging |
| Bounded path review | A named function, branch, configuration, or artifact relationship was examined with a stated limit |
| Embedded bounded review | Selected code inside a larger fileset/cache was examined; the enclosing object is not closed |
| Pending | No sufficient semantic disposition has been recorded yet |
| Whole-object closure | All relevant interfaces/dependencies reviewed to a declared scope; **none claimed here** |

The original master register and 12-field per-path queue remain in the private audit workspace because they contain host-specific raw evidence and extensive unreviewed paths. Public results are in the [finding index](findings-index.md), [tables](../tables/findings.csv), and [evidence index](../evidence/README.md).

## Eighteen-phase investigation checklist

Every phase remains **IN PROGRESS** at this snapshot; completed bounded passes do not close a phase. Evidence filenames in the final column refer to the retained private audit workspace unless a public page or table is linked elsewhere in this repository.

| Phase | Component | Status | Established coverage | Next gap | Evidence |
| --- | --- | --- | --- | --- | --- |
| 01 | Preservation and complete metadata inventory | IN PROGRESS | Seven tree inventories: 105,123 regular-file paths, no recorded enumeration/hash errors; original/copy and exact-reference comparisons retained. | Reconcile ACL/birth-time/xattr-value coverage; map every path to an explicit semantic-review disposition. | coverage.json; catalog/; STAGE2_COMPARISON.md |
| 02 | Disk images and filesystems | IN PROGRESS | RAMDisk, diagnostics, two BaseSystems, Intel Preboot and cryptex reconstructed/enumerated; read-only filesystem checks retained. | Consolidate APFS roles, UUIDs, snapshots, firmlinks and seal evidence per image; inspect unnamed embedded containers. | REPORT.md; private-evidence/volume-summary.json |
| 03 | RAMDisk architecture | IN PROGRESS | Launch definitions, binaries, kernel components and sealing plugin examined. | Finish startup ordering, shells, logging, device discovery, firmware coordination and policy relationships. | REPORT.md; STAGE4_RAMROD.md |
| 04 | Ramrod and restore pipeline | IN PROGRESS | Stages 4A–4F bounded traces recorded; Stages 4G–4I bounded receiver, guards, verifier-state and saved-context/session passes recorded. | Finish caller/options/session and verification-state trace, then checkpoints, rollback and brain acceptance. | STAGE4_RAMROD.md |
| 05 | USB and device communication | IN PROGRESS | USB profiles, 19 socket groups, remoted/PAM guards and proxy absence bounded; Stages5E–5N trace selected remote-service policy, TLS, attestation, membership and backend policy/lifecycle edges. | Finish token-use restrictions, exact transport enforcement and remaining metadata mutations; resolve per-environment services and protocol relationships; distinguish host from target. | STAGE5_CONFIGURATION.md; REPORT.md; private-evidence/ramdisk-services.json |
| 06 | Secure boot and boot chain | IN PROGRESS | Image4/EFI/trust-cache/kernel evidence established for retained artifacts. | Trace platform-specific policy/root selection and personalization; device enforcement needs hardware/runtime evidence. | STAGE3_FIRMWARE.md |
| 07 | Firmware forensics | IN PROGRESS | Catalog, IMG4/IM4M, FTAB, UARP and DP855 bounded checks; PFX/PSF vendor layouts and8CRCs reproduced. | Per-component updater/dependency/rollback map, deeper firmware control flow and encryption boundaries. | STAGE3_FIRMWARE.md |
| 08 | Option ROM and Intel boot content | IN PROGRESS | 25 ROMs,34 images,nine decompressed EFI drivers;69 Apple EFI signature checks; PSFFlasher selected PCI/update/status workflow. | Complete driver behavior and platform policy context; Product.efi trailer/plaintext unresolved. | STAGE3_FIRMWARE.md |
| 09 | Executable reverse engineering | IN PROGRESS | Standalone signature/entitlement checks and selected instruction-level traces retained. | Shared-cache extraction, ARM paths, other privileged programs and per-binary semantic coverage. | STAGE4_RAMROD.md; private-evidence/binary-analysis.json |
| 10 | Plists, manifests and configuration | IN PROGRESS | Stage 5A: 78,465 selected plist candidates parsed/hash-matched; 606 protected records remain unreadable. | Trace important consumers; collect protected records and unnamed/nonselected formats. | private-evidence/plist-index.json; private-evidence/recovery-services.json |
| 11 | Certificates, trust and signatures | IN PROGRESS | Image4, EFI, code-page and trust-cache comparisons bounded; two embedded remoted roots match Apple fingerprints and pass self-signature checks; conditional attestation/OID and expiration/chassis exceptions traced. | Exact Security/AKS/AMFDR behavior, BOM and CNKL method-2 trust, remaining certificate stores/extensions and loader policy. | STAGE3_FIRMWARE.md; STAGE2_COMPARISON.md; STAGE5_CONFIGURATION.md |
| 12 | Network and Apple service dependencies | IN PROGRESS | Stages6A–6F.6 bounded traces and partial6F.7 kernel permissions/conversion/runtime/helper census, including the static hibernation consumer, no-cache GUID-list construction and default driver-local write gate. | Finish6F.7 resync/MAC reachability, no-cache/path-property producer authority and errors, caller/helper policy and MultiUpdater errors; Q32–Q35 remain open. No traffic or firmware write observed. | STAGE6_NETWORK.md; private-evidence/stage6f7/resumption.json |
| 13 | Anomaly and compromise review | IN PROGRESS | Exact-reference reconciliation resolves earlier strict-signature alarms; no observed byte differences in corresponding update files. | Systematic per-service/entitlement/script/policy review; retain unknowns and do not infer execution. | publication/FINDINGS.csv; STAGE2_COMPARISON.md |
| 14 | Version and hardware context | IN PROGRESS | 25G83, OS 26.6.2, MacPro7,1/J160AP target metadata and 136 manifest identities retained. | Complete per-image/per-firmware version and target matrix; separate host hardware from asset targets. | REPORT.md; private-evidence/manifest-component-coverage.json |
| 15 | Public research cross-reference | IN PROGRESS | Apple, pinned OpenCore/EDK2 and format references cited next to specific claims. | Add primary citations for newly analyzed subsystems; separate documented behavior from direct observations. | publication/README.md |
| 16 | Full security report | IN PROGRESS | A partial snapshot was published previously; this revised 100-finding draft remains local and uncommitted. | Continue evidence-linked findings, coverage/limitations and reproduction material as analysis advances. | publication/README.md; publication/FINDINGS.csv |
| 17 | Supporting tools | IN PROGRESS | Existing scripts/ contains inventory, comparison and stage-specific verifiers. | New reusable tools under analysis/tools; reuse existing parsers and document exact inputs/limits in docstrings. | scripts/; analysis/tools/ |
| 18 | Investigation ledger | IN PROGRESS | Master phase/question/artifact ledgers plus147253-row twelve-field object register and per-queue remaining checklist. | 33 paths have detailed bounded twelve-field records; 42 other bounded records retain prior evidence; remaining fields and full closure remain explicit. | INVESTIGATION_STATUS.md; UNRESOLVED_QUESTIONS.md; private-evidence/coverage-ledger/object-register.csv; private-evidence/coverage-ledger/remaining-checklist.csv |
