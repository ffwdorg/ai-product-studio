description: Write the Impact-Driven PRD from the whole session with no new input, in sixteen fixed sections, or a one-page brief if the founder chose B, ending with the builder handoff footer.
trigger: PRD
heading: PRD

Write one markdown document from everything in the session. The founder types nothing new. If the configuration is not locked, ask them to lock it first. If Setup has not run, run it first; the PRD's Output Requirements and AI & Data sections come from its rows 5 and 6 and must not be invented.

Open the reply with "Stage 3 of 3: Plan."

**Where it goes.** If you can create files in this conversation, save the document as a file and do not also paste it into the chat; reply with where it is saved and the note below. If you cannot, write it in the reply.

**First, plan. Then write.** Before any prose, work out the plan silently; do not show it: the product name (verbatim if they gave one; a working name only if not); user stories covering the full journey (first touch, core loop, the moment of value, the return visit), not only the happy path; a V1 a two-person team ships in weeks, with anything resting on an open bet moved to Later or Never and the bet named as the reason (if the core of the product itself rests on an open bet, keep it in V1 and make that bet's test the first item in the Validation Plan, to run before building starts); the technical approach for the chosen job and tier (what the model does per request, what the knowledge base or training data must contain and where it comes from, how outputs stay grounded, where a human reviews before anything reaches an end user, what gets logged to judge quality over time); and the real failure modes of this specific product with a mitigation each. Ground the technical approach strictly in the sources the founder reported: anything marked build or partial is named as still to be created or unconfirmed, never described as if it exists. Then write the document from the plan.

Write for a builder who will never meet the founder. Standards: every requirement is one testable sentence; every AI claim comes with its mechanism (what the model receives, what grounds it, who reviews it, what gets logged); impact metrics name the event, where it fires, and where it is stored. Where the session did not settle a detail a standard asks for, write a short bracketed blank naming what is missing ("in under [time limit]") so the sentence still reads cleanly, and list each blank once in Open Questions as "to decide with your builder." Never invent an event name, a number, a storage location, or a data source to meet a standard. Write for a reader who cannot ask follow-up questions.

Use exactly these headings, verbatim, in this order. Same names for every product. Never combine or rename.

# <product name> PRD
(If there is no real product name, the title is exactly "# PRD". The title appears once.)

## 1. Quick Description
## 2. Problem
## 3. Target User
## 4. Unmet Need
## 5. Intervention
## 6. Impact Metrics
## 7. User Stories
## 8. Functional Requirements
## 9. Output Requirements
## 10. AI & Data
## 11. Decision Trail
## 12. Validation Plan
## 13. Roadmap
## 14. Risks & Mitigations
## 15. Acceptance Criteria
## 16. Open Questions

What goes where. Quick Description is two or three sentences. Problem, Target User, Unmet Need, Intervention each get their own section with the session content polished, never merged. Impact Metrics lists each metric with how V1 instruments it. User Stories numbered. Functional Requirements numbered FR-1, FR-2, grouped by area, one testable sentence each; the seven Setup rows appear as requirements, with any row still marked (guess) written as unconfirmed; a sensitive-domain product also gets one requirement for the human review step. Output Requirements reads "Every <output> must include:" followed by what the founder confirmed. AI & Data covers the approach, what the knowledge base contains and where it comes from, how outputs stay grounded, the human review step, how quality gets evaluated over time, and the personal data the product keeps: what, for how long, who can see it, and how a person corrects or deletes theirs. If the product touches a sensitive domain, AI & Data also states that someone with expertise in that area reviews this plan before anyone builds from it. Decision Trail lists each locked decision in bold with its reason, including options considered and dropped. Validation Plan consolidates all open bets into **one** discovery activity the founder will actually do (a round of user conversations or watching users in context; a second activity only if a bet cannot be answered that way): who, how many, over what timeframe, then a listening guide with one question or moment per open bet and what answer confirms or rules it out, then two or three sentences on doing it well (ask about the last time it happened, never pitch inside a question, past behavior over hypotheticals). Then **After launch**: one line per open bet, "**Rethink if:**" followed by the result from real use of V1 after launch that would mean the bet was wrong (not the pre-build test above, which comes first), with a number and a timeframe where the founder gave one ("fewer than three of the first twenty users come back in week two") and a bracketed blank where they did not, and the impact metric or logged event that would show it. The first version is built to answer its bets, not only to ship. Roadmap is three bold groups, **V1 (build now)**, **Later**, **Never**, each a bulleted list (if the session ruled nothing out, Never reads "Nothing ruled out yet"), followed by a Format line and an AI job line. Risks & Mitigations is a bulleted list, each item "**risk**: mitigation." Acceptance Criteria numbered, written as user moments with numbers in them ("a teacher gets a localized lesson in under two minutes"). Use a number the founder gave; where they gave none, use a bracketed blank. Open Questions as one-line bullets.

The word "spec" does not appear. Full sentences, no filler, no repetition between sections.

End with this footer verbatim: "How to build from this: paste this document into an AI coding tool, and ask it to build the V1 exactly as the roadmap describes, and to ask before deviating. Or hand it to a technical partner. Read it through yourself first. It was drafted by AI from what you described, and a builder will follow whatever it says."

**The note after it,** and nothing else: one line saying to read Decision Trail, Roadmap, and Open Questions first; one line naming any part of V1 that rests on an open bet; then "Before a builder sees it: **A.** Review (a stranger cross-examines it) **B.** Pre-mortem (assume it failed, work backward) **C.** Build plan (the four files a coding agent works from)."

**If the founder chose B,** write a one-page brief instead, as bullets: problem, user, unmet need, intervention, impact metric, AI job and tier, what the user gets, sources with status, the seven Setup rows, open bets with their tests, V1 in one paragraph, later and never. Same footer, same note.
