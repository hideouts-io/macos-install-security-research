---
layout: default
title: "Code signatures and kernel collections"
---

# Code signatures and kernel collections

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

<a id="code-signatures-and-kernel-collections"></a>
## Code signatures and kernel collections

<a id="official-cleanup-bundle-certificate-chain-and-resource-coverage"></a>
### Official cleanup bundle, certificate chain and resource coverage

**SIG-010 — the exact official image reproduces the cleanup signature rejection.** Stage 4K.2 freshly reads the retained Apple update archive, checks its complete SHA-256, reconstructs its Intel BaseSystem member and compares the result with the image used earlier. The resulting 1,464,762,142-byte image has SHA-256 `bbfcbf7bfd09c79465fa92c741ebb665625794c31578b81248f7fa0c2bcd4789` in both routes. Reconstruction uses the same documented decoder algorithm; this is a fresh reference-input comparison, not independent implementation validation.

All **five files and four directories** in the cleanup bundle match the retained bundle's file bytes and item set. Ordinary and strict `codesign` verification directly against the read-only official image both reject the same obsolete custom-omit resource envelope. The rejection is therefore reproduced in the exact Apple-supplied image, rather than being attributable to a discovered local content difference. ACL and extended-attribute equivalence are not claimed.

The CMS chain is **macOS Software Signing → Apple Code Signing Certification Authority → Apple Root CA**. The embedded root is byte-identical to the certificate separately downloaded through [Apple's PKI directory](https://www.apple.com/certificateauthority/), with SHA-256 `b0b1730ecbc7ff4505142c49f1295e6eda6bcaed7e2c68c5be91b5a11001f024`. The leaf is valid from March 30, 2026 to April 27, 2027. Its extensions include code-signing extended key usage, digital-signature key usage and an Apple-internal certificate policy.

OpenSSL chain verification against that root, including its self-signature, succeeds at both the audit date and the CMS signing-time attribute. The host's `security verify-cert` **codeSign certificate policy** also succeeds at both dates using the explicitly supplied root, no keychain search and offline revocation mode. These checks evaluate certificate chains; they do not override full-bundle resource validation or establish recovery/restore acceptance. No fresh positive revocation response was obtained.

The CMS signed attribute reports **August 1, 2026, 08:18:43 UTC**. Its unsigned-attribute set is empty. This is a signer-provided signed time, not an independently verified timestamp-authority token or proof that installation occurred then.

| Bundle file | Purpose and checked protection |
| --- | --- |
| `Contents/MacOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService` | Cleanup XPC executable; code-page and signature-layer checks described above, plus exact official file match |
| `Contents/Info.plist` | Identifies the executable and System-type XPC service; bound through CodeDirectory special slot 1. SDK build `25G74` occurs in this exact `25G83` reference, so that differing metadata is not a discovered local modification |
| `Contents/_CodeSignature/CodeResources` | Resource-rule envelope; bound through special slot 3, but has no listed per-file resource hashes and contains blanket omit rules |
| `Contents/Resources/com.apple.MobileSoftwareUpdate.plist` | Logging configuration: oversize-message settings, category levels/retention values, process signposts and a public default-privacy declaration for `libpartition2`. Exact official match; no individual envelope hash. Actual logging, emitted values and privacy enforcement remain untested |
| `Contents/version.plist` | Project/build/source-version metadata for MobileSoftwareUpdate. Exact official match; no individual envelope hash |

**Assessment:** confirmed expected reference content with a reproducible host resource-policy rejection. This narrows the previous uncertainty substantially without claiming that every signing or runtime policy accepts the bundle. The logging settings describe capability and configuration, not evidence of information disclosure. Three newly bounded resource/configuration paths bring the ledger to **41 inventory paths plus four embedded components**; full per-file semantic coverage remains incomplete. Both read-only image attachments were detached and their absence verified.

<a id="cleanup-bundle-signature-layers"></a>
### Cleanup bundle signature layers

**SIG-009 — matching integrity layers with a rejected resource envelope.** Stage 4K.1 revisits the cleanup service's signature failure without altering the bundle. All five retained bundle files previously matched their acquisition inventory; the executable still has SHA-256 `471b633762d06ffd180cb57cdb865e10ce8b41c8c9242679ee272dfad4318b0d`.

| Layer | Result | Meaning |
| --- | --- | --- |
| Executable code pages | All 396 SHA-256 page hashes match the embedded CodeDirectory | No mismatch within the checked signed code-page ranges |
| Special slots 1, 2, 3, 5 and 7 | All five hashes match | The retained Info.plist, requirements, CodeResources, XML entitlements and DER entitlements match their CodeDirectory slots |
| Special slots 4 and 6 | Zero hashes | No content binding is claimed for these slots |
| CMS signature over the primary CodeDirectory | OpenSSL integrity verification succeeds with `-noverify` | Cryptographic signature integrity passes; certificate-chain trust, revocation and signing-time policy were not validated by this command |
| Full-bundle ordinary and strict `codesign` checks | Previously rejected: obsolete resource envelope/custom omit rules | The separate integrity checks do not turn either rejected bundle check into a pass |

The retained `CodeResources` has empty `files` and `files2` dictionaries. Both rule sets contain `^.*` with `omit=true` and weight 20; `rules2` also contains a nested-code directory pattern with weight zero. The blanket omission provides concrete evidence consistent with the rejection. Its bytes match special slot 3, so the omit-rule file agrees with the checked CodeDirectory; it is not merely an unrelated replacement resource file. Empty resource file maps do not authenticate the contents of individual omitted resources.

Apple documents the same diagnostic as [`errSecCSWeakResourceRules`](https://developer.apple.com/documentation/security/errseccsweakresourcerules). Its [code-signing technical note](https://developer.apple.com/library/archive/technotes/tn2206/) explains the move away from custom omission rules in ordinary application signing. That documentation supplies policy context; it does not establish the acceptance policy of this recovery/restore environment.

**Assessment:** a confirmed resource-envelope validation rejection with matching checked integrity layers, not a demonstrated tampering event or a fully trusted signature. Stage 4K.2 resolves exact official-image comparison, bounded signer-chain checks and the identified resource coverage; environment-specific acceptance remains open. No signature was repaired or replaced, and the service was not run. No vulnerability severity is assigned.


| Scan | Strict codesign | Independent CodeDirectory results | CMS integrity checks |
| --- | --- | --- | ---: |
| Initial source/RAMDisk set: 405 Mach-O files | 254 pass / 151 fail | 409 matching directories; one file without LC_CODE_SIGNATURE | 404 |
| Recovery/cryptex: 2,149 paths, 2,091 unique hashes | 1,394 pass / 755 fail | 2,290 matching directories; five unsigned slices; one unsupported magic | 2,200 |

CMS checks used certificate trust verification disabled; they establish integrity at that layer, not trust-chain validation. Counts represent different units—files, paths, slices, CodeDirectories and signatures—and should not be added as unique executable totals.

Failures include bound Info.plist/resource envelopes, kernel collections without ordinary code-signature commands, and a Metal-library container. Extracting a binary from its bundle did not erase its resource-binding requirements. Format-specific interpretation is required.

All 906 strict failures reconcile to official-matching content. Shared dyld cache files were hashed, but every embedded image has not been independently extracted, measured or decompiled. The 232 RAMDisk prelink records are metadata coverage, not full kernel-extension analysis or observed loaded modules.


