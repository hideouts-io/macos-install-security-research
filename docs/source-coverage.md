---
layout: default
title: Source narrative coverage
---

# Source narrative coverage

[Home](../README.md) · [Documentation](index.md) · [Evidence](../evidence/README.md)

The private `publication/README.md` narrative has 37 substantive second-level sections. This map records the main public destination for each section. It is a section-assignment check, not proof that every byte of the original analysis, raw evidence, or every subordinate path has been published. The original source SHA-256 is in [publication provenance](../evidence/publication-provenance.json). The 100 finding IDs have a separate [source crosswalk](../tables/finding-provenance.csv).

| Retained source section | Public destination |
| --- | --- |
| `publication/README.md:52` — Executive assessment | [audit-overview](audit-overview.md) |
| `publication/README.md:78` — Scope and evidence standards | [methodology](methodology.md) |
| `publication/README.md:105` — OpenCore references and what they mean | [opencore](opencore.md) |
| `publication/README.md:135` — Artifact identity and reference acquisition | [artifact-provenance](artifact-provenance.md) |
| `publication/README.md:183` — Exact Apple comparison | [artifact-provenance](artifact-provenance.md) |
| `publication/README.md:217` — Inventory and folder guide | [inventory-images](inventory-images.md) |
| `publication/README.md:260` — Disk images and reconstruction | [inventory-images](inventory-images.md) |
| `publication/README.md:279` — RAMDisk architecture and services | [ramdisk-ramrod](ramdisk-ramrod.md) |
| `publication/README.md:304` — Configuration coverage and service resolution | [usb-and-services](usb-and-services.md) |
| `publication/README.md:318` — USB multiplexing and network configuration | [usb-and-services](usb-and-services.md) |
| `publication/README.md:808` — Network dependencies and endpoint-reference coverage | [restore-network](restore-network.md) |
| `publication/README.md:848` — Restore server selection and request security | [restore-network](restore-network.md) |
| `publication/README.md:912` — FDR trust objects, AP tickets and response authentication | [restore-network](restore-network.md) |
| `publication/README.md:1003` — FDR ticket verification backend and input provenance | [restore-network](restore-network.md) |
| `publication/README.md:1078` — Restore transport authentication and exact crypto dependencies | [restore-network](restore-network.md) |
| `publication/README.md:1152` — PFX firmware personalization and device-interface boundaries | [firmware-personalization](firmware-personalization.md) |
| `publication/README.md:1221` — PFX staging, device handoff and nested firmware | [firmware-personalization](firmware-personalization.md) |
| `publication/README.md:1267` — PSF EFI flasher and all packaged PSF payloads | [firmware-flashers](firmware-flashers.md) |
| `publication/README.md:1312` — PSF input authority, bounds and device-query errors | [firmware-flashers](firmware-flashers.md) |
| `publication/README.md:1372` — FirmwareUpdateLauncher and the upstream staging workflow | [firmware-flashers](firmware-flashers.md) |
| `publication/README.md:1406` — bless and MultiUpdater boot handoff | [firmware-flashers](firmware-flashers.md) |
| `publication/README.md:1461` — Kernel NVRAM conversion and firmware helper selection | [nvram-efi-paths](nvram-efi-paths.md) |
| `publication/README.md:1697` — Ramrod and APFS sealing | [ramdisk-ramrod](ramdisk-ramrod.md) |
| `publication/README.md:1762` — Update brain and Update.plist | [installer-workflow](installer-workflow.md) |
| `publication/README.md:1816` — Command authorization and endpoints | [installer-workflow](installer-workflow.md) |
| `publication/README.md:1850` — Brain receiver and prepare/apply guards | [installer-workflow](installer-workflow.md) |
| `publication/README.md:1883` — Verification-state flag and error propagation | [installer-workflow](installer-workflow.md) |
| `publication/README.md:2015` — Code signatures and kernel collections | [code-signing-kernel](code-signing-kernel.md) |
| `publication/README.md:2069` — Firmware and Option ROM catalog | [firmware-catalog](firmware-catalog.md) |
| `publication/README.md:2099` — Image4 signatures and certificate constraints | [secure-boot](secure-boot.md) |
| `publication/README.md:2128` — Trust caches and representation differences | [secure-boot](secure-boot.md) |
| `publication/README.md:2162` — Firmware measurement details | [firmware-catalog](firmware-catalog.md) |
| `publication/README.md:2213` — EFI signatures and Product.efi | [firmware-catalog](firmware-catalog.md) |
| `publication/README.md:2241` — SSV and secure-boot boundaries | [sealed-system-volume](sealed-system-volume.md) |
| `publication/README.md:2261` — Resolved anomalies and corrections | [corrections](corrections.md) |
| `publication/README.md:2280` — Reproduction and evidence map | [reproduction](reproduction.md) |
| `publication/README.md:2359` — Remaining work | [audit-status](audit-status.md) |

The original table of contents and publication-directory description are navigation metadata, so they are not counted among the 37 substantive sections. This repository reorganizes the narrative by subsystem. Stage 6F.7 remains partial and the complete 147,253-object dataset has not received whole-object semantic closure.
