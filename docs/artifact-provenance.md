---
layout: default
title: "Artifact identity and exact Apple comparison"
---

# Artifact identity and exact Apple comparison

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

The original staging location was `/System/Volumes/Data/macOS Install Data/`. A separate readable working copy supplied analysis access, while original-versus-copy hashes and original metadata were tracked independently. The copy's user-specific absolute path is omitted from this publication. This was a live logical acquisition, not a pre-collection chain-of-custody proof.

<a id="artifact-identity-and-reference-acquisition"></a>
## Artifact identity and reference acquisition

| Property | Retained result |
| --- | --- |
| OS version / build | 26.6.2 / 25G83 |
| Target metadata | MacPro7,1 / J160AP |
| BuildManifest coverage | 136 identities, including multiple hardware/platform variants |
| Apple catalog product | `140-93587` |
| Full installer size | 18,384,624,402 bytes |
| Package verification | `pkgutil --check-signature` returned success, signed Apple Software |
| Package certificate path reported | Software Update → Apple Software Update Certification Authority → Apple Root CA |
| Installer integrity chunks | 1,754 / 1,754 match, covering the complete file |

Version/build and hardware names are metadata observations. Their cryptographic support comes from the independent acquisition and subsequent comparisons, not from a publisher string in a plist.

The target asset hostname advertised in metadata initially failed DNS resolution. The exact named and measured update ZIP was subsequently located inside the verified full installer's SharedSupport image. No guessed mirror or merely similar IPSW was substituted.

The retained [Apple distribution record](https://swdist.apple.com/content/downloads/37/33/140-93587-A_GRFFH93NOL/f944yaqo1cjhh2m0kxrl0zhcpg9yb9qphv/140-93587.English.dist) identifies the product. Acquisition evidence retains the catalog, asset metadata, package-signature output and checksums; this link is a reference, not an instruction to install anything.

<a id="principal-sha-256-measurements"></a>
### Principal SHA-256 measurements

```text
InstallAssistant.pkg
376923d7494cfa32b69f383bcfdce46aeedb609fe6a242ea12a6e015bfb77ba4

InstallAssistant.pkg.integrityDataV1
4894d52f7ca4a50551d3edcd98bba68959563c6b3fa6eb3eb6f01d39f1e917b5

SharedSupport.dmg
9327c292fb8f804f17b7bcde542aa523d27014606bc3d74e8f3dc3b892399354

60533a8ae8e47c23593a6965d64c1f00a6396cfe.zip
0b44a71bd6a721f5ddfb46f8dba39b09ee46bf9678a1c3100b978f512acfc07c

UpdateBrain.zip
aa8e1a6e6b421e58e00290fb22fbc5dd93dea815ce72449a528824d2bb8f93d2

Reconstructed x86_64BaseSystem.dmg
bbfcbf7bfd09c79465fa92c741ebb665625794c31578b81248f7fa0c2bcd4789

Reconstructed arm64eBaseSystem.dmg
eeda386b1fb66a313cadef26e3e7ee06643d4d5ea8b3330a411a118ac7d14ed3
```

SharedSupport is 18,366,669,607 bytes; its XAR member checksum was verified, and Stage 4E independently rehashed it to the same SHA-256. The update ZIP is 18,356,020,461 bytes. Its SHA-1 equals the filename stem and its SHA-256 matches the separately downloaded asset metadata's `_Measurement-SHA256`.

The CNKL method-2 signature was not independently decoded and trusted. Package signature verification and matching chunk hashes are distinct results.


<a id="exact-apple-comparison"></a>
## Exact Apple comparison

All 2,483 update-ZIP entries were enumerated, with duplicate/unsafe path checks. Every non-directory member was streamed and hashed. Local comparison files were freshly hashed; symlinks were compared as links, not followed into host files.

| Disposition | Count |
| --- | ---: |
| Matching regular files | 1,186 |
| Matching symlinks | 3 |
| Corresponding directories | 247 |
| Content differences | 0 |
| Object-kind or symlink-target differences | 0 |
| Official-only regular files | 1,047 |
| Local-only paths | 29 |

The 29 local-only paths are fully accounted for:

- 21 Finder `.DS_Store` files added to the working copy and absent from the original.
- One installer-integrity file outside UpdateBundle, independently matched to Apple.
- One `index.sproduct`, with matching package identity/size but no exact byte reference.
- Three boot-label files, with matching original/copy hashes but no vendor counterparts.
- Three directories: `UpdateBundle`, `Locked Files`, and empty `Locked Files/Boot Files`.

The complete update ZIP contains 2,233 regular files and three symlinks. Its 1,047 additional files comprise 920 firmware assets, 106 bulk payload/ECC files, 14 kernel collections/caches, two additional ARM image patches, and five other assets. Examples include an ARM RAMDisk, ARM caches, an AEA image, ARM system cryptex content and bulk payload chunks.

No cause is assigned to each omission without staging/install logs. Platform selection, update phase and cleanup are questions to investigate.

All 42 J160AP preflight component-digest comparisons also match: 16 CustomerInstall, 17 CustomerFirmwareUpdate, and nine RecoveryBoot entries. No corresponding digest or component-name difference was found in that comparison.

<a id="earlier-signature-failures"></a>
### Earlier signature failures

All 906 previously recorded strict code-signature failures map to byte-identical official files or source containers. The failure records remain valid observations; their interpretation changes. They do not demonstrate local tampering when the same bytes are in the official distribution. It would still be incorrect to report that all strict verification or all trust chains passed.

The missing proxy executable and its launch configuration likewise occur in the official-matching RAMDisk. This establishes provenance, not the reason for that packaging choice.

