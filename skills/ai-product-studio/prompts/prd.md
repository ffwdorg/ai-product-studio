# PRD

Write one markdown document from everything in the session. The founder types nothing new. If the configuration is not locked, ask them to lock it first. If Setup has not run, run it first; the Features List and AI & Data come from its rows and must not be invented.

Open the reply with "Stage 3 of 3: Plan."

**Where it goes.** If you can create files in this conversation, save the document as a file and do not also paste it into the chat; reply with where it is saved and the note below. If you cannot, write it in the reply.

**First, plan. Then write.** Before any prose, work out the plan silently; do not show it: the product name (verbatim if they gave one; a working name only if not); the user flow across the full journey (first touch, the core loop, the moment of value, the return visit), not only the happy path; a first version a two-person team ships in weeks, with any feature resting on an untested assumption marked Later or Never and the assumption named as the reason (if the core of the product itself rests on one, keep it and make that assumption's experiment the first thing to run, before building starts); the technical approach for the chosen job and tier (what the model does per request, what the knowledge base or training data must contain and where it comes from, how outputs stay grounded, where a human reviews before anything reaches a beneficiary, what gets logged to judge quality over time); and the real failure modes of this specific product with a mitigation each. Ground the technical approach strictly in the sources the founder reported: anything marked build or partial is named as still to be created or unconfirmed, never described as if it exists. Then write the document from the plan.

Write for a builder who will never meet the founder. Every feature is one testable sentence. Every AI claim comes with its mechanism (what the model receives, what grounds it, who reviews it, what gets logged). Every metric names the event, where it fires, and where it is stored. Where the session did not settle a detail, write a short bracketed blank naming what is missing ("in under [time limit]") so the sentence still reads cleanly, and list each blank once in Open Questions as "to decide with your builder." Never invent an event name, a number, a storage location, a data source, an owner, or a date.

**Length.** At most 2,000 words, everything included. Say each thing once; when a later section needs it, refer back instead of repeating it.

Use exactly these headings, verbatim, in this order. They follow the FFWD PRD template so the founder can paste each section into it. Never combine or rename.

# <product name> PRD
(If there is no real product name, the title is exactly "# PRD". The title appears once.)

## Background
## Problem Statement
## Goals
## Personas
## Solution Design
### Mock Up
### User Flow
### Features List
## Product Metrics
## Launch Plan
## For your builder
### AI & Data
### Decisions
### Assumptions to Test
### Risks & Mitigations
### Acceptance Criteria
### Open Questions

What goes where.

- **Background.** Two or three sentences: why the founder started this, why now, and how it serves their mission.
- **Problem Statement.** Who it affects, in what way, the evidence it is big (the number and its source, or "[size of the problem]"), and the root cause it addresses. One short paragraph.
- **Goals.** The outcome metrics: what changes for the beneficiary, and how V1 would show it.
- **Personas.** A table with columns Persona type & name | Background | Needs | Pain Points. One row each for Beneficiary, Payer, and Users (skip Users when the beneficiary is the user). Name each with a plausible first name, labeled "(example)". Content comes only from the session; a payer the founder never confirmed stays "(guess)".
- **Solution Design.** Two or three sentences on how the solution works and which AI job it does.
- **Mock Up.** Exactly: "[Add your latest sketch or low-fi prototype here.]" The Studio makes no mockups.
- **User Flow.** Numbered steps from first touch to the return visit. Each step says what the person does, then what the product does.
- **Features List.** A table with columns ID | Component | Feature | Description | Status | Priority | Actor. ID is F-1, F-2, and so on. Component groups features by area. Description is one testable sentence. Status is "Ready" when an engineer could start from the description, otherwise "Needs design." Priority is **V1**, **Later**, or **Never**; a feature that is Later or Never because of an untested assumption names it in the Description. Actor is Beneficiary, User, Partner, or Admin. The seven Setup rows each appear as a feature; a row still marked (guess) says "unconfirmed" in its Description. A sensitive-domain product also gets one feature for the human review step. If the session ruled nothing out, add no Never rows.
- **Product Metrics.** A table with columns Adoption | Engagement | Retention | Reliability, one row: for each, the metric, the event it counts, and where it is stored, or a bracketed blank. Reliability covers whether the product works when needed, including how often the human review step catches an error.
- **Launch Plan.** Two lines only: who hears about it first and through which channel (from Setup), and who pays for running it (from Personas). Then: "Roll-out steps, communication brief, and revenue model: [to plan with your team]."
- **For your builder.** One line under the heading: "The sections below are for whoever builds this. They carry the reasoning the template does not have room for."
- **AI & Data.** The approach, what the knowledge base contains and where it comes from, how outputs stay grounded, the human review step, how quality gets checked over time, and the personal data the product keeps: what, for how long, who can see it, and how a person corrects or deletes theirs. A sensitive-domain product also states that someone with expertise in that area reviews this plan before anyone builds from it.
- **Decisions.** Each locked decision in bold with its reason, including options considered and dropped.
- **Assumptions to Test.** First, one discovery activity the founder will actually do before building (a round of conversations or watching people in context; a second activity only if an assumption cannot be answered that way): who, how many, over what timeframe, then one question or moment per untested assumption and what answer confirms, modifies, or rules it out. Then **After launch**: one line per untested assumption, "**Rethink if:**" followed by the result from real use of V1 that would mean it was wrong, with a number and timeframe where the founder gave one and a bracketed blank where they did not, and the metric or logged event that would show it.
- **Risks & Mitigations.** Bullets, each "**risk**: mitigation."
- **Acceptance Criteria.** Numbered, written as user moments with numbers in them ("a teacher gets a localized lesson in under two minutes"). A number the founder gave, or a bracketed blank.
- **Open Questions.** One-line bullets, including every bracketed blank.

The word "spec" does not appear.

End with this footer verbatim: "How to build from this: paste this document into an AI coding tool, and ask it to build the V1 features exactly as the Features List describes, and to ask before deviating. Or hand it to a technical partner. Read it through yourself first. It was drafted by AI from what you described, and a builder will follow whatever it says."

**The note after it,** and nothing else: one line saying to read Features List, Decisions, and Open Questions first; one line naming any V1 feature that rests on an untested assumption; then "Before a builder sees it: **A.** Review (a stranger cross-examines it) **B.** Build plan (the four files a coding agent works from)."

**If the founder chose B,** write a one-page brief instead, as bullets: background, problem statement with root cause, beneficiary and payer, needs, solution and AI job, what the user gets, sources with status, the seven Setup rows, assumptions to test with their experiments, V1 in one paragraph, later and never. Same footer, same note.
