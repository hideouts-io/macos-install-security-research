---
layout: default
title: "Signatures, Image4, and trust findings"
---

# Signatures, Image4, and trust findings

[Home](../README.md) · [Findings index](../docs/findings-index.md) · [Subsystem analysis](../docs/secure-boot.md)

The [source crosswalk](../tables/finding-provenance.csv) maps every ID to a retained audit document and distinguishes an explicit ID mention from section context. Each record retains the original audit ledger wording and its explicit limit. Raw disassembly, copies of Apple binaries, and host-specific artifacts are intentionally absent. A **bounded** finding describes only the examined path or artifact.

<a id="sig-001"></a>
## SIG-001 — Supported executable pages match embedded CodeDirectories

**Status:** bounded  
**Retained source:** `REPORT.md:160` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [code-signing-kernel](../docs/code-signing-kernel.md)

**Evidence:** Code-page validation results

**Observation:** Supported executable pages match embedded CodeDirectories

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Certificate trust and resource envelopes are separate

**Follow-up:** Certificate trust and resource envelopes are separate

<a id="sig-002"></a>
## SIG-002 — 906 strict verification failures map to identical official source content

**Status:** confirmed  
**Retained source:** `STAGE2_COMPARISON.md:79` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [code-signing-kernel](../docs/code-signing-kernel.md)

**Evidence:** Signature failure reconciliation ledger

**Observation:** 906 strict verification failures map to identical official source content

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Does not mean strict verification or all trust chains pass

**Follow-up:** Does not mean strict verification or all trust chains pass

<a id="sig-003"></a>
## SIG-003 — 868 standalone and one nested Image4 ticket signatures verify; 25 certificate signatures link to library roots

**Status:** bounded  
**Retained source:** `STAGE3_FIRMWARE.md:27` (relevant source section; ID absent from narrative)  
**Related public data:** [evidence/measurements.json](../evidence/measurements.json)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [secure-boot](../docs/secure-boot.md)

**Evidence:** Ticket and certificate signature ledgers; official-reference-matched libimage4

**Observation:** 868 standalone and one nested Image4 ticket signatures verify; 25 certificate signatures link to library roots

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Complete Image4 policy and hardware root state not evaluated

**Follow-up:** Complete Image4 policy and hardware root state not evaluated

<a id="sig-004"></a>
## SIG-004 — All 69 PE EFI slices pass Apple-format signatures with a published public-key fingerprint

**Status:** bounded  
**Retained source:** `STAGE3_FIRMWARE.md:166` (relevant source section; ID absent from narrative)  
**Related public data:** [evidence/measurements.json](../evidence/measurements.json)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [secure-boot](../docs/secure-boot.md)

**Evidence:** EFI verification ledger and OpenSSL cross-check

**Observation:** All 69 PE EFI slices pass Apple-format signatures with a published public-key fingerprint

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Product plaintext and outer PCI ROM signature mechanisms remain unverified

**Follow-up:** Product plaintext and outer PCI ROM signature mechanisms remain unverified

<a id="sig-005"></a>
## SIG-005 — 9702 signed object records satisfy examined certificate-role rules

**Status:** bounded  
**Retained source:** `STAGE3_FIRMWARE.md:52` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [secure-boot](../docs/secure-boot.md)

**Evidence:** 869-ticket role ledger and three-mode negative controls

**Observation:** 9702 signed object records satisfy examined certificate-role rules

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Not full hardware or device policy authorization

**Follow-up:** Not full hardware or device policy authorization

<a id="sig-006"></a>
## SIG-006 — Three supplied trust-cache encodings match signed ticket digests directly; four do not

**Status:** partial  
**Retained source:** `STAGE3_FIRMWARE.md:66` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (partial scope); interpretation open  
**Subsystem analysis:** [secure-boot](../docs/secure-boot.md)

**Evidence:** SHA384 of complete IM4P encodings compared to same-type DGST

**Observation:** Three supplied trust-cache encodings match signed ticket digests directly; four do not

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Four encodings have signed official counterparts with identical entry arrays but different type and UUID; runtime selection remains unverified

**Follow-up:** Four encodings have signed official counterparts with identical entry arrays but different type and UUID; runtime selection remains unverified

<a id="sig-007"></a>
## SIG-007 — Four alternate trust-cache files have official signed counterparts with identical entry arrays

**Status:** bounded  
**Retained source:** `STAGE3_FIRMWARE.md:88` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [secure-boot](../docs/secure-boot.md)

**Evidence:** Full reference member hashes and byte-level counterpart comparison

**Observation:** Four alternate trust-cache files have official signed counterparts with identical entry arrays

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Type and UUID differ; original encodings are not thereby directly signed

**Follow-up:** Type and UUID differ; original encodings are not thereby directly signed

<a id="sig-008"></a>
## SIG-008 — All 2699 measured CodeDirectory records occur in the 15-cache official reference

**Status:** bounded  
**Retained source:** `STAGE3_FIRMWARE.md:9` (relevant source section; ID absent from narrative)  
**Related public data:** [evidence/measurements.json](../evidence/measurements.json)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [secure-boot](../docs/secure-boot.md)

**Evidence:** Expanded code-hash correlation; 49 earlier nonmatches match an omitted system cryptex cache

**Observation:** All 2699 measured CodeDirectory records occur in the 15-cache official reference

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Membership does not establish loading or effective device authorization

**Follow-up:** Membership does not establish loading or effective device authorization

<a id="sig-009"></a>
## SIG-009 — Cleanup service code pages and populated special slots match; CMS integrity passes; blanket resource omit rules coexist with rejected bundle validation

**Status:** bounded  
**Retained source:** `publication/README.md:2045` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [code-signing-kernel](../docs/code-signing-kernel.md)

**Evidence:** 396page hashes;five special-slot hashes;two zero slots;OpenSSL CMS -noverify exit0;retained CodeResources and ordinary/strict codesign failures

**Observation:** Cleanup service code pages and populated special slots match; CMS integrity passes; blanket resource omit rules coexist with rejected bundle validation

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Not full certificate trust or restore policy acceptance; exact official bundle and omitted-resource coverage remain open

**Follow-up:** Not full certificate trust or restore policy acceptance; exact official bundle and omitted-resource coverage remain open

<a id="sig-010"></a>
## SIG-010 — Fresh exact official BaseSystem and all five cleanup bundle files match; official image reproduces custom-omit rejection; supplied-root certificate checks pass

**Status:** bounded  
**Retained source:** `publication/README.md:2023` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [code-signing-kernel](../docs/code-signing-kernel.md)

**Evidence:** Whole archive SHA256;1397chunk reconstruction;five files/four directories;two official codesign failures;Apple root DER equality;four chain-policy checks

**Observation:** Fresh exact official BaseSystem and all five cleanup bundle files match; official image reproduces custom-omit rejection; supplied-root certificate checks pass

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No fresh revocation proof, independent timestamp, full restore policy, ACL/xattr equivalence or runtime execution; signing policy rejection retained

**Follow-up:** No fresh revocation proof, independent timestamp, full restore policy, ACL/xattr equivalence or runtime execution; signing policy rejection retained
