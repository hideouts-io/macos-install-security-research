---
layout: default
title: "RAMDisk, ramrod, and brain findings"
---

# RAMDisk, ramrod, and brain findings

[Home](../README.md) · [Findings index](../docs/findings-index.md) · [Subsystem analysis](../docs/ramdisk-ramrod.md)

The [source crosswalk](../tables/finding-provenance.csv) maps every ID to a retained audit document and distinguishes an explicit ID mention from section context. Each record retains the original audit ledger wording and its explicit limit. Raw disassembly, copies of Apple binaries, and host-specific artifacts are intentionally absent. A **bounded** finding describes only the examined path or artifact.

<a id="ram-001"></a>
## RAM-001 — Examined patch-plugin sealing call binds to main ramrod and enables root-hash validation

**Status:** bounded  
**Retained source:** `STAGE4_RAMROD.md:50` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [ramdisk-ramrod](../docs/ramdisk-ramrod.md)

**Evidence:** Chained-fixup binding; argument transfer; Image4 callback and failure gate

**Observation:** Examined patch-plugin sealing call binds to main ramrod and enables root-hash validation

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Other branches and runtime device policy remain unverified

**Follow-up:** Other branches and runtime device policy remain unverified

<a id="ram-002"></a>
## RAM-002 — Root-hash code requests xsys despite xmtr diagnostic text

**Status:** bounded  
**Retained source:** `STAGE4_RAMROD.md:76` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [ramdisk-ramrod](../docs/ramdisk-ramrod.md)

**Evidence:** Numeric tag and character formatting; 48 retained system tickets contain both objects

**Observation:** Root-hash code requests xsys despite xmtr diagnostic text

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Does not establish live root-hash contents or execution

**Follow-up:** Does not establish live root-hash contents or execution

<a id="ram-003"></a>
## RAM-003 — Update.plist supplies typed skip-sealing and system-volume-verify-done controls

**Status:** partial  
**Retained source:** `STAGE4_RAMROD.md:104` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (partial scope); interpretation open  
**Subsystem analysis:** [ramdisk-ramrod](../docs/ramdisk-ramrod.md)

**Evidence:** Resolved metadata; loader file path; Boolean checks and branch trace

**Observation:** Update.plist supplies typed skip-sealing and system-volume-verify-done controls

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Reference producer identified in RAM-006; full authorization and runtime file protections unverified; no runtime use established

**Follow-up:** Reference producer identified in RAM-006; full authorization and runtime file protections unverified; no runtime use established

<a id="ram-004"></a>
## RAM-004 — Ordinary loader path does not enter manifest or NVRAM override parser

**Status:** bounded  
**Retained source:** `STAGE4_RAMROD.md:119` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [ramdisk-ramrod](../docs/ramdisk-ramrod.md)

**Evidence:** True/false identity guard; raw bytes; fixup bindings; direct branch census

**Observation:** Ordinary loader path does not enter manifest or NVRAM override parser

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Assumes normal CoreFoundation bindings and ABI behavior; no arbitrary indirect-entry proof

**Follow-up:** Assumes normal CoreFoundation bindings and ABI behavior; no arbitrary indirect-entry proof

<a id="ram-005"></a>
## RAM-005 — All 27 examined softwareupdated command-table entries require a named Boolean-true XPC entitlement before dispatch

**Status:** bounded  
**Retained source:** `STAGE4_RAMROD.md:145` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** Stage 4D original bytes plus chained fixups and disassembly; dispatch-table.json

**Observation:** All 27 examined softwareupdated command-table entries require a named Boolean-true XPC entitlement before dispatch

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Only this dispatch path; reference producer identified in RAM-006; full options authorization and runtime protections unresolved

**Follow-up:** Only this dispatch path; reference producer identified in RAM-006; full options authorization and runtime protections unresolved

<a id="ram-006"></a>
## RAM-006 — Official-reference brain writes Update.plist; typed DoNotSeal feeds skip-sealing; writer requests atomic write and mode0644

**Status:** bounded  
**Retained source:** `STAGE4_RAMROD.md:184` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** Stage4E vendor-member comparison and x86_64 producer trace

**Observation:** Official-reference brain writes Update.plist; typed DoNotSeal feeds skip-sealing; writer requests atomic write and mode0644

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Full authorization and historical file ownership ACLs and execution remain unverified

**Follow-up:** Full authorization and historical file ownership ACLs and execution remain unverified

<a id="ram-007"></a>
## RAM-007 — Brain seven-command table requires named Boolean-true entitlements; gated PingService returns anonymous listener endpoint

**Status:** bounded  
**Retained source:** `STAGE4_RAMROD.md:217` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** Stage4F original x86_64 table bytes and dispatch endpoint excerpts

**Observation:** Brain seven-command table requires named Boolean-true entitlements; gated PingService returns anonymous listener endpoint

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Static base receiver resolved in Stage4G; full runtime and command authorization chain unresolved; no unprivileged endpoint acquisition established

**Follow-up:** Static base receiver resolved in Stage4G; full runtime and command authorization chain unresolved; no unprivileged endpoint acquisition established

<a id="ram-008"></a>
## RAM-008 — Static NSXPC receiver has returning prepare/apply bodies; separate gated command route has options transfer and apply session/lock checks

**Status:** bounded  
**Retained source:** `STAGE4_RAMROD.md:236` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** Stage4G original bytes and Objective-C metadata; fresh symbol-aware trace and 3958 instruction-byte checks

**Observation:** Static NSXPC receiver has returning prepare/apply bodies; separate gated command route has options transfer and apply session/lock checks

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Transitive mutations and client/handle ownership/expiry unresolved; registration traced in Stage4I; no unauthorized route established

**Follow-up:** Transitive mutations and client/handle ownership/expiry unresolved; registration traced in Stage4I; no unauthorized route established

<a id="ram-009"></a>
## RAM-009 — Verification-state flag set before manifest verification; two named direct callers propagate false; restored-state trust remains separate

**Status:** bounded  
**Retained source:** `STAGE4_RAMROD.md:265` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** Stage4H flag store0x74bf; verifier0x75bd; caller guards0x35822 and0x55b9c; restored Boolean0x37634

**Observation:** Verification-state flag set before manifest verification; two named direct callers propagate false; restored-state trust remains separate

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Early flag timing is not a bypass; Stage4I narrows flag0x80 provenance; failed-verification lifecycle and callback semantics remain unresolved

**Follow-up:** Early flag timing is not a bypass; Stage4I narrows flag0x80 provenance; failed-verification lifecycle and callback semantics remain unresolved

<a id="ram-010"></a>
## RAM-010 — Zeroed saved-context loader populates named fields; no ordinary local write sets flag0x80 selecting validation shortcut

**Status:** bounded  
**Retained source:** `publication/README.md:1923` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** Stage4I calloc and bzero0x36fbe/0x36fdb; flag writes0x370cb/0x37110/0x371c8/0x372dc; 87 base-register references

**Observation:** Zeroed saved-context loader populates named fields; no ordinary local write sets flag0x80 selecting validation shortcut

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No plist-selectable bypass demonstrated; local ordinary-code trace is not complete transitive analysis or a memory-safety proof

**Follow-up:** No plist-selectable bypass demonstrated; local ordinary-code trace is not complete transitive analysis or a memory-safety proof

<a id="ram-011"></a>
## RAM-011 — Prepare/resume register numeric context handles; apply/suspend require membership; suspend tests writer failure and attempts output deletion

**Status:** bounded  
**Retained source:** `publication/README.md:1923` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** Stage4I set creation0x41c5e; insertions0x3fe99/0x41786; membership0x40a00/0x41576; resume guard0x4e848; failed-write cleanup0x4e760

**Observation:** Prepare/resume register numeric context handles; apply/suspend require membership; suspend tests writer failure and attempts output deletion

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Handle ownership expiry and failed-verification-to-suspension lifecycle unresolved; serialization failure differs from verification failure; no unauthorized handle established

**Follow-up:** Handle ownership expiry and failed-verification-to-suspension lifecycle unresolved; serialization failure differs from verification failure; no unauthorized handle established

<a id="ram-012"></a>
## RAM-012 — Cleanup commands require Boolean-true helper entitlement; omitted reset-reserve flag defaults true; loaded-context validation failure frees context and returns null

**Status:** bounded  
**Retained source:** `publication/README.md:1933` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** Stage4J.1 seven-entry original table; seven receiver functions2349checked instructions; seven import jump proofs; brain free stub binding

**Observation:** Cleanup commands require Boolean-true helper entitlement; omitted reset-reserve flag defaults true; loaded-context validation failure frees context and returns null

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Full cleanup filesystem/APFS effects and handle lifetime unresolved; signature checker rejects retained obsolete resource envelope; no cleanup executed or bypass shown

**Follow-up:** Full cleanup filesystem/APFS effects and handle lifetime unresolved; signature checker rejects retained obsolete resource envelope; no cleanup executed or bypass shown

<a id="ram-013"></a>
## RAM-013 — Cleanup retains selected preflight/suspended/pending paths; false purge permits later removal; outer success can coexist with cleanup errors

**Status:** bounded  
**Retained source:** `publication/README.md:1954` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** Inventory-matched receiver outer-server branches;2349 byte-checked instructions;23 import bindings;x86_64 FTS SDK ABI assertions

**Observation:** Cleanup retains selected preflight/suspended/pending paths; false purge permits later removal; outer success can coexist with cleanup errors

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No cleanup executed; target/input authenticity, helper effects, relative log-marker context and handle lifetime unresolved; no vulnerability severity

**Follow-up:** No cleanup executed; target/input authenticity, helper effects, relative log-marker context and handle lifetime unresolved; no vulnerability severity

<a id="ram-014"></a>
## RAM-014 — Cleanup connection lifecycle and separate cleanup-target override traced; omitted UUID selects root media; target setter performs setup and can return true after some setup failures

**Status:** bounded  
**Retained source:** `publication/README.md:1976` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** 2846brain+818receiver byte-checked instructions;7original methods;3blocks;56stub and244indirect bindings;386metadata references

**Observation:** Cleanup connection lifecycle and separate cleanup-target override traced; omitted UUID selects root media; target setter performs setup and can return true after some setup failures

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No target operation executed; override producer/client authority, controller scope, libpartition2 policy and handle lifetime unresolved; no bypass established

**Follow-up:** No target operation executed; override producer/client authority, controller scope, libpartition2 policy and handle lifetime unresolved; no bypass established

<a id="ram-015"></a>
## RAM-015 — Constructor validation failure frees outer context; snapshot-prepare failure skips new success handle; internal no-op flag producer used by asset-staging progress code

**Status:** bounded  
**Retained source:** `publication/README.md:2000` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [installer-workflow](../docs/installer-workflow.md)

**Evidence:** 13functions;7076byte-checked instructions;84stubs;358indirect imports;669metadata references;five bounded handle-table references

**Observation:** Constructor validation failure frees outer context; snapshot-prepare failure skips new success handle; internal no-op flag producer used by asset-staging progress code

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No full alias/reuse/removal or nested-resource lifecycle proof; static Intel code; no verification bypass established

**Follow-up:** No full alias/reuse/removal or nested-resource lifecycle proof; static Intel code; no verification bypass established

