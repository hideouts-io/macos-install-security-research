---
layout: default
title: "Firmware catalog, Option ROMs, and EFI signatures"
---

# Firmware catalog, Option ROMs, and EFI signatures

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

<a id="firmware-and-option-rom-catalog"></a>
## Firmware and Option ROM catalog

Initial firmware triage covered **1,302 selected paths** across staging, RAMDisk and diagnostics, recording hashes, headers, entropy, strings and relevant structures. Entropy is descriptive, not a malware score.

| Family / location | Role supported by artifacts | Analysis limit |
| --- | --- | --- |
| EFI/AMDFirmware | GPU updater/payloads and PCI ROM chains | Complete graphics code and outer authentication untraced |
| EFI/USBCUpdater | Board/port Thunderbolt and USB-C updates; Mac Pro front/top I/O, Apple I/O Card and MPX selection data | Selection metadata does not prove a connected board or flash |
| MultiUpdater / SMCPayloads | Orchestration and SMC update tools | No invocation or installed firmware readback |
| AppleSDFirmware | SD-controller payload/configuration and EFI updater | Device verification path incomplete |
| PSFFirmware / PFX | Peripheral firmware/update family | Vendor protocol and all instructions undecoded |
| S4E / t302 / t303 | Storage-controller collections: 15 / 20 / 7 regular files | Blobs are not automatically PCI Option ROMs |
| USB-C_HPM / USB-C_HCPM | Type-C controller variants | AP/DEV names do not establish active development security mode |
| MCDP29XX / DP865 / DP855 | Display bridge/controller resources | DP855 measurements reproduced; broader firmware code incomplete |
| all_flash / dfu | Boot-chain, SEP, boot presentation and restore assets | Types include executable firmware and non-executable artwork |
| SE/Stockholm / SLAM | Secure-element-related resources | Do not conflate every secure element with Secure Enclave firmware |
| ansf / rans / ciof / tmuf / rt13m0 / Ace3 | Storage, peripheral and USB-controller containers | Requires payload-specific interpretation |

Twenty IM4P containers were structurally decoded in the initial focused pass. CIO, TMU and SEP restore digest differences resolve by substituting the expected restore type in analysis bytes: `ciof→rcio`, `tmuf→rtmu`, `sepi→rsep`. Original source bytes were unchanged. This explains measurement representation, not the device-side acceptance algorithm.

<a id="pci-option-roms"></a>
### PCI Option ROMs

Twenty-five retained AMD-vendor ROM files contain 34 parsed images. Their modulo-256 byte sums are zero; that is a format checksum, not signature authentication. Nine images are compressed EFI code type 3, with signature `0xEF1`, x86-64 machine type `0x8664`, subsystem 11 and compression type 1.

All nine decoded to their declared sizes, 183,808–190,976 bytes, and have bounded PE sections. Their certificate-directory offset and size are zero. There is therefore no inner PE certificate-table signature to validate using the separate Apple EFI method. Whole-ROM official byte identity and possible outer/vendor authentication are different evidence layers.

Strings support Radeon graphics roles, including framebuffer, backlight and connector code. Build-path strings do not show that the build host or Windows ran on the examined Mac. No ROM was loaded or flashed in this investigation.

The decompressor was audit-local `uefi-firmware==1.16`, with dependency/source provenance retained. The project's [decompressor advisory](https://github.com/theopolis/uefi-firmware-parser/security/advisories/GHSA-hm2w-vr2p-hq7w) was considered when selecting the analysis dependency. No target firmware was executed.


<a id="firmware-measurement-details"></a>
## Firmware measurement details

<a id="rtkit-ftab"></a>
### RTKit FTAB

`rt13m0/Release/ftab.bin` contains rkos, rrko, bver, _brd, dbgb, vsig and _phy entries. The first two are identical 274,688-byte payloads at offsets 160 and 274,848. Their SHA-384 matches `Timer,RTKitOS,1`:

```text
512d662c2762d25152022b649a9375e3567626dd4405d55868e8403f18c65662eefb28495e379a1178fb5616be4975bc
```

The manifest measures an internal region, not the whole container. Placeholder-like auxiliary bytes do not establish active debugging. A [pinned FTAB implementation](https://github.com/blacktop/ipsw/blob/ee9db4bc6feeeb45d9625687a66aa3ebbb4dd526/pkg/ftab/ftab.go) was used as a format cross-check.

<a id="ace3-uarp"></a>
### Ace3 UARP

The examined j514 UARP version-2 container has 82 table entries and NSKeyedArchiver metadata, decoded as data without instantiating archived classes.

All 36 digest lists reproduce from 126 revision rules:

```text
uint8(minimum revision) || uint8(maximum revision)
    || SHA256(patch payload || configuration payload)
```

Every list covers revisions 0–255 exactly once, without overlap or gaps. Complete list hashes match, and BoardID selection reproduces all 12 relevant manifest references—three identities for each of four controllers. Controllers 1 and 2 sharing a digest explains an earlier unique-digest count discrepancy.

Example list hashes: DL01 `10483e0a9481de87c7ce08be78cd46737d429c3e49ac172c299f453b620b8a0d`; DL03 `a3dd12ef87cb517064cc3b3b2dd6b668a5520e46924c0184e1245e3dfe5bb3ae`; DL07 `c564e2cf33f51715b79b3c8d46fbfd69a62146b313d9221a9f5a4f1ad527b771`.

No controller revision or flash session was observed. Format/composition cross-check: [pinned idevicerestore Ace3 source](https://github.com/libimobiledevice/idevicerestore/blob/60192e97f87d1bbab5c493684e0a245b0966363f/src/ace3.c).

<a id="dp855"></a>
### DP855

All 18 complete-payload SHA-256 declarations across three device configurations match: EDID, FCBIST_Config, FW_Config, LUTS_Config, NVM_IMAGE and TCON_Config.

The separate 61,440-byte main firmware, version 283, uses selected regions:

| Offset | Length |
| --- | ---: |
| `0x0000` | 8 bytes, two big-endian length fields |
| `0x1000` | 28,068 bytes |
| `0x9000` | 6,672 bytes |

Hashing the 34,748 concatenated bytes yields the declared SHA-256:

```text
792a4a0dd8474f3dfa7b9883bbc2c73ceff296b63ff6fdf4ba4e272ff0324313
```

Nearly all excluded bytes are FF, but offset 43,536 is D1; the report does not call every excluded byte padding or claim the digest protects it. Whole-file official identity remains separate coverage of the outer file.

`AppleTCONDP855RestoreInfoCreateRequest` retrieves and forwards the declared digest (`0x27e68–0x27ef1` in the examined libauthinstall trace). That call sequence does not calculate the region digest. Offsets were inferred and validated for this artifact; the device-side verifier and generality across other DP855 versions remain unresolved.


<a id="efi-signatures-and-productefi"></a>
## EFI signatures and Product.efi

<a id="apple-format-pe-efi-signatures"></a>
### Apple-format PE EFI signatures

The eight-byte PE security-directory records point to larger Apple certificate structures; they are not eight-byte signatures. Each examined slice points to a bounded 552-byte structure containing a modulus and signature.

All 69 slices verify using the Apple-format signed ranges, RSA2048/SHA-256 and PKCS#1 v1.5 with exponent 65537 and the expected byte order. Exclusions include the DOS stub, PE checksum, security-directory entry and signature trailer. Every slice rejects a changed-digest negative control; a representative independent OpenSSL cross-check also passes.

The shared public-modulus fingerprint is:

```text
c7a1b9362880de695762b7b65bec6bf156a55cf9247f22ef786235537f952b45
```

It matches the Apple public key published in OpenCore's reference database; it is not evidence that OpenCore signed these files or was installed. Format and hashing references: [OpenCore implementation](https://github.com/acidanthera/OpenCorePkg/blob/2cc2362d3a2cfec2ad66a752603bb4a5ee092d78/Library/OcPeCoffExtLib/OcPeCoffExtLib.c) and [Apple certificate structures documented by that project](https://github.com/acidanthera/OpenCorePkg/blob/2cc2362d3a2cfec2ad66a752603bb4a5ee092d78/Include/Apple/Guid/AppleCertificate.h). This is not generic Authenticode verification or proof of every loader policy.

<a id="productefi-wrapper"></a>
### Product.efi wrapper

Product.efi is excluded from the 69 PE successes. It lacks an observed MZ/PE header and begins with wrapper magic `2112feef dccdbaab`. Its 9,424 bytes comprise a 16-byte header, declared 9,152-byte encrypted region and 256-byte trailer.

SHA-256: `7bec2443520692bcfae58f9410862f0f35e23fce4ca40f7f42a06fdd1fc42bdc`.

The verified diags.efi recognizes the magic and calls a decode routine. The routine requests 32 bytes from runtime variable `application-runtime-data`, vendor GUID `71f5207a-b3a8-4107-bb52-f52cbbb5f8e6`, before block decryption. Calls and structure offsets correspond to UEFI GetVariable; [EDK2 runtime-service definitions](https://github.com/tianocore/edk2/blob/6abc1c06585ffd66d23a74811a930d8d0f88cef7/MdePkg/Include/Uefi/UefiSpec.h) corroborate the layout.

The trace uses 16-byte blocks, reads the final plaintext byte as a padding count and adjusts the returned length. Exact cipher behavior, padding validation, trailer authentication and downstream authorization are not fully traced. No runtime material or plaintext was collected, and no keys were requested.

LLVM initially rejected diags.efi's debug-directory layout. A separate derivative clears only the eight-byte debug-directory entry at file offset 312 for disassembly. Original/derived hashes and the transformation are recorded. Signature conclusions apply to original bytes, not the derivative.


