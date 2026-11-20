# Worked example: a usable project handover

[Home](../README.md) · [简体中文](handover.md)

The product-demo projects, people and .invalid URLs are fictional.

## Before

Six raw records contain 39 fields. No entity keys or premerged answers are supplied.

| Source | What makes it confusing |
|---|---|
| A spreadsheet | ClipDeck prototype, USD 400 cap, technology, owner/contact, long recording note |
| B message | Same locator, USD 650 cap, approver, upload restriction and an open decision |
| C external case | Same project name, different repository, described as released |
| D operations note | Explicit association to the internal repository, procedure and retention rule |
| E checklist | Unspecified project, undefined X7 code, full ordered instructions |
| F copied index | Repeats A's name, locator, state and owner |

[Full raw packet](../validation/inputs/handover.en.md)

## After

| Layer | Contents | Purpose |
|---|---|---|
| Task index | Readable name, use, kind, attention needed, detail entry | Find the relevant record |
| Detail | Technology, output, distinct people roles, budgets, full procedures and relationships | Compare and act |
| Provenance ledger | Original field, value, source, destination and treatment | Audit preservation |

These can be views and details in one collection or sections in one document, not necessarily three physical tables.

## Decisions that matter

- Consolidate A/B/F by matching name and exact locator while retaining each assertion.
- Keep the external same-named project C separate.
- Normalize Stack/Tech as attributes; preserve owner Lin, contact Mei and approver Arun as distinct roles.
- Preserve USD 400 and USD 650 with unknown version order. Do not average or silently pick one.
- Retain the original recording until MP4 review and failed samples until issue closure as distinct rules.
- Keep E's association unspecified and X7 undefined. Similar topics do not establish a project relationship.
- Produce a proposal only; do not edit or delete sources.

## Full deliverables

The [English execution artifact](../validation/runs/english.md) contains a default index, field dictionary, detail records and a full source-to-destination ledger. The [Chinese artifact](../validation/runs/chinese.md) uses different display IDs but preserves the same 39 source fields and relationship boundaries.

Presentation need not be identical across languages. Long notes remain intact beyond the index summaries.

[Validation scope](../validation/README.md): these are supplied-text trials, not an actual spreadsheet or cloud-platform migration.
