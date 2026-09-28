---
layout: default
title: "Image4, trust caches, SSV, and Secure Boot boundaries"
---

# Image4, trust caches, SSV, and Secure Boot boundaries

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

<a id="image4-signatures-and-certificate-constraints"></a>
## Image4 signatures and certificate constraints

All **868 standalone IM4M signed-body RSA/SHA-384 signatures** verify. Bootability contains one additional nested IM4M, which also verifies.

Root candidates were extracted from the official-reference-matched RAMDisk `libimage4.dylib` (SHA-256 `49f290ad765eb84b159502006e789ae7a3295c02436461ab2189c1b5627b7518`). This avoids treating a ticket's own certificate as an independently trusted root. It still does not measure a hardware root.

| Root certificate | DER SHA-256 | Distinct ticket certificates linked |
| --- | --- | ---: |
| Apple X86 Secure Boot Root CA - G1 | `ef4e4b368694cce627aeccdb55486e4f9603e52492377da80aae9011e96bcff6` | 21 |
| Apple Extra Content Global Root CA - G1 | `90816069386977fdd0877f76492fedc1a9437862cea0a37c9cd94071716c73b7` | 2 |
| Apple Wireless Secure Boot Root CA - G1 | `ce3d34694fe1fc28a2c17378399723ca50ac288c80c1131bee973b85c131fed4` | 1 |
| Apple DDI Secure Boot Root CA - G1 | `f4f2cbd3fa6516a2b70fb1d7e8c88e2a526d612deb14e3fd656475a4fcaece2b` | 1, nested Bootability |

All 25 certificate signatures and four root self-signatures verify. The x86 root also matches the Apple certificate copy in [OpenCore's pinned published key source](https://github.com/acidanthera/OpenCorePkg/blob/2cc2362d3a2cfec2ad66a752603bb4a5ee092d78/Library/OcAppleKeysLib/OcAppleKeysLib.c). This is external-copy corroboration, not detection of OpenCore on the Mac. The other roots lack that separate external-copy corroboration in this pass.

Two additional self-signed candidates named Fake Apple DDI and Fake Apple Extra Content occur in the official-matching library. No examined ticket certificate verifies against them. They are not treated as approved trust anchors, and their runtime selection remains untraced.

<a id="signed-role-checks"></a>
### Signed role checks

The Image4 role extension, OID `1.2.840.113635.100.6.1.15`, was parsed for all 869 tickets. All **9,702 signed object records** pass the implemented rules:

- 38,231 exact encoded-value checks.
- 56,469 required-presence checks.
- 12,799 required-absence checks.

Private-tag/name agreement and duplicate names are checked. Negative controls reject removal of required properties and insertion of forbidden ECID. No examined signed manifest contains ECID; that observation does not establish host security mode or rule out later personalization.

These repeated rule counts are not unique binaries or separate hardware trust decisions. Complete chip/board/security-domain interpretation, anti-rollback, personalization and every certificate extension remain outside coverage. The rule implementation was cross-checked against [OpenCore's pinned Image4 verifier](https://github.com/acidanthera/OpenCorePkg/blob/2cc2362d3a2cfec2ad66a752603bb4a5ee092d78/Library/OcAppleImg4Lib/libDERImg4/DER_Img4Manifest.c).


<a id="trust-caches-and-representation-differences"></a>
## Trust caches and representation differences

Trust caches contain code hashes and associated policy metadata. They are not execution logs. Apple's [trust-cache documentation](https://support.apple.com/guide/security/trust-caches-sec7d38fbf97/web) provides the platform context; this audit's counts and comparisons come from the retained bytes.

| Retained type / resource | Version | Entries |
| --- | ---: | ---: |
| trbb / Bootability | 1 | 1 |
| xbtc / `022-22048-093.dmg.aea.x86.trustcache` | 2 | 1,073 |
| trca / diagnostics | 2 | 57 |
| trcs / retained cryptex-related cache | 2 | 135 |
| bstc / `BaseSystem.dmg.trustcache` | 2 | 1,040 |
| xrtc / `arm64eSURamDisk.dmg.x86.trustcache` | 1 | 405 |
| rtsc / Intel RAMDisk | 1 | 407 |
| **Retained total** | | **3,118** |

Version 1 entries are 22 bytes; version 2 entries are 24 bytes and include a constraint category. Categories through 19 were observed. Older category descriptions are not assumed complete for this build.

The expanded official set contains **15 caches / 36,596 entries**, including repeated content. All **2,699 measured CodeDirectory records** occur in at least one official cache. The 49 earlier nonmatches are accounted for by the previously omitted `094-96899-093.dmg.trustcache`: 151 entries, type trcs, signed-digest matches in 40 retained tickets.

<a id="four-alternate-representations"></a>
### Four alternate representations

Three of the original seven encodings directly match signed IM4P digests. Four do not, but each has one signed official counterpart with an identical full entry array:

| Retained encoding | Signed official counterpart | Type relationship | Entries |
| --- | --- | --- | ---: |
| `022-22048-093.dmg.aea.x86.trustcache` | `022-22048-093.dmg.aea.trustcache` | xbtc → bstc | 1,073 |
| `BaseSystem.dmg.trustcache` | `BaseSystem.dmg.x86.trustcache` | bstc → xbtc | 1,040 |
| `arm64eSURamDisk.dmg.x86.trustcache` | `arm64eSURamDisk.dmg.trustcache` | xrtc → rtsc | 405 |
| `x86_64SURamDisk.dmg.trustcache` | `x86_64SURamDisk.dmg.x86.trustcache` | rtsc → xrtc | 407 |

Only the Image4 type and 16-byte cache UUID differ. The corresponding code hashes, hash types, flags, constraint bytes, versions, counts and encoded lengths agree. Eleven official encodings directly match retained signed-ticket measurements; four are alternate representations.

This resolves an allowlist-content comparison gap. It **does not** make the original encodings directly signed by the counterpart tickets: type and UUID are part of the measured encoding. Runtime representation selection or rewriting remains unknown, and cache membership is not proof of effective authorization or execution.


<a id="ssv-and-secure-boot-boundaries"></a>
## SSV and secure-boot boundaries

An SSV protects system content through recursively hashed filesystem data summarized by a seal. Apple documents recomputation and comparison with signed measurements during installation, with boot-time verification differing between Apple silicon and Intel/T2. See [Apple's SSV description](https://support.apple.com/guide/security/signed-system-volume-security-secd698747c9/web).

| Examined volume role | Reported sealed metadata |
| --- | --- |
| ARM BaseSystem | Yes |
| Intel system cryptex | Yes |
| Intel BaseSystem / Preboot | No / No |
| Software Update RAMDisk | No |
| Diagnostics | No |

Different roles need not have identical seal state. These are image metadata observations, not measurements of the currently booted system. A seal flag or filesystem-consistency result does not substitute for full signature and policy validation.

The images include apfs_sealvolume, apfs_checkseal, apfs_checkdigest, apfs_computedigest, apfs_systemsnapshot, apfs_prepare_cryptex, newfs_apfs, fsck_apfs and maintenance tools. Inclusion supports capabilities; this audit did not use them to change a real volume.

Hardware-rooted boot verification is separate from checking a downloaded ticket or EFI file. This investigation did not measure current SIP, LocalPolicy, T2 startup-security mode, installed SSV integrity, Boot ROM contents or running peripheral firmware. [Apple's Intel boot-process documentation](https://support.apple.com/en-gb/guide/security/sec5d0fab7c6/web) supplies architectural context, not evidence of this machine's settings.

No FIPS validation, certification or compliance claim is made for the examined package merely because cryptographic libraries or labels are present.


