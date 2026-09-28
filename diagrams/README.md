---
layout: default
title: Research diagrams
---

# Research diagrams

[Home](../README.md) · [Architecture](../docs/architecture.md) · [Methods](../docs/methodology.md)

SVG files render in GitHub Pages; the paired Mermaid sources remain editable text. Solid arrows represent observed packaging or bounded static relationships. Dashed arrows represent an unknown historical/runtime transition. A diagram does not turn a static capability into an observed event.

| Diagram | Subject |
| --- | --- |
| [Installation flow](installation-flow.svg) ([source](installation-flow.mmd)) | Apple reference, staging, RAMDisk, brain, ramrod, and firmware paths |
| [NVRAM authorization](nvram-authorization.svg) ([source](nvram-authorization.mmd)) | Name matching, process profile, MAC result, and firmware request boundaries |
| [NVRAM request chain](nvram-request-chain.svg) ([source](nvram-request-chain.mmd)) | Setter and kernel request boundaries |
| [NVRAM driver policy](nvram-driver-policy.svg) ([source](nvram-driver-policy.mmd)) | Driver-level static policy checks |
| [EFI path construction](efi-path-construction.svg) ([source](efi-path-construction.mmd)) | Typed and registry-derived input paths |
| [Firmware handoff](firmware-handoff.svg) ([source](firmware-handoff.mmd)) | Launcher, helper, bless, MultiUpdater, EFI/NVRAM |
| [Firmware helper chain](firmware-helper-chain.svg) ([source](firmware-helper-chain.mmd)) | Staging and helper call relationships |
| [Restore server request](restore-server-request.svg) ([source](restore-server-request.mmd)) | Restore service request path |
| [FDR trust object](fdr-trust-object.svg) ([source](fdr-trust-object.mmd)) | Request and trust-object relationships |
| [Restore transport and TLS](restore-transport-tls.svg) ([source](restore-transport-tls.mmd)) | Configuration and transport boundaries |
| [Evidence ladder](evidence-ladder.svg) ([source](evidence-ladder.mmd)) | Measurement, inference, runtime evidence and unresolved policy |
