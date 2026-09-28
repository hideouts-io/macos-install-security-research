---
layout: default
title: "PSF flashers, launcher, bless, and MultiUpdater"
---

# PSF flashers, launcher, bless, and MultiUpdater

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

The Stage 6F.6 coverage and next-segment statements near the end of this page are **historical checkpoint notes**. Stage 6F.7 has since begun; the [current counts and next action](audit-status.md) supersede those checkpoint figures.

![Bounded firmware updater and flasher handoff](../diagrams/firmware-handoff.svg)

The [editable Mermaid source](../diagrams/firmware-handoff.mmd) distinguishes compiled helper-name selection from downstream loader and device-firmware acceptance; the latter remains unobserved.

<a id="psf-efi-flasher-and-all-packaged-psf-payloads"></a>
## PSF EFI flasher and all packaged PSF payloads

Stage 6F.3 covers both directories and all four files under `UpdateBundle/AssetData/boot/EFI/PSFFirmware/`. **FW-007** records the nested payload checks and **FW-008** records the selected EFI execution/PCI transport paths. All four files freshly match their retained hashes and the exact Apple-reference comparison. This is a separate pre-OS route from the RAMDisk PFX library.

| Object | Bytes | Format and role | SHA-256 |
| --- | ---: | --- | --- |
| `PSFFlasher.efi` | 72,400 | x86-64 PE32+, subsystem 10 / EFI application; updater | `7471de9f4d8ec39a1e6d651a964c7115d26aeeb836dd01f5739a2aeda31549b3` |
| `Payloads/bl2_prod_signed_Nv21_0370004f.fwimg` | 150,528 | Vendor type 2, second-stage switch bootloader | `5633beb54a3053876c26aa6c43957880f7855ae99139898acb29bfe18b74e5e2` |
| `Payloads/cfg_prod_signed_Nv21_00080000.fwimg` | 36,992 | Vendor type 3, switch configuration | `41265b8437593a4a8134a0f4f00694128c2ee49152532b4cd19343144330b54e` |
| `Payloads/pfx_prod_signed_Nv21_0370004f.fwimg` | 1,849,088 | Vendor type 4, main switch firmware | `eec38f06e808b6b7c0817c2f929ec3480c35ec8f4db3d995af6ff22bffd8294a` |

The outer directory pairs the EFI updater with its resources; `Payloads/` contains exactly the three inventoried firmware files above. No additional descendant in either inventoried directory was silently omitted. The RAMDisk PFX directory is separately accounted. Directory accounting is not complete semantic closure of their children. The copied source files have mode `0644`, uid 501 / gid 20 and no recorded xattr names; these are copy metadata, not proof of original installed-system write permissions. Firmware data does not have Mach-O entitlements. The processor/ISA and complete executable semantics of the inner bootloader and main-firmware bodies remain unresolved.

Each PSF payload has the same bounded metadata/CRC/signature/padding/body layout as the vendor image above. **All six declared CRCs pass.** Header version is 1 and the firmware version field is `0x0370004f` in all three. The configuration filename ends in `00080000`; the flasher contains a separate filename parser that reads eight hexadecimal characters after the final underscore (`0xbc81`, called at `0xbda4`). These values must not be treated as interchangeable version fields. Complete comparison/selection semantics still need review.

Each payload yields a well-formed 4,096-bit RSA PSS/SHA-512 encoding under its embedded key. **All three PSF keys differ from one another and from the PFX configuration key.** Key roles, accepted key manifests, device fuses and the exact signed message are not yet established; no firmware-authentication verdict is assigned. Type labels and header completeness do not substitute for disassembly of the inner firmware bodies.

<a id="efi-identity-and-pre-os-workflow"></a>
### EFI identity and pre-OS workflow

The flasher's PE entry RVA is `0x8d67`, image base zero. The generic `file` utility's “for MS Windows” wording does not override the EFI subsystem field. There is no normal PE import directory; examined system/device calls go through firmware tables and protocols. Stage 3B already verified this exact hash's Apple EFI RSA-2048/SHA-256 signature and rejected its negative control. That prior result is explicitly linked here; it is separate from the nested switch-image signatures.

The retained selected trace has **15 bounded ranges / 1,841 original-byte-checked instruction records**. Exact range starts avoid jump-table bytes that a whole-section linear listing misdecodes. The full linear listing is retained as a search aid and is not counted as fully analyzed code.

The entry invokes its setup and argument helper, then the main routine at `0x9b03` through call `0x8eb2`. Main has branches for current/proposed versions and platform configuration, calls the download routine `0xb582`, accumulates a successful-download mask and conditionally invokes the partition-toggle routine `0xba70` at `0xa503`. This establishes firmware-update capabilities in the EFI environment. The macOS component that schedules this EFI application, argument authority and actual execution history remain unproven.

The download routine reads the selected file, computes the body CRC using the header's length and compares it to the stored CRC at `+0x54`. A mismatch exits through an error path before the data-transfer loop. Its **256-word CRC table at `0xc480` exactly matches the pinned vendor implementation**, independently linking the container analysis to actual flasher code. The payload transfer sends the complete file in chunks up to `0x3f0` bytes, with offsets and total size in the request. Local header-length/file-length arithmetic and complete malformed-input handling still require review.

<a id="pci-mailbox-transport-and-error-boundaries"></a>
### PCI mailbox transport and error boundaries

The enumeration path uses the original GUID `4cf5b200-68b8-4ca5-9eec-b23e3f50029a`, identifying `EFI_PCI_IO_PROTOCOL`; it reads PCI configuration and compares vendor ID `0x11f8`. The examined protocol calls match the pinned EDK2 structure: `+0x10` memory read, `+0x18` memory write, `+0x30` PCI configuration read, and `+0x38` PCI configuration write. One branch writes value 6 to PCI command offset 4, requesting memory-space and bus-master enables. This is a hardware-access capability, not evidence that DMA or a firmware change occurred. [EDK2 PCI I/O protocol](https://github.com/tianocore/edk2/blob/6abc1c06585ffd66d23a74811a930d8d0f88cef7/MdePkg/Include/Protocol/PciIo.h).

The transaction helper `0xae7e` calls request `0xac16`, poll `0xad1c`, and response `0xad9f`. The request writes 32-bit units through BAR 0: input at offset 0, status at `0x804`, another control word at `0x80c`, and a command word at `0x800`. Download uses command **5**. Poll waits for status 2; response reads the device return code at `0x808` and, when requested, output at `0x400`. These offsets and command meanings correlate with the vendor's MRPC register layout and firmware-download enum. [Vendor registers](https://github.com/Microsemi/switchtec-user/blob/c5aac7b5c36e9ea0ef04112365833826c0a6391a/inc/switchtec/registers.h), [vendor commands](https://github.com/Microsemi/switchtec-user/blob/c5aac7b5c36e9ea0ef04112365833826c0a6391a/inc/switchtec/mrpc.h).

The local request routine discards individual `Mem.Write` return statuses; the transaction subsequently evaluates poll and device return results. Thus it is not accurate to describe the path as either checking every I/O return or having no error handling. Whether an ignored early I/O failure can yield misleading completion requires further analysis. The payload-version and hardware-selection branches also need their complete input provenance. These are Q35 review items, with no exploit or severity assigned.

The observed path is PCI memory-mapped I/O. Generic USB/DFU device-path formatting strings elsewhere in this EFI image do not establish a USB transport, usbmux session or historical DFU event.

<a id="temporary-efi-status-exchange"></a>
### Temporary EFI status exchange

The runtime-table initializer at `0x227c` loads `SystemTable+0x58` into the retained runtime-services pointer. Main calls its `SetVariable` slot `+0x58` at `0xa6a1` and `0xa6d6`, passing `PSFF_STATUS` and `PSFF_MESSAGE`, eight bytes of data, and attributes **2**. The entry has corresponding `GetVariable` calls before its EFI exit path. The message value is an eight-byte pointer to a prepared message buffer in this examined flow, rather than a persistent copy of that entire message.

UEFI defines attribute 2 as `EFI_VARIABLE_BOOTSERVICE_ACCESS`; the calls do not request nonvolatile or runtime-access attributes. This supports a temporary pre-OS status/result exchange. It does not establish an NVRAM persistence mechanism, changes to Apple LocalPolicy, SSV sealing, or Secure Boot databases. [UEFI variable services](https://uefi.org/specs/UEFI/2.11/08_Services_Runtime_Services.html#variable-services).

**Segment outcome:** every PSF directory descendant has a bounded record; all four exact-reference comparisons and all six payload CRCs pass. The signed Apple EFI flasher has a concrete pre-OS PCI firmware-write route, with separate download/toggle and temporary status handling. Device authentication, inner firmware code, argument authority, selection/downgrade semantics and malformed-input/I/O-error handling remain open. No local tampering, actual flashing or startup-security change is established.


<a id="psf-input-authority-bounds-and-device-query-errors"></a>
## PSF input authority, bounds and device-query errors

Stage 6F.4 follows the same exact-reference-matching `PSFFlasher.efi` into its input providers and error paths. **FW-009–FW-011 are static code-review findings, not demonstrated exploits or evidence of tampering.** The new trace contains 21 selected ranges and 1,306 original-byte-checked instruction records, and rechecks the earlier 1,841 records. Some ranges contain adjacent helper bodies. No EFI code, malformed input, PCI transaction or firmware payload was executed.

<a id="inputs-and-selection-decisions"></a>
### Inputs and selection decisions

The entry obtains `EFI_LOADED_IMAGE_PROTOCOL` and reads `LoadOptions` at offset `+0x38`. Its helper at `0x8ef9` treats the options as a terminated UTF-16 string, passes it to a formatter with the `%ls` format, then splits the resulting byte string on spaces. `LoadOptionsSize` at `+0x30` is tested for zero, but is not used as the bound for the subsequent string traversal. The protocol and member meanings come from the [UEFI Loaded Image specification](https://uefi.org/specs/UEFI/2.11/09_Protocols_EFI_Loaded_Image.html); the offsets, calls and parser behavior are verified in this binary.

**FW-009** records the following parser routes at `0x9550`. They describe capabilities; the actual authorized producer of these inputs remains unidentified.

| Input | Verified local effect | Boundary that remains open |
|---|---|---|
| `-d` | Sets the debug-output flag at RVA `0x11460` | Who supplies load options |
| `-f` | Sets the force-update flag at `0x11461` | Host selection policy is separate from device signature/rollback enforcement |
| `-v` | Sets the version/display flag at `0x11462`; main has a branch that skips the payload-update selection path | This is not proof that every earlier hardware access is skipped |
| `-g` / `-s` | Parses the next token as a decimal integer and uses it as an index into the target-selection table at `0x10fa0` | Valid index range is not checked in the local parser |
| `-p` | Converts the next token into a UTF-16 payload pathname and appends its pointer to the payload list | Path length, list count and availability of the next token |
| Token starting with the 15-character `efi-apple-payload` prefix | Uses the full converted token as an EFI variable name, reads its value under GUID `7c436110-ab2a-4bbb-a880-fe41995c9f82`, and extracts a file-path device node | Variable writer, attributes, access policy, value integrity and path provenance |

The last route calls `GetVariable`; it does not set the input variable. It passes a null attributes-output pointer, so this parser does not inspect the returned variable's authentication attributes. On `EFI_BUFFER_TOO_SMALL` it allocates using the returned length and tries again. A separate local issue is that the first call passes `DataSize` at `[rbp-0x48]` without an earlier initialization visible in the complete parser body, despite allocating 512 bytes for the initial data buffer. This is an uninitialized input-length finding; its actual value and runtime consequence are unknown.

Payload selection at `0xbcdb` constructs a pattern from `cfg_`, `pfx_`, `bl2_` or `keym_`, a signing label, and a target suffix. The target table contains `_Nv21` and `_MLB`; the signing table contains `dev_signed` for selectors 0 and 1, and `prod_signed` for selector 2. The search takes the first input pathname containing the pattern as a substring. This is not whole-basename validation or signature verification. The version helper at `0xbc81` scans backward to the last underscore, copies eight UTF-16 code units, and converts a hexadecimal prefix. No local check establishes that eight characters remain after that underscore.

Main's comparison at `0xa314` downloads when the proposed filename-derived version exceeds the device-derived value, or when the force flag is set. Separate configuration transition conditions can clear the force flag; therefore `-f` is not an unconditional override of every host decision. None of these comparisons establishes the device's anti-rollback or firmware-authentication policy. The packaged configuration's filename version and its header version remain distinct fields.

<a id="file-providers-and-malformed-input-boundaries"></a>
### File providers and malformed-input boundaries

The file wrapper at `0xb1c3` builds a device path using the loaded image's device handle and the selected filename. The reader at `0x902d` contains firmware-volume, simple-filesystem, LoadFile2 and LoadFile routes, identified through their original protocol GUIDs and method-table offsets. The wrapper requests false `BootPolicy`. On the filesystem route it opens for reading, obtains `FileSize`, allocates a buffer and reads into it. The firmware-volume route accepts an authentication-status output, but the selected caller does not inspect that output locally. These are UEFI file-provider interfaces, whose existence does not establish network boot, USB traffic or unauthenticated platform loading. See the [UEFI media-access protocols](https://uefi.org/specs/UEFI/2.11/13_Protocols_Media_Access.html) and the pinned EDK2 headers in the private evidence.

**FW-010** records concrete missing local checks. These are important because this application executes before the normal macOS user environment. Reachability by a lower-privileged or untrusted producer has not been established.

| Boundary | Original-byte evidence | Assessment |
|---|---|---|
| Argument pointer array | Allocates 512 bytes at `0x8f90–0x8f95`; loop stores eight-byte pointers at `0x8fdc` and increments the count without a 64-slot check | Excess token counts are not locally bounded |
| Payload pointer array | Main allocates 96 bytes at `0x9b41–0x9b46`; parser appends pointers without a 12-slot check | Excess payload counts are not locally bounded |
| Target index | `0x9693–0x96a6` converts the next token to a signed integer and writes `table[index] = 1` | No local sign/range check or next-token availability check |
| Path buffers | Parser allocates 512 bytes; `0xafc2` copies byte characters into UTF-16 until the terminator; the EFI-variable route uses the terminated-string copy at `0x1855` into the same allocation size | Neither copy receives a 256-code-unit destination capacity; null/alignment/overlap assertions in the latter do not establish that capacity |
| EFI variable's initial buffer size | First `GetVariable` receives an uninitialized local `DataSize`; the retry uses the returned size | Initial buffer capacity is not reliably communicated by this parser |
| Firmware header/body | `0xb69c–0xb6b6` reads the 32-bit header length at `+0x10`, advances the pointer, subtracts that length from the low 32 bits of file length, and calls the CRC walker | No preceding local minimum-header-length or `header_length <= file_length` check on this examined route; subtraction can wrap for malformed values |
| Body CRC field | Reads `file+0x54` at `0xb6ca`; later signed-positive file-length check occurs at `0xb6e8`, after the CRC traversal | Later checks do not protect these earlier reads |

The three packaged payloads are structurally consistent, use a 4,096-byte header and passed all six CRC checks in Stage 6F.3. Their actual sizes do not trigger the malformed-length conditions described above. A CRC is a corruption check, not authentication. The findings therefore identify parser contracts requiring investigation; they do not identify a corrupt packaged firmware image.

The PCI mailbox error path also deserves review. Request writes in `0xac16` discard individual `Mem.Write` return statuses. Polling at `0xad1c` handles `EFI_TIMEOUT` explicitly but does not treat every other EFI error as failure before interpreting the status output. The response helper at `0xad9f` ignores the return from the initial return-code-register read before consulting its retained value; its later output-buffer read does return a status. The outer transaction checks helper results. Thus later polling/device error handling exists, but does not prove that every earlier transport failure is preserved. No injected I/O failure or successful firmware write was observed.

<a id="a-failed-query-can-be-classified-as-unfused"></a>
### A failed query can be classified as “UnFused”

**FW-011** is a conditional error-propagation finding in the signing-label selector at `0xbf3a`:

1. Set the output selector to 3 and zero an 88-byte response buffer (`0xbf56–0xbf6e`). The memory-fill helper is separately byte-checked.
2. Call the security-configuration query at `0xbf79`. Its wrapper at `0xc139` requests vendor command `0x101` and 22 output words through the previously traced transaction helper.
3. Ignore the returned status and copy the 64 bytes starting at response offset `+0x18`. The intervening helper at `0xbeed` displays these words; it does not repair a failed query.
4. Compare those bytes against two compiled constants. A complete production match chooses 2; a development match chooses 1; all zeros choose 0 and print `Switch is UnFused`. A nonzero unknown value returns an error.

If the transaction fails before filling the response, the cleared bytes remain zero and this selector reports success through the “UnFused” branch. Selector 0 maps to the `dev_signed` filename label. This follows statically from the buffer initialization, unchecked query result and comparison branches; it is not a captured device event.

The host label does not burn or clear fuses, change Secure Boot, authenticate a payload, or compel the switch to accept an image. The available PSF payloads are named `prod_signed`; misclassification may instead leave no matching payload. Device-side key acceptance, key-manifest policy, the exact signed message and the actual caller's input authority remain unresolved. Consequently no exploitability score or signature-bypass claim is assigned.

**Segment outcome:** load-option and EFI-variable consumers, filename/version decisions, file providers, missing local bounds and transport/query error handling are now traced. The unchanged, Apple-reference-matching file contains security-relevant error and input contracts that warrant deeper review. Expected UEFI protocols and valid packaged length/CRC values remain consistent with an ordinary peripheral updater. The precise next segment is the upstream launcher/variable producer and the controller's key/signed-message/inner-firmware boundary. All earlier SSV, Recovery, Preboot, services, nested-container and metadata queues remain open.


<a id="firmwareupdatelauncher-and-the-upstream-staging-workflow"></a>
## FirmwareUpdateLauncher and the upstream staging workflow

Stage 6F.5 advances the producer search into the Intel BaseSystem. **FW-012** records a concrete generic EFI staging workflow and a compiled PSF association; it does not establish that this workflow ran on the examined Mac. Two fresh read-only acquisitions used the reconstructed BaseSystem whose SHA-256 equals the independent official reconstruction. Both image attachments were detached successfully.

| Artifact in Intel BaseSystem | Size | SHA-256 | Bounded result |
|---|---:|---|---|
| `usr/libexec/FirmwareUpdateLauncher` | 68,224 | `b0d6a3d243f190c7e27a00cb489b6fe7660857307ef76ccba7e6f0df206c085c` | Ten selected functions/ranges, 2,361 byte-checked instructions; 179 metadata-reference displacements checked |
| `usr/libexec/efiupdater` | 53,232 | `28e0ae3a93a439cc77594decb896a1f8be7d30b65eb19ab3442166c751cf8278` | Hash, Mach-O, imports, strings, signing and Objective-C metadata acquired; full workflow still pending |

Both are thin x86-64 Mach-O executables, match their original inventory hashes, and pass fresh strict signature verification with the Apple macOS Software Signing chain. No entitlement payload was printed. This does not confer root access or establish runtime authorization. Their bytes originate from the exact-reference-matching BaseSystem, and neither was executed during this investigation.

<a id="from-helper-output-to-boot-staging"></a>
### From helper output to boot staging

`FirmwareUpdateLauncher` has a `BlessData` Objective-C class with original methods for initialization, option adjustment, payload-index adjustment, option serialization and NVRAM requests. Main is identified by `LC_MAIN` at unslid address `0x1000030fe`. The trace distinguishes these steps:

1. Main locates `MultiUpdater.efi` under the supplied firmware directory and discovers updater helpers. The default helper-directory constant is `/usr/libexec`; command-line options can select a directory. The full directory trust and invocation policy are still open.
2. The preparation function at `0x100002529` forms the child arguments `-p <directory> -s`. The child runner at `0x100002388` configures an `NSTask`, captures stdout, waits for termination, and parses property-list data. The preparation route accepts an array result or wraps a dictionary as an array. This identifies a producer/consumer contract, not the PSF helper's implementation.
3. `-[BlessData initWithDictionary:updater:]` reads `Priority`, `Retry` and `BlessArguments`. It recognizes `-payload`, `-firmware` and `-options`; normalizes paths; checks that referenced flasher and payload paths exist; and retains `SetNVRAM` / `ClearNVRAM` requests. Existence checks alone do not prove content authentication or trusted ownership.
4. `updatePayloadIndices:` recognizes the `efi-apple-payload` prefix, reads its numeric index, adds a caller-supplied offset, and formats `efi-apple-payload%ld-data`. `optionsString` joins option tokens. This produces the variable-name form consumed by the EFI parser examined in Stage 6F.4.
5. The assembler at `0x1000027ac` sorts updater descriptions and builds arguments including `-mount /`, `-folder MULTIUPDATER`, `-firmware`, payload entries and serialized options. Its executable-path global resolves through the original fixups to `/usr/sbin/bless`. The ordinary task-launch branch starts that program and checks its termination status; a separate dry-run branch logs the proposed command.
6. The subsequent flow requests multi-updater state handling and calls each description's `updateNVRAM`. The method contains `IORegistryEntrySetCFProperty` calls for deletion requests through `IONVRAM-DELETE-PROPERTY` and for dictionary-supplied property values. These calls request changes through the kernel interface; their presence does not establish that the kernel permits an arbitrary caller or variable.

This narrows the workflow to **updater helper → structured description → launcher option/payload assembly → `bless` staging → EFI consumer**. The next section advances the `bless` device-path writer and MultiUpdater child-launch analysis. The helper implementation and kernel-side variable access rules remain open before treating this as a fully established PSF authorization chain. `SetNVRAM` / `ClearNVRAM` in a generic helper description also must not be confused with the separate, boot-service-only `PSFF_STATUS` and `PSFF_MESSAGE` outputs of the EFI flasher.

<a id="what-the-psf-association-proves"></a>
### What the PSF association proves

A compiled constant dictionary contains `brief = P`, `flasher = PSFFlasher.efi` and `updater = psfupdater`. The original pointer slots, strings and fixups are retained. This is evidence that the launcher knows the PSF component names. It is not, by itself, proof that the PSF helper was found, that it emitted any particular `BlessArguments`, or that a flash occurred.

An exact-basename search of all 147,253 canonical inventory objects finds `FirmwareUpdateLauncher`, `efiupdater`, `bless` and several copies of `MultiUpdater.efi`, but **no inventoried path named `psfupdater`**. This is a scope-specific gap, not evidence of deletion or compromise: unexplored nested containers, another installed-system component or a different input source remain possible. The same `bless` hash is inventoried in the Intel BaseSystem and RAMDisk; the next section follows that exact binary. No collected executable was run, including in its advertised dry-run mode.

The adjacent `AppleFirmwareUpdate` framework was also acquired as 100,166 bytes of selected original regions and tables from the inventory-verified `.01` shared-cache companion. An initial main-cache-only attempt failed because its address lay outside that file's mappings; the failure is preserved, and explicit companion acquisition resolved it. Symbols describe early-boot accessory/update services. It remains a separately queued component; this acquisition does not establish a call from the PSF launcher or complete framework semantics.

**Segment outcome:** two additional paths have bounded records, the generic helper-to-`bless` route is traced, and the producer gap is narrower. These are expected but security-sensitive Apple components. No new package modification, unauthorized firmware write or security-policy bypass is demonstrated. The following section traces the exact matching `bless` firmware/payload writer and `MultiUpdater.efi` child handoff; PSF helper provenance and device-side firmware trust remain open.


<a id="bless-and-multiupdater-boot-handoff"></a>
## bless and MultiUpdater boot handoff

Stage 6F.6 follows the exact programs queued by the launcher analysis. **FW-013–FW-015** cover a bounded userspace-to-EFI handoff, its verification requests, and two error-reporting gaps. The reconstructed Intel BaseSystem was attached read-only, the inventoried `usr/sbin/bless` was copied and hash-checked, and the attachment was detached. Three source paths containing the identical MultiUpdater were independently rehashed. No collected executable, EFI application or firmware payload was run.

| Artifact | Size and architecture | SHA-256 | Provenance and status |
| --- | --- | --- | --- |
| Intel BaseSystem `usr/sbin/bless` | 255,568 bytes; x86-64 Mach-O | `f38a45c0ef8554c74668c9889cbbe8bdaf56754b09ad220092101f7b31c07fcf` | Inventory match from exact-reference-matching image; fresh strict Apple signature verification passes |
| `MultiUpdater.efi` | 102,968 bytes; x86-64 PE32+ EFI application | `699cd1a833827a701c589ae0655bc9191fa39daff94d011ca5a1b62b0ce8a9f0` | All three source copies match the prior exact official comparison and hash-linked Apple EFI signature verification |

The three MultiUpdater source locations are `UpdateBundle/AssetData/boot/EFI/MultiUpdater/`, `UpdateBundle/AssetData/boot/Firmware/MultiUpdater/` and `UpdateBundle/AssetData/boot/Firmware/usr/standalone/firmware/FUD/MultiUpdater/`. Their common bytes support grouped behavioral analysis while retaining three separate path records. Copied source ownership `501:20`, mode `0644`, is metadata about the examined copy; it does not identify EFI runtime privilege. The BaseSystem `bless` inventory records owner/group `0:0`, mode `0755`.

<a id="privileged-userspace-staging"></a>
### Privileged userspace staging

**FW-013.** `bless` identifies as `com.apple.bless` and verifies through macOS Software Signing, Apple Code Signing Certification Authority and Apple Root CA. Its signed entitlements include `com.apple.private.IASInstallerAuthAgent`, `com.apple.private.bootability`, `com.apple.private.iokit.system-nvram-allow`, `com.apple.private.security.bootpolicy`, `com.apple.private.vfs.snapshot`, `com.apple.rootless.internal-installer-equivalent`, and a private TCC allow list containing `kTCCServiceSystemPolicyRemovableVolumes`. These explain why this is a security-sensitive installer utility. They do not establish that an arbitrary caller can perform every operation, that these rights were exercised, or that the examined Mac's boot policy changed.

The selected trace contains **six ranges and 1,915 original-byte-checked instruction records**, with ten resolved CFString references and 139 import-callsite checks. It excludes the entry function's `LC_DATA_IN_CODE` jump tables from instruction decoding. The firmware dispatch at unslid `0x10000a742` enters the EFI staging function at `0x10000aa2b` when its environment check selects that backend. Other legacy and APFS pathways remain separate work.

For payloads, this backend constructs `efi-apple-payload%d` keys and calls the copy/staging function at `0x10000d1e1`. That function traverses the selected source using `fts`, handles files/directories, and passes the staged destination to `0x100014646`. The latter resolves the path, obtains filesystem context, constructs a relative EFI media path, changes path separators, and assembles dictionaries containing `IOEFIDevicePathType`, `MediaFilePath`, `Path` and, when supplied, `IOEFIBootOption`. It serializes these with `IOCFSerialize` and returns a string representation.

The EFI backend adds these values to its property dictionary and obtains `IODeviceTree:/options`. At `0x10000b88b` it calls `IORegistryEntrySetCFProperties`; a nonzero result follows an explicit error path. A separate removal branch uses `IONVRAM-DELETE-PROPERTY`. The generic single-value writer at `0x10001dc9b` also checks the result of `IORegistryEntrySetCFProperty`. This establishes a request to the kernel interface, not the kernel's authorization decision.

**Open boundary:** this `bless` trace produces serialized path/option properties named without the `-data` suffix. MultiUpdater consumes binary device-path variables with that suffix. The precise kernel/platform conversion and access-control implementation still need same-build corroboration. A “Not run as root” string elsewhere in `bless` has not been established as a gate on this firmware branch, so it is not used to claim one here. Weak dependencies on Bootability, libbootpolicy, libimg4 and libauthinstall likewise do not substitute for tracing the selected branch.

<a id="efi-child-selection-and-verification-requests"></a>
### EFI child selection and verification requests

**FW-014.** MultiUpdater's PE entry is RVA `0xe50b`. The selected analysis covers **21 ranges and 1,401 instruction records**, all checked against the original EFI bytes. LLVM rejected the original debug-directory layout as uneven. The retained decoder copy clears only the eight-byte debug-directory entry at file offset 312; its SHA-256 is `391807b5d15e99d36746dab9e3ec17bf7bdb19482be888d50e8a52f5a438bde4`. This derivative is explicitly marked as analysis-only and is not treated as signed Apple evidence. The original hash and prior signature result remain intact. The layout rejection alone is not a tampering finding.

The entry initializes Boot Services and Runtime Services from the supplied EFI System Table. Its main function locates a required protocol with GUID `6c6148a4-97b8-429c-955e-4103e8aca0fa` and an optional protocol with GUID `24b73556-2197-4702-82a8-3e1337dafbf2`. The published upstream definitions identify these as Apple LoadImage and Apple Secure Boot. These references are pinned in the evidence, with the distinction between observed GUID/call offsets and externally reconstructed semantics retained. [Apple LoadImage definition](https://github.com/acidanthera/OpenCorePkg/blob/6fe4d15cb66596d99d8cfedce69d8fc6dad71886/Include/Apple/Protocol/AppleLoadImage.h), [Apple Secure Boot definition](https://github.com/acidanthera/OpenCorePkg/blob/6fe4d15cb66596d99d8cfedce69d8fc6dad71886/Include/Apple/Protocol/AppleSecureBoot.h).

The data flow is:

1. The enumerator at `0xcdc3` tries `efi-apple-payload0-data` through index 99 in the Apple variable namespace `7c436110-ab2a-4bbb-a880-fe41995c9f82`, stopping at an error. `EFI_NOT_FOUND` terminates enumeration as a normal end condition. The variable reader initializes the requested size to zero, allocates after `EFI_BUFFER_TOO_SMALL`, and retries. This differs from the earlier PSFFlasher uninitialized-size finding.
2. MultiUpdater obtains its own LoadedImage options and tokenizes them. The tokenizer at `0xe33f` handles whitespace/parenthesis groups and checks a 128-token ceiling before storing another token. Main forms updater name/options pairs; full malformed and odd-pair analysis remains open.
3. The matching function at `0xd3d5` compares each requested updater name with names reconstructed from enumerated payload device paths. On a match it calls `0xcfe1` with the parent handle, device path and updater record.
4. If the optional Secure Boot protocol exists, the child loader requests its policy. A policy-query error returns without loading. When the policy byte is nonzero, the caller tries verification against seven object types: `thou`, `hpmu`, `gpuu`, `ethu`, `sdfu`, `dthu`, and **`psfu`**. If all return EFI errors, the caller returns the failure. The `psfu` constant is observed directly in this binary; it is not supplied by the older upstream type list.
5. The caller then invokes the Apple loading protocol with a callback at `0xcfdb` that returns one. The upstream callback definition interprets true as requesting image-signature verification. Missing/zero optional Secure Boot policy therefore does not, by itself, demonstrate an unsigned-load path: the Apple loader is still called with this callback. The actual firmware implementation and its enforced trust anchors remain unexamined.
6. After loading, MultiUpdater obtains the child's LoadedImage protocol, sets `LoadOptionsSize` at offset `0x30` to the UTF-16 byte count including terminator, allocates/copies the options, and sets `LoadOptions` at offset `0x38`. It calls Boot Services `StartImage` at `0xd1af`, retaining status and exit-data fields. These field and service layouts agree with the standard ABI. [LoadedImage structure](https://github.com/tianocore/edk2/blob/6abc1c06585ffd66d23a74811a930d8d0f88cef7/MdePkg/Include/Protocol/LoadedImage.h), [UEFI service tables](https://github.com/tianocore/edk2/blob/6abc1c06585ffd66d23a74811a930d8d0f88cef7/MdePkg/Include/Uefi/UefiSpec.h).

**OpenCore attribution:** using OpenCorePkg's published Apple protocol definitions as reverse-engineering references does not show that OpenCore is installed, embedded, or running here. The observed MultiUpdater GUIDs identify interfaces implemented by Apple firmware as well. This artifact's exact official-byte match and Apple EFI signature are distinct provenance evidence. Any claim of a separately installed OpenCore bootloader still requires an actual bootloader/configuration artifact and boot-chain corroboration; protocol names shared with the research project are insufficient.

<a id="retry-state-results-and-error-reporting-limits"></a>
### Retry state, results and error-reporting limits

The state reader validates minimum lengths, version one, matching updater count and a valid resume index before copying saved counters. Main increments attempt counters and invokes each selected updater. A retry-limit check bounds ordinary retries; status zero and the special value `0xc8` advance to the next updater in the examined branch. The special value's device-specific meaning is not established here.

`multiupdater-state`, per-attempt `multiupdater-%d-%d` results and `multiupdater-start-timestamp` use `SetVariable` attributes **7**, requesting nonvolatile, boot-service and runtime access. This is persistent update bookkeeping, distinct from PSFFlasher's attributes-2 status/message outputs. It is not evidence of malware persistence. The completion route calls a helper containing Runtime Services `ResetSystem` with reset-type value **2**, which the standard defines as shutdown; the diagnostic's “Restarting” wording must not be substituted for the actual argument. The helper also makes preceding vendor-protocol calls whose hardware effects remain open.

**FW-015.** At `0xd3d5`, the unmatched-search path initializes/returns zero when it exhausts available payloads. Only a matched child reaches the loading call. Therefore a zero return from this helper alone is insufficient evidence that an updater actually ran. Separately, the resume-state writer calls `SetVariable` at `0xd624` and then frees its buffer without testing that write result. Main also ignores the return from the per-attempt result writer at `0xdb48`. A failed state/result write could impair reporting or retry continuity, but that consequence is an interpretation requiring reachable inputs and platform behavior; no failure was injected. No arbitrary code execution, successful flash or boot-security bypass is demonstrated.

**Segment outcome:** four additional inventoried paths receive partial semantic records. The staging and child-execution relationship is materially clearer, while kernel conversion/authorization, helper provenance, actual loader policy and device trust remain explicit gaps. The Apple reference/signature matches and standard EFI field usage are expected. The unmatched-child zero return and ignored write results remain follow-up findings. SMC/other protocol setup, complete parser/device-path bounds and downstream trust behavior have not been declared finished.

**Coverage at the Stage 6F.6 checkpoint:** 63 distinct inventoried paths have bounded semantic records, plus four previously tracked embedded components. The 147,253-row register contains 21 detailed twelve-field records, 42 other bounded prior records and 147,190 rows awaiting semantic reconciliation. There are 94 finding entries. No whole-artifact closure is inferred from these bounded passes.

**At the Stage 6F.6 checkpoint, the next segment was Stage 6F.7** — kernel EFI-path conversion and NVRAM authorization, followed by launcher helper discovery/acceptance and MultiUpdater error reachability. That work is now [partially documented](nvram-efi-paths.md). The inner firmware signed-message/key/ISA work and earlier PFX, restore, ramrod/SSV, ARM, Recovery/Preboot, cryptex, services, nested-container, metadata and protected-path queues remain open.

