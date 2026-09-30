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




<a id="bootabilitybrain-bounded-trace"></a>
## BootabilityBrain entry and queue boundary

The original and working-copy BootabilityBrain framework have matching corresponding file hashes; its arm64e executable (SHA-256 `5455c47d5f9b9712a03fe64870f8e6ad864688c3fd2be4655bb40a617c8ad773`) also matched the exact official comparison. Ordinary/strict full-bundle `codesign` verification fails on both with an obsolete custom-omit resource envelope. Code-only verification with `--ignore-resources --strict` passes while explicitly leaving resources unverified. This is a **verification coverage limit**, not a demonstrated alteration or effective boot-policy verdict.

An original-byte-checked 725-instruction trace of selected entry/controller ranges shows `BYBrain` delegating bootable-volume, medium-security update and manifest-verification requests. The controller constructs a sequence containing mount, version analysis, authorization, LocalPolicy, personalization, boot-object installation and set-boot operations, then invokes its runner. The existence and order of queue construction do not prove that the operations executed or changed a volume. Runner dispatch and selected mount/authorization branches are now bounded, but actual dispatch, authenticated mount, caller credentials, manifest acceptance, LocalPolicy effects, rollback and active SSV enforcement remain open. Detailed evidence is retained privately under `private-evidence/stage6f7-bootability-20260929/`.

### Bootability dispatch and XPC service continuation

The controller runner conditionally starts required operations and passes a Boolean success value into cleanup after the queue. FindAndMountVolumes resolves Preboot/recovery candidates and can request a read-write remount through `/sbin/mount -uw`. Its position before the named authorization operation is queue order, not a mount-authorization bypass: the service caller, mount API, OS privilege check, request handler and LocalPolicy enforcement remain separate. The named authorization operation conditionally checks owner state and obtains an externalized authentication context through a handler. The checked Brain continuation covers 6,252 original-byte instructions, 37 independent call anchors and 21 independently resolved class references.

The reconstructed arm64e BaseSystem contains an Apple-signed BootabilityService XPC executable (SHA-256 `5240c87b4809350158fb0576da4ee9c46411b5e83c56a528080a808639df3aa1`). Its static incoming-connection path checks for a non-nil `com.apple.private.bootability` entitlement value and rejects a second connected client. A `BYServiceClient` records the peer PID, effective UID and path; the checked admission method does not compare those values to an allowlist. Its `obtainAuthenticationContext` method asks the client through a synchronous XPC reply. None of this establishes who connected or whether an authentication context was accepted.

The XPC make-bootable method passes its options dictionary to the loader. Original-byte and rebase checks resolve `BootabilityBrainPath` and `BootabilityTrustcachePath` lookups. A string-valued Brain path skips the Preboot-selection helper but still enters bundle handling and a conditional `LSMinimumSystemVersion` comparison; a negative comparison reaches a local error. Without that typed path, the helper checks packaged Preboot Brain/trust-cache presence and selects between Preboot and the running OS. A string-valued trust-cache path enters `open`/`mmap` and an AppleMobileFileIntegrity user-client selector-2 call. On the checked success branch, that call precedes `dlopen`; a nonzero result takes an error route. Without a typed trust-cache path, this local call is skipped. These branches do not prove that either override was accepted or that AMFI or dyld loaded it.

The 4,814-instruction service trace resolves 23 service methods and 15 corroborated call anchors. A further 220 original-byte-checked client instructions, 22 call anchors and 11 branch anchors bound the connection and loader handoff. Thirteen retained executable hashes across 14 catalog paths declare the required client entitlement, including `bless`, `bputil` and startup helpers. They are candidates, not observed callers. Full-bundle strict resource verification reports an obsolete custom-omit envelope; code-only strict verification passes with resources unverified. No unauthorized caller, arbitrary framework loading, trust bypass or boot-policy modification is established.

The matching ARM BaseSystem `bputil` is one concrete **static call-site client** (SHA-256 `80c9ae8b7536d0ee923a034198d201fe8773d71eea7b9f4bcb3244a2a2a630c2`). Its selected branch passes a dictionary containing `BYBootOptionSecurityMode` and `BYBootOptionForceCreateLocalPolicy` to `BYManager makeVolumeBootableWithGroupUUID:options:error:` at `0x100005d5c`. The cached Bootability.framework version 82 connects `BYManager` to `com.apple.BootabilityService` and forwards the incoming options over XPC (`0x19fd76044..0x19fd761f0`). The framework exports the two Brain/trust-cache path keys, but this `bputil` branch does not set them. A literal-key search of seven selected readable entitled executables found no producer; other callers and data-driven inputs remain open. These checks do not show that `bputil` ran or the service accepted it.

### Startup Disk option and helper chain

The same ARM BaseSystem contains three compiled clients of the on-demand `com.apple.startupdiskhelper` Mach service: Boot Picker, Startup Disk and StartupDiskWidgetExtension. The helper executable (SHA-256 `cf5a19431f103ecfdb7b4090031128b50dfa4586dfb585df87c8c91297096bd1`) is configured by launchd for `UserName=root`; this is configuration, not an observed launch. Its checked incoming-connection branch requires a true, `NSNumber`-typed `com.apple.startupdiskhelper` entitlement. Boot Picker and Startup Disk declare that key. The widget extension's **own** signed entitlement set does not, despite containing matching client methods; its effective process/host identity and any accepted connection are unknown. The helper separately declares `com.apple.private.bootability`, the credential checked at the downstream BootabilityService boundary.

Selected Boot Picker and Startup Disk methods construct dictionaries using SetBoot/SetBootOnce, conditional SkipVerification, ForceCreateLocalPolicy, ForcePersonalization, ForceInstallBootObjects and AllowLocalAuthenticationPrompt. A Startup Disk security-level method additionally supplies SecurityMode. The helper's selected `makeBootableWithGroupUUID:localAuthenticationContext:options:withReply:` method forwards its caller-supplied options to `BYManager` at `0x100008444`. Selected `bless` and Boot Recovery Assistant methods also build non-path dictionaries before `BYManager` calls. Across these six catalog-matching executables, 533 selected instructions were checked against original bytes and independent disassembly; none of these selected constructions produces `BootabilityBrainPath` or `BootabilityTrustcachePath`. Dynamic or other option producers remain unresolved. Conditional option names do not by themselves establish a verification bypass, an accepted service request, or a LocalPolicy change.

A further inventory-matched census checked all **149 staging plists** (17,049,850 bytes) and found neither path key as an ASCII or UTF-16 literal. In five matching ARM dyld subcaches, both strings occur in Bootability.framework and its cached BootabilityBrain.framework. Original BootabilityBrain bytes link the strings to CFStrings and exported `BYBootOptionBootabilityBrainPath`/`BYBootOptionBootabilityTrustcachePath` slots at `0x1ac770b48`/`0x1ac770b50`; the original export trie independently confirms the symbol names and slot offsets. A narrow direct-address code scan found no nearby ADRP/LDR/ADD reference to those slots or CFStrings. These are **framework constants, not a demonstrated option-value producer**. Optimized binds, indirect references, other files and dynamically supplied dictionaries remain open. No path override or trust-cache load was observed.

A wider original-code scan found eight apparent Brain slot references, but each crosses a same-register ADRP overwrite; independent disassembly points the final load to a different page. An original symbol-table pass covered **all 764 mapped cache images and 237,197 undefined symbols** with no named `_BYBootOption` import; it recovered two known Bootability class imports as parser checks. Using the original cache's version-5 slide records and Apple's pinned [dyld format definitions](https://github.com/apple-oss-distributions/dyld/blob/fd8d0c4d52320ebf64db34f3cb280310d905c5ae/include/mach-o/dyld_cache_format.h), a second pass decoded **5,747,605 rebase-pointer locations**: none targets a path-key slot, and the only four pointers to the selected CFStrings are the four exported slots themselves. Those four witnesses agree with the independent export/CFString chain. These bounded negatives narrow the search for a statically linked cached client but do not exclude prebuilt loader/closure records, code-address construction, external clients, `dlsym`, computed keys or dynamic dictionaries. Seven inventoried scopes contain four standalone Intel kernel collections and 48 source-tree kernel-collection IM4M manifests, but no standalone ARM KC executable for selector-2 implementation analysis. The effective AMFI and mount decisions remain unknown.

Boot Picker, Startup Disk and the widget extension carry Apple signing chains and matching catalog hashes. Their strict full-bundle checks return `resource envelope is obsolete (custom omit rules)`; strict code-only verification passes while leaving resources unverified. The same bounded packaging limit applies to the separately reviewed BootabilityBrain bundle. No alteration is inferred from this result. Raw binaries, signatures, exact instruction proofs and read-only scan errors remain in the private audit under `private-evidence/stage6f7-bootability-options-20260930/`.

The exact-matching Restore BootabilityBrain implements `LPStaticAPFSVolume mountAtPath:options:error:` at `0xdbd20`. It prepares `/sbin/mount_apfs` arguments, invokes a `posix_spawn` helper and waits for its result. The `/sbin` path is a symlink to the ARM BaseSystem `mount_apfs` executable (SHA-256 `6f9626cab9682d1df2c56040a613a335236cf5abcefc0ac7147044afc1dd25a4`), whose selected code calls imported `_mount` at `0x1000017c4`. Original-byte and independent disassembler checks cover 146 cached-framework, 40 `bputil`, 652 mount-method, 284 spawn-helper and eight `mount_apfs` instructions. The helper's declared APFS, I/O catalog and restricted-block-device entitlements are capability context; the effective service UID, spawned child, VFS/MAC decision and mount result are unobserved. The seven inventoried scopes contain no standalone ARM kernel collection from which to resolve the AppleMobileFileIntegrity selector-2 implementation. No severity or compromise verdict changes.

Next inspect prebuilt loader/closure or other optimized cache binding records for the four path-key slots and follow any actual dictionary-value producer and its caller constraints. Locate a same-build ARM AMFI implementation if retained, and resolve runtime mount/LocalPolicy authority only with appropriate isolated evidence. Apple’s [LocalPolicy architecture](https://support.apple.com/en-ca/guide/security/secc745a0845/web) provides context for the device-side boundary; static package analysis does not measure that boundary on a running Mac.
