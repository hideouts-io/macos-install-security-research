---
layout: default
title: Sealed System Volume and APFS update boundaries
---

# Sealed System Volume and APFS update boundaries

[Home](../README.md) · [Ramrod and sealing](ramdisk-ramrod.md) · [Secure Boot](secure-boot.md)

The signed system volume (SSV) work in this collection concerns **update preparation and static sealing paths**, not a verified seal on the currently installed Mac. The examined ramrod patch plugin calls the main `ramrod_seal_system_volume_with_root_hash_verify` routine and propagates the selected result. The plugin requests the `xsys` root-hash object; an `xmtr` string in nearby logging was an earlier misleading clue. Both objects are present in the examined tickets. See [RAM-001 and related records](../findings/ram.md#ram-001) and [ramrod](ramdisk-ramrod.md).

The official-reference update brain has a bounded writer that can map Boolean `DoNotSeal` to `skip-sealing` in `Update.plist`. Reader, validation, saved-context and selected command guards have been traced, but the historical file is absent from retained inventories, and the upstream authority of every option producer is not resolved. A skip option's existence is **not** a demonstrated bypass or use. There was no live experiment forcing a seal skip.

The reconstructed BaseSystems, Intel Preboot and system cryptex have recorded image properties, filesystem checks and selected code/signature measurements. The investigation has not yet closed each APFS snapshot, firmlink, Preboot linkage, cryptex mount policy, LocalPolicy or device boot-policy relationship. The [audit status](audit-status.md) and [Q12 in open questions](open-questions.md) retain these gaps. A matched image or successful static signature check does not certify an installed SSV snapshot.
