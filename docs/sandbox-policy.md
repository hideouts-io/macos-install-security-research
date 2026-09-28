---
layout: default
title: Sandbox policy and NVRAM authorization
---

# Sandbox policy and NVRAM authorization

[Home](../README.md) · [Stage 6F.7 detail](nvram-efi-paths.md) · [Findings](findings-index.md)

The matching Intel `BootKernelExtensions.kc` contains the sandbox evaluation code and a compiled platform rule for operation `0x76`, identified as `nvram-set`. The research followed the original bytes and fixups rather than interpreting string hits alone. The KC SHA-256 is `c80161fa3065883753fc285339281361a8469cbb6fb27653c88e2a22eb4807a4`; addresses on this page apply to that exact 25G83 artifact.

The compiled platform rule has root node **474** and 38 reachable nodes. Its name filter `0x2d` selects 12 compiled FSA pattern records. Across those records, 39 normalized exact/prefix conditions were decoded; the four earlier complex cases account for 28 conditions. The examined records contain no callback opcodes. Symbolic and concrete candidate checks corroborated the decoded patterns. This establishes how selected names are **matched**, not the final allow/deny result for an actual caller.

Terminals **0, 5, and 21** feed an initial static action combination. Terminal 21 conditionally invokes `csr_check(0x40)` for a rootless modifier on `nvram-set`. The sandbox KEXT registration route through `_mac_policy_register`, `_policy_conf`, `_policy_ops`, `_hook_policy_init`, and `_profile_init` was statically linked to the embedded platform profile. This narrows the code path but does not show that a specific machine loaded this exact policy or evaluated a particular request. The second process-profile combination and approval modifier remain open.

![NVRAM sandbox action evaluation](../diagrams/nvram-authorization.svg)

[Editable Mermaid source](../diagrams/nvram-authorization.mmd).

This diagram is a **static control-flow map**. The final result depends on process profile, caller credentials/entitlements, CSR and active policy state. The trace does not provide those runtime inputs. A null process label is not, by itself, a sandbox bypass: the examined path still evaluates the global platform rule. The exact [next trace](audit-status.md#exact-next-investigative-action) is `_sb_evaluate_internal` at `0xffffff8003034156` through the process-profile `_eval_op`, second `_action_combine` at `0xffffff80030342b0`, and approval modifier branch through `0xffffff8003034364`.

This policy sits **after** selected `AppleEFINVRAM::verifyPermission` rules and **before** any conclusion about firmware persistence. The entitlement table, special GUID rule, and IOKit/MAC route are detailed in [Stage 6F.7](nvram-efi-paths.md); AMFI authenticity is a separate [boundary](amfi-entitlements.md). No live NVRAM write or sandbox authorization experiment was performed. The publication finding [FW-016](../findings/fw.md#fw-016) is a scoped static authorization observation, not an authorization verdict for the examined host.
