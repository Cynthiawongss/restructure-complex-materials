# Classify and Restructure Complex Materials

[简体中文](README.zh-CN.md) · [Install](docs/INSTALL.md) · [Worked example](examples/handover.en.md) · [Validation](validation/README.md)

**Make someone else's organized-but-confusing materials understandable and usable for the next person.**

![Complex material gains clearer entry points through reclassification. The sieve is a metaphor for structural cleanup, not deletion of material outside the main view.](assets/hero.png)

*Reorganize information while preserving detail and sources.*

An instruction-based Codex skill for handovers, confusing resource libraries and tables with too many fields. Recover the existing logic, separate categories from attributes, establish useful entry points and track where content goes.

## More than shortening a list

| Problem | Response |
|---|---|
| Purpose, technology and status share one category level | Choose a primary axis and keep other dimensions as attributes |
| Too many visible fields | Keep action-critical fields in the main view; preserve details and traceability elsewhere |
| Same name assumed to mean same object | Check sources, identity and versions before merging |
| Conflicting field values | Preserve both values with their sources |
| Unexplained codes and labels | Define them or mark them unknown |
| Long notes removed for brevity | Keep full notes with accessible detail entry points |

## A concrete result

**Input:** Six fictional handover records. Two projects named ClipDeck. Conflicting USD 400/650 budget caps. Aliases for technology fields and distinct owners, contacts and approvers.

| Entry point | Content | Key decision |
|---|---|---|
| Product demos / prototype | Internal ClipDeck in A, B and F | Merge complementary content; preserve budget disagreement |
| Product demos / external case | Separate ClipDeck in C | Different repository: keep separate |
| Maintenance / troubleshooting | Audio drift note D | Link to the explicitly named internal repository |
| General references / input checks | Checklist E | Project unspecified; code X7 unknown |

The main view is concise; procedures, restrictions, role distinctions and source mappings remain accessible. Originals are not deleted.

[Read the raw packet, field dictionary and complete restructuring →](examples/handover.en.md)

## Install

Send this in Codex:

~~~text
Use skill-installer to install the skill from:
https://github.com/cynthiawongss/restructure-complex-materials/tree/main/skills/restructure-complex-materials
~~~

Or get an English or Chinese skill ZIP from the [v0.1.0 release](https://github.com/cynthiawongss/restructure-complex-materials/releases/tag/v0.1.0). Install one language variant only. [Manual setup and updates →](docs/INSTALL.md)

## Use it

> Someone handed me this collection and I cannot understand the fields. Explain the existing structure, then propose entry points for business and maintenance users. Preserve details and sources. Proposal only.

To select the skill explicitly:

~~~text
Use $restructure-complex-materials to inventory and reorganize these
materials around their users' tasks. Retain long notes, field mappings
and conflicts. Do not delete originals.
~~~

Default instructions are English; [complete Chinese instructions](docs/SKILL.zh-CN.md) are also included. Either can handle requests in the other language. Automatic selection depends on task and host; see [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Scope and limits

- For restructuring existing material, not translation, summarization or cosmetic formatting alone.
- No bundled spreadsheet, mind-map or cloud-document editor; actual reading and writing depend on the host.
- State incomplete coverage and do not invent relationships, owners or version order.
- A proposal request remains a proposal. Editing and deleting originals are different permissions.
- Field preservation does not prove visual usability. Report content and display checks separately.

**Version 0.1.0 — early public release.** English and Chinese offline simulated trials are documented. Large real collections, every file format and external-platform writes are not validated. [Validation scope →](validation/README.md)

## Companion skill

Need to find new resources and decide what fits? See [Research and Select Resources for a Specific Purpose](https://github.com/cynthiawongss/purpose-led-resource-research).

[MIT License](LICENSE)
