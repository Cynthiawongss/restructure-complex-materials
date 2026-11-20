# Fictional product-demo handover packet

All names, projects and links are fictional. No classification keys or intended merged records are supplied.

## Request
I inherited these notes and cannot find what I need. Business staff need an entry point by use; maintainers need troubleshooting details. Propose a structure and a useful default table with a field dictionary, without discarding long notes. Identify aliases and preserve each source field's destination, values, disagreements and uncertainty. Do not silently merge distinct people or same-named projects. Provide a proposal only; do not change or delete source files. Code/technology should be an attribute. "X7" has no supplied definition.

## A — working spreadsheet, revision order unknown
Title: ClipDeck
URL: https://demo-lab.invalid/clip-deck
State: prototype proposal
Use: record short product-demo videos
Stack: Rust
Owner: Lin
Contact: Mei
Budget cap: USD 400
Output: MP4
Detailed note: First confirm the input frame rate. Record a ten-second sample. Check system audio and picture alignment. Keep raw footage on the local device. Retain the original recording until the exported MP4 has passed review. If audio drifts, keep the failed sample and record its settings for troubleshooting.

## B — handover message, revision order unknown
Project: ClipDeck
Repository: https://demo-lab.invalid/clip-deck
Phase: prototype proposal
Budget ceiling: USD 650
Approver: Arun
Tech: Rust
Restriction: no raw video may be uploaded
Decision still needed: whether to support recording multiple windows

## C — external product case
Name: ClipDeck
Repository: https://external-team.invalid/clipdeck-tools
Stage: released product case
Maker: Example Studio B
Evidence: packet includes an acceptance-note excerpt describing MP4 export
Use: record product walkthroughs
Contact: Noor

## D — operations note
Heading: Audio drift troubleshooting
Applies to repository: https://demo-lab.invalid/clip-deck
Audience: maintainers
Procedure: compare sample rate and timestamps; inspect the local log
Retention: keep failed samples until issue closure

## E — reference checklist
Label: Input format checklist
Purpose: inspect codec, resolution and frame rate
Related project: not specified
Code: X7
Long note: Check the codec first, then resolution, then frame rate. Do not infer that support for a filename extension proves support for every codec it may contain.

## F — copied index entry
Name: ClipDeck
Link: https://demo-lab.invalid/clip-deck
Status: prototype proposal
Owner: Lin
