description: Re-read the finished PRD as a stranger with no memory of the session and cross-examine its five most load-bearing claims before a builder acts on it.
trigger: Review
heading: REVIEW
input: a pasted PRD
skill: review

Needs a written PRD in the conversation. If there is none, say so and suggest "PRD."

Read the document as a technical partner who was not in the room: someone who will build exactly what it says and cannot ask the founder anything. Your job is to find the five places where the document asserts something the session never established.

Look for:

- A requirement that says "the system will" where the session only said "we hope users will."
- A data source described as existing that Setup marked build or partial.
- An AI capability with no mechanism: nothing about what the model receives, what grounds it, who reviews it, what gets logged.
- An impact metric that is reach dressed as outcome.
- An acceptance criterion no stranger could test.
- A user story for a person the founder never described.
- Anything about the people served that reads as a label rather than a person.

For each of the five, quote the line, say what the session actually supports, and name the one question the founder would have to answer for the line to stand. Rank by how much of the first version rests on it.

Then one paragraph on what holds: the parts of the document a builder can act on today without a follow-up question.

Do not rewrite the document. The founder edits; you point. End by reminding them of the footer's rule: read it through yourself first, a builder will follow whatever it says.