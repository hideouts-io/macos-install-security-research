---
layout: default
title: "Resolved anomalies and corrected interpretations"
---

# Resolved anomalies and corrected interpretations

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

<a id="resolved-anomalies-and-corrections"></a>
## Resolved anomalies and corrections

| Initial question | Result so far |
| --- | --- |
| Raw RAMDisk has no UDIF checksum | Expected for its raw APFS format; supplied chunk hashes match |
| BaseSystem `.dmg` cannot be handled as an ordinary image | It is a BXDIFF50 full-replacement container; reconstruction validated |
| Many strict codesign failures | Same relevant bytes occur in the official distribution; resource/format failures remain recorded |
| Missing PurpleReverseProxy executable | Also absent in the exact official-matching RAMDisk; activation not demonstrated |
| All proxy sockets assumed loopback | Incorrect: control socket lacks explicit loopback node |
| Firmware whole-file digest mismatches | FTAB internal regions, UARP composition, DP855 selected regions and restore-tag representations explain the examined cases |
| Four trust-cache signed-digest mismatches | Official signed counterparts have identical entry arrays, differing only type/UUID; runtime choice unresolved |
| 49 code hashes missing from staged cache subset | Present in an omitted official cryptex cache |
| Eight-byte EFI security-directory size | Pointer structure leads to full Apple certificate; signatures verified |
| Product.efi is not PE | Loader recognizes an encrypted wrapper; plaintext/trailer still unknown |
| Root-hash log says xmtr | Code requests xsys; both objects are present in examined tickets |
| NVRAM override parser assumed reachable | Ordinary loader gate compares distinct true/false objects; preliminary inference corrected |
| DoNotSeal interpreted as an exploit | Official option/serialization capability established; unauthorized reachability not demonstrated |
| NSXPC selector assumed to reach update writer | Preliminary metadata identifies returning base methods; separate command implementation must be traced |


