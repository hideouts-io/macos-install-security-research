---
layout: default
title: "Update brain, commands, contexts, and Update.plist"
---

# Update brain, commands, contexts, and Update.plist

[Home](../README.md) · [Documentation](index.md) · [Findings](findings-index.md) · [Status](audit-status.md)

> This page is a build-25G83 research snapshot. Static code paths and declared capabilities do not establish execution or effective runtime policy. Original raw evidence is retained privately; public tables and measurements are linked where available.

<a id="update-brain-and-updateplist"></a>
## Update brain and Update.plist

<a id="immediate-input-and-consumers"></a>
### Immediate input and consumers

The ramrod plugin builds the options path from the update-volume mountpoint plus `Update.plist`. It opens a CFReadStream and parses a property list. No runtime file with that name was present in the seven retained inventories. This is not proof of deletion: a runtime update-volume file need not remain in the supplied staging package.

A Stage 4D scan hash-verified 1,020 Intel BaseSystem executable/cache files. Exact option strings led to the plugin plus three MobileSoftwareUpdate executables:

| Component | Confirmed static role |
| --- | --- |
| softwareupdated | Reads update attributes/build and `prepare-snapshot`; also retrieves update information |
| MSUTargetController path getter | Appends `Update.plist` to `preparePath` |
| CleanupPreparePathService | Obtains that path and calls `unlink`; success log describes cleanup without a suspended/pending update |
| CryptegraftService | Contains the same path getter |

The complete cleanup predicates are not fully traced. A deletion call establishes capability, not an event affecting the examined machine.

<a id="official-reference-writer"></a>
### Official-reference writer

The 4,393,914-byte update-brain ZIP is byte-identical to the brain archive inside official SharedSupport. It contains 147 entries, including 96 regular files. Both the service and library pass the retained strict codesign checks. The library is universal x86_64/arm64e; the service is x86_64/arm64. The following control-flow analysis is x86_64 only.

```text
Upstream option: DoNotSeal (CFBoolean)
    -> update-context skip field
    -> _store_options_for_patchd
    -> Update.plist key: skip-sealing = true, when the field is set
    -> ramrod plugin's typed skip branch

This describes linked static producer/consumer behavior.
Full call authorization and historical use remain unestablished.
```

| Evidence | Observation |
| --- | --- |
| Symbol `0x3a0388` → CFString `0x3b6918` → text `0x28d54b` | `_kMSUOptionsKeySkipVolumeSealing` is `DoNotSeal` |
| `0x32b8a–0x32be6` | Context creator type-checks CFBoolean and stores the value at `+0x2d49` |
| Writer `0x35eb0`; insertion `0x362d2–0x362df` | Nonzero skip field inserts `skip-sealing` using `kCFBooleanTrue` |
| `0x36070–0x3608d` | Context `+0x4861` inserts `system-volume-verify-done` |
| Getter `0x158ce`; writer `0x3668e–0x366ce` | Constructs `Update.plist` path and calls `_store_dict` |
| `_store_dict` `0x1d645`; `_store_dict_with_mode` `0x3e155` | Requests `writeToFile:atomically:` with true, then chmod `0644` |
| Apply server `0x4e318` | Calls the writer and tests its result |

The write helper returns failure for invalid inputs, failed write or failed chmod; success is zero. Its caller propagates failure. Mode `0644` means owner-write and group/other-read in Unix mode bits. Historical ownership, ACLs, parent-directory security, actual resultant permissions and Foundation replacement internals were not acquired. No file-race exploit is established by this sequence.

The verification-state field is set in `_verify_postbom` before further operations and can also be restored from context. Complete success/failure handling must be traced before interpreting the word “done” as proof of completed verification.

<a id="brain-service-sandbox"></a>
### Brain service sandbox

The service's small entry point transfers to the library's `_update_brain_service_main`. The library locates `UpdateBrainService.sb` and calls `sandbox_init`. Missing profile returns **72**; failed initialization returns **70**, before normal startup continues.

The profile allows operations by default, then restricts dynamic code generation, executable mapping and process execution. Explicit execution exceptions include sqlite3, bless, FirmwareUpdateLauncher, efiupdater, mount, umount, mount_apfs and seputil. Mapping exceptions cover extension/plugin needs; AppleConnect-related mappings are explicitly denied in the retained text.

This is policy text plus startup control flow. Imported profiles, runtime kernel enforcement and every executed subprocess remain outside the finding. None of these update tools was launched by the audit.


<a id="command-authorization-and-endpoints"></a>
## Command authorization and endpoints

<a id="softwareupdated-27-commands"></a>
### softwareupdated: 27 commands

The table at `0x100156a10` contains 27 records; its caller supplies that count. The dispatcher calls the entitlement helper before invoking the selected handler. All entries have non-null entitlement names.

| Entitlement | Commands |
| --- | --- |
| `allow-softwareupdated` | CreateUpdateBrainConnection, PurgeSuspendedUpdate, CalculatePrepareSize, CalculateApplySize, LoadBrain, LoadMABrain, CancelLoadBrain, AdjustLoadBrainOptions, MAAdjustLoadBrainOptions, RequiredDiskSpace, CheckPreparationSize, CheckInstallationSize, BrainIsLoadable, RetrieveLastUpdateResult, RetrievePreviousUpdateState, IsFirstBootAfterUpdate, RetrievePreviousUpdateDate, GetStashedConnectivityData, RetrievePreviousRestoreDate, PerformReportAndCleanup, GetUpdateInformation, PerformCryptegraftSemiSplat, PerformCryptegraftDownlevel |
| `com.apple.private.mobile.softwareupdate-tools` | PurgeBrains |
| `com.apple.private.softwareupdated-helpers` | MarkSelfDirty |
| `com.apple.private.mobile.reboot-nerd` | RebootToNerd |
| `com.apple.private.mobile.releasevalidation.tests` | RVTriggerNeRDUpdate |

Missing, non-Boolean or false entitlement values are rejected. The helper permits a null entitlement argument, but none of these entries supplies one. Prefix comparison uses the registered command's length; the selected record's entitlement gate still applies. No bypass is inferred from matching semantics alone.

<a id="updatebrainlibrary-seven-commands"></a>
### UpdateBrainLibrary: seven commands

| Command | Handler address | Required entitlement |
| --- | --- | --- |
| PreflightUpdate | `0x42a86` | `allow-softwareupdated` |
| PrepareUpdate | `0x43574` | `allow-softwareupdated` |
| ApplyUpdate | `0x43745` | `allow-softwareupdated` |
| SuspendUpdate | `0x4383a` | `allow-softwareupdated` |
| ResumeUpdate | `0x438c9` | `allow-softwareupdated` |
| PingService | `0x43941` | `com.apple.private.softwareupdated-helpers` |
| CommitStash | `0x43c34` | `allow-softwareupdated` |

The table starts at `0x3a0940`, with seven 24-byte records. Gate `0x52b83` precedes handler call `0x52ba6`; false goes to error handling. Its helper likewise requires a named XPC Boolean true.

The brain creates an **anonymous NSXPC listener**. PingService can return its endpoint under `MSUBrainEndpoint` (`0x43e2d–0x43e44`). Thus the traced endpoint-distribution command is entitlement-gated. The connection acceptance method configures interfaces, resumes and returns true on its normal path; its dispatch-once block obtains the remote proxy and sets the delegate.

The small NSXPC prepare/apply wrappers forward to a brain object without a separate entitlement check in those wrappers. Endpoint acquisition and the concrete receiver must be considered before calling this missing authorization. No unprivileged endpoint acquisition or full unauthorized update route has been demonstrated.


<a id="brain-receiver-and-prepareapply-guards"></a>
## Brain receiver and prepare/apply guards

**Stage 4G: bounded static pass complete.** The local receiver and selected state guards are now recorded; complete transitive dataflow and client authorization remain unfinished.

<a id="static-nsxpc-receiver"></a>
### Static NSXPC receiver

Server initialization allocates `MSUBrain` (`0x3b8e4–0x3b8eb`) and stores it at object offset `+0x18`. The `brain` getter returns that field. Objective-C metadata maps prepare/apply to `0x53fc` and `0x5408` respectively.

Both original method bodies are six bytes:

```text
55 48 89 e5 5d c3
push rbp; mov rsp, rbp; pop rbp; ret
```

The local category section does not name an MSUBrain category. These recorded methods simply return. Runtime replacement, other loaded images and all initialization behavior have not been excluded. Consequently the NSXPC wrappers are **not a proven route to the Update.plist writer** in this analysis.

<a id="separate-concrete-command-path"></a>
### Separate concrete command path

The entitlement-gated PrepareUpdate command reads `ClientOptions`, passes it to `_handle_MSUPrepareUpdate_impl`, and makes a mutable copy (or an empty dictionary when null). An ordinary branch passes the options toward `_MSUPrepareUpdate_server`, then `_create_update_context_with_error`, whose DoNotSeal lookup is traced in Stage 4E.

Key transfer points: `0x43632–0x43719`, mutable-copy store `0x3ecdd`, server call `0x3fbff`, context-creator call `0x4c5cb`, and option lookup `0x32b94`. The concrete ApplyUpdate implementation likewise has an ordinary call to `_MSUApplyUpdate_server` at `0x40d8b`; alternative branches call Splat-specific functions.

Additional traced conditions narrow that chain:

- The Splat-only prepare branch changes OS-personalization and BridgeOS-install options and removes the personalized-manifest-roots option (`0x3f55b–0x3f5bd`). A snapshot branch inserts the prepare-snapshot option (`0x3f810–0x3f82e`). Those update-mode changes are not by themselves vulnerabilities.
- Target UUID selection and target-volume configuration must succeed on the traced prepare-server route (`0x4c403–0x4c440`). Existing preflight context and new context use different branches; the new-context route checks cleanup and creation results.
- Apply checks for a supplied session handle and membership in the process's `_gMSUHandleTable` (`0x409e5–0x40a19`). This does not establish per-client ownership of the handle.
- An apply semaphore has a 90-second timeout; failure produces an error (`0x40d0d–0x40d66`). The successful route selects ordinary or Splat-only apply.
- Update-volume preparation, boot-environment preparation and options writing have tested return values on the examined ordinary apply route (`0x4e177`, `0x4e2e5`, `0x4e318`).

No direct overwrite or deletion of DoNotSeal was identified in the reviewed local mutation sites. Helpers receive the dictionary, so its preservation through every transitive call remains unproven. Stage 4I below traces prepare/resume handle creation; ownership/expiry, the complete restored-context lifecycle, endpoint forwarding and authorized client origin remain open. This is not an exploit, an unfiltered input route, or evidence that a particular update chose DoNotSeal.


<a id="verification-state-flag-and-error-propagation"></a>
## Verification-state flag and error propagation

**Stage 4H: bounded static pass complete.** `system-volume-verify-done` is serialized state, not independent proof of successful verification.

On the manifest/seal-data branch, `_verify_postbom` sets context byte `+0x4861` at `0x74bf` **before** `_pm_verify_manifest_with_path` runs at `0x75bd`. The branch prepares `remap.plist` and `remove_list.plist` paths. A separate `msu_use_boms` NVRAM read and post.manifest availability test can select a post.bom route instead; this audit measured neither a live NVRAM value nor its write authorization.

The manifest wrapper checks open/read/seek and directory-verifier errors and, when selected, remove-list and sealer-data output failures. Its verification-operation result byte at `+0x53` belongs to a different object from the serialized update-context byte `+0x4861`.

Both named direct callers found in the retained disassembly test the return value:

| Caller | False-result path | Limit |
| --- | --- | --- |
| `_calculate_update_progress` | `0x35822–0x35824` branches to a zero return | Progress-calculation mode is not proof of completed full verification |
| `_prepare_snapshot` | `0x55b9c–0x55b9e` branches to cleanup and a zero return | The false branch does not reach the later prepare-snapshot creation call |

The early flag is not cleared within the examined helper's return span, but the traced callers do propagate false. **That timing alone does not demonstrate a failed verification being accepted.** Failed-context reuse, persistence and every caller still need lifecycle analysis.

Context loading reads `system-volume-verify-done` with a CFBoolean type check and restores `+0x4861` (`0x37600–0x37634`). The ordinary load/validate wrapper can check target-group UUID and prepare-snapshot reversion before calling the context validator. A separate context-flag test (`0x37de4–0x37de8`, bit `0x80`) branches directly to its success block. Stage 4I below finds no normal population route to that bit in the called loader. The branch must not be presented as a demonstrated bypass or a plist-selectable switch. The log text “context validated” and the validator's name also do not prove cryptographic re-verification.

These are state-management and verification mechanisms with explicit remaining questions. No bypass or historical use has been established. Fresh symbol-aware listings for Stages 4G/4H contain 3,958 and 3,255 parsed instructions checked against original bytes; those totals are not counts of instructions fully reverse engineered.

<a id="saved-context-flags-and-session-lifecycle"></a>
### Saved-context flags and session lifecycle

**Stage 4I: bounded static pass complete.** This pass separates reconstructed state, successful serialization and session authorization.

`_load_context_from_path` allocates and zeroes `0x4868` bytes (`0x36fb4–0x36fdb`). It reconstructs named fields rather than copying a stored raw flags word. The only direct assignment to the low flag byte `+4` is OR `0x20` for a typed, true `firmware-only` option (`0x37110`). Three other flag writes affect byte `+5`, representing word masks `0x0200`, `0x0800` and `0x0400`. None sets low-byte bit `0x80`. Review of the retained loader's 87 base-register references and explicit field aliases found no ordinary route that populates that bit. This is a bounded code-path conclusion, not a memory-safety proof or a claim about every other context constructor.

The writer independently serializes `system-volume-verify-done` from byte `+0x4861` (`0x3697d–0x3699b`) and `skip-sealing` from byte `+0x2d49` (`0x36c1c–0x36c33`). Its body does not re-run the manifest verifier. The suspension server checks the writer's return: on failure it attempts to unlink the selected output and returns false (`0x4e6f8–0x4e6ff`, `0x4e75d–0x4e798`). Preflight state selects a separate options path. Successful ordinary suspension attempts to remove the stale alternate preflight file; that cleanup failure does not itself change the local success result.

This establishes **handling of serialization failure**, not a complete chain from failed verification to accepted resumed state. Whether a failed verification leaves a usable context that can reach suspension remains open. No such execution was observed.

| Session step | Observed static condition | Remaining boundary |
| --- | --- | --- |
| Initialize service | Creates process-global mutable CFSet with CF object callbacks (`0x41c55–0x41c63`) | Does not establish per-client ownership |
| Prepare succeeds | Creates a numeric handle from the context slot, inserts it into the set, delivers it to a callback (`0x3fe68–0x3fe99`, `0x3ff68–0x3ff6f`) | Transport exposure and authorized recipient chain unfinished |
| Apply or suspend | Rejects missing/nonmember handles before extracting a context (`0x409e5–0x40a19`, `0x4155f–0x4159b`) | Handle expiry, revocation and all aliases unfinished |
| Resume | Requires a non-null loaded context and null error (`0x4e833–0x4e84b`), then registers a handle only after server success (`0x41758–0x41791`) | Stored-file protection and full validation semantics remain separate |

The numeric representation is a CFNumber created with type `0x0a` from the context-pointer slot in this x86_64 implementation. Set membership and the previously traced command entitlement gates are real conditions; they do not by themselves establish the entire authorization model. This analysis does not demonstrate an unauthorized accepted handle, stale-pointer exploit or validation bypass.

**Findings RAM-010 and RAM-011:** expected update-state handling with unresolved lifecycle and client-authorization questions. Confidence is high for the listed local calls/branches, limited for end-to-end policy conclusions. Evidence is the official-reference brain slice, SHA-256 `119378e94de84054826a58809a84cbef7c201b318af6ad289525efb83b365b21`, and 4,072 byte-matching instructions across 12 selected symbols. This count overlaps earlier passes and is not an additional unique-instruction total. Follow-up: trace failed-context disposal/retry, handle ownership/expiry, client forwarding and runtime file protection. No vulnerability severity is assigned.

<a id="prepare-failure-cleanup-current-lifecycle-boundary"></a>
### Prepare-failure cleanup: current lifecycle boundary

Stage 4J is in progress. The ordinary prepare handler checks the server result before creating and registering a handle. Its false branch invokes a staged-asset purge helper and requests `CleanupPreparePath` over synchronous XPC. On this route the request sets `ShouldPurge`, `ShouldPurgeStagedAssets` and `ShouldDisableAssetStaging` false, omits `ShouldResetAPFSReserve`, and includes `TargetUUID` if supplied. The receiver defaults are traced below; actual file/APFS effects remain unobserved.

Cleanup failure is logged, and the prepare-failure continuation remains false. This is evidence of failure handling; it is not proof that every failed context is destroyed or cannot later reach suspension. The receiver gate and defaults are traced below; connection authority, target provenance and complete context lifetime remain under review. Seven selected functions were byte-checked against the exact-reference brain slice; the 3,702 instruction records overlap prior stages and are not added as new unique coverage. No cleanup operation was executed.

<a id="cleanup-receiver-reserve-default-and-failed-context-disposal"></a>
### Cleanup receiver, reserve default and failed-context disposal

**RAM-012 — bounded receiver and failure-path finding.** Stage 4J.1 follows the inventory-matched Intel `com.apple.MobileSoftwareUpdate.CleanupPreparePathService` XPC service. Its Info.plist declares a system service. All seven decoded command records require `com.apple.private.softwareupdated-helpers`; the dispatcher requires the copied entitlement value to have XPC Boolean type and a true value before invoking the selected handler. The helper's null-entitlement-name shortcut does not apply to these seven non-null table entries. Endpoint distribution and the complete caller authorization chain remain separate questions.

| Receiver field | Absent or wrong-type default | Reviewed effect |
| --- | --- | --- |
| `ShouldPurge` | false | Skips the initial purge branch, not the entire cleanup function |
| `ShouldPurgeStagedAssets` | false | Skips the optional staged-asset purge call |
| `ShouldDisableAssetStaging` | false | Skips the optional staging-disable call |
| `ShouldResetAPFSReserve` | **true** | Requests `resetAPFSFreeBlocksThreshold:` after target selection succeeds |

Valid CFBoolean values override these defaults. The ordinary brain prepare-failure request sets the first three fields false and omits the fourth. The handler requires `setSystemTargetUUID:` to succeed before calling the cleanup server. Consequently, the omitted fourth field reaches the reserve-reset request on this accepted-target route. The receiver does not immediately inspect that reset method's return value; this is a requested operation, not proof that a disk's reserve changed.

The initial `ShouldPurge` branch contains upgrade-boot-command cleanup, deletion of the `update-volume` and `target-uuid` NVRAM variables, unlink calls for the ordinary/preflight options and brain-locator paths, and Preboot/Data cleanup helpers. The false-purge route skips that initial branch but rejoins subsequent update-volume and prepared-update cleanup. All later deletion/retention predicates and backend effects remain under review. No cleanup command or collected executable was run.

A separate brain failure edge is now resolved: when `_validate_update_context` returns false, `_load_context_from_path_and_validate` reaches a verified `libSystem/_free` call with the loaded outer context and returns null (`0x37ef6–0x38050`). This narrows the saved-context validation failure path. It does not prove disposal of every nested resource, every prepare context, or every registered handle, nor establish an end-to-end verification bypass.

**Integrity and signature qualification:** the executable SHA-256 is `471b633762d06ffd180cb57cdb865e10ce8b41c8c9242679ee272dfad4318b0d`; all five reacquired bundle files match the earlier inventory. Isolated executable verification fails with an Info.plist-binding error. Restoring the complete bundle changes the diagnostic, but both ordinary and strict full-bundle verification still fail with **“resource envelope is obsolete (custom omit rules)”**. Signature/entitlement display succeeds, which is not signature verification. This pass reports the verification failure without upgrading it to valid signing or claiming modification. Stage 4K.1 below resolves the matching code-page, special-slot and CMS-integrity layers and identifies the omission rules; full trust interpretation remains unresolved.

**Coverage and assessment:** seven receiver functions contain 2,349 byte-checked instruction records; seven command records and seven import stubs are independently resolved. Seven brain functions contain 3,702 checked records, with overlap from earlier passes. These are decoding counts, not complete semantic coverage. Two new bounded reviews—the executable and Info.plist—bring the current ledger to **38 inventory paths plus four embedded components**. Confidence is high for these local branches and parameter defaults; no vulnerability severity is assigned. Follow-up is full cleanup path selection/retention, target and connection provenance, resource-envelope interpretation and remaining context/handle lifetime.

<a id="prepared-update-retention-and-cleanup-results"></a>
### Prepared-update retention and cleanup results

**RAM-013 — bounded cleanup-selection and result-handling finding.** Stage 4J.2 traces the outer cleanup server after its purge/reserve branches. A false `ShouldPurge` still permits this later pass. First, `configureUpdateVolumeWithReserve:andErase:withError:` receives false for both reserve and erase arguments; failure returns false. The subsequent logic reads the ordinary and preflight options dictionaries.

| Decision | Observed local behavior |
| --- | --- |
| Both options describe the same `UpdateUUID` | Requires dictionary-typed asset attributes and non-null equal UUID objects; ignores the duplicate preflight dictionary |
| Preflight has a string `suspended-update-path` with successful canonicalization and stat | Selects that path for retention |
| No preflight path was selected | Tries ordinary string `update-path`, then string `suspended-update-path`; requires successful canonicalization and stat |
| Ordinary path exists | Presence of the `suspended-update-path` key selects suspended retention; otherwise a string NVRAM `boot-command` equal to `upgrade` selects pending retention |
| Prepared-directory walk | Examines non-root preorder directories whose names begin with the 14 bytes `softwareupdate`; preserves an exact canonical-path match when retention is selected, otherwise requests recursive removal |
| A retained state exists after the walk | Returns through the retained-state completion, skipping the later global cleanup |
| No retained state exists | Requests upgrade-command/target-UUID cleanup and deletion of both options files, followed by update-volume/log/download and snapshot cleanup |

The directory walk uses flags `0x15`, corroborated in the local Apple SDK as `FTS_COMFOLLOW | FTS_NOCHDIR | FTS_PHYSICAL`. FTS struct offsets and constants were checked by compiling x86_64 static assertions without running a program. Each non-root preorder directory is skipped for further traversal after selection, so the reviewed pass does not recursively enumerate arbitrary nested directories before selecting a removal root. `removefile` itself receives the recursive flag. These facts do not prove race-free path handling, authenticated options, or identical behavior in every libc version. The two string-to-C-buffer calls do not immediately test conversion success; input guarantees remain open.

The later log pass considers top-level regular files with a `patchd-` prefix and requires the numeric parser's remaining suffix to equal `.log`. It checks a relative `.patchd-saved-` marker. An existing marker, or a zero return from `_submitRestoreLogFile`, leads to an unlink request. The marker's effective base directory and submission helper's destination/transport are not yet traced; the symbol name is not evidence of network transmission or historical log collection.

**A success reply does not certify complete cleanup.** Prepared-directory removal failures can populate an error and continue. Options-file unlink failures do not force an outer false result. The later `UpdateDownloads` removal reports non-ENOENT errors but can continue; app-demotion cleanup failure is logged. A non-null root snapshot name triggers a request to prepare the target by reverting to that snapshot, followed by an unmount attempt even if reversion failed. Those failures are logged, but this continuation still sets the outer result true. The receiver chooses its status reply from that Boolean rather than separately rejecting a non-null error. By contrast, the earlier update-volume configuration failure and prepared-root canonicalization/open failures have explicit false exits.

These are cleanup capabilities and error-handling semantics in a privileged update helper. They do not establish unauthorized deletion, log exfiltration, rollback bypass, successful disk changes or compromise. No target operation was invoked and no vulnerability severity is assigned. The existing 2,349 receiver instruction records now support this additional bounded interpretation; 23 import-stub bindings and the SDK ABI check support attribution. Coverage stays at **38 bounded inventory paths and four embedded components**. Target/connection provenance, options-file protection, indirect helper behavior and handle lifetime remain unfinished.

<a id="cleanup-connection-and-target-selection"></a>
### Cleanup connection and target selection

**RAM-014 — bounded connection and target-selection finding.** Stage 4J.3 resolves how the update brain requests this cleanup service and how the receiver selects a disk target. These checks concern retained Intel code; no live service, UUID, mount or log file was accessed.

The brain creates its cleanup queue once and runs connection acquisition on that queue. It first calls `dlopen` for the MobileSoftwareUpdate framework, then `xpc_connection_create` with `com.apple.MobileSoftwareUpdate.CleanupPreparePathService`, installs its event handler and resumes the connection. Subsequent acquisitions retain the cached connection. An event whose XPC type is error releases and clears that shared pointer, allowing later acquisition to create a new connection. The call is the named-service creation API; the reviewed instruction is not the separate Mach-service API with a privileged-lookup flag. Creation of an object is not proof that a peer was reachable or accepted the request. The receiver's Boolean-true helper entitlement requirement from RAM-012 still applies.

The prepare handler copies its options input and initially takes the cleanup target from `TargetUUID`. A non-null **`__CleanupTargetUUID`** value replaces that target for the later failure-cleanup request (`0x3ed73–0x3edee`, `0x400bc–0x400c3`). This establishes a separate cleanup-target override consumer. It does not identify every producer of that option or prove that an unauthorized client can supply it. Although the handler does not immediately branch on an early target-setter result, `_MSUPrepareUpdate_server` subsequently checks its own setter result for the ordinary `TargetUUID` and fails on false (`0x4c403–0x4c407`). The earlier unchecked call must not be presented as absence of all target checks.

| Receiver target condition | Observed behavior |
| --- | --- |
| Existing target's `mediaUUID` matches the supplied value | Returns true before the rest of target setup |
| Non-null UUID needs lookup | Builds an NSUUID, fills a zero-initialized 16-byte buffer and rejects a null UUID result before querying media; a mounted snapshot can be replaced by its live media |
| UUID omitted/null | Explicitly resolves `/`; uses the live-media-for-snapshot route when the root lookup indicates a snapshot or produces no media |
| Newly resolved media is not an APFS-volume object | Returns false |
| APFS role equals 3 | The local diagnostic identifies this as a data volume; uses its paired volume and fails if no pair exists |
| Update-container selection fails | Returns false |
| Selected target needs further setup | Stores target state and can request update-volume configuration, conditional mounting and restore-log opening; some setup failures are logged without making the final result false |

The one-argument setter supplies timeout zero. Its UUID lookup helper still makes at least one media query; a miss invokes a one-second sleep before the retry counter expires. This is static control flow, not a measured delay. Internal media ordinarily supplies its own container. An external-media branch conditioned on embedded-root policy searches the primary media's APFS physical stores for a role-zero container. Exact libpartition2 policy and the hardware conditions behind that branch remain unresolved; a selected update container should not simply be assumed identical to the target's own container in every case.

The method is therefore a **target-resolution and setup operation**, not solely a passive UUID-format check. Its true result does not guarantee that an update volume was successfully configured or mounted. Conversely, the explicit root/default and snapshot/pair handling are not evidence that this audit modified the booted system. The relevant services were never run. Stored target-volume and volume-group fields are traced, but per-client ownership, shared-state lifetime, the override's full provenance and indirect storage operations remain open. No unauthorized target selection or security bypass is established, and no vulnerability severity is assigned.

**Evidence quality:** seven brain functions contain 2,846 checked instruction records; seven receiver methods contain 818. Original method records agree with all seven receiver implementations. Three block pointers, 56 imported stubs, 244 indirect import references and 386 selector/CFString references are checked against the retained source/fixups; metadata RIP displacements also match original bytes. An older linear listing had one instruction-boundary mismatch at the prepare-handler prologue. This pass uses symbol-aware, byte-checked instructions and retains that discrepancy instead of using the misaligned line. Counts overlap earlier work and do not mean every selected branch or dependency is fully reviewed. Coverage remains **38 bounded inventory paths and four embedded components**; the earlier bundle-signature limitation remains unresolved.

<a id="failed-preparation-context-disposal-and-the-no-op-flag"></a>
### Failed preparation, context disposal and the no-op flag

**RAM-015 — bounded failure-propagation and internal context-producer finding.** Stage 4J.4 follows failure returns across the update-context constructor, prepare server and outer handle-registration branch. It also identifies a concrete producer of the context flag `0x80`. These are static observations in the retained, exact-reference Intel update brain; no restore operation was executed.

| Question | Observed code and implication |
| --- | --- |
| What happens when a newly allocated context fails structural validation? | The constructor retains the false `_validate_update_context` result, builds an error and eventually calls `free` on the outer context allocation before returning null (`0x32f46–0x32fd5`, with the continuation at `0x333c9`). This complements the previously traced loaded-context failure. It does not establish that every nested allocation is released, and context validation must not be equated with cryptographic manifest verification. |
| Does snapshot-preparation failure produce a new successful update handle? | `_MSUPrepareUpdate_server` checks `_prepare_snapshot` at `0x4d3a9–0x4d3b0`; false reaches the failure block at `0x4db0a`, preserves a false result through its common exit and returns it at `0x4d03b`. The outer prepare handler then skips the successful `CFNumber` creation and `CFSetAddValue` registration (`0x3fe68–0x3fe99`). |
| Where does the `0x80` flag come from in one concrete route? | `_shared_noop_update_context` clears a static `0x4868`-byte context and writes `0x80` at offset `+4` (`0x32077–0x32095`). The asset-staging method calls it at `0x2093c`, installs a dictionary and null progress callback, and supplies the context to `_report_progress` in its download-wait loop at `0x214b9`. |
| What does the handle-table search establish? | Five source-byte-checked RIP-relative MOV/LEA references cover table initialization, successful prepare/resume insertion and apply/suspend membership checks. This limited instruction-encoding search does not establish that aliases, other access patterns or removal mechanisms are absent. |

The snapshot-failure result extends the earlier `_verify_postbom` → `_prepare_snapshot` failure trace. The early `system-volume-verify-done` store remains a relevant implementation detail, but **this ordinary failure route does not register a new success handle**. The traced suspend handler requires handle-table membership before decoding and using a handle. These observations constrain a failure-to-suspension hypothesis; they do not prove that all prior handles, aliases, retries or alternate callers are excluded. The prepare server's common exit also does not itself demonstrate complete context-memory reclamation.

The no-op context is an explicit internal object used by asset-staging progress code. Its existence provides a concrete explanation for one producer of `0x80`; it does not show that a saved plist or unauthorized caller can set that flag. The earlier result that the ordinary saved-context loader does not populate this raw flag remains intact. No connection from this asset-staging object to an accepted verification bypass has been established. No vulnerability severity is assigned.

**Evidence and limits:** 13 selected functions contain 7,076 original-byte-checked instruction records. The pass checks 84 import stubs, 358 indirect import references and 669 selector/CFString references. Counts include earlier overlap and branches outside the conclusions above; they are not a count of fully understood instructions. Semantic coverage remains 38 bounded inventory paths and four embedded components. Full handle removal/expiry, client ownership, transitive resource disposal, target-override authority and ARM behavior remain open. The next bounded pass examines the cleanup bundle's unresolved signature/resource-envelope rejection.


