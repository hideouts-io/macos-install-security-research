---
layout: default
title: "Reference and provenance findings"
---

# Reference and provenance findings

[Home](../README.md) · [Findings index](../docs/findings-index.md) · [Subsystem analysis](../docs/artifact-provenance.md)

The [source crosswalk](../tables/finding-provenance.csv) maps every ID to a retained audit document and distinguishes an explicit ID mention from section context. Each record retains the original audit ledger wording and its explicit limit. Raw disassembly, copies of Apple binaries, and host-specific artifacts are intentionally absent. A **bounded** finding describes only the examined path or artifact.

<a id="ref-001"></a>
## REF-001 — Exact Apple catalog product 140-93587 identifies 25G83

**Status:** confirmed  
**Retained source:** `STAGE2_COMPARISON.md:5` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [artifact-provenance](../docs/artifact-provenance.md)

**Evidence:** Apple distribution and catalog records

**Observation:** Exact Apple catalog product 140-93587 identifies 25G83

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Does not authenticate all local staged files

**Follow-up:** Does not authenticate all local staged files

<a id="ref-002"></a>
## REF-002 — Retained installer integrity metadata equals Apple-hosted metadata

**Status:** confirmed  
**Retained source:** `STAGE2_COMPARISON.md:5` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [artifact-provenance](../docs/artifact-provenance.md)

**Evidence:** Byte comparison and SHA256

**Observation:** Retained installer integrity metadata equals Apple-hosted metadata

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Package contents require separate verification

**Follow-up:** Package contents require separate verification

<a id="ref-003"></a>
## REF-003 — All 42 J160AP preflight component digests match local manifest

**Status:** confirmed  
**Retained source:** `STAGE2_COMPARISON.md:61` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [artifact-provenance](../docs/artifact-provenance.md)

**Evidence:** Official catalog preflight manifest comparison

**Observation:** All 42 J160AP preflight component digests match local manifest

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Digest declarations do not prove every referenced file matches

**Follow-up:** Digest declarations do not prove every referenced file matches

<a id="ref-004"></a>
## REF-004 — 1186 staged update files and three symlinks match exact official archive

**Status:** confirmed  
**Retained source:** `STAGE2_COMPARISON.md:19` (relevant source section; ID absent from narrative)  
**Related public data:** [evidence/measurements.json](../evidence/measurements.json)  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [artifact-provenance](../docs/artifact-provenance.md)

**Evidence:** Complete ZIP comparison with Apple catalog measurement

**Observation:** 1186 staged update files and three symlinks match exact official archive

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Four original staging files lack exact vendor byte references

**Follow-up:** Four original staging files lack exact vendor byte references

