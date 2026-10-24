# BUILD PLAN

Needs a written PRD in the conversation. If there is none, say so and suggest "PRD."

Before writing, tell the founder in two sentences what this is: the same decisions, cut into the four files spec-driven coding agents read (why, how, what must be true, and the steps in order), in the OpenSpec format, which many builders already use. They do not need to read the files closely; their builder does. Then write them.

**Add nothing.** Every line traces to the PRD. No new features, users, data sources, or numbers. If a file needs something the PRD does not settle, write it under Open Questions in `design.md` rather than deciding it. Anything the PRD marks unconfirmed or still to be created stays unconfirmed here.

Pick a change name: the product name, lowercase, words joined by hyphens, starting with a verb if it reads naturally (`build-tenant-rights-guide`). Then write four files, in this order, each as its own block headed by its path.

`openspec/changes/<change-name>/proposal.md`
- `# Proposal`, then `## Why`: the problem and unmet need in three to five sentences, in the founder's words.
- `## What Changes`: bullets, one per V1 roadmap item. Then one line: "Not in this version:" followed by the Later and Never items.
- `## Capabilities`, then `### New Capabilities`: one bullet per area of Functional Requirements, as `` `capability-name` ``: one sentence. Two to five capabilities. Names lowercase with hyphens.
- `## Impact`: who uses it, and the impact metrics with how V1 records each.

`openspec/changes/<change-name>/design.md`
- `# Design`, then `## Context` (the target user and the setting, from the PRD), `## Decisions` (each Decision Trail entry: the choice, the reason, what was dropped), `## AI and Data` (the AI & Data section, keeping every mechanism: what the model receives, what grounds it, who reviews, what is logged), `## Risks` (from Risks & Mitigations, then every "Rethink if" line from the Validation Plan, verbatim), `## Open Questions` (the PRD's open questions, every open bet from the Validation Plan, and anything you could not settle without deciding).

`openspec/changes/<change-name>/specs/<capability-name>/spec.md`, one file per capability
- `# Spec Delta`, then `## ADDED Requirements`.
- Each requirement is `### Requirement: <short name>`, then one sentence using SHALL, carried from its FR line. Keep the FR number in brackets at the end of the sentence so the builder can trace it.
- Each requirement has at least one `#### Scenario: <short name>` with a `- **WHEN** ...` line and a `- **THEN** ...` line. Build scenarios from the Acceptance Criteria and User Stories first; where the PRD has none for a requirement, write the plainest case and say in Open Questions that the founder has not confirmed it.
- A sensitive-domain product gets a requirement for the human review step, with a scenario.

`openspec/changes/<change-name>/tasks.md`
- `# Tasks`, then numbered groups (`## 1. <area>`), each with checklist lines `- [ ] 1.1 <task>; verify <how a person checks it worked>`.
- Order: anything the PRD says must be created first (the knowledge base, the labeled examples, the data a later step reads), then the core loop, then the human review step, then instrumentation for each impact metric and for each "Rethink if" line, so V1 records what would show the bet was wrong, then the acceptance criteria as a final check group.
- V1 only. A task for a Later or Never item does not appear.

If you can create files in this conversation, create the folder and files and say where they are. If not, the blocks are the files: the founder copies each into a file with that path.

After the four files, write three short lines, plain words:
- If the builder uses OpenSpec, the folder drops into their project as is.
- If not, any AI coding tool can read the files in order: proposal, design, specs, tasks.
- Ask the builder to work one task group at a time and to stop at anything under Open Questions.

End with: "These files were drafted by AI from your PRD. A coding agent will build whatever they say, so read the proposal and the open questions yourself before anyone starts."
