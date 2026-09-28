---
layout: default
title: "Remote services, TLS, and identity findings"
---

# Remote services, TLS, and identity findings

[Home](../README.md) · [Findings index](../docs/findings-index.md) · [Subsystem analysis](../docs/usb-and-services.md)

The [source crosswalk](../tables/finding-provenance.csv) maps every ID to a retained audit document and distinguishes an explicit ID mention from section context. Each record retains the original audit ledger wording and its explicit limit. Raw disassembly, copies of Apple binaries, and host-specific artifacts are intentionally absent. A **bounded** finding describes only the examined path or artifact.

<a id="svc-001"></a>
## SVC-001 — Intel remoted CoreDevice handler checks caller audit-token entitlement presence; separate device-admin helper controls sensitive-property descriptions

**Status:** bounded  
**Retained source:** `publication/README.md:355` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5C remoted listener block0x100063040; token lookup0x100003dae; missing-object branch0x100003dc6; helper0x10002c9b8 and selector0x10002b924

**Observation:** Intel remoted CoreDevice handler checks caller audit-token entitlement presence; separate device-admin helper controls sensitive-property descriptions

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Presence check differs from Boolean-true check; not complete command authorization or network-peer authentication; no unauthorized route established

**Follow-up:** Presence check differs from Boolean-true check; not complete command authorization or network-peer authentication; no unauthorized route established

<a id="svc-002"></a>
## SVC-002 — Intel BaseSystem PAM module delegates to sshd-fvunlock through a pipe and checks helper failures before success reboot transition

**Status:** bounded  
**Retained source:** `publication/README.md:359` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5C matched PAM module; spawn0x87c; pipe write0x8d1; wait0x8f7; exit classification0x973; reboot3 call0xa29; version-bounded Apple FileVault documentation

**Observation:** Intel BaseSystem PAM module delegates to sshd-fvunlock through a pipe and checks helper failures before success reboot transition

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Stage5D extends helper AKS/APFS tracing; backend throttling full target/input mapping and PAM module resolution remain open; Remote Login enabled state and historical unlocking unmeasured

**Follow-up:** Stage5D extends helper AKS/APFS tracing; backend throttling full target/input mapping and PAM module resolution remain open; Remote Login enabled state and historical unlocking unmeasured

<a id="svc-003"></a>
## SVC-003 — Identical USB mux sandbox profiles use active deny-default plus explicit grants; broad allow-default examples are comments

**Status:** bounded  
**Retained source:** `publication/README.md:365` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5C both profile hashes04dce17fc70baebcc38bbec7711208986808baa2f2621c29262d67f1e937aab9; retained profile text

**Observation:** Identical USB mux sandbox profiles use active deny-default plus explicit grants; broad allow-default examples are comments

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Imported policy composition and actual consumer untraced; capabilities do not prove execution pairing or network traffic

**Follow-up:** Imported policy composition and actual consumer untraced; capabilities do not prove execution pairing or network traffic

<a id="svc-004"></a>
## SVC-004 — Intel sshd-fvunlock checks AKS status and caller error state before APFS unlock loop; subsequent ACM callback logs policy result without constructing an authentication error

**Status:** bounded  
**Retained source:** `publication/README.md:371` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5D inventory-matched helper f3632d5a884f458c2f8446f498f4f9f004eac5a6ad8b0e5bb301359c0e76b99e; AKS gate0x100007435; caller0x1000039be; APFS0x1000045fa; callback0x100004aa0; function-start and LLDB entry checks

**Observation:** Intel sshd-fvunlock checks AKS status and caller error state before APFS unlock loop; subsequent ACM callback logs policy result without constructing an authentication error

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Not a bypass finding; backend verifier throttling full target/input mapping ARM equivalence and runtime unlocking remain unverified; public source version differs

**Follow-up:** Not a bypass finding; backend verifier throttling full target/input mapping ARM equivalence and runtime unlocking remain unverified; public source version differs

<a id="svc-005"></a>
## SVC-005 — Intel remoted local and remote service policy producers and override precedence traced with three access-helper callers

**Status:** bounded  
**Retained source:** `publication/README.md:389` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5E local init0x100005494; description writer0x100005cf7; remote constructor0x10000c956; gate0x100029d88; callers0x10000c600 0x10002cc0c 0x10002d2a7

**Observation:** Intel remoted local and remote service policy producers and override precedence traced with three access-helper callers

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Remote description provenance and transport identity unresolved; entitlement presence is not Boolean true; no unauthorized override or complete connection authorization established

**Follow-up:** Remote description provenance and transport identity unresolved; entitlement presence is not Boolean true; no unauthorized override or complete connection authorization established

<a id="svc-006"></a>
## SVC-006 — Sixteen RemoteServices declarations and selected remoted exposure-policy branches reviewed; missing EncryptSocketData defaults false in local description

**Status:** bounded  
**Retained source:** `publication/README.md:395` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5E 14 hash-linked plist paths; setExposePolicy0x100005ee0; selected serviceWantsToBeExposedToDevice branches; default writer0x100005e37

**Observation:** Sixteen RemoteServices declarations and selected remoted exposure-policy branches reviewed; missing EncryptSocketData defaults false in local description

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Exposure flags do not establish activation or unauthenticated access; per-service encryption property does not prove outer transport plaintext; ARM control flow and full policy composition untraced

**Follow-up:** Exposure flags do not establish activation or unauthenticated access; per-service encryption property does not prove outer transport plaintext; ARM control flow and full policy composition untraced

<a id="svc-007"></a>
## SVC-007 — Intel remoted checks required TLS before ordinary handshake completion and supplies a separate Boolean verification callback to RemoteXPC

**Status:** bounded  
**Retained source:** `publication/README.md:417` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5F policy mapper0x10001c7a4; negotiation0x100007b9f; required check0x100007f37; cancel0x100008097; set_tls0x100008458; callback0x100008bc8; authentication helper0x10001f9dc

**Observation:** Intel remoted checks required TLS before ordinary handshake completion and supplies a separate Boolean verification callback to RemoteXPC

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Enable flag is negotiation intent not crypto success; certificate evaluator identity provenance backend policy RemoteXPC enforcement and accepted-description integrity unresolved; no runtime authentication measured

**Follow-up:** Enable flag is negotiation intent not crypto success; certificate evaluator identity provenance backend policy RemoteXPC enforcement and accepted-description integrity unresolved; no runtime authentication measured

<a id="svc-008"></a>
## SVC-008 — Intel remoted conditionally verifies DCRT/DAK and compares attested public key with selected peer certificate; two embedded roots match Apple public constants

**Status:** bounded  
**Retained source:** `publication/README.md:429` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5G evaluator0x10001fec9; trust helper0x1000230de; AKS verify0x100021130; equality0x100021264; two extracted root self-signatures and DER hash matches

**Observation:** Intel remoted conditionally verifies DCRT/DAK and compares attested public key with selected peer certificate; two embedded roots match Apple public constants

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Required OID set and device type determine paths; chassis and AKS internals remain incomplete; public Security source not exact-build verification; no peer authentication tested

**Follow-up:** Required OID set and device type determine paths; chassis and AKS internals remain incomplete; public Security source not exact-build verification; no peer authentication tested

<a id="svc-009"></a>
## SVC-009 — Intel remoted DCRT helper accepts certain expiration failures through either expired-only check or error domain/code match

**Status:** requires investigation  
**Retained source:** `publication/README.md:446` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED observation; impact UNKNOWN  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5G SecTrustEvaluateWithError0x1000238db; SecTrustIsExpiredOnly0x1000238ec; NSOSStatusErrorDomain/-67818 match0x10002390a; null-error success0x100023ba5

**Observation:** Intel remoted DCRT helper accepts certain expiration failures through either expired-only check or error domain/code match

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Domain/code fallback does not itself inspect all trust failures; exact-build aggregation and effective peer policy unresolved; no arbitrary certificate acceptance or exploitable bypass demonstrated

**Follow-up:** Domain/code fallback does not itself inspect all trust failures; exact-build aggregation and effective peer policy unresolved; no arbitrary certificate acceptance or exploitable bypass demonstrated

<a id="svc-010"></a>
## SVC-010 — Intel remoted base/controller/node required-OID methods include DCRT and DAK; node conditionally adds chassis OID; ordinary chassis policy precedence and false default traced

**Status:** bounded  
**Retained source:** `publication/README.md:456` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5H three constant arrays; four class methods; verification caller0x10001fa38; chassis helper0x10001a4e8; setting resolver0x10001c7ff

**Observation:** Intel remoted base/controller/node required-OID methods include DCRT and DAK; node conditionally adds chassis OID; ordinary chassis policy precedence and false default traced

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Loopback returns empty; TLS activation and all class inheritance not established; preferences implementation and effective settings unresolved

**Follow-up:** Loopback returns empty; TLS activation and all class inheritance not established; preferences implementation and effective settings unresolved

<a id="svc-011"></a>
## SVC-011 — Intel remoted outer chassis checks permit success on local-manifest-unavailable type16 or absent optional peer manifest type15

**Status:** requires investigation  
**Retained source:** `publication/README.md:469` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED observation; impact UNKNOWN  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5H null local manifest0x1000217b6 to success0x100021f3e; peer absence0x100021988 and policy0x1000220e0; optional success0x100022c43; present-invalid and matcher-result failure routes

**Observation:** Intel remoted outer chassis checks permit success on local-manifest-unavailable type16 or absent optional peer manifest type15

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Earlier DCRT/DAK requirements remain; inner matchers AMFDR and settings protections incomplete; no hostile input control or unauthorized peer access demonstrated

**Follow-up:** Earlier DCRT/DAK requirements remain; inner matchers AMFDR and settings protections incomplete; no hostile input control or unauthorized peer access demonstrated

<a id="svc-012"></a>
## SVC-012 — Intel remoted chassis matching compares numeric identity pairs; parsers check hex scan success without explicit full-field consumption and local identity conversions have unchecked results

**Status:** requires investigation  
**Retained source:** `publication/README.md:484` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED observation; impact UNKNOWN  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5I parsers0x100023c55/0x100025206; node comparisons0x1000248aa/0x1000248ba; controller equality0x100025042; CFNumberGetValue0x100024c41/0x100024c51; separate seven-case host Scanner probe

**Observation:** Intel remoted chassis matching compares numeric identity pairs; parsers check hex scan success without explicit full-field consumption and local identity conversions have unchecked results

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Host25G229 differs from audited25G83; input authenticity and provider guarantees unresolved; no target execution or forged identity acceptance demonstrated

**Follow-up:** Host25G229 differs from audited25G83; input authenticity and provider guarantees unresolved; no target execution or forged identity acceptance demonstrated

<a id="svc-013"></a>
## SVC-013 — RSDPreferences uses stored-domain current-user/current-host CFPreferences reads/writes and a bounded version-marker migration

**Status:** bounded  
**Retained source:** `publication/README.md:494` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5I getter0x100011133; setter0x1000111c3; migration0x100010f9b; embedded integers0/1; synchronize0x100011212; six direct setter-selector references

**Observation:** RSDPreferences uses stored-domain current-user/current-host CFPreferences reads/writes and a bounded version-marker migration

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No backing-file path ACL effective runtime user persistence success or caller write authorization established; no live preferences read or changed

**Follow-up:** No backing-file path ACL effective runtime user persistence success or caller write authorization established; no live preferences read or changed

<a id="svc-014"></a>
## SVC-014 — Intel remoted string preference then enabled feature then boot argument selects TLS policy before backend defaults

**Status:** bounded  
**Retained source:** `publication/README.md:504` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5J resolver0x10001ce4b; compute0x1000323c5; NCM0x100037805; loopback0x100039d24; five-entry hardware dictionary0x1000658c0

**Observation:** Intel remoted string preference then enabled feature then boot argument selects TLS policy before backend defaults

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Defaults differ by backend; no actual MobileGestalt preferences boot arguments or traffic acquired; disabled policy does not prove plaintext or a vulnerability

**Follow-up:** Defaults differ by backend; no actual MobileGestalt preferences boot arguments or traffic acquired; disabled policy does not prove plaintext or a vulnerability

<a id="svc-015"></a>
## SVC-015 — Compute TLS mutation is gated by audit-token entitlement object presence and maps Boolean false/true to optional/required

**Status:** requires investigation  
**Retained source:** `publication/README.md:504` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED observation; impact UNKNOWN  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5J entitlement lookup0x10001bd71 presence check0x10001bd82; require_tls handler0x10001c638 and setter0x100032359

**Observation:** Compute TLS mutation is gated by audit-token entitlement object presence and maps Boolean false/true to optional/required

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No explicit entitlement Boolean-truth test on reviewed path; issuance external writers persistence and runtime reachability unresolved; no unprivileged mutation demonstrated

**Follow-up:** No explicit entitlement Boolean-truth test on reviewed path; issuance external writers persistence and runtime reachability unresolved; no unprivileged mutation demonstrated

<a id="svc-016"></a>
## SVC-016 — Identity startup schedules scoped stored-identity deletion separately from generation and replacement of the TLS prerequisite slot

**Status:** bounded  
**Retained source:** `publication/README.md:522` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5J startup0x10001f335 block0x10001f41f deletion0x10001e87d replacement0x10001d32e; generation wrapper0x10001d301 and administrative entitlement lookup0x10002ee96

**Observation:** Identity startup schedules scoped stored-identity deletion separately from generation and replacement of the TLS prerequisite slot

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Stage5K expands ordinary generator and reload behavior; complete caller framework and metadata-publication enforcement remain partial; no live keychain identity or private key acquired

**Follow-up:** Stage5K expands ordinary generator and reload behavior; complete caller framework and metadata-publication enforcement remain partial; no live keychain identity or private key acquired

<a id="svc-017"></a>
## SVC-017 — Intel remoted requests a 256-bit EC AppleKeyStore key and separately adds the resulting identity to the system keychain

**Status:** bounded  
**Retained source:** `publication/README.md:534` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5K ACL0x10001d615 flags0x40000000; key0x10001d73a; integer256 at0x100065890; identity-add0x10001dfb9; pinned Apple headers

**Observation:** Intel remoted requests a 256-bit EC AppleKeyStore key and separately adds the resulting identity to the system keychain

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Token name does not prove Secure Enclave residency; public header permits kernel emulation; no actual key storage or hardware state acquired

**Follow-up:** Token name does not prove Secure Enclave residency; public header permits kernel emulation; no actual key storage or hardware state acquired

<a id="svc-018"></a>
## SVC-018 — Identity generation can omit DCRT DAK and chassis extensions while creation/storage failures return null

**Status:** bounded  
**Retained source:** `publication/README.md:542` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5K missing-material branches0x10001d796/0x10001dcc7/0x10001dd7f; self-sign0x10001dead; failure cleanup0x10001e3d5 and return0x10001e586

**Observation:** Identity generation can omit DCRT DAK and chassis extensions while creation/storage failures return null

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Producer success is separate from peer verification; required OIDs remain enforced on earlier examined class paths; exact backend and exception behavior unresolved

**Follow-up:** Producer success is separate from peer verification; required OIDs remain enforced on earlier examined class paths; exact backend and exception behavior unresolved

<a id="svc-019"></a>
## SVC-019 — Async reload checks requested extension presence on stored identity but not after regeneration; null-slot refresh leaves OID metadata unchanged

**Status:** requires investigation  
**Retained source:** `publication/README.md:555` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED observation; impact UNKNOWN  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5K containment0x10001f13e; regenerate0x10001f206 to replacement dispatch0x10001f284; refresh0x10000d064/0x10000d08a

**Observation:** Async reload checks requested extension presence on stored identity but not after regeneration; null-slot refresh leaves OID metadata unchanged

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Caller completion other writers publication timing and peer enforcement unresolved; no stale wire advertisement or authentication bypass demonstrated

**Follow-up:** Caller completion other writers publication timing and peer enforcement unresolved; no stale wire advertisement or authentication bypass demonstrated

<a id="svc-020"></a>
## SVC-020 — Local get_local_device_identity serializes token object blob and certificate; no entitlement or UID gate in inspected listener/getter route

**Status:** requires investigation  
**Retained source:** `publication/README.md:565` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED observation; impact UNKNOWN  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5L Mach listener0x10002bed9; dispatcher0x10002c04b; async caller0x10002ec1b; completion0x10002f3ed; token attribute0x10002f622; reply0x10002ed27

**Observation:** Local get_local_device_identity serializes token object blob and certificate; no entitlement or UID gate in inspected listener/getter route

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** External Mach/sandbox reachability and token-use rights unresolved; no plaintext key disclosure or actual request demonstrated; query can reach generation

**Follow-up:** External Mach/sandbox reachability and token-use rights unresolved; no plaintext key disclosure or actual request demonstrated; query can reach generation

<a id="svc-021"></a>
## SVC-021 — Identity completions differ; compute helper selects TLS-disable configuration on null identity while TLS-enabled loopback crashes

**Status:** requires investigation  
**Retained source:** `publication/README.md:578` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED observation; impact UNKNOWN  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5L six direct callers; arrays657b8/657e8; compute helper0x100032e1e; nw_parameters_create_secure_tcp0x100017748; loopback0x100039408 to0x10004cee7

**Observation:** Identity completions differ; compute helper selects TLS-disable configuration on null identity while TLS-enabled loopback crashes

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Layer-specific configuration not established accepted plaintext transport; downstream RemoteXPC setup and enforcement incomplete; no identity or connection experiment

**Follow-up:** Layer-specific configuration not established accepted plaintext transport; downstream RemoteXPC setup and enforcement incomplete; no identity or connection experiment

<a id="svc-022"></a>
## SVC-022 — Global populated-OID metadata is included in outgoing handshake Properties and peer parser collects string elements

**Status:** bounded  
**Retained source:** `publication/README.md:565` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5L global0x10006e370; property attachment0x100008600; send0x100008ad9; tlsOidsPopulatedOnPeer0x10000791e

**Observation:** Global populated-OID metadata is included in outgoing handshake Properties and peer parser collects string elements

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Other writers and timing incomplete; no stale wire metadata or peer acceptance established; advertisement not certificate authentication

**Follow-up:** Other writers and timing incomplete; no stale wire metadata or peer acceptance established; advertisement not certificate authentication

<a id="svc-023"></a>
## SVC-023 — authenticate_device parses supplied certificate and returns a checked type/OID evaluator result; it is distinct from private-key possession or live TLS authentication

**Status:** bounded  
**Retained source:** `publication/README.md:600` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5M dispatcher0x10002adb6; call0x10002b49f; identity_cert read0x10002e0ab; parse0x10002e0c2; evaluator0x100023033; OK0x10002e15d

**Observation:** authenticate_device parses supplied certificate and returns a checked type/OID evaluator result; it is distinct from private-key possession or live TLS authentication

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Endpoint distribution and complete authorization unresolved; earlier evaluator exceptions remain; no actual certificate or peer submitted; does not consume identity_key

**Follow-up:** Endpoint distribution and complete authorization unresolved; earlier evaluator exceptions remain; no actual certificate or peer submitted; does not consume identity_key

<a id="svc-024"></a>
## SVC-024 — Exact-cache framework reconstructs local identity through AppleKeyStore token-OID attributes and adapts it to a TLS identity

**Status:** requires investigation  
**Retained source:** `publication/README.md:610` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED observation; impact UNKNOWN  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** 132 exports agree with original nlist; client request and checked parsing; 33 slide-pointer checks and 13 import-stub corroborations; SecKeyCreateWithData and SecIdentityCreate argument trace; Stage5O Security token dispatch session construction object lookup and registered-token exception

**Observation:** Exact-cache framework reconstructs local identity through AppleKeyStore token-OID attributes and adapts it to a TLS identity

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No real token obtained or used; endpoint reachability and provider authorization unresolved; no plaintext private-key disclosure or accepted TLS session established; nonnull wrapper is not proof of usable token object or signing

**Follow-up:** No real token obtained or used; endpoint reachability and provider authorization unresolved; no plaintext private-key disclosure or accepted TLS session established; nonnull wrapper is not proof of usable token object or signing

<a id="svc-025"></a>
## SVC-025 — RSD certificate-query reply callback accepts null result-string return and feeds a TLS verification adapter

**Status:** requires investigation  
**Retained source:** `publication/README.md:654` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED observation; impact UNKNOWN  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5O exact-cache query and reply branches0x7ff814639d77/0x7ff814639e21; TLS adapter0x7ff81463e98c; byte and selector rechecks

**Observation:** RSD certificate-query reply callback accepts null result-string return and feeds a TLS verification adapter

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Server producer returns OK/ERROR; adverse reply producer endpoint control exact API handling and accepted transport remain unestablished; no bypass or severity claimed

**Follow-up:** Server producer returns OK/ERROR; adverse reply producer endpoint control exact API handling and accepted transport remain unestablished; no bypass or severity claimed

<a id="svc-026"></a>
## SVC-026 — AppleKeyStore request selects SEP token/session classes; local key implementation selected through typed nonzero current-task entitlement gate unless explicit ctkdConnection exists

**Status:** bounded  
**Retained source:** `publication/README.md:679` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5P exact constants and class/selector pointers; canUseSEPLocally0x7ff813c68f86; entitlement query0x7ff813c69003 and flag store0x7ff813c6909f;1376 selected instructions byte-checked

**Observation:** AppleKeyStore request selects SEP token/session classes; local key implementation selected through typed nonzero current-task entitlement gate unless explicit ctkdConnection exists

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Routing gate is not complete key-use authorization; sik.access failure only logs in examined block; SVC-027/028 trace constructors and retry/parameters; server/AKS rights and hardware backing unresolved

**Follow-up:** Routing gate is not complete key-use authorization; sik.access failure only logs in examined block; SVC-027/028 trace constructors and retry/parameters; server/AKS rights and hardware backing unresolved

<a id="svc-027"></a>
## SVC-027 — Concrete SEP key constructors distinguish unknown identifiers from denied system keys; reference-key signing checks AKS status; remote attributes use synchronous CTKD IPC

**Status:** bounded  
**Retained source:** `publication/README.md:709` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5Q30 functions2538 byte-checked instructions;93 pointer chains15 CFStrings; system-key entitlement and caller route; AKS blob/sign results; CTKD Mach service and required reply fields

**Observation:** Concrete SEP key constructors distinguish unknown identifiers from denied system keys; reference-key signing checks AKS status; remote attributes use synchronous CTKD IPC

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Client checks do not prove server caller authorization or backend ACL enforcement; no actual token import signing identity request or accepted transport; operation-block caller mapping and ARM equivalence remain open

**Follow-up:** Client checks do not prove server caller authorization or backend ACL enforcement; no actual token import signing identity request or accepted transport; operation-block caller mapping and ARM equivalence remain open

<a id="svc-028"></a>
## SVC-028 — Deferred token object is reconstructed before operation; registered-token errors permit one guarded retry; authentication handle and ACL/caller-group intersection reach AKS parameters

**Status:** bounded  
**Retained source:** `publication/README.md:742` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5R6 Security and17 CryptoTokenKit functions;1398 byte-checked instructions83 pointer chains10 CFStrings; ensureTokenObject and retry predicates; externalizedContext requirement; cag membership and AKS parameter keys1/3

**Observation:** Deferred token object is reconstructed before operation; registered-token errors permit one guarded retry; authentication handle and ACL/caller-group intersection reach AKS parameters

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** No live credential context or key used; operation blocks server audit-token checks context validation AKS backend and ARM remain unresolved; no unrestricted-access or authentication-bypass claim

**Follow-up:** No live credential context or key used; operation blocks server audit-token checks context validation AKS backend and ARM remain unresolved; no unrestricted-access or authentication-bypass claim

<a id="svc-029"></a>
## SVC-029 — CTKD passes the current XPC connection to a new local key; shared key-cache hits compare object ID and auth context without an explicit caller or force-session comparison

**Status:** bounded; requires investigation  
**Retained source:** `publication/README.md:769` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5S 11 CTKD functions832 instructions10 original methods47 references; local initializer51 instructions4 pointer chains; four inventory-matched files

**Observation:** CTKD passes the current XPC connection to a new local key; shared key-cache hits compare object ID and auth context without an explicit caller or force-session comparison

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Context binding and availability; server-instance scope; retained-caller and AKS authorization unresolved; no cross-client key use or bypass demonstrated

**Follow-up:** Context binding and availability; server-instance scope; retained-caller and AKS authorization unresolved; no cross-client key use or bypass demonstrated

<a id="svc-030"></a>
## SVC-030 — AKS setter removes prior parameter before replacement validation; import/signing wrappers check preparation results and propagate operation status

**Status:** bounded  
**Retained source:** `publication/README.md:791` (explicit ID in source narrative)  
**Related public data:** No independent per-ID dataset is published; see the scoped evidence description below.  
**Evidence level:** VERIFIED (bounded static or measured observation)  
**Subsystem analysis:** [usb-and-services](../docs/usb-and-services.md)

**Evidence:** Stage5T4body functions plusentry thunk390instructions excluding11padding bytes; original internal symbols

**Observation:** AKS setter removes prior parameter before replacement validation; import/signing wrappers check preparation results and propagate operation status

**Interpretation:** Prior scoped conclusion retained; see status and limit

**Security relevance:** See linked finding context; not independently re-rated in this segment

**Confidence field:** Unknown in this new field; prior status/evidence classification preserved

**Limit:** Ignored setter status is a caller review question; backend authorization/context binding and external import targets unresolved; no unauthorized key use demonstrated

**Follow-up:** Ignored setter status is a caller review question; backend authorization/context binding and external import targets unresolved; no unauthorized key use demonstrated

