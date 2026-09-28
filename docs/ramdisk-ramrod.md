---
layout: default
title: "Software Update RAMDisk, ramrod, and sealing"
---

# Software Update RAMDisk, ramrod, and sealing

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

<a id="ramdisk-architecture-and-services"></a>
## RAMDisk architecture and services

The RAMDisk identifies itself as a 25G83 restore environment. It contains launchd, a kernel collection, libraries, disk tools, ramrod and firmware resources. Its purpose is to support update/restore work outside the ordinary installed system. The RAM-backed disk service configuration supports that architecture; mounting the image for examination does not demonstrate that the machine historically booted it from RAM or entered DFU.

<a id="launch-configuration"></a>
### Launch configuration

| Definition | Observed configuration | Executable at configured path |
| --- | --- | --- |
| ramrod | RunAtLoad, interactive spawning, console output/logging variables, `Umask=0` | Present |
| diskimagesiod | On-demand Mach services | Present |
| diskimagesiod.ram | Same executable with `--ram` | Present |
| syslogd | KeepAlive | Present |
| PurpleReverseProxy.ramdisk | Socket activation | **Absent** |
| ReportCrash.Root | Mach-service definition | **Absent** |

Six launch definitions were examined. A definition whose binary is absent is not an operational-service observation. Another runtime source or deliberate image reduction is possible but not established.

<a id="kernel-frameworks-and-privileges"></a>
### Kernel, frameworks and privileges

The RAMDisk kernel collection exposes **232 prelink records**. Their identifiers, versions, paths and dependencies were cataloged. This is bundled-driver metadata, not a live loaded-driver list.

Private frameworks and libraries cover hardware discovery, storage, archive/compression handling, cryptography, update protocols and device-specific support. Their inclusion does not demonstrate that every code path was invoked.

Ramrod's entitlement declarations include APFS unlock/sealed-snapshot operations, raw disk/NVMe interfaces, SMC and USB-C controllers, boot policy, restricted NVRAM, Image4, FDR, keystore and rootless installation operations. Capture, HID, camera and mobile-platform declarations also appear. Declarations establish requested capabilities, not effective runtime grants or evidence of recording, keylogging or exfiltration.


<a id="ramrod-and-apfs-sealing"></a>
## Ramrod and APFS sealing

<a id="traced-sealing-path"></a>
### Traced sealing path

The plugin calls `ramrod_seal_system_volume_with_root_hash_verify` at `0x1145c`. Chained fixups bind that import at `0x621d0` to **the main ramrod executable**, not the similarly named library implementation used in the earliest trace.

| Location | Established behavior |
| --- | --- |
| Plugin `0x1142a–0x1145c` | Supplies log path, root data and validation argument 1 |
| Main wrapper `0x10003d6ae` | Transfers the validation choice to the internal routine |
| Main internal `0x10003d6cd`; validation call `0x10003d97c` | Performs the validation path before spawning the sealing utility |
| Main trust helper `0x10003c845` | Constructs Image4 validation context |
| Main callback `0x10003cd91` | Non-null validated image is success; null image is failure |
| Plugin error path `0x1148c–0x114cd` | Wraps sealing failure in MobileSoftwareUpdate error 1130 |

The library's related implementation independently corroborates argument handling and the failure gate. It is not assumed identical in every respect to main ramrod.

The helper supports custom manifest-hash handling and additional chip candidates when a custom input is present. The examined sealing caller supplies a null custom hash, leaving the effective AP chip candidate on this path. Full device-policy interpretation is not emulated.

The command is constructed as an argument array and passed through an execution helper to `posix_spawn`, not interpolated into a shell command. No such operation was run during this audit.

<a id="inputs-and-command-construction"></a>
### Inputs and command construction

| Context field / argument | Meaning established by the trace |
| --- | --- |
| Plugin `+0x2fb8` | `OS.dmg.mtree` path |
| Plugin `+0x2fc8` | `OS.dmg.root_hash` path |
| Plugin `+0x2fc0` | `OS.dmg.mtree.%@.im4m` ticket path |
| Plugin `+0x2fd0` | `OS.dmg.root_hash.%@.im4m` ticket path |
| `-R <value>` | Conditional mtree-related argument |
| `-P` | Conditional manifest/container-related mode |
| `-I /mnt5/root_hash` | Supplied root bytes written successfully before use |
| `-u /mnt5/manifest_and_db/digest.db` | Conditional readable digest database |
| `-E /mnt5/apfs_sealvolume.log` | Plugin-supplied log destination |
| `-d -v <device>` | Final utility arguments |

Additional branches build `-a`, `-m` or output-root `-L -M` arguments. Their presence is recorded; undocumented meanings and reachability are not inferred from spelling. Ticket filenames use a lowercased substitution; its full upstream source and containing directory remain incompletely traced.

<a id="the-xsysxmtr-discrepancy"></a>
### The xsys/xmtr discrepancy

The root-hash diagnostic says “xmtr,” while code passes `0x78737973`, formatted as **xsys**. The mtree helper uses **xmtr** (`0x786d7472`). All 48 examined system root/mtree tickets contain both objects. J160 ticket pairs are byte-identical within the corresponding Boot, Preboot and FirmwareUpdate variants, while xsys/xmtr represent distinct digests.

This resolves the code-versus-log interpretation. A misleading log string is not proof that signature validation was skipped.

<a id="skip-and-verification-controls"></a>
### Skip and verification controls

| Input / state | Handling | Effect |
| --- | --- | --- |
| `skip-sealing` | CFBoolean checked; stored at plugin `+0x2d49` | True branches around the sealer, advances progress, refreshes volume references and reports checkpoint success |
| `system-volume-verify-done` | CFBoolean checked; stored at plugin `+0x4849` | Selects a remap/sealer-data path when manifest checking is enabled |
| Manifest-check default | `APFSShouldSealSystemVolume` output contributes to `+0x2fb0` | Policy-derived initial setting; APFS internals untraced |
| Previously sealed | Requests volume capabilities and tests `VOL_CAP_FMT_SEALED` | Skips resealing when the bit is set |

A Boolean claiming prior verification does not prove verification occurred. The skip capability is concrete, but an unprivileged route to supply it has not been established.

The previously-sealed path uses `ATTR_VOL_CAPABILITIES` (`0x00020000`) and tests `VOL_CAP_FMT_SEALED` (`0x02000000`) in a zeroed 36-byte response. The call site does not separately check the `fgetattrlist` result or valid-capabilities bitmap before testing the bit. That is a bounded code observation, not a demonstrated exploit or measurement of the host's booted SSV. Constant definitions are corroborated by [Apple's XNU attribute header](https://github.com/apple-oss-distributions/xnu/blob/main/bsd/sys/attr.h).

<a id="correction-manifestnvram-override-reachability"></a>
### Correction: manifest/NVRAM override reachability

The ordinary loader loads `kCFBooleanTrue` into callee-preserved r15, then compares it with `kCFBooleanFalse` at `0x16a47`. Entry into the override parser requires equality. Under normal CoreFoundation bindings and ABI-preserving callees, that condition is false. Apple's [CoreFoundation source](https://github.com/apple-oss-distributions/CF/blob/main/CFNumber.c) corroborates separate true/false objects; it is not a same-build runtime measurement.

The other direct branch into the address span targets an allocation-error block and exits without falling through to the parser. This corrects the earlier preliminary interpretation that the `verify-system-manifest` / `ota-arv-mode` parser was ordinarily reachable.

The retained NVRAM helper reads `IODeviceTree:/options`; it was not executed, and a property read is not a write-authorization check. Arbitrary indirect entry, runtime patching and broken bindings are outside the reachability model.


