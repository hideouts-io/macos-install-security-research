---
layout: default
title: "PFX personalization and device handoff"
---

# PFX personalization and device handoff

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

<a id="pfx-firmware-personalization-and-device-interface-boundaries"></a>
## PFX firmware personalization and device-interface boundaries

Stage 6F.1 follows the remaining RAMDisk `usr/lib/updaters/libPFXUpdater.dylib` reference into its command dispatcher, Objective-C subclasses, personalization callbacks and IOKit endpoint initialization. **NET-012** establishes a PFX-specific local-signing branch alongside generic remote-personalization machinery. **NET-013** establishes the initial kernel-interface path. Neither finding establishes execution on this Mac, a firmware modification, an unsigned-image acceptance path or a change to startup security.

<a id="identity-provenance-and-method-resolution"></a>
### Identity, provenance and method resolution

The 248,448-byte x86_64 dylib has SHA-256 `cb046aeafb05ddeab17a02687a007e9af78fd95afee18bcb72642ef205d9aa0a`. Its retained bytes match the RAMDisk inventory; that RAMDisk matches the exact official update as documented above. Fresh strict `codesign` verification passes. The identifier is `com.apple.libPFXUpdater`, with the macOS Software Signing → Apple Code Signing Certification Authority → Apple Root CA chain. No entitlement payload was printed. The load commands name Foundation, CoreFoundation, IOKit, libobjc, libSystem and libcompression. The library's presence and signature do not establish the privileges of its eventual loader.

This binary uses relative Objective-C method records and chained pointers. Reading these slots as ordinary absolute addresses gives incorrect results. The evidence resolves 16 selected method records, five classes, 20 same-image bindings and seven command/configuration keys against original bytes. Format definitions were cross-checked against retained SDK headers and [Apple's dyld chained-fixup definitions](https://github.com/apple-oss-distributions/dyld/blob/dyld-1245.1/include/mach-o/fixup-chains.h). This is format context, not a claim that the public dyld release is this RAMDisk's exact loader build.

The retained trace covers 31 bodies and **3,451 byte-checked code records**. A further 60 decoder records fall inside a declared 120-byte `LC_DATA_IN_CODE` jump table and are excluded from the code count. One older linear-listing prologue discrepancy remains recorded; 44 other listing differences fall inside that table. These are analysis-format corrections, not evidence of injected instructions. Byte checking validates the retained decoding against source bytes; it does not establish that every transitive routine has been semantically reviewed.

<a id="command-flow-and-inputs"></a>
### Command flow and inputs

`PFXUpdaterCreate` at `0xbd0` constructs the PFX controller. Its factory at `0x16b8` creates `PFXUpdaterInstance`, whose superclass is `UARPSoCUpdaterInstance`. `PFXUpdaterExecCommand` at `0xc12` transfers to the shared dispatcher at `0xb060`.

| Command / stage | Established action | Boundary still open |
| --- | --- | --- |
| `queryTags` | Returns build-identity and ticket tags | Which caller supplies the matching build identity |
| `queryInfo` | Produces updater information, including `LocalSigningID` | How the external caller interprets that result |
| `generateMeasurements` | Offers the caller's firmware data; after success, returns collected personalization requests | Complete measurement construction and external signing caller |
| `performNextStage` | Offers personalization responses; checks success, then calls `applyStagedFirmware` and checks its result | Transitive firmware write and device authentication |

The firmware lookup at `0x2aa9–0x2abd` resolves to the actual key **`FirmwareData`**. Missing data returns failure in the selected helper. The response controller at `0x236d` skips completed updater instances; otherwise it forwards the input response dictionary to `offerPersonalizationResponse:` and checks the returned boolean. This is an in-process plugin interface. No standalone launchd job or independent privilege grant is established by these functions. The privileged loader, input authority and full firmware selection remain open.

`PFXUpdateQueryNumberOfAccessories` at `0x18308` simply returns **1**. Its callers therefore do not prove that a physical accessory was found. A packaged target name or this constant cannot identify the Mac's attached hardware.

<a id="local-signing-changes-which-response-path-runs"></a>
### Local signing changes which response path runs

The PFX override `useLocalSigning` at `0xd5e` returns true. The generic controller separately reads `ForceLocalSigning`; its information path also sets the reported flag if any updater reports local signing. The exported information key resolves to **`LocalSigningID`**. Names alone would not establish these behaviors; the return value, branches and original CFString records do.

In `offerPersonalizationResponse:` at `0x99c3`, a true `useLocalSigning` result takes the branch at `0x9a20` that logs its local-signing decision and returns success at `0x9b38`. It does **not** call the generic TSS response parser on that branch. This explains why finding a TSS server URL in the same binary is insufficient to claim that this PFX path requests or consumes a remote ticket.

“Local signing” here is the updater's workflow flag. This segment has not located a local signing private key or established how the device authenticates the final firmware. It does not demonstrate that firmware signatures are optional or that Secure Boot has been disabled.

<a id="generic-personalization-request-and-response-boundary"></a>
### Generic personalization request and response boundary

The shared request producer stores a request dictionary and, at `0x70ec–0x70f3`, supplies the compiled `https://gs.apple.com:443` value to a callback. The selected callback setup and queue-handler bodies connect the layer-3 TSS request interface to the layer-4 callback slot; the latter reaches `_UARPSoCUpdaterFirmwareTssRequest` at `0xa848`. The complete transitive endpoint setup remains only partly reviewed.

The receiving Objective-C method at `0x9d90` copies the request options, retains the server URL, records asset/endpoint context, and sets a completion flag before calling the transfer-completion method. The selected storage body performs no HTTP operation. The outer component that would submit a request and provide a response has not yet been established. No request was sent during this audit.

A diagnostic about invalid options occurs on a non-null-options branch, but control flow continues to the copy. It is therefore not evidence of a rejecting validation check. This is another case where log wording must be checked against the instructions.

On the generic **non-local** route, `CoreUARPRestorePersonalizationTssResponse` at `0x5c54` looks up ticket data using a configured key, obtains its length and bytes, allocates storage, copies the bytes, and subsequently builds a UARP superbinary with metadata and payload. The selected front of this function assumes the expected CFData input and successful allocation without explicit local checks before the copy. Caller contracts, malformed-input reachability and downstream validation remain unresolved; this observation is not an exploit finding. Completion of the offer method is also not proof that device-side cryptographic verification succeeded.

<a id="iokit-entry-and-the-misleading-send-function-name"></a>
### IOKit entry and the misleading send-function name

The PFX layer-4 initializer resolves to `PFXUpdateEndpointInitialize` at `0x19545`. Its selected path:

1. Builds the endpoint callback table, including an apply-staged-assets callback.
2. Matches the **`ApplePM40100MgmtEP`** IOKit service and traverses its parent in the `IOService` plane, reading `name` and `pcidebug` properties.
3. Calls `IOServiceOpen` at `0x19ae4` with user-client type 0.
4. Calls `IOConnectCallScalarMethod` at `0x19a6c`, selector 2, with zero scalar inputs and two scalar outputs; the returned words are decoded and stored in version-related fields.

These are static capabilities. The audit made no IOKit connection, and this trace has not yet resolved the user client's authorization checks or write selectors.

`PFXSendMsgToAccessory` at `0x189c4` validates its arguments and transfers to the library's own `uarpPlatformEndpointRecvMessage` at `0xfdf4`. At this point, the apparent “send” is an **in-process delivery**. Its name does not establish USB multiplexing, an external network connection or a connected device. Later callbacks may reach hardware; those paths are the next segment.

<a id="segment-disposition-and-exact-continuation"></a>
### Segment disposition and exact continuation

**Newly confirmed:** command keys and input flow; the PFX local-signing override and response-parser skip; generic request storage and callback URL; initial IOKit service open/version query; and the constant accessory count. **Expected within this scope:** signed Apple firmware-updater bytes from the official-matching RAMDisk, embedded generic UARP machinery and conventional framework dependencies. No new byte-integrity or signature anomaly was found.

**Worth deeper investigation:** the actual firmware write and acceptance policy, loader authority, generic response type/allocation contracts, and whether any external caller can influence the relevant options. The local-signing flag alone is not a maliciousness indicator.

The Stage 6F.1 checkpoint records **49 distinct inventory paths with bounded semantic reviews**, plus four embedded components. The twelve-field register retains all **147,253 objects**, including seven detailed current records, 42 other prior bounded records, and explicit unknowns elsewhere. It declares no whole object newly closed. Prior container, firmware, SSV, Preboot/Recovery, LocalPolicy, USB, service, ARM and protected-file queues remain open.

**Stage 6F.1 handoff, completed in the bounded pass below: Stage 6F.2 — `_fApplyStagedAssets`, PFX IOKit write/completion/error paths, and `usr/standalone/firmware/PFX/PFX_J180dAP.uarp`.** Correlate the payload's structure, version, selection and digest with the exact official RAMDisk, then trace device-side validation and caller authority as available. Q34 tracks this work; Q32/Q33 retain earlier authority and conditional RSA questions. No component was executed and nothing has been published.



<a id="pfx-staging-device-handoff-and-nested-firmware"></a>
## PFX staging, device handoff and nested firmware

Stage 6F.2 continues the same PFX binary, rather than restarting its analysis. **NET-014** traces payload selection, buffering, the actual driver submission and the later apply callback. **FW-006** accounts for every byte region of the packaged UARP and its nested vendor image. These are bounded static results, not evidence that firmware was installed on this Mac.

<a id="where-the-device-submission-actually-occurs"></a>
### Where the device submission actually occurs

The normal options factory, `-[PFXUpdaterInstance uarpRestoreInitOptions]` at `0xc43`, allocates one zeroed byte. The endpoint initializer copies that byte to its context at `+0x5a0`. The examined factory path therefore selects the IOKit route. A nonzero alternative instead writes a relative file named `PFXPayload.bin`; the authority to select that alternative remains unresolved.

| Step | Original PFX location | Confirmed behavior and limits |
| --- | --- | --- |
| Select | `_fAssetAllHeadersAndMetaDataComplete`, `0x19027` | Queries payload index zero, compares its four-word version with the device version, allocates payload length plus eight bytes and selects index zero. Equal versions call asset-abandon with reason `0x400`, but execution then reaches allocation; whether downstream state suppresses transfer still needs tracing. |
| Buffer | `_fPayloadData`, `0x18313` | Copies incoming chunks to the allocation after an eight-byte prefix. The local range comparison uses a 32-bit `offset + length`; upstream constraints and input authority are not yet established. This arithmetic warrants review but is not a demonstrated overflow exploit. |
| Submit | `_fPayloadDataComplete2`, `0x1840f` | On the normal route, `IOConnectCallStructMethod` at `0x184dc` uses selector **4**, the buffer including its eight-byte prefix, and payload length plus eight. There is no output buffer. The prefix contains a 32-bit length and a zeroed reserved word. |
| Complete / abandon | `0x184aa` / `0x184f7` | A successful driver return leads to `AssetFullyStaged`; driver or staging failure reaches abandon reason `0x900`. This establishes the caller's result handling, not what the kernel or controller validates. |
| Apply | `_fApplyStagedAssets`, `0x18ca9` | The PFX callback validates pointers, ORs bit 0 into the result byte and returns success. It contains no further IOKit call. Device submission has already occurred during staging. |

The shared `applyStagedFirmware` method sends the UARP apply command and waits on its completion semaphore. Its completion callback stores apply flags and signals the semaphore; the reviewed method returns true after the wait without interpreting those flags itself. This is a local completion contract, not independent proof of verified installation. The transitive UARP state machine and device response remain open.

The debug-file branch calls `fopen("PFXPayload.bin", "w")`, `fwrite` and `fclose`, then marks the asset staged. The selected local body does not check the first two return values. The normal zeroed options factory does not select this branch. Its existence neither proves an artifact was written nor establishes an unprivileged file-write capability.

The evidence retains **40 function bodies / 1,879 byte-checked code records**, including overlap with Stage 6F.1; 1,560 instruction addresses are outside that earlier selection. Seven relative Objective-C method records and five raw callback references tie the selected implementations to their registrations. Counts describe retained trace coverage, not complete understanding of every instruction or transitive callee.

<a id="pfx-uarp-and-its-vendor-image"></a>
### PFX UARP and its vendor image

`usr/standalone/firmware/PFX/` contains one inventoried file, `PFX_J180dAP.uarp`: **1,475,250 bytes**, SHA-256 `0a387af623b50a0e2e3fadb248b67436127f5f144bd311412e5ff60726ce5af5`. It was acquired from a fresh read-only RAMDisk attachment, matched to the existing inventory, and the attachment was detached. The RAMDisk's previously established exact-reference identity remains the outer provenance boundary.

| Outer region | Offset | Bytes | Meaning |
| --- | ---: | ---: | --- |
| Version-3 header | 0 | 44 | Declares length, version and table locations |
| One payload table entry | 44 | 40 | `PCIE`, version words `3.144.8.93`, payload offset and length |
| Metadata TLVs | 84 | 25 | Two bounded records; includes the `0.1.6` string |
| Vendor image | 109 | 1,474,304 | `MSCC_MD ` image, vendor type 3 / configuration |
| Appended keyed archive | 1,474,413 | 837 | Decoded as data without instantiating archived objects |

The archive identifies super-binary version `0.1.7`, minimum version `0.1.6`, urgent update true, and one payload named `Cmplt_J180_Ver_8.fwimg`, described as `PCIe PFX V8 Config`. The super-binary version, payload version words, vendor header version and filename revision are separate fields. Their differences are not automatically mismatches. `J180dAP` appears in the update's supported-model list; that does not identify the investigator's hardware or prove that this payload was selected.

The extracted image SHA-256 is `f32d87c67efadf0dbc44617e609affaa0abcd25810d95db8947868e5be8f6447`. Its 4,096-byte header contains 624 metadata bytes, a four-byte header CRC, a 512-byte signature candidate and 2,956 zero bytes; the remaining **1,470,208 bytes** are the configuration body. Declared lengths account for the complete image. The retained vendor layout identifies the type; the exact configuration registers remain undecoded. [Pinned vendor firmware layout](https://github.com/Microsemi/switchtec-user/blob/c5aac7b5c36e9ea0ef04112365833826c0a6391a/lib/fw.c).

Both CRCs reproduce: header `0x23e2d45b`, body `0xf064cb05`. The vendor uses a non-reflected `0x04c11db7` CRC with initial/final `0xffffffff`; substituting ordinary zlib CRC32 gives a different result because it is a different algorithm. A one-bit header mutation changes the recomputed checksum in the retained negative control. CRC checks detect corruption and do not authenticate a signer. [Pinned vendor CRC implementation](https://github.com/Microsemi/switchtec-user/blob/c5aac7b5c36e9ea0ef04112365833826c0a6391a/lib/crc.c).

The embedded modulus is 4,096 bits, with exponent 65,537. Applying the public RSA operation to the candidate signature yields a well-formed PSS encoding with SHA-512/MGF1-SHA-512 and a 64-byte salt. **The signed message has not been identified.** Fifteen ordinary message/hash hypotheses and twelve additional SHA-512 constructions did not verify. These failed hypotheses do not establish an invalid firmware signature. Neither an embedded public key nor the `secure_version=0` field establishes device trust, unsigned acceptance or disabled Secure Boot.

Microchip identifies PM40100 as a PFX100xG4 PCIe fanout switch, which supports the interpretation of the updater's `ApplePM40100MgmtEP` target. It does not establish that the service or device existed during a particular installation. The retained 232-entry RAMDisk prelink dictionary has no textual PM40100/PFX/Switchtec match; another driver source or runtime environment remains possible. [Microchip PM40100](https://www.microchip.com/en-us/product/pm40100).

**Segment outcome:** the normal library route submits a length-prefixed payload to IOKit selector 4; the later PFX apply callback reports a flag. The packaged vendor container is structurally bounded and its CRCs pass. No new local byte modification is established. Caller authority, user-client permissions, equal-version abandonment, chunk arithmetic, device-side signature verification and rollback policy remain Q34. Stage 6F.3 follows the related EFI/PSF assets below.


