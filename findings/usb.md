---
layout: default
title: "USB and launch services findings"
---

# USB and launch services findings

[Home](../README.md) · [Findings index](../docs/findings-index.md) · [Subsystem analysis](../docs/usb-and-services.md)

The [source crosswalk](../tables/finding-provenance.csv) maps every ID to a retained audit document and distinguishes an explicit ID mention from section context. Each record retains the original audit ledger wording and its explicit limit. Raw disassembly, copies of Apple binaries, and host-specific artifacts are intentionally absent. A **bounded** finding describes only the examined path or artifact.

<a id="usb-001"></a>
## USB-001 — Proxy service definition references absent executable

**Status:** confirmed  
**Retained source:** `REPORT.md:89` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Ramdisk inventory and launch plist

**Observation:** Proxy service definition references absent executable

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Other runtime sources not established

**Follow-up:** Other runtime sources not established

<a id="usb-002"></a>
## USB-002 — Control socket lacks explicit loopback binding

**Status:** confirmed  
**Retained source:** `REPORT.md:118` (relevant source section; ID absent from narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Proxy launch plist

**Observation:** Control socket lacks explicit loopback binding

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No active listener or exploitability demonstrated

**Follow-up:** No active listener or exploitability demonstrated

