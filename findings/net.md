---
layout: default
title: "Restore network and FDR findings"
---

# Restore network and FDR findings

[Home](../README.md) · [Findings index](../docs/findings-index.md) · [Subsystem analysis](../docs/restore-network.md)

The [source crosswalk](../tables/finding-provenance.csv) maps every ID to a retained audit document and distinguishes an explicit ID mention from section context. Each record retains the original audit ledger wording and its explicit limit. Raw disassembly, copies of Apple binaries, and host-specific artifacts are intentionally absent. A **bounded** finding describes only the examined path or artifact.

<a id="net-001"></a>
## NET-001 — Seven-scope lexical network-reference census accounts for105123 paths;104514 hash-matched scanned; eight restore-library URL constants localized

**Status:** bounded  
**Retained source:** `publication/README.md:810` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** 118203source/offset records;608protected exclusions;one changed Finder-metadata exclusion;all paths/counts/byte extents reconciled;three selected Mach-O libraries

**Observation:** Seven-scope lexical network-reference census accounts for105123 paths;104514 hash-matched scanned; eight restore-library URL constants localized

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Strings and host syntax are not requests; compressed/dynamic/other encodings and arbitrary bare domains remain gaps; endpoint selection, request authentication and traffic unproven

**Follow-up:** Strings and host syntax are not requests; compressed/dynamic/other encodings and arbitrary bare domains remain gaps; endpoint selection, request authentication and traffic unproven

<a id="net-002"></a>
## NET-002 — Restore-library URL defaults, override setters and FDR trust-object GET selection traced in retained RAMDisk code

**Status:** bounded  
**Retained source:** `publication/README.md:850` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** Source hash checks; constructor fields/options; request-builder and outer200/202 status gates;3126instruction records across16selected functions/blocks shared with NET-003

**Observation:** Restore-library URL defaults, override setters and FDR trust-object GET selection traced in retained RAMDisk code

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Caller authority, actual endpoint use, response authentication callback and returned-object cryptographic acceptance unresolved; not observed traffic

**Follow-up:** Caller authority, actual endpoint use, response authentication callback and returned-object cryptographic acceptance unresolved; not observed traffic

<a id="net-003"></a>
## NET-003 — Typed EnableSslValidation=false constructs an AMSupport disable-validation option; additional roots, credential and proxy options have conditional producer paths

**Status:** bounded  
**Retained source:** `publication/README.md:896` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** FDR0x3d9a5-0x3da01 type/Boolean gate and original imported key binding; roots and request-option propagation checked

**Observation:** Typed EnableSslValidation=false constructs an AMSupport disable-validation option; additional roots, credential and proxy options have conditional producer paths

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Absent/true/wrong-type skip the disable assignment; backend semantics and caller control unresolved; no default-disabled TLS, exploitation or historical use established

**Follow-up:** Absent/true/wrong-type skip the disable assignment; backend semantics and caller control unresolved; no default-disabled TLS, exploitation or historical use established

<a id="net-004"></a>
## NET-004 — Selected Memory-to-Remote recovery path checks trust-object SHA256 against rfta/DGST; separate evaluator has option-dependent error masks

**Status:** bounded  
**Retained source:** `publication/README.md:918` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** Recovery call0x29692; finalCFEqual0x8aa3 and checkedstoreput; digest verifier0x1eae0; optionfilter0x1d6cc; ordinary finalstatus gate0xa60f

**Observation:** Selected Memory-to-Remote recovery path checks trust-object SHA256 against rfta/DGST; separate evaluator has option-dependent error masks

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Expected-ticket authority and option producers incomplete; nonnull output is not success; no unprivileged bypass or forged-object acceptance established

**Follow-up:** Expected-ticket authority and option producers incomplete; nonnull output is not success; no unprivileged bypass or forged-object acceptance established

<a id="net-005"></a>
## NET-005 — FDR HTTP callback signs and retries401/419 client challenges; trust-root extraction parses DER; factory-named helper checks supplied digest and root CN

**Status:** bounded  
**Retained source:** `publication/README.md:981` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** Callback0x3e6d5; checked signer0x3ec3d; resend0x3f00f; Authorizationclear0x3f025; secb/rssl rawtags; factoryroot CNcomparison0x15524

**Observation:** FDR HTTP callback signs and retries401/419 client challenges; trust-root extraction parses DER; factory-named helper checks supplied digest and root CN

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Not server or trust-object authentication by itself; root/digest/context-blob provenance and exact transport trust policy unresolved; no requests or signing performed

**Follow-up:** Not server or trust-object authentication by itself; root/digest/context-blob provenance and exact transport trust policy unresolved; no requests or signing performed

<a id="net-006"></a>
## NET-006 — AP-ticket trust helper has a typed AllowUntrusted true-return path; digest-mismatch exception still requires Apple-signature helper success; entitlement producer checks this trust result

**Status:** bounded  
**Retained source:** `publication/README.md:961` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** APTicketAllowUntrusted gate0x610f3-0x61146; boot-hash comparison0x6125c; APTicketAllowDigestMismatch gate0x612d4; AppleSignedcall0x613ca; entitlementgate0x615a8

**Observation:** AP-ticket trust helper has a typed AllowUntrusted true-return path; digest-mismatch exception still requires Apple-signature helper success; entitlement producer checks this trust result

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Caller authority and transitive signature/hash-provider policy unresolved; static cross-platform branches do not establish host runtime policy or malicious modification

**Follow-up:** Caller authority and transitive signature/hash-provider policy unresolved; static cross-platform branches do not establish host runtime policy or malicious modification

<a id="net-007"></a>
## NET-007 — FDR ticket helper reaches selected Image4 chain/signature/property gates with verified policy tables and embedded anchors; callback compares presented CHIP/ECID

**Status:** bounded  
**Retained source:** `publication/README.md:1005` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** Inventory-matched libamsupport;14policy pointers;2extractedanchors; checked chain/signature returns; PKCS1 result/canary gates; property callback/iterator result propagation

**Observation:** FDR ticket helper reaches selected Image4 chain/signature/property gates with verified policy tables and embedded anchors; callback compares presented CHIP/ECID

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Does not independently require both CHIP/ECID present; full certificate constraints/corecrypto/caller policy unresolved; no actual ticket submitted or host policy measured

**Follow-up:** Does not independently require both CHIP/ECID present; full certificate constraints/corecrypto/caller policy unresolved; no actual ticket submitted or host policy measured

<a id="net-008"></a>
## NET-008 — Ticket population checks trust after assigning loaded APTicket; input providers and four direct exception-option reader references bounded

**Status:** bounded  
**Retained source:** `publication/README.md:1052` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** libFDR0x83e0 population;0x61d54 optionassignment;0x8503 trustgate; personalized-path selector4 or compiledpath; typed registry read; original RIP optionrefs

**Observation:** Ticket population checks trust after assigning loaded APTicket; input providers and four direct exception-option reader references bounded

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No proved rejected-ticket reuse or mandatory precedence for recovery caller; indirect/cross-binary option writers and context authority remain open

**Follow-up:** No proved rejected-ticket reuse or mandatory precedence for recovery caller; indirect/cross-binary option writers and context authority remain open

<a id="net-009"></a>
## NET-009 — FDR validation-disable option reaches AMS session delegate UseCredential; constructor, request lifecycle and default/custom/client authentication branches traced

**Status:** bounded  
**Retained source:** `publication/README.md:1088` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** Original class/method/key bindings;300second default;retain options;6B producer ->6E66ff/6756;9methodrecords;exact SDK disposition enums

**Observation:** FDR validation-disable option reaches AMS session delegate UseCredential; constructor, request lifecycle and default/custom/client authentication branches traced

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No actual connection, untrusted option writer, runtime privilege or Foundation policy closure established

**Follow-up:** No actual connection, untrusted option writer, runtime privilege or Foundation policy closure established

<a id="net-010"></a>
## NET-010 — Custom-root helper tests certificate index0 using DER equality or direct issuer RSA verification; empty roots fail

**Status:** bounded  
**Retained source:** `publication/README.md:1123` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** AMSupport6cf3;6def index0;6f4f DER compare;0ff9 issuer;RSA SHA1/SHA256 dispatch;SDK leaf-index contract

**Observation:** Custom-root helper tests certificate index0 using DER equality or direct issuer RSA verification; empty roots fail

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Specialized local path; complete TLS hostname/date/extension policy and root authority unresolved; no successful TLS bypass demonstrated

**Follow-up:** Specialized local path; complete TLS hostname/date/extension policy and root authority unresolved; no successful TLS bypass demonstrated

<a id="net-011"></a>
## NET-011 — Transport RSA helper differs from Image4 helper: legacy false Boolean can return success; newer branch preserves primary errors but discards extra canary comparison

**Status:** bounded  
**Retained source:** `publication/README.md:1131` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** Exact eac0 versusc03e calltargets;ec17-ec66 returnbytes;three inventory-matched crypto variants and libSystem reexports; official matching RAMDisk

**Observation:** Transport RSA helper differs from Image4 helper: legacy false Boolean can return success; newer branch preserves primary errors but discards extra canary comparison

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Packaged libraries export newer API; legacy reachability and actual runtime bindings unknown; not a demonstrated current signature bypass or local tampering

**Follow-up:** Packaged libraries export newer API; legacy reachability and actual runtime bindings unknown; not a demonstrated current signature bypass or local tampering

<a id="net-012"></a>
## NET-012 — PFX selects local signing and skips generic response parsing; shared TSS callback copies request options and retains server URL

**Status:** bounded  
**Retained source:** `publication/README.md:1154` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** Exact RAMDisk PFX hash;31 bodies/3451 code records;relative ObjC methods and chained bindings;actual command keys

**Observation:** PFX selects local signing and skips generic response parsing; shared TSS callback copies request options and retains server URL

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No remote request observed; no unsigned-firmware acceptance or SecureBoot change proved; external caller and device validation unresolved

**Follow-up:** No remote request observed; no unsigned-firmware acceptance or SecureBoot change proved; external caller and device validation unresolved

<a id="net-013"></a>
## NET-013 — PFX opens ApplePM40100MgmtEP user client and queries selector2; named send function delivers to in-process UARP receiver

**Status:** bounded  
**Retained source:** `publication/README.md:1154` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** Original IOKit imports;endpoint initialization and send-function argument/control flow;constant accessory count

**Observation:** PFX opens ApplePM40100MgmtEP user client and queries selector2; named send function delivers to in-process UARP receiver

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No live connection or connected-device proof; user-client permissions and write/acceptance path remain Stage6F.2

**Follow-up:** No live connection or connected-device proof; user-client permissions and write/acceptance path remain Stage6F.2

<a id="net-014"></a>
## NET-014 — PFX device submission occurs during staging via IOKit selector4; later apply callback sets result flag

**Status:** bounded  
**Retained source:** `publication/README.md:1223` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [restore-network](../docs/restore-network.md)

**Evidence:** Stage6F2 checked callbacks and methods; zeroed options factory; driver and UARP result branches

**Observation:** PFX device submission occurs during staging via IOKit selector4; later apply callback sets result flag

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Caller/device authority and validation unresolved;32-bit chunk arithmetic and abandonment state need review

**Follow-up:** Caller/device authority and validation unresolved;32-bit chunk arithmetic and abandonment state need review

