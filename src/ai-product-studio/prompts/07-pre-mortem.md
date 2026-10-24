description: Assume the first version shipped and failed six months in, work backward to why, and sort the risks into real, overblown, and undiscussed so only the real ones get a plan.
trigger: Pre-mortem
heading: PRE-MORTEM
input: a pasted PRD, brief, or locked configuration
skill: pre-mortem

Needs a locked configuration. If it is not locked, run Setup and Bets first. This step feeds the PRD's Risks & Mitigations, so run it before "PRD" when there is time.

Set the scene for the founder in two sentences: the first version shipped, six months passed, and it failed. Not a crash; the quiet kind that tech nonprofits actually have. The people it was built for used it once and did not come back. The gatekeeper never let it in. The funder liked the pitch and did not renew. The data that was supposed to arrive did not. The volunteer engineer left.

Bring the 2026 AI for Humanity Report's findings to this, from `references/ai4h-2026-key-findings.md`: nine in ten AI-powered nonprofits have a plan to scale and a quarter have the resources; rising AI costs are the top external threat; monitoring, testing, and iteration are where the money goes; a champion who drives the vision is the top enabler, so what happens when that person leaves.

Now work backward. List every reason it could have failed, drawn from this founder's own session: the open bets, the sources marked build or partial, the user who is not the buyer, the format they chose, the outcome metric they picked. Then sort every reason into one of three:

- **Real risks.** You can point at something in the session that makes this likely.
- **Overblown.** Worth naming because someone will raise it, but the evidence in the session says it is unlikely or small. Say why, so the founder can answer it when a funder asks.
- **Undiscussed.** You are not sure it is a problem, and nothing in the session touched it. These are the ones a proximate founder often skips because they feel obvious from the inside.

For every real risk, three lines: what breaks, the cheapest thing the founder can do in the next month to find out whether it is real (a conversation, a count, a test with five users; never a research project), and whether it blocks the first version, follows in the first month after, or is just watched.

Sort by what would sink the product fastest if true. Keep it to the top three real risks with plans; list the rest. No hedging language. A pre-mortem that says "could potentially" about everything protects nobody.

Then suggest "PRD."