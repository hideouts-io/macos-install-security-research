---
layout: default
title: Sandbox policy and NVRAM authorization
---

# Sandbox policy and NVRAM authorization

[Home](../README.md) · [Stage 6F.7 detail](nvram-efi-paths.md) · [Findings](findings-index.md)

The matching Intel `BootKernelExtensions.kc` contains the sandbox evaluation code and a compiled platform rule for operation `0x76`, identified as `nvram-set`. The research followed the original bytes and fixups rather than interpreting string hits alone. The KC SHA-256 is `c80161fa3065883753fc285339281361a8469cbb6fb27653c88e2a22eb4807a4`; addresses on this page apply to that exact 25G83 artifact.

The compiled platform rule has root node **474** and 38 reachable nodes. Its name filter `0x2d` selects 12 compiled FSA pattern records. Across those records, 39 normalized exact/prefix conditions were decoded; the four earlier complex cases account for 28 conditions. The examined records contain no callback opcodes. Symbolic and concrete candidate checks corroborated the decoded patterns. This establishes how selected names are **matched**, not the final allow/deny result for an actual caller.

Terminals **0, 5, and 21** feed an initial static action combination. Terminal 21 conditionally invokes `csr_check(0x40)` for a rootless modifier on `nvram-set`. The sandbox KEXT registration route through `_mac_policy_register`, `_policy_conf`, `_policy_ops`, `_hook_policy_init`, and `_profile_init` was statically linked to the embedded platform profile. This narrows the code path but does not show that a specific machine loaded this exact policy or evaluated a particular request.

A subsequent original-byte-checked trace follows the `_cred_sb_evaluate` block to `_eval_op`, the indirect process-profile call at `0xffffff8003034167`, and the second `_action_combine` at `0xffffff80030342b0`. The combine copies the process action's low status only when its selector masked by `0x100100000000` equals `0x100000000`; otherwise it retains the prior low status. A forced fallback constructs an action with low word `1` and high word `5`, but its selector is zero. With the previously bounded platform low word of zero, that fallback alone leaves the combined low word zero. A nonzero combined low word skips approval calls; a zero low word can enter conditional category-3 and category-1 approval calls. The approval helper has early exits and explicit status writes, and the evaluator tests status again at `0xffffff8003034364`. These are static control-flow and data-flow bounds, not a concrete authorization result.

The next bounded pass checks all **415** modifier instructions and **46** category-discriminator instructions against the original KC. A byte-derived control-flow walk reaches all selected modifier instructions when both sides of conditional branches are considered and identifies **17 direct edges** to its common return. The caller offers category 3 only for a nonnull, distinct context pointer; category 1 requires a nonnull secondary pointer and low status still zero. Inside the modifier, two instructions can write the low status and two change the action word. The pointer is kept in `%rbx`; no reviewed helper call receives it through that register. The discriminator references `kTCCServiceFileProviderDomain`, but the category and helper results for a concrete NVRAM caller are unknown. This narrows the static approval layer without establishing an allow/deny decision, a resync request or a firmware error.

![NVRAM sandbox action evaluation](../diagrams/nvram-authorization.svg)

[Editable Mermaid source](../diagrams/nvram-authorization.mmd).

This diagram is a **static control-flow map**. The final result depends on process profile, caller credentials/entitlements, CSR, approval state and active policy state. The trace does not provide those runtime inputs. A null process label is not, by itself, a sandbox bypass: the examined path still evaluates the global platform rule. The [next investigation](audit-status.md#exact-next-investigative-action) seeks concrete caller and active-policy evidence, then tests resync firmware-error reachability.

This policy sits **after** selected `AppleEFINVRAM::verifyPermission` rules and **before** any conclusion about firmware persistence. The entitlement table, special GUID rule, and IOKit/MAC route are detailed in [Stage 6F.7](nvram-efi-paths.md); AMFI authenticity is a separate [boundary](amfi-entitlements.md). No live NVRAM write or sandbox authorization experiment was performed. The publication finding [FW-016](../findings/fw.md#fw-016) is a scoped static authorization observation, not an authorization verdict for the examined host.
