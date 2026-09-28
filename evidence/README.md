---
layout: default
title: Public evidence and provenance
---

# Public evidence and provenance

[Home](../README.md) · [Findings](../docs/findings-index.md) · [Methods](../docs/methodology.md)

This directory contains **derived, publication-safe evidence only**. The [measurement file](measurements.json) records build identity, counts, selected hashes and bounded validation results from the existing audit. [Publication provenance](publication-provenance.json) records SHA-256 values of the retained source documents used to construct this repository. The [finding ledger](../tables/findings.csv) holds observations and scoped limits; the [source crosswalk](../tables/finding-provenance.csv) maps all 100 IDs to a retained document and source line, distinguishing explicit ID mentions from earlier section context. The [EFI converter branch register](../tables/efi-converter-branches.csv) and [firmware-helper census](../tables/firmware-helpers.csv) are related derived datasets, not whole-object evidence. The [external-link check](external-links.json) records HTTP results for reference URLs. The [`checksums.sha256`](checksums.sha256) file hashes the public data and diagrams.

| Evidence class | Public representation | Original retained privately |
| --- | --- | --- |
| Original versus copy | Counts and comparison conclusion | Full path inventory, hashes, original metadata, exceptions |
| Exact Apple reference | Matched counts and source-document hashes | Acquired package, distribution records, archive member records and extraction logs |
| Disk images and firmware | Sizes, digests, format/signature conclusions | Apple binaries, reconstructed images, firmware payloads, full parser output |
| Reverse engineering | Bounded addresses, branch tables, call relationships and limitations | Original-byte checks, decoded instructions, symbol/fixup dumps and intermediate analysis |
| Services and transport | Configuration/path findings and negative limits | Full launch inventories, protected files, logs and host metadata |
| Coverage | Counts, status and exact next step | 147,253-row path register, private validation/manifests and unresolved queue |

Public files do **not** contain Apple binaries, raw disassembly dumps, secrets, credentials, personal identifiers, machine serials, local usernames, raw NVRAM values, private certificates/keys, or runtime traffic. Static certificate/public-key fingerprints and artifact hashes appear where they support a concrete comparison; they are not host secrets. A private evidence file name in a research page is a provenance pointer for the original audit, not a broken promised download.

The manifest here verifies **this public draft's files**, not the Apple originals, historical custody, or a future GitHub release. The retained source-document digests allow a holder of the private audit workspace to verify which report versions informed this draft; readers without those documents cannot independently reproduce the crosswalk. Use the [reproduction guide](../docs/reproduction.md) and [limitations](../docs/limitations.md) before treating a result as independently repeatable. No original material was changed to create this repository.
