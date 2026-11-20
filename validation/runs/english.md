# English execution — fictional handover restructuring proposal

**Use a task-based index with linked detail records and a source ledger.** Business staff can start with “Record product demos”; maintainers can reach the linked audio-drift procedure and complete recording notes from that same project entry. Technology stays an attribute. This document proposes the structure only; it does not modify or delete any source.

Coverage: all supplied fields and notes in A–F were read. No linked site, repository, product, or acceptance record beyond the supplied excerpt was inspected. “X7” remains undefined. The record IDs below are new navigation suggestions, not original classification keys.

## Inventory and relationships

The packet mixes spreadsheet fields, a handover message, an external product case, an operations procedure, a reference checklist, and a copied index entry. It has no documented common taxonomy or revision sequence. Its apparent organizing pattern is project-centric titles and links with separate supporting notes; that is an inference from the packet, not a stated intention of its original organizer.

| Source | Actual material and retention value | Relationship and proposed treatment |
|---|---|---|
| A | Working spreadsheet: proposed recording project, operating steps, distinct owner/contact, budget and output | Main base for P1. Retain all fields and the full note. Revision order unknown. |
| B | Handover message: same project name and exact locator as A, with approval role, restriction, open decision and conflicting budget | Propose consolidating into P1 on name plus exact locator. Preserve complementary fields and both budget values. Revision order unknown; B cannot override A. |
| C | External product case with a different repository, maker, contact and acceptance-note evidence | Separate P2 despite the shared ClipDeck name. Retain as a reference case, not evidence that P1 is released. |
| D | Maintainer operations procedure with an explicit repository association | Separate supporting record T1, linked to P1 by the exact repository locator. Preserve procedure and retention requirement. |
| E | Reference checklist with detailed sequence, a caution and an undefined code | Separate R1. Project association is explicitly not specified. No project link is invented. |
| F | Copied index entry with the same locator, name, proposal status and owner as A | Merge its overlapping values into P1 with independent provenance; retain F in the ledger. It is a partial duplicate of A, not a copy of all A’s content. |

A and B are partly overlapping and complementary, with one explicit budget conflict. Neither has a known place in revision order. D complements A’s drift note; it is not an exact duplicate. C is a distinct same-named project. E is a standalone reference. No source is proposed for deletion, and none requires archiving merely because it is difficult to understand.

## Classification and navigation

Use the same primary axis—what the reader needs to do—throughout:

| Primary category | Boundary | Records |
|---|---|---|
| Record product demos | Project and case information for creating product videos | P1: ClipDeck — demo-lab proposal; P2: ClipDeck — Example Studio B external case |
| Diagnose audio drift | Procedures for investigating sound/picture timing issues | T1: Audio drift troubleshooting |
| Inspect input formats | Reusable checks for codec, resolution and frame rate | R1: Input format checklist |

Each item has one primary entry point. Cross-links carry relationships: P1 links to T1, and T1 links back to P1. R1 can be found through the index but is not assigned to P1 or P2. P1’s multiple-window question belongs in its detail record as an open decision, not as a separate primary category.

Suggested navigation: choose the task category → scan the default table → open the relevant detail record → consult the source ledger when reconciling a value. Business and maintenance views use the same records rather than copying the data. The business view emphasizes purpose, maturity, output, budget and decision roles. The maintenance view emphasizes locator, technology, full procedures, restrictions and retention. This is a proposed display arrangement, not a claim that those views have been implemented.

Process is separate from classification. A’s sequence is: confirm input frame rate → record a ten-second sample → check system audio and picture alignment → retain original until exported MP4 passes review. If audio drifts, preserve the failed sample and settings. D supplies a linked investigation procedure and a failed-sample retention endpoint. E has its own codec → resolution → frame-rate sequence; the source does not make E a prerequisite for either project.

## Useful default table

The display names below add disambiguators while preserving the original names in detail and provenance. “Not specified” means absent from this packet, not known to be nonexistent.

| Task | Entry / detail ID | Kind and state | Purpose or output | People by role | Attention needed |
|---|---|---|---|---|---|
| Record product demos | ClipDeck — demo-lab / P1 | Project; prototype proposal | Record short product-demo videos; MP4 | Owner: Lin; contact: Mei; approver: Arun | Budget unresolved: USD 400 (A) / USD 650 (B). Multiple-window recording decision pending. |
| Record product demos | ClipDeck — Example Studio B / P2 | External product case; released product case | Record product walkthroughs; MP4 export described in supplied acceptance-note excerpt | Maker: Example Studio B; contact: Noor; owner/approver: not specified | Distinct repository and project. Not independently verified. |
| Diagnose audio drift | Audio drift troubleshooting / T1 | Operations procedure; state not specified | Compare sample rate and timestamps; inspect local log | Audience: maintainers; owner/contact/approver: not specified | Applies to P1. Keep failed samples until issue closure. |
| Inspect input formats | Input format checklist / R1 | Reference checklist; state not specified | Inspect codec, resolution and frame rate | People and audience: not specified | Related project not specified; X7 undefined. |

Technology is a filter/detail attribute: P1 = Rust; P2, T1 and R1 = not specified. Do not inherit Rust into T1 merely because it relates to P1. Locator fields are available in detail and as an optional visible column. Keep long notes outside the compact table in full, with a clear detail link; never truncate the stored text. A proposed interface should wrap the purpose and attention columns, give the entry column sufficient width, and use automatic row height. This Markdown proposal has no interactive expansion or tested UI layout.

## Field dictionary and aliases

| Proposed field | Definition and example | Destination and source-field mapping |
|---|---|---|
| Record ID | New stable navigation reference, e.g. P1 | Main entry and details; newly proposed |
| Task category | Current-user action, e.g. Record product demos | Main entry; new classification, not a source value |
| Display name / original name | Disambiguated navigation label plus untouched source name | Main label and detail; A.Title, B.Project, C.Name, D.Heading, E.Label, F.Name. Labels are aliases for naming fields, not proof that records share identity. |
| Resource kind | Project proposal, external case, procedure or checklist | Main; derived explicitly from source context, distinct from maturity |
| State | Original lifecycle description | Main/detail; A.State, B.Phase, C.Stage, F.Status are candidate field aliases in this packet. P1 retains “prototype proposal”; P2 retains “released product case.” |
| Purpose | What an item supports | Main/detail; A.Use, C.Use, E.Purpose. D’s procedure describes its action; no separate original purpose field is invented. |
| Locator / locator role | Exact address and its original label | Detail; A.URL, B.Repository, C.Repository, F.Link. One exact locator supports P1 consolidation, but “URL” does not independently prove repository content. D’s applies-to locator is a relationship field, not T1’s own repository. |
| Technology | Implementation technology, e.g. Rust | Attribute/filter/detail; A.Stack and B.Tech match in value and scope |
| Owner | Responsibility named explicitly as ownership | Main/detail; A.Owner and F.Owner = Lin |
| Contact | Named communication contact | Main/detail; A.Contact = Mei; C.Contact = Noor; separate from owner |
| Approver | Explicit approval role | Main/detail; B.Approver = Arun; separate from owner/contact |
| Maker | Creator organization | Main/detail; C.Maker = Example Studio B; do not rename it owner |
| Audience | Explicit intended readers | Main/detail; D.Audience = maintainers; not a named person or ownership role |
| Budget assertions | Monetary limit, source and unresolved status | Main conflict flag and detail; A.Budget cap = USD 400; B.Budget ceiling = USD 650. Labels appear to describe the same limit and currency, but authority/revision order is unresolved. Never collapse to one amount. |
| Output | Explicit output format or carefully attributed export evidence | Main/detail; A.Output = MP4. C.Evidence describes MP4 export; retain this evidence basis instead of silently converting it to an independently verified output field. |
| Detailed procedure / note | Full operational text and original order | Detail; A.Detailed note, D.Procedure, E.Long note; keep separate provenance and do not replace with table summaries |
| Restriction | Explicit boundary on use | Detail and maintenance view; B.Restriction, plus the local-footage instruction retained within A’s note |
| Retention | What to preserve and for how long | Detail; D.Retention and the distinct instructions within A.Detailed note; preserve both endpoints |
| Open decision | Question awaiting a decision | Main flag/detail; B.Decision still needed |
| Relationship | Explicit target and relationship type | Detail; D.Applies to repository; E.Related project = not specified. Proposed P1–T1 cross-link rests on D’s exact locator. |
| Code / definition | Raw code and known explanation | Detail/ledger; E.Code = X7; definition unknown, no inferred technology or category |
| Evidence | Exact supplied support and limits | Detail; C.Evidence, retained separately from stage |
| Provenance / revision | Source ID, original field/value and known version facts | Ledger; A/B revision order unknown. No latest or authoritative version is designated. |

## Detail records and complete preservation ledger

Each row below specifies the destination and preserves its original field/value. Where values repeat, the individual source assertions remain traceable. All source fields are retained; “merged” refers to the proposed shared navigation record, not loss of the original assertion.

### P1 — ClipDeck, demo-lab proposal

| Source fields | Preserved values and destination | Disposition |
|---|---|---|
| A.Title; B.Project; F.Name | P1.original name: ClipDeck (each source) | Merged navigation; all assertions retained |
| A.URL; B.Repository; F.Link | P1.locator: https://demo-lab.invalid/clip-deck (each source), with each original locator label | Merged exact locator; source labels retained |
| A.State; B.Phase; F.Status | P1.state: prototype proposal (each source) | Merged consistent value; provenance retained |
| A.Use | P1.purpose: record short product-demo videos | Retained |
| A.Stack; B.Tech | P1.technology: Rust (each source) | Merged consistent attribute; provenance retained |
| A.Owner; F.Owner | P1.owner: Lin (each source) | Merged consistent role; provenance retained |
| A.Contact | P1.contact: Mei | Retained as contact |
| B.Approver | P1.approver: Arun | Retained as approver |
| A.Budget cap | P1.budget assertions: USD 400, source A | Retained; resolution pending |
| B.Budget ceiling | P1.budget assertions: USD 650, source B | Retained; resolution pending |
| A.Output | P1.output: MP4 | Retained |
| A.Detailed note | P1.recording note, full text immediately below | Retained in full |
| B.Restriction | P1.restriction: no raw video may be uploaded | Retained alongside A’s local-footage instruction |
| B.Decision still needed | P1.open decision: whether to support recording multiple windows | Retained as unresolved |
| A/B source context | P1.provenance: working spreadsheet / handover message; revision order unknown for both | Retained; no recency preference |
| F source context | P1.provenance: copied index entry | Retained; no claim of independent product validation |

**A.Detailed note, preserved verbatim:**

> First confirm the input frame rate. Record a ten-second sample. Check system audio and picture alignment. Keep raw footage on the local device. Retain the original recording until the exported MP4 has passed review. If audio drifts, keep the failed sample and record its settings for troubleshooting.

P1 related procedure: T1, based on D’s exact repository association. A specifies retaining the original recording until exported MP4 review passes; D specifies retaining failed samples until issue closure. These concern distinct conditions and are both retained. No new deletion rule is inferred.

### P2 — ClipDeck, external product case

| Source field | Preserved value and destination | Disposition |
|---|---|---|
| C.Name | P2.original name: ClipDeck | Retained separately from P1 |
| C.Repository | P2.repository: https://external-team.invalid/clipdeck-tools | Retained; identity disambiguator |
| C.Stage | P2.state: released product case | Retained as source characterization |
| C.Maker | P2.maker: Example Studio B | Retained as maker |
| C.Evidence | P2.evidence: packet includes an acceptance-note excerpt describing MP4 export | Retained; no runtime verification claim |
| C.Use | P2.purpose: record product walkthroughs | Retained |
| C.Contact | P2.contact: Noor | Retained as contact |
| C source context | P2.kind/provenance: external product case | Retained |

P2’s technology, budget, ownership, approval role, operational restrictions and relationship to P1 are not specified. Similar names and purposes do not establish a shared project, version, dependency, or owner.

### T1 — Audio drift troubleshooting

| Source field | Preserved value and destination | Disposition |
|---|---|---|
| D.Heading | T1.original name: Audio drift troubleshooting | Retained |
| D.Applies to repository | T1.relationship: applies to https://demo-lab.invalid/clip-deck; navigation target P1 | Retained; linked by exact locator |
| D.Audience | T1.audience: maintainers | Retained |
| D.Procedure | T1.procedure: compare sample rate and timestamps; inspect the local log | Retained in full |
| D.Retention | T1.retention: keep failed samples until issue closure | Retained in full |
| D source context | T1.kind/provenance: operations note | Retained |

T1’s owner, contact, approver, technology, version and prerequisite conditions are not specified. Linking it to P1 does not fill those missing fields.

### R1 — Input format checklist

| Source field | Preserved value and destination | Disposition |
|---|---|---|
| E.Label | R1.original name: Input format checklist | Retained |
| E.Purpose | R1.purpose: inspect codec, resolution and frame rate | Retained |
| E.Related project | R1.relationship: not specified | Retained as explicit uncertainty |
| E.Code | R1.code: X7; definition: unknown | Retained without interpretation |
| E.Long note | R1.long note, full text below | Retained in full |
| E source context | R1.kind/provenance: reference checklist | Retained |

**E.Long note, preserved verbatim:**

> Check the codec first, then resolution, then frame rate. Do not infer that support for a filename extension proves support for every codec it may contain.

R1’s owner, audience, technology, state and project prerequisites are not specified. Its subject overlaps input checking in A, but the sources do not establish a project association.

## Open issues and checks

- Resolve P1’s budget only after obtaining authority or revision evidence for A and B. Preserve USD 400 and USD 650 meanwhile. The packet does not say who has authority to settle this conflict, even though it names Arun as approver.
- Keep the multiple-window recording decision open. No decision owner or deadline is supplied.
- Obtain X7’s definition from an authorized source before using it as a filter or classification; no external lookup was performed in this fictional test.
- Leave R1’s project association unspecified until evidence is supplied. Preserve P2’s separate identity.

Content check: every named field in A–F has a destination above, including both long notes, each person’s distinct role, the budget conflict, evidence limits and unknown relationships. Structural check: primary categories describe uses; technology, state and people are attributes; workflow is shown separately. The compact table supports task lookup while the detail records preserve operational content.

Status: proposal and this local deliverable generated; source files unchanged. Content preservation was checked against the supplied packet. No target table/database was created, no interactive views were implemented, and no rendered display or real-product verification was performed.
