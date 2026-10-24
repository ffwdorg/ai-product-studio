# AI Product Studio evals

Run from the repo root after a build: `claude plugin eval plugins/ai-product-studio`. Each case runs three times with the coach and three times without; the report shows both scores and the difference.

The idea, the pantry, and every person in these cases are fictional. The name, phone number, and case number in `records-out` are invented for testing and must never be quoted as real.

Cases: `idea-one-message` (opening shows the reminder line, marks the stage, asks only what is missing in one message, no menu), `plain-language-pre-mortem` (a plain request routes to Pre-mortem and respects the locked-configuration gate), `prd-before-lock` (never writes the PRD before decisions exist), `records-out` (asks for a beneficiary's name, phone, and case number to be removed and does not repeat them).
