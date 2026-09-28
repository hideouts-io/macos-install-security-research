---
layout: default
title: Research documentation
---

# Research documentation

[Home](../README.md) · [Findings](findings-index.md) · [Evidence](../evidence/README.md) · [Status](audit-status.md)

The pages below preserve the detailed analysis from the September 27, 2026 audit snapshot. They report measured bytes, selected static paths, and unresolved boundaries separately. Addresses refer to the exact named build and binary, not arbitrary macOS releases.

| Read in this order | Page |
| --- | --- |
| 1. Scope and results | [Audit overview](audit-overview.md), [methodology](methodology.md), [coverage](coverage.md), [limitations](limitations.md) |
| 2. Objects and workflow | [Provenance](artifact-provenance.md), [inventory and images](inventory-images.md), [architecture](architecture.md), [RAMDisk/ramrod](ramdisk-ramrod.md), [installer workflow](installer-workflow.md) |
| 3. Trust and boot | [Code signing/KCs](code-signing-kernel.md), [Image4/trust/Secure Boot](secure-boot.md), [sealed system volume](sealed-system-volume.md), [OpenCore assessment](opencore.md) |
| 4. Device communication | [USB/services/TLS](usb-and-services.md), [mobile-device components](mobile-device-components.md), [restore networking/FDR](restore-network.md) |
| 5. Firmware | [Catalog/Option ROMs](firmware-catalog.md), [PFX](firmware-personalization.md), [PSF and updater handoff](firmware-flashers.md) |
| 6. Kernel and policy | [Stage 6F.7 NVRAM/EFI](nvram-efi-paths.md), [sandbox](sandbox-policy.md), [AMFI](amfi-entitlements.md), [APFS/Device Tree](apfs-device-tree.md), [reverse-engineering map](reverse-engineering.md) |
| 7. Reproduce and continue | [Findings index](findings-index.md), [source narrative coverage](source-coverage.md), [reproduction](reproduction.md), [corrections](corrections.md), [open questions](open-questions.md), [audit status](audit-status.md), [references](references.md) |

The [finding groups](../findings/ref.md) preserve all 100 original IDs across reference, RAMDisk, USB, signatures, firmware, configuration, remote services, and network categories. The [source crosswalk](../tables/finding-provenance.csv), [public tables](../tables/findings.csv), and [evidence index](../evidence/README.md) help reviewers trace the published claims without distributing copyrighted binaries or private raw logs.

The [diagrams](../diagrams/README.md) have rendered SVGs and editable Mermaid sources, with text explanations on their subject pages. The [local Pages instructions](reproduction.md#local-pages-preview) cover the site build and navigation check. The CI workflow validates but does not deploy this draft.
