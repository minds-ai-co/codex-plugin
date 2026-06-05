---
name: sort-group
description: Organize a group of Minds into subgroups by trait, role, or behavior — useful when a panel grows past 10 personas and the user wants to slice it. Wraps Minds `list_groups` + group categorization tools.
---

# Sort a group into subgroups

Subgroups are post-hoc presentational splits over an existing group. They do NOT change panel inference (panels still run group-level).

## When to load

- "Split my [group name] into [trait]"
- "Group my personas by [role / region / behavior]"
- "Show me the [subgroup] subset"

## Steps

1. **Find the group.** `list_groups` → match by name → grab `structuredContent.groups[].id`.
2. **Pick the formation lens.** A Formation = a sorting rubric (e.g. "by industry", "by seniority"). If one exists for the rubric the user asked for, reuse it. Otherwise create one via `create_group_from_brief`.
3. **Confirm to the user that subgroups are a UI bucketing**, not a different panel run. If they wanted different answers from a subset, what they actually want is a NEW group containing just those Minds — clarify before doing extra work.

## Pitfalls

- Subgroups do NOT affect panel sample size or alignment. Don't claim "the engineering subgroup said X" when the entire group answered and you're just bucketing the responses.
- Formations are per-group. A formation built for group A can't be reused on group B.
