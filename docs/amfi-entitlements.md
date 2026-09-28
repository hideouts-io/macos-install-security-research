---
layout: default
title: AMFI and entitlement boundaries
---

# AMFI and entitlement boundaries

[Home](../README.md) · [Sandbox](sandbox-policy.md) · [Stage 6F.7](nvram-efi-paths.md)

The selected `AppleEFINVRAM::verifyPermission` branch asks `IOUserClient::copyClientEntitlement` about `current_task()` and compares the returned object to **`kOSBooleanTrue`**. A missing entitlement, or a Boolean false value, does not satisfy this branch. A separate BootPolicyLocalPolicyStorage GUID branch requires `com.apple.private.security.bootpolicy.nvram`; this is distinct from the `com.apple.private.security.bootpolicy` declaration observed in `bless`. The compiled rule table also handles selected Wi-Fi credential and Find My variable prefixes. These are names of protected variables, not secrets retrieved from the host.

In the matching KC, a bounded AMFI credential entitlement-presence dependency was followed through **120 original-byte-checked instructions in three ranges**. That trace and the NVRAM entitlement call establish code relationships, not whether a particular launcher or helper possessed an effective entitlement at runtime. Signature metadata and an entitlement declaration are evidence of a claimed capability; AMFI, the kernel, sandbox/MAC policy, SIP/CSR, and the requested operation are distinct authorization layers. [FW-016](../findings/fw.md#fw-016) records the scoped driver check.

The official-reference brain command table and `softwareupdated` dispatch show named Boolean-true entitlements for selected commands. The remote-service analysis similarly distinguishes local entitlement-presence checks, serialized service policy, TLS peer evaluation, and actual transport acceptance. See [installer workflow](installer-workflow.md) and [USB/services/TLS](usb-and-services.md). Neither table proves that an unexamined client can invoke a privileged operation.

For the NVRAM path, the missing evidence is concrete caller identity, signed entitlement state, active process profile, effective sandbox decision, CSR state, and downstream firmware acceptance. Those unknowns are part of the [coverage and open-question register](open-questions.md). No entitlement forgery, bypass, or successful unauthorized write has been established.
