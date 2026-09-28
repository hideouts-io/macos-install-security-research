---
layout: default
title: Limits and evidence boundaries
---

# Limits and evidence boundaries

[Home](../README.md) · [Methods](methodology.md) · [Coverage](coverage.md) · [Open questions](open-questions.md)

This is a **live logical examination of staged update data and reconstructed images**, not a physical disk image, a firmware readback, or a capture of an active restore/boot session. Original hashes establish the files' state during examination, not custody before collection. Reading may affect access times. A Finder working copy has different ownership/timestamps; source and copy metadata are kept distinct in the private workspace.

Exact corresponding-file matches against an Apple distribution support origin of the matched bytes. Four original presentation/index files lack exact vendor counterparts. The retained folder is a subset of the complete update, so absent files are not by themselves evidence of deletion or tampering. A valid hash, signature, certificate chain, or trust-cache entry does not establish the device's effective boot policy, rollback decision, runtime acceptance, or absence of software vulnerabilities.

Static code and configuration show capabilities and selected paths. They do not prove that a service launched, a socket listened, a USB peer connected, a token was accepted, an NVRAM variable changed, firmware was flashed, a seal was skipped, or a system was compromised. Some analyses are exact-build and architecture-specific: the detailed KC/NVRAM/EFI work is on the matched **Intel** artifact and does not close Apple Silicon LocalPolicy/SEP behavior.

The 147,253-object path register is fully enumerated but far from fully semantically analyzed: 72 bounded path records and zero whole-object closures. Eight embedded components have separate bounded records. Uninspected code, unnamed nested containers, protected/inaccessible paths, original ACL/creation-time/xattr-value gaps, runtime policy, caller provenance, historical logs, and hardware acceptance remain open. See [coverage](coverage.md) and [audit status](audit-status.md).

Public reproducibility is intentionally constrained. This repository does not redistribute proprietary Apple binaries, full extracted images, firmware payloads, raw disassembly dumps, machine identifiers, credentials, logs, or private evidence manifests. It provides hashes, selected addresses/offsets, derived tables, methods and qualified findings. A reviewer needs a legally acquired exact-build artifact for byte-for-byte independent reproduction. [Evidence handling](../evidence/README.md) and [reproduction](reproduction.md) explain what is and is not repeatable from this repository alone.
