---
layout: default
title: "USB, launch services, remote identity, and TLS"
---

# USB, launch services, remote identity, and TLS

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

<a id="configuration-coverage-and-service-resolution"></a>
## Configuration coverage and service resolution

Stage 5A selected **79,071 plist candidates** across all seven scopes and freshly hash-checked and parsed **78,465**. The remaining **606** are access-restricted account-template paths: 303 in each BaseSystem. They are explicit collection gaps. No evidence permissions were changed.

The parsed files include 67,385 localization resources, 2,631 bundle-metadata files, 2,569 version files, 5,403 other configuration files and 477 launch-directory plists. These are structural coverage counts, not 78,465 individually analyzed behaviors or security controls. Text resources with other filenames and unnamed embedded plists remain outside this candidate selection.

Seven Intel files rejected by Python's XML parser passed Apple's `plutil` and parsed after native text-to-binary conversion. The collector now routes text plists through Apple's parser and binary plists through Python's binary parser. Original bytes remain unchanged and are hashed before parsing. A strict XML parser error on these files did not establish tampering.

Of 477 launch-directory plists, 475 declare programs. **439** program paths resolve to regular files in the same image inventory, while **36** do not. The other two are BaseSystem `com.apple.jetsamproperties.Mac.plist` policy dictionaries with memory-limit/priority records, not ordinary jobs missing a program. Image-relative symlink resolution prevents accidentally using an executable from the analysis host.

The RAMDisk contains six launch daemons **and one ReportCrash launch agent**. The agent declares `/System/Library/CoreServices/ReportCrash agent` and a crash Mach service, but that executable is absent from the examined RAMDisk, as is the program for the root crash daemon. PurpleReverseProxy is also absent. These declarations do not prove any corresponding service executed.

The 36 unresolved declarations require deployment/activation review: content from other mounts and platform-specific launch conditions may matter. No compromise or vulnerability is inferred from absence in a single image. Socket-bearing plist counts are 1 for the RAMDisk and 7 in each BaseSystem; these count configurations, not active sockets or remote reachability.


<a id="usb-multiplexing-and-network-configuration"></a>
## USB multiplexing and network configuration

`USBDeviceConfiguration.plist` defines reusable composite profiles including mux, NCM networking, restore, PTP, audio, keyboard, CarPlay and display-camera variants. `standardRestore` includes AppleUSBMux and auxiliary NCM interfaces. These are selectable configurations; the audit did not observe the selected hardware profile or a USB peer.

| PurpleReverseProxy socket | Port | Address declaration |
| --- | ---: | --- |
| SOCKS | 1081 | Explicit `127.0.0.1` |
| Control | 1082 | `IPv4v6`, **no explicit loopback node** |
| Notification | 1084 | Explicit `127.0.0.1` |

It is inaccurate to call all three declarations explicitly loopback-only. It is also unsupported to claim an exposed control service: the configured proxy executable is absent, and no running listener or traffic was captured. Authentication, actual binding and external reachability remain untested.

Both recovered BaseSystems include remoted/CoreDevice service-discovery configuration and SSH definitions with `Disabled=true`. These files do not establish enabled Remote Login, a paired device, a remote session or a tunnel.

Stage 5B reconciles the 477 launch-directory plist hash references and classifies **19 socket groups across 15 plists**:

| Kind of declaration | Groups | What is actually recorded |
| --- | ---: | --- |
| Filesystem socket | 14 | Seven per BaseSystem: FilesystemUI, diagnosticd, logd, mDNSResponder, two msrpc.srvsvc groups and systemkeychain |
| Service-name socket | 5 | Three RAMDisk proxy groups and one SSH group per BaseSystem |

These are configuration groups, not measured ports, connections or descriptors. Filesystem socket modes range from 0644 to 0777, but pathname mode alone does not establish a protocol's authentication or permitted operations. A local mDNSResponder socket also does not describe every network socket the daemon can create.

Each SSH definition specifies inetd compatibility, `Wait=false`, the `ssh` service name and Bonjour names `ssh`/`sftp-ssh`; its explicit program resolves to `sshd-keygen-wrapper`. Apple's historical [launchd manual](https://github.com/apple-oss-distributions/launchd/blob/main/man/launchd.plist.5) distinguishes a plist's `Disabled` default from the running job state, and describes Unix-path sockets and inetd handoff. Actual startup overrides and this dataset's authentication path remain unmeasured.

The proxy control declaration lacks an explicit loopback node address. It remains an activation/authentication question, not evidence of an exposed port. Apple's [startup documentation](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html) explains that launchd may register sockets before starting their consumer, so a missing executable alone also cannot prove that no socket would be registered in a deployed environment.

Of the 36 unresolved program declarations, **11 have a same-relative-path candidate in another image and 19 have a same-basename candidate**; these sets overlap. Examples include ReportCrash in the BaseSystems and platform-specific RepairAssistant/CVMCompiler counterparts. Cross-image candidates do not establish that a deployed process can load them, especially across architectures. No regular file named PurpleReverseProxy or testmanagerd was found in the seven saved scopes. Each gap remains queued rather than being silently treated as resolved.

Remoted is present in both BaseSystems and declares KeepAlive plus six Mach service names. These names do not constitute six network ports or evidence of remote access. **Finding CFG-004:** expected service-configuration mechanisms with unresolved activation, deployment and authentication; high confidence in the recorded declarations, limited confidence in runtime conclusions. No vulnerability severity is assigned.

USB controller firmware, USB composite-device profiles and host-side multiplexing are separate layers. A firmware payload's existence does not prove communication through a proxy.

<a id="service-authentication-what-the-next-trace-establishes"></a>
### Service authentication: what the next trace establishes

**Stage 5C** freshly acquired 15 selected files from each read-only BaseSystem. All 30 hashes match the initial inventories; all 16 selected Mach-O files pass current strict codesign verification with displayed Apple signing authorities. The seven selected configuration files are identical across architectures. Both images were detached. No collected service was executed and no credentials or host private keys were acquired.

**SVC-001 — Remoted local checks.** Intel remoted's `com.apple.remoted.coredevice` listener is linked through its handler blocks to an audit-token lookup for `com.apple.private.remoted.coredevice` (`0x100003c35–0x100003cef`, `0x100003d9e–0x100003dc6`). A missing entitlement object takes a cleanup/cancellation route; the present-object branch can proceed toward `add_listener_device`, `add_client_device` or `remove_device`. This check tests presence, not an explicit Boolean-true value. It does not establish unauthorized access or authenticate a remote network peer.

A separate helper (`0x10002c9b8`) requires the device-admin entitlement, then either allow-sandbox entitlement presence or a successful `forbidden-remote-device-admin` sandbox check. One traced caller uses its result as the argument to `copyClientDescriptionWithSensitiveProperties:`. This is evidence of selective disclosure, not a proven universal command gate. Service-definition policy origins, transport setup and peer authentication remain unfinished.

**SVC-002 — BaseSystem SSH has a volume-unlock role.** The dedicated BaseSystem PAM configuration names `pam_basesystem.so`; the retained module is `pam_basesystem.so.2`, with runtime module resolution still untraced. Its Intel authentication function obtains a username and password, spawns `sshd-fvunlock --no-reboot USER`, passes the password through a pipe, and checks the helper's result. Incorrect-password, temporarily-unavailable and system-error outcomes take nonzero return paths. The helper-success path requests a userspace reboot transition toward `/System/Volumes/macOS`. Stage 5D below traces the helper's keystore-result gate and APFS loop; backend verification, account throttling and complete target selection remain open.

The Swift SSH wrapper calls `os_variant_is_basesystem` and contains separate BaseSystem PAM options. Apple's [pinned SSH/FileVault documentation](https://github.com/apple-oss-distributions/OpenSSH/blob/2cc66abd7f8f1eb27d6a3074e476514194efe07e/apple_ssh_and_filevault.7) explains password-based FileVault unlocking when Remote Login is enabled, followed by a transition before ordinary login, as a macOS26 feature. This supports an expected purpose for these powerful components. It does not show that Remote Login was enabled, a volume was unlocked remotely, or a shell was opened on this Mac.

The public [wrapper source](https://github.com/apple-oss-distributions/OpenSSH/blob/2cc66abd7f8f1eb27d6a3074e476514194efe07e/sshd-keygen-wrapper/SSHDWrapper.swift) is OpenSSH354.120.2; the retained binary identifies 354.160.6. Source corroboration is therefore version-bounded, not an exact source/build match. Ordinary template SSH settings and this BaseSystem path must not be conflated.

**SVC-003 — USB mux sandbox.** In the identical `com.apple.usbmuxd.sb` files, the permissive “Training wheels ON” examples are comments. Active rules use deny-default with imports and exceptions for USB user clients, selected files/Mach services and outbound networking. The outbound permission and lockdown-directory access are capabilities, not traffic or pairing evidence. Imported policy composition and the actual consumer remain untraced; a sandbox profile or account record does not establish a running usbmuxd.

These three findings have high confidence for the listed configuration and local code paths, with no confirmed security bypass or vulnerability severity. ARM instruction-level equivalence and complete protocol authentication remain open.

<a id="filevault-helper-what-actually-gates-the-unlock-request"></a>
### FileVault helper: what actually gates the unlock request

**SVC-004 — The examined Intel helper checks the keystore result before its APFS unlock loop.** Stage 5D rechecked `usr/libexec/sshd-fvunlock` against the original inventory: SHA-256 `f3632d5a884f458c2f8446f498f4f9f004eac5a6ad8b0e5bb301359c0e76b99e`. It is one of Stage 5C's strictly verified Apple-signed binaries. Its powerful unlock-related entitlements are consistent with its role; the evidence does not show that it ran or unlocked this Mac.

The bounded direct trace establishes:

1. A false BaseSystem check branches into error construction (`0x100008671–0x100008678`). Disk-management calls resolve a disk, volume UUID and volume group, and request that group's data-volume objects. Noninteractive DiskManagement configuration is not an omitted password check.
2. A helper prepares LocalAuthentication context data and calls imported `aks_fv_verify_user_opts`. The checked return branches at `0x100007435` and `0x1000076d2` send nonzero results to error propagation. Multiple import call sites occur in Swift Data handling; counting those sites does not measure authentication attempts or retries.
3. The caller checks the Swift error register after the helper (`0x1000039af–0x1000039be`). Its no-error branch reaches the volume loop. For each selected object, code obtains a BSD device name and requests `APFSVolumeUnlockAnyUnlockRecordWithOptions` (`0x1000045fa`) with password data and options zero. Status zero or `EALREADY` continues; another result enters failure handling.

There is a subtle second stage: after successful keystore verification, an ACM policy call uses `UserAuthenticationWithPasscodeRecovery`. The reviewed callback combines status-zero with a satisfied Boolean, logs passed or failed, and returns. It does not construct an authentication error. **That callback is not the sole credential gate:** the earlier AKS result and later APFS result are separately checked. This finding does not demonstrate an incorrect-password unlock or a security bypass; backend policy effects remain untraced.

Apple's [public DiskManager implementation](https://github.com/apple-oss-distributions/OpenSSH/blob/2cc66abd7f8f1eb27d6a3074e476514194efe07e/sshd-fvunlock/DiskManager.swift) corroborates this design. Its [command implementation](https://github.com/apple-oss-distributions/OpenSSH/blob/2cc66abd7f8f1eb27d6a3074e476514194efe07e/sshd-fvunlock/FileVaultUnlock.swift) also describes input handling, the pivot path and differentiated error exits. This public `OpenSSH-354.120.2` source is **not an exact source match** for the retained `354.160.6` binary; those additional behaviors require their own instruction-level checks.

Confidence is high for the listed local gates; no vulnerability severity is assigned. Follow-up covers exact username/target/input selection, backend credential verification and throttling, error-state implications, PAM module resolution and ARM equivalence. Neither live credentials nor the host's account database were read. Static capability, enabled Remote Login, network reachability and a historical unlock remain different questions.

The helper's 12,872 linear disassembly records match source bytes, but are not all semantically reviewed. Whole-section decoding misaligns across embedded data/padding before two ACM function entries; function-start metadata and 22 separately anchored LLDB instruction checks recover those entries. LLDB was used offline without launching the helper.

<a id="remote-service-policy-declarations-overrides-and-exposure"></a>
### Remote-service policy: declarations, overrides and exposure

**SVC-005 — Policy fields have identifiable producers and consumers.** In the examined Intel `remoted`, `RSDLocalService` reads `RequireEntitlement` from its event dictionary and rejects construction when the string is absent. A separate legacy-service initializer uses the fixed policy `AppleInternal`. The local description writer serializes an ordinary entitlement, with a special case: `None-AppleInternal` becomes both `Entitlement=AppleInternal` and `EntitlementOverride=None-AppleInternal`.

The receiving `RSDRemoteService` constructor prefers a string `EntitlementOverride`; otherwise it requires a string `Entitlement`. Missing or invalid ordinary policy causes null construction. The reviewed update method only updates the port. These observations establish where policy is stored and selected; authentication and provenance of the received description remain unresolved.

The local access helper permits `None-AppleInternal` directly, and has an internal-content alternative for `AppleInternal`. Its ordinary dictionary route permits presence of a device-admin, restricted-coprocessor or service-named entitlement object. Presence is not a Boolean-true comparison. Three traced callers use the result to answer a service-existence query, filter a list or return an error instead of a service-description reply. This is bounded discovery/access-policy evidence, not proof of complete connection authorization or a remotely exploitable override. The investigation has not shown an unauthorized caller controlling a trusted service description.

**SVC-006 — “Exposed to untrusted devices” is an explicit service policy, not proof of compromise.** The retained configurations declare eight service names per BaseSystem, across seven plist files per architecture:

| Service family | Selected declared exposure controls |
| --- | --- |
| Test manager | AppleInternal entitlement policy; RemoteXPC false |
| QEMU guest agent | Untrusted exposure true; limited to virtual-machine host type; named entitlement |
| Diagnostics log relay | Untrusted exposure true; named entitlement; RemoteXPC true |
| Core capture | Named entitlement; RemoteXPC true; no explicit untrusted-exposure field |
| Storage-mounter proxy, two service names | PreSetup and internal-security-policy exposure flags; named entitlement |
| Diagnostics log transfer | Untrusted exposure true; compute-node type restriction; named entitlement |
| Cryptex remote service | PreSetup/internal-security-policy exposure; compute-node restriction; named entitlement; CryptexInstall among declared features |

The exact names, values and inventory hashes are retained in the stage evidence. None of these 16 declarations uses `None-AppleInternal`; this does not exclude other registrations or advertisements. Their presence is consistent with the examined Apple recovery environment and is not evidence that they executed, were reachable, or accepted an untrusted peer.

The Intel policy parser handles Boolean exposure and named array flags separately. Selected later exposure branches consult setup state, an AKS-owner result, OS internal-security policy and a device `isTrusted` method, following earlier device-type filters. The trust method's provenance and the transport handshake require further tracing.

One additional distinction matters: the local description writer defaults an absent `EncryptSocketData` property to false. This is a per-service description value. It does **not** establish an unencrypted outer transport, plaintext traffic or missing peer authentication. Those are separate questions requiring transport and service-consumer analysis.

Both findings have high confidence for the listed code paths and retained declarations; neither receives vulnerability severity. Stage 5E rechecks the retained binary and saved instruction bytes, and adds bounded review records for 14 configuration paths. The queue now records **32 unique paths with bounded semantic reviews** among 147,253 objects. All remaining paths remain queued; no reviewed path is thereby declared fully reverse engineered.

<a id="tls-a-required-policy-refusal-and-a-separate-authentication-callback"></a>
### TLS: a required-policy refusal and a separate authentication callback

**SVC-007 — The examined Intel RemoteXPC path distinguishes TLS negotiation from peer verification.** The base device `isTrusted` method delegates to a device-type classifier; it is not itself a certificate check. Subclass overrides and the later TLS verifier form separate analysis targets.

The traced negotiation method considers connection state, availability of a prerequisite object, peer messaging protocol version, backend TLS policy and required OID-set availability. It builds a `StartTls` message containing a Boolean decision and numeric policy. The policy parser maps disabled, optional and required to 1, 2 and 3. Policy selection varies by backend: the base and CoreDevice implementations return disabled for this mechanism, while other subclasses delegate to their own policy helpers. This does not establish whether other transport protection exists.

On the reviewed peer-message route, both sides must request TLS to set `_enable_tls`. **That flag is negotiation intent, not proof of successful authentication.** The separate `handshakeCompleted:` method checks whether either side's policy is required. If so, and `_enable_tls` is false, it takes the failure route, resets connection state, cancels an existing connection and clears it. The ordinary completion branch follows only when that check permits it.

A later setup path calls `xpc_remote_connection_set_tls` with a callback. That callback passes the returned Boolean from an authentication helper to RemoteXPC's completion block. The helper reaches certificate-chain handling and a separate evaluator supplied with the device type and required OID set. Copying a certificate chain and checking a negotiation flag are not substitutes for analyzing that evaluator.

This establishes concrete refusal and verification-delegation paths with high confidence, without assigning vulnerability severity. The next section narrows the certificate/attestation question. Full OID-policy provenance, identity provenance, backend policy inputs, RemoteXPC completion handling and service-description integrity remain unfinished. No network connection or authentication experiment was performed. The earlier `EncryptSocketData=false` service default therefore still cannot be treated as proof of plaintext traffic or absent peer authentication.

<a id="peer-attestation-trusted-roots-key-binding-and-an-expiration-exception"></a>
### Peer attestation: trusted roots, key binding and an expiration exception

**SVC-008 — Intel remoted conditionally verifies an embedded certificate chain and binds attested public-key bytes to the selected peer certificate.** The evaluator at `0x10001fec9` receives the device type, a required-OID set and a certificate selected by the preceding helper. That helper takes `lastObject` from its copied certificate chain; its exact role in every runtime chain is not assumed here.

OID `1.2.840.113635.100.6.84` carries the certificate-set data called DCRT by the executable; `.83` carries the data it calls DAK attestation. The code parses these separately. It checks the DCRT chain when required or present, trying the System attestation policy first and the User policy if the first returns an error. It enters DAK verification when that OID is required or an attestation context exists. Consequently, **this is not evidence that every possible peer must supply both extensions**. The next section identifies four required-OID producers; effective backend policy remains incomplete.

On the DAK path, the code obtains public-key bytes from the first DCRT certificate and requires success from `aks_attest_context_verify`. It then extracts field 1 from the verified context and compares those bytes with the selected peer certificate's public-key representation. A mismatch reaches the evaluator's false-result cleanup. This establishes an actual checked binding, beyond merely finding attestation-related strings. It does not independently validate the imported AKS implementation, freshness or replay handling. Device types 15 and 16 subsequently enter chassis-related checks; the next section traces their outer branches, while inner matching remains open.

The trust helper uses these embedded public certificates:

| Subject | DER SHA-256 |
| --- | --- |
| Basic Attestation System Root CA, Apple Inc. | `10d3c867f0aefb2431a0a97a8818bd64f7f90ffe1194484fca97f0f29eca0047` |
| Basic Attestation User Root CA, Apple Inc. | `03751c80fcbe5819d170d267ce1ad6d094407c91d873d7a6562de3666d3594c6` |

Both roots were extracted from the original binary; both self-signatures verify. They have 384-bit EC public keys, ECDSA-SHA384 signatures and encoded validity ending March 22, 2032. Their DER fingerprints exactly match the constants in [Apple's pinned Security source](https://github.com/apple-oss-distributions/Security/blob/db15acbe6a7f257a859ad9a3bb86097bfe0679d9/OSX/sec/Security/SecPolicy.c#L4398-L4471). That source also describes root pinning, a three-certificate chain and leaf-validity checking. This provides external corroboration, **not an exact-build verification of Security.framework**.

The examined helper sets an explicit anchor on a newly created SecTrust object; it does not install a root into the Mac's keychain or alter Secure Boot. Apple's [anchor API contract](https://github.com/apple-oss-distributions/Security/blob/db15acbe6a7f257a859ad9a3bb86097bfe0679d9/trust/headers/SecTrust.h#L291-L317) documents restriction to supplied anchors unless additional anchors are reenabled. No reenabling call appears in the reviewed helper. Offline self-signature checks used only the extracted anchors with time checks disabled; they do not establish acceptance of any peer certificate.

**SVC-009 — The DCRT helper explicitly allows certain expiration failures to continue.** After `SecTrustEvaluateWithError` fails, it calls `SecTrustIsExpiredOnly`. If that returns true, it reaches the success continuation. If false, a second branch checks whether the error has `NSOSStatusErrorDomain` and code `-67818`, which Apple defines as [errSecCertificateExpired](https://github.com/apple-oss-distributions/Security/blob/db15acbe6a7f257a859ad9a3bb86097bfe0679d9/base/SecBase.h#L627). That match also reaches success. The helper returns a null error object, which its caller treats as passing this DCRT trust stage.

These branches are not equivalent: Apple's [SecTrustIsExpiredOnly contract](https://github.com/apple-oss-distributions/Security/blob/db15acbe6a7f257a859ad9a3bb86097bfe0679d9/trust/headers/SecTrustPriv.h#L236-L250) describes expiration as the only chain problem; the separate domain/code branch does not itself inspect every failure. Whether the exact framework can report that code alongside other failures is unresolved. This warrants further policy analysis, not a claim that arbitrary certificates are accepted.

**Assessment:** high confidence in these static branches and root identities. The root/key-binding mechanisms are consistent with Apple's attestation design. The expiration exception is classified **requires investigation**, with no vulnerability severity assigned. It appears in the inventory-matched artifact; it is not evidence of local modification or observed compromise. The later attestation/key comparison remains a separate condition when required or present. No peer chain was submitted and no authentication was performed. The next section narrows chassis/OID policy; exact-build error aggregation, AKS behavior and RemoteXPC enforcement remain open.

Stage 5G rechecked 79,871 saved instruction records and retained 2,162 bounded excerpt records. Its two root self-signature checks and two external fingerprint matches add evidence, not two newly reviewed filesystem paths. Unique bounded semantic coverage remains 32 paths.

<a id="required-certificate-extensions-and-same-chassis-checks"></a>
### Required certificate extensions and same-chassis checks

**SVC-010 — The examined default and compute-class methods require both DCRT and DAK.** The verification helper obtains the device's class, calls its `tlsOidsRequiredOfPeer` class method, and passes that set to the evaluator. Original constant-array bytes and decoded fixups establish these results:

| Class | Required extensions returned by the examined method |
| --- | --- |
| RSDRemoteDevice | `.84` DCRT and `.83` DAK |
| RSDRemoteComputeControllerDevice | `.84` and `.83` |
| RSDRemoteComputeNodeDevice | `.84` and `.83`, plus `.85` chassis manifest if its policy helper returns true |
| RSDRemoteLoopbackDevice | Empty set |

All suffixes refer to `1.2.840.113635.100.6`. These are local code-selected requirements, not a peer's advertised set. They narrow the preceding conditional-check finding: both DCRT and DAK are required on the examined compute-class verification routes. They do not prove TLS is selected on every backend or that any of these classes executed on this Mac.

The chassis requirement is selected through an ordered resolver: an NSNumber preference named `compute-node-tls-chmf-required` takes precedence; otherwise an enabled `RemoteServiceDiscovery/ComputeNodeTLSRequiresChassisManifest` feature selects true; otherwise a parsed `rsd_compute_node_tls_chmf_required` boot argument selects true only for the exact string `1`. When none supplies a value, this helper defaults to false. A factory check changes the default-path log wording, not that false result. The preference object is initialized with domain `com.apple.remoted`; the following section traces its storage calls, while access controls and effective persistence remain unresolved. These are observed input names, not measured host settings or instructions to change them.

**SVC-011 — Same-chassis membership is not established on every successful evaluator route.** The device-type methods return 16 for RSDRemoteComputeControllerDevice and 15 for RSDRemoteComputeNodeDevice. Their evaluator branches check different peer roles:

| Route | Manifest available | Manifest absent or unavailable |
| --- | --- | --- |
| Type 16: controller route checking a node peer | Requests local `ChMf` with `GetCombined=true`; checks the peer as a node and itself as controller, with identity-helper results checked | If the local manifest request returns null, explicitly skips those membership checks and continues to evaluator success |
| Type 15: node route checking a controller/BMC peer | Reads `.85` from the selected certificate; passes it to AMFDR; checks the peer as controller and itself as a node | If `.85` is absent, rereads chassis-required policy: true fails, false skips membership and continues to success |

A present peer manifest that fails processing takes a failure route even when an absent manifest would be optional. Required helper results are checked rather than merely logged. Both routes also reject a missing DAK context, and the previously traced DCRT trust and DAK key-binding checks remain separate requirements on the examined compute-class paths.

This is a narrow exception to **additional chassis membership validation**, not proof that all authentication is skipped. The following section traces the numeric identity matchers; AMFDR implementation review remains open, and a returned dictionary alone is not independent proof of signature validation. The policy helper is read at separate points, so policy stability across negotiation and verification also remains unmeasured.

**Assessment:** high confidence in the OID arrays, ordinary policy precedence and outer success/failure paths. The two chassis exceptions are classified **requires investigation**, with no vulnerability severity assigned. We have not established hostile control over manifest availability or policy, unauthorized access, or historical use. Stage 5H retained 1,484 instruction records, checked eight function starts and left inner identity matching, preference protections and framework validation explicitly open. No live hardware identifiers or settings were collected; bounded semantic coverage remains 32 unique paths.

<a id="identity-matching-parser-limits-and-preference-storage"></a>
### Identity matching, parser limits and preference storage

**SVC-012 — The chassis helpers match numeric identifier pairs; their parsing checks are narrower than strict validation of the entire string.** The attested-identity extractor reads field 4 from the AKS context, requires nonempty data, decodes a string and requires exactly four hyphen-separated components. It scans the first two components as hexadecimal 64-bit values, checks both scan results and returns those numbers. Its reviewed success path does not inspect the other two components or explicitly require each scan to consume its entire field.

The manifest parser instead requires exactly two components and checks both hexadecimal scans. Node membership searches string keys with prefix `N`, suffix `1` and length four; it requires a data value, decodes that value and compares both parsed numbers with the supplied identity. Unsupported or unparseable entries are skipped during that search; success requires one matching entry. Controller membership reads the `BM02` data entry and likewise requires both numeric values to match. These are concrete comparisons, not conclusions drawn from log messages.

A separate local-identity helper rejects missing objects from two MobileGestalt queries, then calls `CFNumberGetValue` twice. The reviewed path does not check either conversion's Boolean result before returning success. Provider type/value guarantees and behavior under unexpected values remain unverified. The code's references to chip identifiers are not evidence that any real identifier was collected or transmitted during this audit.

An authored **synthetic host-Foundation probe**, using no collected service code, demonstrated why scan success and complete consumption differ: `1234junk` produced the value 4660 while leaving `junk` unread. Leading spaces and `0x` were accepted in other cases; seventeen `F` characters produced UInt64 maximum on that host. Empty and nonhexadecimal examples failed. Apple's [Scanner exhaustion documentation](https://developer.apple.com/documentation/foundation/scanner/isatend) describes the separate end-of-input condition. The probe ran on **26.7 / 25G229**, not the audited **26.6.2 / 25G83** framework build, so these observations are not a target-acceptance demonstration.

**Assessment:** the numeric comparisons and checked scan results are established with high confidence. Parser strictness and unchecked local conversion results are classified **requires investigation**, with no vulnerability severity. No forged identity, certificate or manifest was submitted. Earlier attestation and manifest-processing boundaries still matter; this does not prove arbitrary identities can authenticate or that unused fields lack validation elsewhere.

**SVC-013 — RSDPreferences delegates reads and writes to CFPreferences.** Its getter and setter pass the stored domain with `kCFPreferencesCurrentUser` and `kCFPreferencesCurrentHost`. The earlier initialization supplies `com.apple.remoted`. Apple's [CFPreferencesCopyValue contract](https://developer.apple.com/documentation/corefoundation/cfpreferencescopyvalue(_:_:_:_:)) describes an exact-domain lookup. These calls do not establish a backing-file path, permissions, runtime user, or which callers can change the settings.

The reviewed migration method reads `remoted-prefs-version`, treats absence as integer 0, and writes integer 1 plus a synchronization request when the value differs from 1. It does not perform a broader migration or call the separately implemented erase-all method. The synchronization result is not checked in its wrapper, so a requested write must not be reported as confirmed persistence.

Six direct setter-selector references cover device-name mapping, a device UUID, the version marker, compute-platform TLS requirement, and Bonjour interface selection. Their presence does not prove remote write access. The scan does not establish that these are every possible writer or that the chassis-policy key is immutable. Caller authorization, OS preference-service enforcement and effective settings remain open.

Stage 5I retained 1,896 instruction records, checked 13 function starts and ran seven synthetic scanner cases. It adds bounded evidence for the existing remoted path; unique semantic-review coverage remains 32 paths. No real preferences or hardware identifiers were read, and the collected service was never executed.

<a id="backend-tls-defaults-and-policy-mutation"></a>
### Backend TLS defaults and policy mutation

**SVC-014 / SVC-015:** the Intel remoted paths reviewed in Stage 5J do not share one universal required-TLS policy. Their common resolver checks a recognized string preference first, then an enabled feature flag, then a recognized boot-argument string. Supported strings are `disabled` (1), `optional` (2) and `required` (3). Missing, wrong-class or unrecognized preferences continue to the later sources. An enabled feature selects required; an unset result lets the backend supply its default.

| Backend | Default when the shared resolver supplies no policy |
| --- | --- |
| NCM | Disabled at this remoted TLS layer |
| Compute | A first cached MobileGestalt Boolean selects disabled; a second selects optional. Otherwise five embedded hardware identifiers select optional, and an absent/unmatched model selects disabled |
| Loopback | Required when `os_variant_is_darwinos("com.apple.remoted")` returns true; disabled otherwise |

Compute's constant dictionary at `0x1000658c0` maps `j126bap`, `j126cap`, `j226bap`, `j226cap` and `j226pap` to 2. Its model producer requires an NSString and lowercases it before lookup. The two earlier Boolean helpers require NSNumber values. Their log suffixes mention hactivated devices and factory operation; **those strings do not show that this Mac was hactivated, in factory mode or compromised**. No MobileGestalt values, live boot arguments or preferences were collected.

This precedence allows an explicit preference to select a less restrictive policy before a feature default, so write authority matters. The located compute setter has a concrete local caller: Mach service `com.apple.remoted.compute-platform` processes `require_tls` after obtaining the connection's audit token and looking up `com.apple.private.RemoteServiceDiscovery.compute-platform`. A null entitlement object leads to cancellation. The reviewed branch tests **object presence**, without an explicit Boolean-truth/type check. Whether false or differently typed entitlement values can be supplied by an authorized executable remains unresolved; this does not demonstrate entitlement forgery or an unprivileged caller.

The command itself requires an XPC Boolean named `is_tls_required`. False maps to **optional**, true to **required**; this route cannot request disabled. It writes the corresponding string to `compute-platform-tls-requirement` through RSDPreferences. The bounded setter contains no synchronization call, and its `OK` reply is not proof of persistence or a completed TLS session. A separate query reports whether the getter currently returns required.

Evidence anchors: shared resolver `0x10001ce4b`, compute/NCM/loopback getters `0x1000323c5` / `0x100037805` / `0x100039d24`, entitlement lookup `0x10001bd71`, command helper `0x10001c638`, setter `0x100032359`. Static confidence is high within these boundaries. No vulnerability severity is assigned: effective settings, other preference writers, entitlement issuance, ARM behavior and full transport enforcement remain open. **Disabled or optional policy in code is not evidence of active plaintext traffic or absence of protections in another layer.**

<a id="identity-initialization-is-separate-from-identity-generation"></a>
### Identity initialization is separate from identity generation

**SVC-016:** TLS negotiation obtains its prerequisite object from global `0x10006e0b0`. The examined replacement helper retains a new object, swaps the slot, releases the old object and calls a continuation still awaiting review. The saved listing has one direct RIP-relative store to that slot; indirect writes and other modules are outside that scan.

Initialization creates a queue named `com.apple.remoted.identity`. When the DarwinOS variant query is false, it schedules a block that reaches **SecItemDelete**, with a query restricted to identity-class items labeled `com.apple.remoted.identity`, access group `com.apple.remoted`, and the system-keychain-always option. Apple documents [SecItemDelete](https://developer.apple.com/documentation/security/secitemdelete(_:)) as deleting items matching the supplied query. The observed call establishes a capability and intended scope, not historical deletion or access to unrelated credentials. The private option's exact framework behavior remains unverified.

Startup's queued work is therefore not proof that a usable TLS identity has been generated. Separate wrappers clear the in-memory slot, generate and replace an identity, or replace it from an asynchronous block. A reviewed administrative generation caller also obtains an audit token and checks the presence of `com.apple.private.RemoteServiceDiscovery.device-admin` before calling the generation wrapper. Its outer command routing remains partial.

The generator contains key creation, DCRT retrieval, DAK attestation, chassis-data retrieval, self-signed certificate construction, identity creation and keychain-add calls. Stage 5K below traces their ordinary argument/result paths; exact framework behavior and complete caller enforcement remain open. No keychain API was invoked by this audit and no private key or live identity was collected.

Stage 5J retained 1,585 instruction records, checked 30 function starts and decoded five hardware-policy entries. It adds depth to the existing remoted review; unique bounded semantic coverage remains **32 paths**, not 32 complete binary audits.

<a id="identity-generation-optional-attestations-and-reload-limits"></a>
### Identity generation, optional attestations and reload limits

**SVC-017:** generator `0x10001d35c` first calls the scoped identity-deletion helper, then tests `os_variant_is_darwinos("com.apple.remoted")`. True enters generation; false returns null through the unsupported path. The predicate's actual value and any historical execution remain unknown. The caller does not receive a deletion-success Boolean, and the reviewed flow is not a proven transactional replacement with rollback.

The creation request specifies **256-bit ECSECPrimeRandom**, AppleKeyStore token, `IsPermanent=false`, a returned access-control object and system-keychain-always true. The access-control call requests `AccessibleAlwaysThisDeviceOnlyPrivate` and flags `0x40000000`. Apple's pinned [SecAccessControl header](https://github.com/apple-oss-distributions/Security/blob/db15acbe6a7f257a859ad9a3bb86097bfe0679d9/keychain/headers/SecAccessControl.h#L86-L104) identifies that flag as PrivateKeyUsage; the bitmask does not contain user-presence, biometry or passcode constraints. This alone does not establish unrestricted access: framework entitlements, access groups and provider controls still matter.

**AppleKeyStore does not, by its name alone, prove hardware-backed storage.** Apple's [private item header](https://github.com/apple-oss-distributions/Security/blob/db15acbe6a7f257a859ad9a3bb86097bfe0679d9/keychain/headers/SecItemPriv.h#L521-L533) describes a Secure Enclave implementation on supported devices and kernel emulation otherwise. The source is pinned public API context, not a proven exact match for the collected framework or a measurement of this Mac.

Nonpermanent key creation is followed by a separate **identity storage request**: SecItemAdd receives the generated identity, label `com.apple.remoted.identity`, access group `com.apple.remoted`, identity class, the same accessible protection and system-keychain selection. Its return must be zero before the code wraps and returns the identity. Thus `IsPermanent=false` in the earlier dictionary must not be reported as proof that this flow never stores an identity. ACL, key, certificate, identity, storage or wrapper failures lead to a null generator result on the reviewed ordinary paths.

**SVC-018:** attestation material is conditional during certificate construction:

| Producer result | Observed next step |
| --- | --- |
| DCRT data present | Insert `.84`, then attempt DAK attestation of the new key |
| DCRT data absent | Skip `.84` and the DAK request; continue to chassis acquisition |
| DAK key or attestation unavailable | Omit `.83`; continue |
| Chassis data unavailable | Omit `.85`; continue to certificate construction |

These suffixes belong to `1.2.840.113635.100.6`. The DAK request uses system-key type 7, identified as DAKCommitted by Apple's [SecKeyPriv header](https://github.com/apple-oss-distributions/Security/blob/db15acbe6a7f257a859ad9a3bb86097bfe0679d9/keychain/headers/SecKeyPriv.h#L891-L953). The generator supplies a self-signed certificate subject with common name `remoted-identity`, country `US` and organization `Apple Inc`. Subject text does not establish Apple CA issuance. The receiver's DCRT/DAK/chassis checks provide separate trust decisions.

The certificate parameters contain the encoded extension dictionary, without explicit lifetime, serial-number or digest overrides. Apple's [certificate-request header](https://github.com/apple-oss-distributions/Security/blob/db15acbe6a7f257a859ad9a3bb86097bfe0679d9/trust/headers/SecCertificateRequest.h#L76-L97) documents defaults; this audit has not generated a certificate or measured the exact framework's output. Generator success without an extension also does not establish successful authentication: the previously examined peer-class methods separately require particular extensions.

**SVC-019, requires investigation:** the asynchronous reload path retrieves an existing stored identity and checks requested extension names against a presence list. It examines `.83`, `.84` and `.85`; a nonnull extension value adds its name to the list. This collector does not validate the extension's contents, signature or freshness. Missing identity, load/wrap failure or a missing requested name triggers regeneration.

The examined flow does **not repeat that requested-OID comparison after regeneration** before queuing replacement. The replacement may receive null; its completion block runs when supplied. Completion therefore does not independently prove a usable identity satisfying the requested set. Stage 5L below traces the six direct callers and their differing completion behavior.

The replacement helper's continuation also has a narrower role than a connection notification: it updates `EncryptedRemoteXPCPopulatedOIDs` in a global dictionary when an identity exists. With a null identity it returns without clearing the key. This helper can therefore leave prior metadata unchanged, but other writers, publication timing and peer impact remain unresolved. The separate negotiation path still checks identity presence; no stale advertisement on the wire or authentication bypass has been demonstrated.

Stage 5K retains 1,795 instruction records, checks 13 function starts and decodes the key-size/OID constants. These are bounded static findings with no vulnerability severity assigned. No real identity, keychain data, private key or peer session was acquired or created.

<a id="identity-replies-completion-differences-and-oid-publication"></a>
### Identity replies, completion differences and OID publication

**Stage 5L adds SVC-020–SVC-022.** These findings concern the retained Intel BaseSystem remoted binary, not observed activity on the current Mac. All six direct asynchronous identity callers were reconciled; indirect callers and exact framework enforcement remain incomplete.

**SVC-020, requires investigation:** the `com.apple.remoted` local Mach service handles `get_local_device_identity`. The inspected listener, command dispatch and getter route contain no command-specific entitlement or UID check. The device-admin gate described earlier protects a different creation command; it cannot be assumed to protect this getter. System Mach lookup restrictions, client sandbox policy and actual client reachability remain unverified.

The getter can trigger the asynchronous reload/generation path with no requested extension set. It is therefore not necessarily a side-effect-free query: that worker can attempt replacement through the previously traced generator. Its completion starts with an error reply, requires a current identity, checks successful key-reference/certificate retrieval, and requires token attributes and certificate data before attaching an `identity` dictionary and setting `result=OK`.

| Reply field | Observed source | What is established |
| --- | --- | --- |
| `identity_key` | Bytes of the private key reference's `kSecAttrTokenOID` attribute | A token-specific blob is serialized; plaintext private-key export is not established |
| `identity_cert` | SecCertificateCopyData | Certificate bytes are serialized after checked prerequisites |

Apple's pinned [token attribute declaration](https://github.com/apple-oss-distributions/Security/blob/db15acbe6a7f257a859ad9a3bb86097bfe0679d9/keychain/headers/SecItemPriv.h#L344-L347) describes an encoded libaks key blob for AppleKeyStore/SecureEnclave tokens. The audit has not established the exact blob protections, import permissions, caller binding or whether an unauthorized recipient could use it. This merits investigation; it is not a demonstrated plaintext key leak, nor evidence that the returned blob is harmless. The examined send is a **local XPC reply**, not proof of network exfiltration. No actual identity, key blob or certificate was requested or collected.

**SVC-021, requires investigation:** completion after reload/generation does not have a universal success check.

| Caller family | Static completion behavior |
| --- | --- |
| Compute initialization/callbacks | Request `.84/.83` (controller helper conditionally adds `.85`); several calls supply no completion |
| Compute node needsConnect | Wraps a pending connection or descriptor and calls connect:, or waits; no immediate identity-success check in this block |
| Compute controller NW route | A helper selects a TLS configure block when identity exists, but the imported TLS-disable configuration when identity is null; the selected block reaches nw_parameters_create_secure_tcp |
| Local identity getter | Returns error unless identity and serialization prerequisites succeed |
| Loopback | With tlsEnabled=true, a null identity reaches an explicit crash; otherwise a nonnull identity is supplied for TLS setup. With tlsEnabled=false, this block activates without that TLS call |

The compute branch is a concrete layer-specific TLS-disable selection, **not proof that a later plaintext session is accepted**. RemoteXPC parameter setup, connection flags, later negotiation, required-policy refusal and framework enforcement remain relevant. No connection, forced error or crash was induced. Neither a requested local OID set nor an advertised extension name proves peer authentication.

**SVC-022, bounded:** the OID properties dictionary now has a traced outgoing path: refresh `EncryptedRemoteXPCPopulatedOIDs` → attach global dictionary as handshake `Properties` → xpc_remote_connection_send_message. The peer parser reads the key as an array and retains string elements in a set; a missing array gives an empty set. This parses advertised metadata, separately from certificate/attestation verification.

Stage 5K showed that one null-identity refresh route leaves prior metadata untouched. Stage 5L proves that the dictionary can reach handshake serialization, but does not establish stale data on the wire: other mutations, ordering and reconnect behavior remain unresolved. No authentication bypass or historical misuse is demonstrated. The pass retains 2,584 instruction records, checks 27 function starts and decodes two constant arrays and three block pointers. Unique bounded semantic coverage remains 32 artifact paths; the whole audit is unfinished.

<a id="later-tls-checks-and-a-separate-certificate-query-api"></a>
### Later TLS checks and a separate certificate-query API

Stage 5M narrows the previous transport finding. In base connect:, `_enable_tls=true` requires a nonnull identity; missing identity reaches an explicit crash. When present, the identity is supplied to RemoteXPC TLS setup. The `tlsEnabled` property is assigned from configuration state **before activation**, so that property assignment alone is not proof of completed cryptographic authentication. The previously traced required-policy refusal still applies. These checks do not yet resolve every framework effect or connection transition around the compute TLS-disable configuration branch.

Loopback's verification block also delegates to the examined type/OID-aware verifier and passes its Boolean result to the completion. It does not return unconditional success. No connection, policy change or failure injection was performed.

**SVC-023, bounded:** a separate per-device command, `authenticate_device`, takes `identity_cert` data, requires successful certificate parsing, and calls the existing evaluator with the device type and class-required OIDs. It returns OK only when that evaluator returns true; missing data, parse failure and a false result return ERROR. The earlier attestation, expiry and chassis findings still apply to that evaluator.

This certificate query does not consume the exported `identity_key` blob. Its reviewed success path returns a result; it does not itself demonstrate private-key possession, establish TLS or mark a device authenticated. Endpoint distribution, caller authorization and consumers of the result remain incomplete. A certificate-validation reply must not be mistaken for proof of a live authenticated peer.

A fresh read-only census hash-checked **1,023 executable/cache-data files** for the identity command, fields and selected transport symbols. This includes cache atlas/symbol records and is a different selection from the earlier 1,020-file scan. The command and key-field literals were mapped into **RemoteServiceDiscovery.framework**, using the hash-matched cache map, mapping records and embedded Mach-O identity. Apple's pinned [dyld format definitions](https://github.com/apple-oss-distributions/dyld/blob/fd8d0c4d52320ebf64db34f3cb280310d905c5ae/include/mach-o/dyld_cache_format.h#L33-L40) provide structural context for that mapping.

Stage 5M retained 104,538 bytes of relevant cache regions/tables and detached the image. That acquisition established framework attribution; Stage 5N below traces the consumer instructions. No live blob was collected. Raw Apple cache excerpts remain private. The path ledger retains 32 unique bounded reviews, with embedded framework review tracked separately; acquisition and string searching alone do not count as reverse engineering.

<a id="how-the-framework-reconstructs-the-local-identity"></a>
### How the framework reconstructs the local identity

**SVC-024 — bounded client reconstruction; authorization implications require investigation.** Stage 5N follows the exact Intel BaseSystem cache's `_local_device_copy_identity`, rather than inferring behavior from symbol names. Its connection initializer selects `com.apple.remoted` with flag 2, identified by the SDK as [XPC_CONNECTION_MACH_SERVICE_PRIVILEGED](https://developer.apple.com/documentation/xpc/xpc_connection_mach_service_privileged). This selects privileged bootstrap lookup. It does not mean every connecting client must be root or prove that the service authorizes the getter.

The client sends `cmd=get_local_device_identity` synchronously, rejects an XPC error reply, and reads the nested `identity` dictionary. A nonnull `result` string must exactly equal `OK`; a null string result proceeds to nested parsing. The certificate and token fields must still be present and successfully reconstructed. This result-field tolerance is not evidence that an attacker can substitute a reply or bypass authentication.

The `identity_cert` bytes are copied into NSData and parsed with `SecCertificateCreateWithData`. The `identity_key` bytes are copied into a second NSData object. The crucial distinction is where the second object goes:

| Argument or attribute | Observed client value |
| --- | --- |
| SecKeyCreateWithData data argument | Empty NSData object |
| kSecAttrTokenOID | Data copied from the `identity_key` field |
| kSecAttrTokenID | AppleKeyStore |
| kSecAttrAccessControl | Newly created access-control object: AccessibleAlwaysThisDeviceOnlyPrivate, PrivateKeyUsage flag `0x40000000` |
| kSecAttrIsPermanent | false |
| kSecUseSystemKeychainAlways | true |

The client therefore requests a **token-backed key reference**. It does not pass the returned blob as ordinary plaintext private-key material. The [Apple token-OID contract](https://github.com/apple-oss-distributions/Security/blob/db15acbe6a7f257a859ad9a3bb86097bfe0679d9/keychain/headers/SecItemPriv.h#L344-L347) supports interpreting this attribute as provider-specific encoded key data. It does not settle the blob's wrapping, caller binding, import restrictions or ability to sign. The requested attributes do not themselves confer authorization, prove Secure Enclave backing or establish that the blob is harmless to disclose.

Null key creation follows a failure return. A successful key reference and the parsed certificate go to `SecIdentityCreate`; the identity must also be nonnull. A separate exported wrapper, `_remote_device_copy_xpc_remote_connection_tls_identity`, calls this helper and passes its result to `sec_identity_create`. That is a concrete route toward a TLS identity object, not proof of an accepted TLS session or private-key possession by an unauthorized client. No live request, import or signing operation was performed.

This consumer path explains why the server serializes the two fields, narrowing SVC-020's uncertainty. What remains unresolved is consequential: **who can reach the getter, which processes can import/use the token, and how later transport authentication constrains its use?** The report neither calls this a demonstrated private-key leak nor dismisses it as automatically safe. No vulnerability severity is assigned.

For reproducibility, all 132 framework exports agree with original nlist symbols; 18,279 LLVM instruction records account for the original 66,194 code bytes without gaps or mismatches. Thirty-three cache pointers were checked against slide chains and defining exports/selectors, including independent corroboration of 13 import stubs. Eight selected function ranges contain 685 retained instruction records. These are bounded checks, not complete framework semantics or independent instruction decoding. The generated analysis object and raw cache pages remain private, and this adds one embedded component review without treating the entire shared cache as reviewed.

<a id="what-securityframework-does-with-the-token-blob"></a>
### What Security.framework does with the token blob

Stage 5O follows the exact-cache `SecKeyCreateWithData` implementation, extending **SVC-024**. A nonnull `kSecAttrTokenID` selects `SecKeyCreateCTKKey`, which initializes a `SecCTKKey` object. A failed token construction returns failure; it does not fall back to parsing the blob as an ordinary raw key.

For the five attributes supplied by RemoteServiceDiscovery, the initializer constructs a CryptoTokenKit session using the AppleKeyStore token ID. The system-keychain helper checks that `u_SystemKeychainAlways` is an NSNumber with true boolValue; the caller then requests a force-system-session parameter. This is a request to the provider, not evidence that an entitlement or access check has been bypassed. The client supplies no explicit authentication context, credential reference or existing token session, so the examined ordinary session construction receives a null LAContext.

The supplied `kSecAttrTokenOID` selects **objectForObjectID:error:** on that session. The separate no-OID branch creates an object with attributes. Supplied ACL metadata is subsequently incorporated into the local key wrapper; the audit has not established that this overwrites the provider's access restrictions. Provider lookup, wrapper creation and successful signing are distinct milestones.

| Exact-cache evidence | Meaning and limit |
| --- | --- |
| `SecKeyCreateWithData`, token dispatch at `0x7ff8039a4958` | Routes token attributes into CryptoTokenKit; no ordinary raw-key fallback after token failure |
| `SecCTKKey` session initialization at `0x7ff803999bd6` | Passes token, context, parameters and an error output; inner provider authorization remains unreviewed |
| `objectForObjectID:error:` at `0x7ff803999c7d` | Consumes the returned identity blob as token-specific object data |
| Token-object check at `0x7ff803999e18` | Normally rejects an absent object, with the registered-token exception below |

There is a specific deferred-object exception. The initializer checks TKErrorDomain and `TKTokenNotFoundAndRegistered`, resolved by name through dlsym. The matching symbol in the exact CryptoTokenKit cache contains **-1002**. A matching error sets an instance flag that permits the wrapper to continue without a token object. Its retry methods are traced in Stage 5R below. This does not establish that AppleKeyStore can trigger the exception or that such a wrapper can sign. A nonnull wrapper therefore must not be equated with successful private-key use.

This is a bounded, high-confidence implementation finding; its security implications still **require investigation**, with no vulnerability severity assigned. The next boundary is session/provider operation authorization and external endpoint access. No real token, keychain entry, import or signing operation was requested.

<a id="certificate-query-replies-and-their-tls-consumer"></a>
### Certificate-query replies and their TLS consumer

**SVC-025 — null result-string acceptance requires investigation.** The exact RemoteServiceDiscovery client supplies SVC-023's certificate query to a TLS verification adapter. That makes the reply contract security-relevant, while leaving actual transport acceptance unresolved.

`remote_device_authenticate` obtains a certificate chain from the supplied sec_trust object and selects its `lastObject`, copies that certificate's bytes, and sends `cmd=authenticate_device` with `identity_cert` through the device's XPC connection and queue. The audit does not assume lastObject is always a leaf certificate. This per-device endpoint is distinct from the global identity getter's connection.

The reply callback at `0x7ff814639d26` implements:

| Reply condition | Completion result |
| --- | --- |
| XPC error object | false |
| Result string exactly `OK` | true |
| Other nonnull result string | false |
| `xpc_dictionary_get_string` returns null | **true** |

The null-string branch is explicit at `0x7ff814639d77`; it reaches Boolean true at `0x7ff814639e21` and the completion call at `0x7ff814639e26`. This callback does not perform another certificate/key reconstruction check after selecting that result.

A separate exported TLS-verifier wrapper returns no block when its tls_enabled helper is false. On the true route it creates a block whose invoke at `0x7ff81463e98c` forwards the captured device and callback inputs to `remote_device_authenticate`. The service-level wrapper delegates through its device. This establishes that the query result supplies this TLS verification completion, rather than merely appearing in an unrelated diagnostic API.

**What this proves:** the client accepts a null result-string return, and a TLS verification adapter consumes its verdict. **What remains unknown:** whether any reachable trusted reply can omit that result, who can obtain/control the endpoint, exact malformed-object/API behavior, and how the transport combines this verdict with key-possession and other checks. The examined daemon producer returns OK or ERROR after the evaluator. No reply forgery, bypass, unauthorized peer or completed handshake has been demonstrated. Confidence is high for the static branch and adapter; severity is unassigned pending impact evidence.

The query function also invokes failure completion for a null chain or null lastObject, then locally falls through toward further certificate processing. Exact Security API null handling and input guarantees are still unreviewed. The report records this for follow-up without claiming a demonstrated crash or repeated callback.

Stage 5O retains 4,647,368 bytes of Security regions/tables and 609,488 bytes of CryptoTokenKit regions/tables, excluding separate symbols/headers. Seven selected Security functions account for 2,036 checked instructions; five receive bounded semantic tracing, while two retry methods were prepared there and are traced in Stage 5R below. Two embedded jump tables are correctly treated as data, with all 14 destinations checked against instruction boundaries. Eighty-six pointer chains, 39 CFStrings and three plain literals are rechecked from saved bytes; six selected RSD functions contain 363 instructions. These checks add Security as a second bounded embedded-component review, keeping the inventory-path count at 32. Acquisition alone does not mark CryptoTokenKit or the parent cache reviewed. Raw Apple bytes remain private.

<a id="concrete-provider-selection-and-the-local-entitlement-check"></a>
### Concrete provider selection and the local entitlement check

**SVC-026 — bounded provider-routing finding; operation authorization remains unresolved.** Stage 5P follows the exact CryptoTokenKit classes selected by the token attributes. It identifies a real current-process entitlement check, while distinguishing that check from the permissions needed to use a particular key.

The exact constant values are `com.apple.setoken` for SecureEnclave and `com.apple.setoken:aks` for AppleKeyStore. The token classifier compares the first colon-separated component with the SecureEnclave identifier, selecting **TKSEPClientToken** for this AppleKeyStore request. The session initializer then selects **TKSEPClientTokenSession** for that token class. The alternative is an extension-token implementation. These conclusions use original class symbols, selector references, constant bytes and conditional branches, rather than matching names in strings.

The SEP session also checks membership in its built-in token list. The list includes AppleKeyStore on both branches of the `hasSEP` test; SecureEnclave is additionally included on the true branch. The `hasSEP` implementation and actual hardware state have not been measured. Consequently, a `SEP` class name remains insufficient evidence of hardware-resident private keys.

Object lookup decodes the supplied token object identifier, rejects a null result or a certificate-marked identifier on the examined key route, and constructs a TKSEPKey. Unsupported object types are rejected after the initializer's data/property-list conversion checks. The parser internals and every possible input remain outside this pass; decoding is not proof of authenticity or permission.

TKSEPKey then makes a separate locality decision:

| Condition in the examined code | Selection |
| --- | --- |
| An explicit `ctkdConnection` is present | `canUseSEPLocally` returns false |
| Otherwise, current-process `com.apple.keystore.access-keychain-keys` is an NSNumber with nonzero integerValue | Enables the cached local-route flag |
| Entitlement missing, wrong class or zero | Does not enable that flag in the examined initialization block |
| Locality result true | Constructs TKLocalSEPKey |
| Locality result false | Constructs TKRemoteSEPKey |

The decisive lookup is `SecTaskCopyValueForEntitlement` at `0x7ff813c69003`; the class/nonzero checks precede the flag store at `0x7ff813c6909f`. This query concerns the process executing the framework, consistent with Apple’s [SecTaskCreateFromSelf contract](https://developer.apple.com/documentation/security/sectaskcreatefromself%28_%3A%29). Apple documents [entitlement lookup](https://developer.apple.com/documentation/security/sectaskcopyvalueforentitlement%28_%3A_%3A_%3A%29) as returning the represented task’s value; these API descriptions do not establish the runtime value here. The `forceSystemSession` parameter is forwarded separately and does not itself bypass this locality decision.

A subsequent `com.apple.keystore.sik.access` check also tests class and nonzero value. Its failure produces a diagnostic but does not clear the previously enabled local-route flag in the reviewed block. That is a bounded observation about this routing helper, not proof that operations requiring the SIK entitlement are allowed elsewhere.

The retained, previously signature-checked Intel remoted declares both entitlement names as Boolean true. This does not establish the entitlement state of every client, effective runtime values or successful key use. A process does not inherit the daemon's entitlements merely by calling a framework. The `Remote` class name also does not establish communication over an external network; Stage 5Q below identifies its NSXPC transport, while server authorization remains open.

Finally, the SEP token-object wrapper requires `publicKeyWithError:` to return a nonnull result before ordinary initialization continues. A returned public key or token wrapper still does not prove permission to sign. **No unauthorized import, key disclosure, signing, peer impersonation or completed TLS session has been demonstrated.** Confidence is high for these static dispatch/gate branches; no vulnerability severity is assigned.

The pass checks **24 selected functions containing 1,376 instructions, 91 pointer chains and 12 CFStrings**. These are decoding and attribution counts, not complete semantic review of every selected instruction. CryptoTokenKit becomes the third bounded embedded-component review; the inventory-path count stays 32. Stage 5Q below follows the concrete local/remote implementations; deferred-object retries continue in Stage 5R. All raw cache material remains private.

<a id="concrete-key-import-signing-and-the-ctkd-connection"></a>
### Concrete key import, signing and the CTKD connection

**SVC-027 — bounded key-operation finding; full provider authorization remains open.** Stage 5Q follows the local and remote key implementations selected in Stage 5P. It establishes several checks between receiving an object identifier and producing a usable key or signature. It does not demonstrate unauthorized signing, private-key disclosure or peer impersonation.

The local implementation first tries a system-key identifier. It tries the reference-key blob constructor only if the system-key constructor returns null **and explicitly marks the identifier unknown**. A recognized system key denied by its entitlement check does not take that fallback. The dispatch tests are at `0x7ff813c7a602–0x7ff813c7a60b`; the unknown-ID flag is written at `0x7ff813c7da18`.

Recognized system-key requests call `callerHasEntitlement:error:` with `com.apple.security.attestation.access`, or `com.apple.private.playgrounds-local-signing-allowed` for internal key type7. This helper requires an NSNumber-compatible value whose `boolValue` is true. It then remains necessary to obtain an authentication context and pass `hasSystemKey:ACMHandle:`. The key-type numbers are internal identifiers, not a complete documented algorithm or hardware catalog.

The entitlement belongs to a specific caller. When the stored caller is nonnull, the helper delegates to that object's `valueForEntitlement:`. When it is null, the helper creates a task object for its own process and reads that task's entitlement. Stage 5P's in-process local route supplies null. This distinction is directly traced; the identity and trust of a server-supplied caller remain open. Apple's [SecTaskCreateFromSelf documentation](https://developer.apple.com/documentation/security/sectaskcreatefromself%28_%3A%29) confirms the current-task API meaning.

Reference-key construction and signing have separate checks:

| Step | Observed behavior | What it does not establish |
| --- | --- | --- |
| Import the blob | Calls `aks_ref_key_create_with_blob` and requires status0 (`0x7ff813c7ada9`) | Permission to perform every operation on the imported reference |
| Reconstruct protection | Derives protection from AKS key class, checks SetProtection's result and copies nonnull external ACL constraints | Replacement or weakening of the backend ACL |
| Check key type | Rejects types outside values0–16 or absent from mask0x1e7fa | Hardware support for every accepted numeric type |
| Select keybag argument | Force-system-session or runsInSystemSession true returns handle-6; otherwise-3 | Actual keybag state, privilege elevation or an AKS bypass |
| Sign a digest | Requires an authentication context; passes ACM-derived parameters and digest to `aks_ref_key_sign` (`0x7ff813c7be27`) | Successful signing merely because the object exists |
| Handle signing result | Nonzero AKS status returns null with an error; status0 proceeds through result conversion | Independent verification of the kernel/SEP backend's checks |

The remote implementation uses **NSXPC IPC**. Its connection resource can use an explicit or instance connection, otherwise creating TKCTKDConnection. The connection method uses an existing/provided listener endpoint, or falls back to the exact Mach service **`com.apple.ctkd.token-client`**. Thus the word “remote” in this class name does not establish an external network connection. The service's reachability, endpoint provenance and server caller checks remain separate questions.

The client obtains a synchronous proxy and requests `getAttributesOfKey:authContext:forceSystemSession:reply:`. Apple's [synchronous proxy contract](https://developer.apple.com/documentation/foundation/nsxpcconnection/synchronousremoteobjectproxywitherrorhandler%28_%3A%29?changes=_6_2) says the reply/error handlers run on the calling thread before the proxy message returns. This supports the observed immediate reading of reply slots; that pattern alone is not a demonstrated race.

Remote initialization requires a nonnull reply and a successful attribute processor. That processor requires **keyType, keySize, systemKey and systemSessionKey** to be present, and requires `SecAccessControlCreateFromData` to produce a nonnull access-control object. These are presence/decoding checks, not comprehensive type/range validation. It stores publicKey without a nonnull requirement in that method; the later token wrapper's separate public-key prerequisite was traced in Stage 5P. Returning attributes still does not prove permission to sign.

The base session's `isValidWithError:` method also turns out to return constant true. Its name is not an extra authorization guarantee. The explicit connection setter replaces a stored global; its callers and effective runtime state remain untraced.

**Coverage:** 30 selected functions contain **2,538 byte-checked instructions**, with **93 pointer-chain checks and 15 CFStrings**. These are decoding and attribution counts, not a complete review of every callee or exceptional path. The existing CryptoTokenKit review is extended; totals remain **32 bounded inventory-path reviews and three embedded-component reviews**. No real token, keychain item or identity was requested, imported or used.

Stage 5R below traces Security's deferred-object retry and authentication parameters. Server caller provenance, remote signing, reconnect behavior and deeper CTKD/AKS authorization continue in Stage 5S. The null-result-string TLS finding also remains unresolved at the adverse-reply producer and accepted-transport boundaries. No vulnerability severity is assigned to these expected powerful capabilities.

<a id="deferred-key-objects-retry-and-authentication-parameters"></a>
### Deferred key objects, retry and authentication parameters

**SVC-028 — bounded retry and parameter-flow finding.** Stage 5R follows the deferred-object exception identified in Stage 5O. A wrapper can exist before its token object is available, but the examined operation helper still requires object lookup to succeed.

`ensureTokenObject:` returns true if an object is already stored. Otherwise it rebuilds the token/session, carries system-keychain and authentication-context parameters, requests card-insertion capability, looks up the stored object ID, and returns whether a nonnull object was obtained (`0x7ff80399a9ed–0x7ff80399aa14`). Requesting card insertion is not evidence that a UI appeared or a card was present. It prefers a supplied authentication context; otherwise it can try an externalized credential reference, or pass a nil context. None of those paths automatically marks the lookup successful.

The operation wrapper first requires that helper to succeed. It permits **one additional operation attempt** only when an error belongs to TKErrorDomain and has code -7, -1002 or -1003, the registered-smartcard flag is true, and both the stored object ID and token object are present. It clears the old object, requires reconstruction to succeed and invokes the operation again (`0x7ff80399ad0e–0x7ff80399ad42`). The first result need not be null for the error-based retry decision. The wrapper does not convert those error codes into success, and its callers and concrete operation blocks remain part of the review queue.

The local provider also separates authentication-context data from access-group data:

| Input or step | Observed behavior | Remaining boundary |
| --- | --- | --- |
| Authentication context | Uses the supplied context or a temporary shared resource, then requires nonnull externalizedContext | Context creation is not successful user authentication; full loader and LocalAuthentication validation are unreviewed |
| Handle transport | Stores that data as TKAuthContext ACMHandle and sends it under AKS parameter key3 | The handle's authenticity and rights are enforced, if applicable, deeper in the stack |
| Caller groups | Reads an array-valued keychain-access-groups entitlement and a string-valued com.apple.application-identifier | Effective entitlements and remote caller provenance are unmeasured |
| ACL group selection | Recursively visits ACL dictionaries and includes cag entries only when the caller-group list contains them | Complete schema, recursion limits and backend ACL enforcement remain open |
| Group transport | Encodes the selected groups and supplies them under AKS parameter key1 | Sending groups does not establish permission to use a key |
| Parameter encoding | Calls aks_params_get_der, checks its status and raises on failure | The set-data wrapper does not inspect its setter's return here; backend semantics remain open |

The ACL array route uses membership checks without a separate element-class check. No SAC or no candidate groups leaves the output group array empty; the meaning of that empty input in the backend is not yet established. This report does not interpret it as unrestricted access.

Apple documents [context creation and authentication-policy evaluation](https://developer.apple.com/documentation/localauthentication/lacontext) as distinct actions, and explains [entitlement-derived keychain access groups](https://developer.apple.com/documentation/security/sharing-access-to-keychain-items-among-a-collection-of-apps) within the documented keychain scope. Those sources support the conceptual distinctions; the private helper's exact branches are observations from this dataset, not a claim about every macOS keychain path.

**Coverage:** six Security and 17 CryptoTokenKit functions, totaling **1,398 byte-checked instructions, 83 pointer-chain checks and 10 CFStrings**. Existing component reviews are extended; totals remain 32 bounded inventory paths plus three embedded components. The report does not claim complete semantics for every decoded instruction or callee. No actual credential reference, authentication context or key was obtained or used, and no vulnerability severity is assigned.

Stage 5S below traces the CTKD caller route and acquires AppleKeyStore from its companion cache.

<a id="ctkd-caller-provenance-and-key-object-cache"></a>
### CTKD caller provenance and key-object cache

**SVC-029 — bounded caller-provenance finding; cache authorization requires investigation.** The Intel BaseSystem `System/Library/Frameworks/CryptoTokenKit.framework/ctkd`, both `com.apple.ctkd.plist` launch files and `com.apple.ctkd.sb` match their saved inventory hashes. The executable passes strict static code-signature verification. These checks concern the retained recovery image, not a running service or the installed Mac.

The launch declarations explain two service contexts. The LaunchDaemon specifies `_ctkd`, arguments `-st`, and the Mach services `com.apple.ctkd.slot-registry`, `com.apple.ctkd.slot-client` and `com.apple.ctkd.token-client`. The LaunchAgent supplies `-tw`, advertises the token-client service, and lists Aqua, LoginWindow and Background sessions. Both declare `RunAtLoad=false`, `EnablePressuredExit=true` and adaptive spawn behavior. These are declarations; the command-line flag parser, actual activation and effective bootstrap reachability remain unreviewed. Neither plist declares a network socket.

The executable declares keychain/keystore privileges, AppleCredentialManager access, the `com.apple.token` access group and `seatbelt-profiles=[ctkd]`. The acquired sandbox text denies by default, imports `system.sb`, permits selected Mach lookups and preferences, permits reads/writes below `/private/var/db/ctkd`, and allows opening AppleKeyStore and AppleCredentialManager user clients. The imported profile and the exact effective compiled sandbox are not verified here. These capabilities fit the observed token-broker role; declarations alone do not show successful key access, NFC activity or compromise.

The selected `TKTokenServer` listener first compares the supplied listener with its own token-server listener. A mismatch returns false. A match creates a `TKTokenClientConnection`, exports `TKClientTokenServerProtocol`, sets `TKProtocolTokenWatcherHost` as the remote interface, resumes the connection and returns true (`0x100018dec–0x100018f44`). This method contains no explicit application-entitlement or caller-UID test. That observation is limited to this listener; it is not evidence that all callers can reach the service or perform privileged operations.

The examined attribute and signing methods on that client wrapper forward to the server's `SEPKeyServer`. On a **cache miss**, `keyForObjectID:authContext:forceSystemSession:error:` decodes the supplied object record, obtains `NSXPCConnection.currentConnection`, and passes it as the caller to `TKSEPKey`'s local initializer (`0x10000c001–0x10000c031`). The exact-cache initializer at `0x7ff813c6958a` allocates `TKLocalSEPKey` and preserves the object ID, authentication context, caller, force-system-session flag and error pointer when forwarding them. This connects the incoming connection to the caller-dependent entitlement route traced in Stage 5Q. Apple's [current-connection documentation](https://developer.apple.com/documentation/foundation/nsxpcconnection/current%28%29) explains that the API identifies the connection responsible for an exported-object call; the private initializer and its argument flow are direct artifact observations.

**The cache-hit path needs separate scrutiny.** The token-server constructor creates one `TKSEPKeyServer` stored at offset `0x30`; the client wrappers retain the same server passed by the listener. The key-server lookup checks two cached key slots. In each slot it compares the decoded object ID and authentication context with `isEqual:`. A match returns that existing key without invoking the new local constructor. The reviewed lookup contains no explicit comparison of the current caller or requested force-system-session flag before that return. On insertion, `systemKey` selects which slot is replaced; this is distinct from the `systemSessionKey` attribute.

This is a concrete static review question, **not a demonstrated cross-client key-use vulnerability**. The scope of token-server instances, authentication-context equality and binding, whether a different caller can supply an accepted matching context, key-object lifetime, retained-caller effects and backend operation checks remain unresolved. A cached constructor is not proof that an operation bypasses authorization. No identity, authentication context or private key was requested or used.

The attribute path requires a nonnull key and a nonnull `publicKeyWithError:` result before constructing its six-field reply: `keyType`, `keySize`, `systemKey`, `systemSessionKey`, `publicKey` and serialized `accessControl`. This supplies the counterpart to Stage 5Q's remote attribute consumer. The signing handler obtains a key through the same lookup, calls `signDigest:error:` only for a nonnull key, and returns the result and error through its reply block (`0x10000c2ae–0x10000c3b2`). A null key therefore does not become a fabricated successful signature. Actual signature generation and deeper AKS authorization are not established.

**Coverage:** 11 selected CTKD functions contain **832 byte-checked instructions**; ten original Objective-C method records, two protocol references and 47 selector/CFString references were resolved. One additional CryptoTokenKit initializer contains **51 checked instructions and four verified cache pointer chains**. The whole CTKD text was separately byte-checked across 36,746 decoded instructions; that larger number is not semantic-review coverage. Four new bounded path reviews bring the current total to **36 inventory paths plus three embedded components**.

AppleKeyStore acquisition is now resolved: its header belongs to the inventory-matched `dyld_shared_cache_x86_64.01`, not the primary cache. A companion-aware reader retained the image's own mappings and regions. The refactored primary reader reproduced all 14 prior CryptoTokenKit acquisition files byte for byte. Acquisition alone does not add an AppleKeyStore semantic review. Stage 5T continues with its parameter/import/signing functions and the cache-hit authorization question. ARM equivalence, endpoint-provider/reconnect behavior, imported sandbox policy and complete operation authorization remain open. No vulnerability severity is assigned.

<a id="applekeystore-parameter-and-signing-wrappers"></a>
### AppleKeyStore parameter and signing wrappers

**SVC-030 — bounded parameter/error-flow finding.** Stage 5T follows four entry points in the inventory-matched Intel companion cache: `aks_params_get_der`, `aks_params_set_data`, `aks_ref_key_create_with_blob` and `aks_ref_key_sign`. These routines are part of the key-operation path identified earlier; they were disassembled without invoking them.

| Routine | Directly observed behavior | Boundary |
| --- | --- | --- |
| Parameter encoder | The exported get-DER entry tail-jumps to `encode_list_dict`; null arguments or an empty list fail, and outputs are written only after encoding checks succeed | Encoding success does not authenticate an ACM handle or authorize a key |
| Data setter | Resolves the requested key for type2, removes its prior entry, then validates/adds replacement data; returns nonzero on examined failure paths | Stage5R's CryptoTokenKit wrapper does not inspect this return |
| Reference import | Rejects null blob/zero length, requires the size helper's result to equal the supplied length, checks object creation and `__set_blob`, then stores the reference through the output pointer | Size agreement and a returned reference do not prove authorization or hardware-backed key availability |
| Signing | Requires merged-parameter, data-add, reference-add and encoder success before invoking `__aks_operation`; propagates that operation's result | The operation backend, context binding and actual signing rights remain unresolved |

The setter at `0x7ff903686175` calls `encode_list_remove_key` before inspecting replacement data. A null data pointer therefore takes the successful removal path after the earlier checks. For key1 and key2, it checks a decoded tag against `0x2000000000000010` and `0x2000000000000011`, respectively, before adding the encoded value. Other supported keys use the data-add helper. If replacement validation fails after removal, the outer function does not restore the previous entry. A failure status therefore matters: ignoring it can leave the caller without a successfully installed replacement. This is an observed control-flow property, not evidence that the ordinary access-group/context inputs trigger failure or that missing parameters grant rights.

The reference-import function (`0x7ff903686ad7`) returns `0xe00002c2` on its initial blob/length/size-check failures. It stores the requested bag value in the reference structure and requires `__set_blob` to return zero before publishing the reference. Its outer body does not establish the deeper helper's validation guarantees. The signing function (`0x7ff903687b2f`) constructs a request using globals named `der_key_op`, `der_key_op_sign`, `der_key_data` and `der_key_ref_key`; these names come from original defined symbols. Their pointer values were not slide-resolved in this pass. The call to `__aks_operation` at `0x7ff903687c2d` is reached only after the selected preparation checks, and its return becomes the wrapper's return.

**Decoder limits were preserved rather than hidden.** The get-DER thunk consists of ten code bytes followed by seven zero bytes before the next function-start entry. The signing body ends in a return followed by four zero bytes. Those suffixes are retained as padding and excluded from the **390 selected instruction records**. Four body functions and the thunk were byte-checked against retained regions. Several import-stub indirect-table entries contain zero, which mechanically yields an unrelated first-symbol label; those labels are explicitly excluded from callee attribution. The report uses checked internal symbol addresses and leaves external stub targets unresolved.

AppleKeyStore now has a fourth **bounded embedded-component review**. The inventory-path count remains36; the companion cache as a whole is not marked reviewed. No key, identity, credential reference or authentication context was obtained, no signing request was issued, and no severity is assigned. The next work returns to update-brain/ramrod lifecycle analysis. The AKS operation backend, parameter-field guarantees, cache-hit authority from Q29 and ARM equivalence remain explicit follow-up work.


