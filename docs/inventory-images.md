---
layout: default
title: "Inventory, disk images, and reconstruction"
---

# Inventory, disk images, and reconstruction

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

<a id="inventory-and-folder-guide"></a>
## Inventory and folder guide

<a id="recursive-coverage"></a>
### Recursive coverage

| Scope | Regular-file paths | Directories | Symlinks |
| --- | ---: | ---: | ---: |
| Working staging copy | 1,212 | 250 | 3 |
| Software Update RAMDisk | 979 | 769 | 379 |
| AppleDiagnostics | 361 | 99 | 0 |
| ARM BaseSystem | 48,411 | 13,508 | 6,241 |
| Intel BaseSystem | 47,983 | 13,176 | 6,204 |
| Intel BaseSystem Preboot | 27 | 19 | 0 |
| Intel system cryptex | 6,150 | 1,383 | 99 |
| **Total regular-file paths** | **105,123** | | |

Original staging contains 1,191 regular files; the 21 extra working-copy entries are Finder metadata. Both source trees have 250 directories and three links. Privileged read-only enumeration resolved the initial access gap and confirmed that `Locked Files/Boot Files` is empty.

The initial recursive inventories record no enumeration/hash errors. Counts include repeated assets and potentially multiple hard-link paths; they are not unique-code counts or physical storage usage. The later Stage 4D executable/cache scan was narrower: 1,020 Intel recovery files hash-verified. An ancillary recursive listing encountered protected local-user template paths; that pass is not described as a fresh complete traversal.

Per-path catalogs retain format, size, SHA-256, ownership, mode, timestamps, link target and a bounded role description. They remain in the private audit workspace pending publication review; this README does not pretend to reproduce 105,123 individual records or manual analyses. No nested DMG/PKG/ZIP/AEA filename was found in the recovered BaseSystem/cryptex inventories, which does not exclude embedded containers without those names.

<a id="staging-layout-and-roles"></a>
### Staging layout and roles

| Path or family | What it contains / does | Interpretation boundary |
| --- | --- | --- |
| `Locked Files` | Boot-label images and text; empty `Boot Files` subdirectory | Empty staging is not proof of update success, failure or deletion |
| `index.sproduct` | Structured product/package index | A package reference does not supply the package body |
| `InstallAssistant.pkg.integrityDataV1` | CNKL integrity metadata | Not an executable installer; the original folder did not contain the full package |
| `UpdateBundle/Info.plist` | MobileAsset identity, models, size requirements and policy hints | Publisher declarations are not signatures |
| `UpdateBundle/META-INF` | ZIP metadata | Archive metadata is not runtime activity |
| `UpdateBundle/AssetData/Info.plist` | Target/staging metadata | Identifies the intended asset context |
| `boot/BuildManifest.plist` | Recipes and component digests for 136 identities | Not every component applies to the target or is locally present |
| `payload.bom`, `payloadv2.bom`, `pre.bom`, `post.bom` | Expected filesystem inventories | A BOM entry does not establish installation or presence |
| BOM `.signature` companions | Authentication data | Complete trust-chain verification remains unfinished |
| `payload`, `payloadv2` | Staged update data and chunk descriptions | Retained `data_payload` and `prepare_payload` are 12-byte PBZX headers without blocks |
| `payload_chunks.txt` | Chunk-size description | Does not replace absent chunk bodies |
| `basesystem_patches` | Replacement BaseSystem containers and companions | `.dmg` filenames conceal a patch/container format |
| `image_patches` | System/cryptex image patches | Needs format-specific reconstruction |
| `Restore/BootabilityBundle` | Restore metadata, manifests and BootabilityBrain framework | Bootability coordination capability; no disk-change event established |
| `boot/EFI`, `boot/Firmware`, `all_flash`, `dfu` | EFI tools, hardware firmware, boot-chain material and artwork | Mixed executable and data formats; not all images are code |

Inside the RAMDisk, `bin`, `sbin`, `usr`, `System`, `private` and `dev` provide tools, libraries and runtime structure. `etc` and `var` are aliases. `mnt1` through `mnt11` are staging mountpoints, not evidence that hidden disks were attached.


<a id="disk-images-and-reconstruction"></a>
## Disk images and reconstruction

| Artifact | Format / size | Validation so far |
| --- | --- | --- |
| `x86_64SURamDisk.dmg` | Raw APFS, 270,532,608 bytes | All 26 chunk hashes match; read-only mount and filesystem check passed |
| `AppleDiagnostics.dmg` | Compressed image, 2,889,199 bytes | UDIF checksum and one chunk hash match; filesystem check passed |
| `arm64eBaseSystem.dmg` patch | BXDIFF50 full replacement | Reconstructed 1,562,348,679 bytes; embedded SHA-1, 149 chunk hashes, UDIF and filesystem checks passed |
| `x86_64BaseSystem.dmg` patch | BXDIFF50 full replacement | Reconstructed 1,464,762,142 bytes; embedded SHA-1, 140 chunk hashes, UDIF and filesystem checks passed |
| `cryptex-system-x86_64` patch | RIDIFF10 full replacement | Host Apple parser succeeded; mountable APFS output and filesystem check passed |
| Official `SharedSupport.dmg` | Installer reference container | XAR member checksum checked; reference SHA-256 recorded and rechecked |

A raw APFS RAMDisk does not have a UDIF checksum to verify. That format distinction is not evidence of corruption.

The BaseSystem containers carry complete replacement bytes in PBZX streams; reconstruction did not require an older BaseSystem. Header layout, expanded size and embedded output digest were checked. Supplied hashes establish consistency with supplied metadata, not an independently trusted signature by themselves.

The RIDIFF reconstruction used the host's Apple `libParallelCompression` and wrote a new analysis artifact. Independent full-image authentication of that reconstructed output was not completed. Its source patch nevertheless matches the exact official update.

Embedded images are covered by complete source-container identity. This is not misrepresented as independently reconstructing every image a second time from a separate vendor release.


