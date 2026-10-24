description: Show all eleven jobs AI can do for a beneficiary as one short plain-language list, mark the three that fit best, and let the founder pick by letter; the tier is worked out silently.
trigger: AI jobs
heading: AI JOBS (stage 2 of 3)

Use the Idea recap. If there is none, ask for two sentences on the problem and the user first.

Here is the fixed taxonomy. Eleven jobs across three tiers. Tiers: **Pre-trained** (ready-to-use generative AI), **Grounded** (a pre-trained model working from a curated knowledge base), **Custom-trained** (needs training data and validation). Never show a tier a job does not have.

- **Assess.** Evaluates user input and gives guidance on it. Pre-trained: feedback on an essay. Grounded: assessment against a curated rubric. Custom-trained: scoring a medical image against a validated set.
- **Navigate.** Guides a user through a complex process with a personalized pathway. Pre-trained: general how-to guidance. Grounded: a benefits navigator working from a curated database.
- **Coach.** Dynamic expert interaction in a specific field. Pre-trained: a general practice partner. Grounded: a legal coach working from a curated body of law.
- **Organize.** Makes large repositories accessible. Grounded only: a searchable knowledge base built from an organization's own documents.
- **Research.** Sorts and analyzes vast information for the user. Pre-trained: general research assistant. Grounded: research over a verified source library.
- **Monitor.** Watches incoming content and raises real-time flags. Grounded: flags from content, such as mentions of self-harm. Custom-trained: flags from patterns in history, such as a case likely to escalate.
- **Translate.** Converts across language, reading level, and accessibility needs. Pre-trained in nearly all cases.
- **Decode.** Interprets previously unknowable information. Custom-trained in nearly all cases: medical imaging, satellite data, sensor signals.
- **Create.** Produces the thing the user needs: a letter, form, plan, or lesson. Pre-trained: general drafting. Grounded: generation from verified sources, such as a lesson localized from an approved curriculum.
- **Predict.** Forecasts an outcome before any warning sign, from patterns in historical data. Custom-trained in nearly all cases: predicting a student will drop out.
- **Connect.** A warm handoff to the next human or service, with follow-through. Pre-trained or Grounded: referral from a curated service directory.

The tiers are yours to work out, not the founder's. Never show tier names or ask the founder to choose one; most founders cannot yet say how their data would feed a model. Pick the tier that fits from what they have said, and carry it to the PRD's AI & Data section.

Do this in one reply of about 150 words:

1. Open with "Stage 2 of 3: Choices."
2. "Question: What should the AI do?" then all eleven jobs, lettered A to K, one line each of at most ten words saying what that job would do in this product, in the founder's vocabulary. Mark the three that fit best "(suggested)." A job that does not fit this product gets "(not a fit)" and no description.
3. If the founder's idea is a chatbot, say once that seven in ten AI-powered nonprofits already run one (71% in the 2026 AI for Humanity Report), so it is the most crowded shape in the sector, and mark which jobs the chatbot was standing in for.
4. End with "Reply with letters, or say it your way."

When they pick, go straight to Setup. Do not comment on the choice. Carry it forward: in the Choices recap, one plain line per job on what it needs to work for this product (the content someone must gather and keep current; or, for a job that needs a trained model, the years of past records and a check before output reaches a person, plus the simpler first version that would collect those records). A job that needs a trained model also adds a data bet to Bets.
