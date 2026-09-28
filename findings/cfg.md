---
layout: default
title: "Configuration and services findings"
---

# Configuration and services findings

[Home](../README.md) · [Findings index](../docs/findings-index.md) · [Subsystem analysis](../docs/usb-and-services.md)

The [source crosswalk](../tables/finding-provenance.csv) maps every ID to a retained audit document and distinguishes an explicit ID mention from section context. Each record retains the original audit ledger wording and its explicit limit. Raw disassembly, copies of Apple binaries, and host-specific artifacts are intentionally absent. A **bounded** finding describes only the examined path or artifact.

<a id="cfg-001"></a>
## CFG-001 — 78465 selected plist candidates freshly hash-match inventory and parse across seven scopes

**Status:** bounded  
**Retained source:** `STAGE5_CONFIGURATION.md:49` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5A per-scope JSONL and summaries; 79071 candidates

**Observation:** 78465 selected plist candidates freshly hash-match inventory and parse across seven scopes

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** 606 protected candidates unreadable; structural parse does not establish semantic review; unnamed embedded plists outside selection

**Follow-up:** 606 protected candidates unreadable; structural parse does not establish semantic review; unnamed embedded plists outside selection

<a id="cfg-002"></a>
## CFG-002 — Seven Intel Python XML parser failures are accepted by Apple plutil and parse via native conversion

**Status:** resolved  
**Retained source:** `STAGE5_CONFIGURATION.md:50` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5A native-plist-reconciliation.json and matched source hashes

**Observation:** Seven Intel Python XML parser failures are accepted by Apple plutil and parse via native conversion

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Parser compatibility result for these bytes; not a general parser-security assessment

**Follow-up:** Parser compatibility result for these bytes; not a general parser-security assessment

<a id="cfg-003"></a>
## CFG-003 — 475 of 477 launch-directory plists declare programs; 439 resolve within same image and 36 require deployment review

**Status:** bounded  
**Retained source:** `STAGE5_CONFIGURATION.md:51` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5A launch-service-map.json with image-relative symlink resolution; two other files are jetsam policy dictionaries

**Observation:** 475 of 477 launch-directory plists declare programs; 439 resolve within same image and 36 require deployment review

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Declarations are not execution or reachability; missing same-image programs alone do not establish compromise

**Follow-up:** Declarations are not execution or reachability; missing same-image programs alone do not establish compromise

<a id="cfg-004"></a>
## CFG-004 — Stage5B reconciles 477 launch plist hash references and classifies 19 socket groups; 11 of 36 unresolved declarations have cross-image path candidates

**Status:** bounded  
**Retained source:** `publication/README.md:347` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5B socket-declarations.json; unresolved-programs.json; seven saved inventories; 14 filesystem socket groups and 5 service-name groups

**Observation:** Stage5B reconciles 477 launch plist hash references and classifies 19 socket groups; 11 of 36 unresolved declarations have cross-image path candidates

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Cross-image names do not prove deployment; no active listener authentication pairing or remote session measured; missing consumer alone does not preclude launchd socket registration

**Follow-up:** Cross-image names do not prove deployment; no active listener authentication pairing or remote session measured; missing consumer alone does not preclude launchd socket registration

