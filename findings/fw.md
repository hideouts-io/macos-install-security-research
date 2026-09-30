---
layout: default
title: "Firmware, EFI, and NVRAM findings"
---

# Firmware, EFI, and NVRAM findings

[Home](../README.md) · [Findings index](../docs/findings-index.md) · [Subsystem analysis](../docs/firmware-flashers.md)

The [source crosswalk](../tables/finding-provenance.csv) maps every ID to a retained audit document and distinguishes an explicit ID mention from section context. Each record retains the original audit ledger wording and its explicit limit. Raw disassembly, copies of Apple binaries, and host-specific artifacts are intentionally absent. A **bounded** finding describes only the examined path or artifact.

<a id="fw-001"></a>
## FW-001 — Three restore digest differences resolve by type-tag substitution

**Status:** bounded  
**Retained source:** `REPORT.md:126` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-catalog](../docs/firmware-catalog.md)

**Evidence:** Restore firmware comparison

**Observation:** Three restore digest differences resolve by type-tag substitution

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Device-side enforcement and full firmware analysis remain incomplete

**Follow-up:** Device-side enforcement and full firmware analysis remain incomplete

<a id="fw-002"></a>
## FW-002 — FTAB and DP855 declared digests reproduced from internal measured regions

**Status:** confirmed  
**Retained source:** `STAGE3_FIRMWARE.md:109` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-catalog](../docs/firmware-catalog.md)

**Evidence:** Stage 3 firmware report and digest reconstruction records

**Observation:** FTAB and DP855 declared digests reproduced from internal measured regions

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** DP855 region layout inferred for this artifact; device verifier not traced

**Follow-up:** DP855 region layout inferred for this artifact; device verifier not traced

<a id="fw-003"></a>
## FW-003 — All 36 UARP digest lists and 12 manifest board selections reproduced

**Status:** confirmed  
**Retained source:** `STAGE3_FIRMWARE.md:117` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-catalog](../docs/firmware-catalog.md)

**Evidence:** 126 revision-rule measurements and board selection ledger

**Observation:** All 36 UARP digest lists and 12 manifest board selections reproduced

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No controller session or installed revision observed

**Follow-up:** No controller session or installed revision observed

<a id="fw-004"></a>
## FW-004 — Nine compressed PCI EFI payloads decode into bounded x86-64 PE drivers without certificate tables

**Status:** confirmed  
**Retained source:** `STAGE3_FIRMWARE.md:192` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-catalog](../docs/firmware-catalog.md)

**Evidence:** Decompression size/hash/PE checks and saved disassembly

**Observation:** Nine compressed PCI EFI payloads decode into bounded x86-64 PE drivers without certificate tables

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Outer ROM authentication and historical loading are separate

**Follow-up:** Outer ROM authentication and historical loading are separate

<a id="fw-005"></a>
## FW-005 — Product.efi wrapper dispatch depends on runtime-variable decryption material

**Status:** bounded  
**Retained source:** `STAGE3_FIRMWARE.md:180` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-catalog](../docs/firmware-catalog.md)

**Evidence:** Static diagnostic loader trace and wrapper length fields

**Observation:** Product.efi wrapper dispatch depends on runtime-variable decryption material

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No runtime material collected; plaintext and trailer remain unverified

**Follow-up:** No runtime material collected; plaintext and trailer remain unverified

<a id="fw-006"></a>
## FW-006 — PFX UARP and nested vendor configuration length-accounted with matching header/body CRCs

**Status:** bounded  
**Retained source:** `publication/README.md:1223` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-personalization](../docs/firmware-personalization.md)

**Evidence:** All outer/nested byte regions; pinned vendor CRC; archive/TLV decoding; encoding checks

**Observation:** PFX UARP and nested vendor configuration length-accounted with matching header/body CRCs

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Signed message and device trust anchor unverified; register semantics incomplete

**Follow-up:** Signed message and device trust anchor unverified; register semantics incomplete

<a id="fw-007"></a>
## FW-007 — All3PSFfirmware containers match reference and pass6CRCs; embedded RSA keys are distinct

**Status:** bounded  
**Retained source:** `publication/README.md:1269` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-flashers](../docs/firmware-flashers.md)

**Evidence:** Stage6F3 acquired hashes; prior exact-reference linkage; bounded vendor layout and encoding

**Observation:** All3PSFfirmware containers match reference and pass6CRCs; embedded RSA keys are distinct

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** PSS encoding is not signature verification; inner code and device key policy unresolved

**Follow-up:** PSS encoding is not signature verification; inner code and device key policy unresolved

<a id="fw-008"></a>
## FW-008 — Apple-signed PSFFlasher uses PCI mailbox firmware download and boot-service-only status variables

**Status:** bounded  
**Retained source:** `publication/README.md:1269` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-flashers](../docs/firmware-flashers.md)

**Evidence:** 15byte-checked ranges1841records; original PCI GUID; vendor MRPC and UEFI ABI; prior exact-hash EFI signature

**Observation:** Apple-signed PSFFlasher uses PCI mailbox firmware download and boot-service-only status variables

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No execution established;launch/argument authority, malformed-input and individual I/O error handling incomplete

**Follow-up:** No execution established;launch/argument authority, malformed-input and individual I/O error handling incomplete

<a id="fw-009"></a>
## FW-009 — LoadedImage input and -p / efi-apple-payload* routes feed substring filename selection and conditional filename-version/force gate

**Status:** confirmed static consumers; upstream authority unknown  
**Retained source:** `publication/README.md:1314` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-flashers](../docs/firmware-flashers.md)

**Evidence:** Stage6F4 inputs.original-byte trace and Stage6F3 main/download/PCI trace; RVAs 0x8ef9,0x9550,0xbc81,0xbcdb,0xa314

**Observation:** LoadedImage input and -p / efi-apple-payload* routes feed substring filename selection and conditional filename-version/force gate

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No authenticated external producer identified; no observed launch or rollback bypass

**Follow-up:** No authenticated external producer identified; no observed launch or rollback bypass

<a id="fw-010"></a>
## FW-010 — 512-byte argv and path allocations,96-byte payload-pointer list, unchecked signed target index, uninitialized initial EFI variable DataSize, header arithmetic before bounds, individual PCI errors discarded

**Status:** confirmed local checks absent; exploitability unknown  
**Retained source:** `publication/README.md:1341` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-flashers](../docs/firmware-flashers.md)

**Evidence:** Stage6F4 inputs.original-byte trace and Stage6F3 main/download/PCI trace; RVAs 0x8fdc,0x9b41,0x965b,0x966b,0x96a6,0x9748,0x982d,0xb69c,0xb6ca,0xac16,0xad1c,0xad9f

**Observation:** 512-byte argv and path allocations,96-byte payload-pointer list, unchecked signed target index, uninitialized initial EFI variable DataSize, header arithmetic before bounds, individual PCI errors discarded

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Three valid packaged files pass all6CRCs; caller input control, runtime effects and transport-error reachability unproven

**Follow-up:** Three valid packaged files pass all6CRCs; caller input control, runtime effects and transport-error reachability unproven

<a id="fw-011"></a>
## FW-011 — Security-query return ignored after buffer zeroing; unfilled zero response selects UnFused success and dev_signed host filename label

**Status:** confirmed conditional control flow; no observed hardware event  
**Retained source:** `publication/README.md:1314` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-flashers](../docs/firmware-flashers.md)

**Evidence:** Stage6F4 inputs.original-byte trace and Stage6F3 main/download/PCI trace; RVAs 0xbf56,0xbf6e,0xbf79,0xbf7e,0xc107,0xc10c,0xc139,0x10fd0

**Observation:** Security-query return ignored after buffer zeroing; unfilled zero response selects UnFused success and dev_signed host filename label

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Does not alter fuses or enforce/bypass device authentication; packaged PSF names areprod_signed; no malformed inputs executed

**Follow-up:** Does not alter fuses or enforce/bypass device authentication; packaged PSF names areprod_signed; no malformed inputs executed

<a id="fw-012"></a>
## FW-012 — FirmwareUpdateLauncher consumes helper plists, assembles bless firmware/payload options and efi-apple-payload index names, requests NVRAM changes; compiled status table associates PSFFlasher with psfupdater

**Status:** Confirmed bounded static workflow; exact PSF producer authority incomplete  
**Retained source:** `publication/README.md:1374` (explicit ID in source narrative)  
**Related public data:** [tables/firmware-helpers.csv](../tables/firmware-helpers.csv)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-flashers](../docs/firmware-flashers.md)

**Evidence:** Stage6F5 launcher10ranges2361records179metadata checks; fresh exact-image acquisition and strict signing; path census

**Observation:** FirmwareUpdateLauncher consumes helper plists, assembles bless firmware/payload options and efi-apple-payload index names, requests NVRAM changes; compiled status table associates PSFFlasher with psfupdater

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No inventoried psfupdater path; a USB-C helper corroborates the generic schema, while initiating caller/helper authority, effective kernel/firmware policy and PSF-specific handoff remain unknown; no execution or writes performed

**Follow-up:** Locate an authoritative same-build psfupdater or alternate producer; trace launcher acceptance and device-side trust without running an updater on the production host

<a id="fw-013"></a>
## FW-013 — bless stages payloads and serializes EFI media paths/boot options for an IOKit NVRAM property request; signed private installer/boot/snapshot/NVRAM entitlements present

**Status:** Confirmed bounded static workflow  
**Retained source:** `publication/README.md:1408` (explicit ID in source narrative)  
**Related public data:** [tables/firmware-helpers.csv](../tables/firmware-helpers.csv)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-flashers](../docs/firmware-flashers.md)

**Evidence:** Stage6F6 fresh reference-linked bless;6ranges1915records10metadata139import checks

**Observation:** bless stages payloads and serializes EFI media paths/boot options for an IOKit NVRAM property request; signed private installer/boot/snapshot/NVRAM entitlements present

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Kernel conversion to -data variables and authorization not traced; entitlement presence does not prove execution or root caller

**Follow-up:** Kernel conversion to -data variables and authorization not traced; entitlement presence does not prove execution or root caller

<a id="fw-014"></a>
## FW-014 — MultiUpdater reads staged payloads, optionally requests IMG4 verification for seven types including psfu, supplies true verification callback to Apple loader, sets child LoadOptions and calls StartImage; update state uses attributes7

**Status:** Confirmed caller behavior; protocol meaning corroborated by upstream definitions  
**Retained source:** `publication/README.md:1431` (explicit ID in source narrative)  
**Related public data:** [tables/firmware-helpers.csv](../tables/firmware-helpers.csv)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-flashers](../docs/firmware-flashers.md)

**Evidence:** Stage6F6 21ranges1401original-byte records; pinned AppleLoadImage/AppleSecureBoot headers and UEFI ABI; prior exact reference/signature links

**Observation:** MultiUpdater reads staged payloads, optionally requests IMG4 verification for seven types including psfu, supplies true verification callback to Apple loader, sets child LoadOptions and calls StartImage; update state uses attributes7

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Protocol definitions are external research, not OpenCore evidence; actual Apple firmware loader/device acceptance and active policy unknown

**Follow-up:** Protocol definitions are external research, not OpenCore evidence; actual Apple firmware loader/device acceptance and active policy unknown

<a id="fw-015"></a>
## FW-015 — MultiUpdater child lookup returns zero when no payload matches; resume-state writer discards SetVariable return; selected caller ignores result-writer status

**Status:** Confirmed static error-reporting gaps; runtime impact unverified  
**Retained source:** `publication/README.md:1408` (explicit ID in source narrative)  
**Related public data:** [tables/firmware-helpers.csv](../tables/firmware-helpers.csv)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [firmware-flashers](../docs/firmware-flashers.md)

**Evidence:** Stage6F6 checked d3d5-d440, d578-d63e and main db45/db48

**Observation:** MultiUpdater child lookup returns zero when no payload matches; resume-state writer discards SetVariable return; selected caller ignores result-writer status

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No malformed input or failure injected; no proof of successful flash, exploitability or boot-policy bypass; trusted producer constraints unresolved

**Follow-up:** No malformed input or failure injected; no proof of successful flash, exploitability or boot-policy bypass; trusted producer constraints unresolved

<a id="fw-016"></a>
## FW-016 — Ordinary dictionary writes pass false permission override; current-task Boolean-true entitlement checks, legacy/name rules and separate LocalPolicy-storage entitlement

**Status:** Observed static authorization checks  
**Retained source:** `publication/README.md:1463` (explicit ID in source narrative)  
**Related public data:** [tables/efi-converter-branches.csv](../tables/efi-converter-branches.csv)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [nvram-efi-paths](../docs/nvram-efi-paths.md)

**Evidence:** Stage6F7 nvram.instructions, entitlement-table, legacy-table and rebase-corroboration; 196403a/196403c,196358d,19635bd

**Observation:** Selected caller passes false; checker compares entitlement object with kOSBooleanTrue; LocalPolicy storage additionally requires com.apple.private.security.bootpolicy.nvram

**Interpretation:** Firmware-payload ordinary write route is gated; generic root privilege does not replace the GUID-specific entitlement

**Security relevance:** Kernel NVRAM mutation boundary

**Confidence field:** Observed

**Limit:** MAC/sandbox/AMFI/entry checks and all override callers remain open; no runtime policy test

**Follow-up:** Trace registry/MAC entry path and every true override caller

<a id="fw-017"></a>
## FW-017 — XML array/dictionaries convert to binary EFI paths; successful conversion queues a -data companion; sync reaches a static indirect EFI runtime call with attributes7

**Status:** Observed selected conversion and persistence-request chain  
**Retained source:** `publication/README.md:1497` (explicit ID in source narrative)  
**Related public data:** [tables/efi-converter-branches.csv](../tables/efi-converter-branches.csv)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [nvram-efi-paths](../docs/nvram-efi-paths.md)

**Evidence:** Stage6F7 provider.instructions, pointer-links, nvram.instructions; 14865d1,1486602,196317b,1963263,196066f,19628b0

**Observation:** OSUnserializeXML, typed casts, UTF16 media-path/option construction, -data suffix and pending dictionary-to-setVariable calls retained

**Interpretation:** Companion data is an EFI path representation and queued modification, not firmware bytes or proof of persistence

**Security relevance:** Pre-boot payload selection and kernel-to-firmware handoff

**Confidence field:** Observed

**Limit:** No actual write observed; full input validation, MAC/entry authority and firmware acceptance unresolved

**Follow-up:** Complete converter size/error/ownership branches and registry/MAC entry controls; firmware implementation needs additional artifact

<a id="fw-018"></a>
## FW-018 — Eight mappings cover seven helper names; eleven signed Mach-O helper paths and fifteen EFI flasher paths; psfupdater basename absent in enumerated trees

**Status:** Observed compiled mapping and scoped absence  
**Retained source:** `publication/README.md:1646` (explicit ID in source narrative)  
**Related public data:** [tables/efi-converter-branches.csv](../tables/efi-converter-branches.csv)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [nvram-efi-paths](../docs/nvram-efi-paths.md)

**Evidence:** Stage6F7 launcher-authority constant/instruction proof, helper-census; publication/FIRMWARE_HELPERS.csv

**Observation:** Fixed updater-name predicate and all eight dictionaries decoded; census joins hashes and retained signing records

**Interpretation:** Architecture variants and repeated/alternate payload locations explain multiplicity; missing helper remains provenance question

**Security relevance:** Helper selection and privileged producer inputs

**Confidence field:** Observed

**Limit:** No historical helper binary established; helper-internal authorization/platform restrictions not traced; absence not exhaustive across opaque containers

**Follow-up:** Reverse engineer located helpers and trace caller/directory authority; inspect package manifests for psfupdater

<a id="fw-019"></a>
## FW-019 — setProperty calls setMagicVariable but does not directly reject its subsequent original-variable queueing on a false conversion result

**Status:** Observed result-propagation gap; impact unknown  
**Retained source:** `publication/README.md:1519` (explicit ID in source narrative)  
**Related public data:** [tables/efi-converter-branches.csv](../tables/efi-converter-branches.csv)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [nvram-efi-paths](../docs/nvram-efi-paths.md)

**Evidence:** Stage6F7 nvram.instructions/annotated; 1963625 through19637ea

**Observation:** Return used for optional logging, no result-dependent rejection before original-variable cache/pending processing

**Interpretation:** Conversion and original-property acceptance have separate outcomes; conversion failure may not surface as property failure

**Security relevance:** Error reporting and possible stale/partial state across a firmware staging boundary

**Confidence field:** Observed

**Limit:** Not a demonstrated vulnerability or successful persistent write; stale companion behavior and reachable failure inputs need further work

**Follow-up:** Trace all companion consumers/deletion and synchronization results; define a safe isolated model before any runtime experiment

<a id="fw-020"></a>
## FW-020 — Typed EFI path conversion and registry transport construction have bounded validation, append-result, media-read-error and metadata-ownership limitations

**Status:** bounded static analysis; runtime impact unresolved  
**Retained source:** `publication/README.md:1527` (explicit ID in source narrative)  
**Related public data:** [tables/efi-converter-branches.csv](../tables/efi-converter-branches.csv)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [nvram-efi-paths](../docs/nvram-efi-paths.md)

**Evidence:** Stage6F7 provider.instructions; continuation converter-new.*, converter-types, converter-branch-review and arithmetic-examples; EFI_CONVERTER_BRANCHES.csv; stage6f7-transport-20260927 transport.provenance.json, transport-review.json and iomedia-slot-links.json; 1820 checked instructions/11 helpers

**Observation:** 22typed branches reviewed; four-field MAC parser;16bit file/node arithmetic; common append failures ignored while CDROM checks; retained metadata lacks release on selected replacement/error/null-output paths; eleven selected transport append results unused; MBR read error can return success without setting the zero-initialized signature output

**Interpretation:** Potential malformed or incomplete path generation and reference-leak candidates; OSData itself rejects length overflow and inadequate capacity; MBR zero-signature node is a static error-propagation candidate, not an observed boot failure

**Security relevance:** Privileged boot-path parsing and error/ownership boundary before NVRAM staging

**Confidence field:** Observed branch behavior; arithmetic/lifetime effects Supported inference; runtime impact Unknown

**Limit:** No runtime malformed input or allocation/read failure induced; firmware acceptance, boot impact, overflow exploitation and security bypass unproven

**Follow-up:** Trace authorized caller/property producers, append/read failure reachability, downstream EFI-path consumers and firmware acceptance in an isolated model

<a id="fw-021"></a>
## FW-021 — AppleEFINVRAM resync error-return path contains no matching unlock after acquiring the NVRAM mutex

**Status:** bounded static analysis; reachability and impact unresolved  
**Retained source:** `publication/README.md:1463` (explicit ID in source narrative)  
**Related public data:** [tables/efi-converter-branches.csv](../tables/efi-converter-branches.csv)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [nvram-efi-paths](../docs/nvram-efi-paths.md)

**Evidence:** resyncAllVariables196420e..42c8; lock4228; firmware call4240; error4247->429d->4290/4297; success unlock4288; continuation validation.json15recordCFG; stage6f7-policy-20260927 exact equality/sandboxcallback/pointer proofs

**Observation:** Nonzero ResyncNVRam deletion result follows optional logging to return without the local unlock; successful route flushes/caches/unlocks

**Interpretation:** Potential retained-lock error-handling defect in official-matching binary; not evidence of modification or unauthorized firmware access

**Security relevance:** Possible availability impact at privileged NVRAM synchronization boundary if the error route is reachable

**Confidence field:** Observed local control flow; retained-lock consequence Supported inference; reachability/impact Unknown

**Limit:** No resync request or firmware-error induction; equality and concrete sandboxcallback traced, but evaluator/profile/caller and firmware-error reachability unresolved; no demonstrated deadlock or denial of service

**Follow-up:** Resolve sb_evaluate_internal3033f55, effectiveprofile/globalpolicy, remainingMACregistration/kernelcallers and firmwareerrors before isolated dynamicvalidation
