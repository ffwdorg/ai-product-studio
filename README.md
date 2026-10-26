# Fast Forward Sector Tools

Coaches for people building tech nonprofits. Each one runs inside your own Claude, Gemini, or ChatGPT, uses the same lens Fast Forward uses with the organizations it funds, and never sees what you type.

Built by [Fast Forward](https://ffwd.org), the accelerator for tech nonprofits.

## The tools

<!-- TOOLS:START -->
| Tool | What it does | First command | Download |
|---|---|---|---|
| **AI Product Studio** | Pressure-test a product idea before you build it. Three stages take a non-technical founder from a story to a build-ready PRD in about fifteen minutes, with the bets named along the way. | **Idea** | [ai-product-studio.zip](https://github.com/ffwdorg/ffwd-sector-tools/raw/main/dist/ai-product-studio.zip) |
<!-- TOOLS:END -->

Each tool is a set of prompts. You paste what you have, name a command or say what you want in plain words, and the coach works through it with you. More tools will join this repository as they finish testing.

## Install

Pick the AI you already use. Installing takes about a minute.

### Claude (claude.ai or the desktop app)

1. Download the tool's zip from the table above.
2. On a Free, Pro, or Max plan, first open **Settings**, then **Capabilities**, and turn on **Code execution and file creation**. Skills do not appear until it is on. Team and Enterprise plans have it on already unless an owner turned it off.
3. In Claude, open **Customize**, then **Skills**.
4. Click **+**, then **Create skill**, then **Upload a skill**, and choose the zip.
5. Start a new chat and describe your idea. The coach takes it from there.

Works on Free, Pro, Max, Team, and Enterprise plans. On Team and Enterprise, you can share a tool with colleagues from the **...** menu next to it, and an owner can publish it to the whole organization.

### Claude Code

In a terminal:

```
claude plugin marketplace add ffwdorg/ffwd-sector-tools
claude plugin install ai-product-studio@ffwd-sector-tools
```

Inside a Claude Code session, `/plugin marketplace add` and `/plugin install` do the same. To pick up a new version later, run `claude plugin marketplace update ffwd-sector-tools`, or turn on auto-update for this marketplace under **Marketplaces** in `/plugin`.

### Gemini

Works at gemini.google.com and in the Gemini app on Mac.

1. Download the tool's zip from the table above. No need to unzip it.
2. In Gemini, open **Customize** in the sidebar (under **More** if you don't see it), then **Skills**.
3. Click **Create**, then **Upload**, and choose the zip.
4. Review the skill and click **Create**.
5. Start a new chat and describe your idea, or type `/` to pick the skill.

You need to be 18 or older with **Keep Activity** turned on. To update, upload the new zip again; Gemini cannot pull from GitHub.

### ChatGPT

Works on ChatGPT Business, Enterprise, Healthcare, and Edu. Free, Go, Plus, and Pro plans do not have skills yet.

1. Download the tool's zip from the table above.
2. In ChatGPT, open **Plugins** in the sidebar, then the **Skills** tab.
3. Click **Create**, then **Upload from your computer**, and choose the zip.
4. Start a new chat and describe your idea.

ChatGPT scans every uploaded skill before it is available. If your workspace has uploads turned off, ask an admin.

## Before you start

Tell stories, not records. "A single mother in Fresno" works as well as her name. Leave out names, contact details, case records, government ID numbers, and unreleased financials. The coach will stop and ask you to remove them if it sees them, but it is better not to paste them at all.

What you paste stays in your own Claude, Gemini, or ChatGPT account under that provider's terms. Fast Forward does not receive it.

## What the tools will not do

Pick for you. Invent a statistic, a quote, or a precedent. Write a product plan before you have made the decisions behind it. Name a Fast Forward portfolio organization as an example.

## Staying updated

Claude Code users get new versions by updating the marketplace, or automatically if they turned auto-update on. If you uploaded a zip to Claude, Gemini, or ChatGPT, you have the version you uploaded. The zip in the table above is always the latest; to update, download it again, remove the old skill, and upload the new one. Ask the coach "what version are you" at any time.

## Help us improve

Something fell flat, a prompt gave bad advice, a reference is out of date: email hello@ffwd.org or [open an issue](https://github.com/ffwdorg/ffwd-sector-tools/issues).

## For Fast Forward staff

[MAINTAINING.md](MAINTAINING.md) covers the layout, the edit loop, how to add a tool, and the checklist before one goes public.

## License

[CC BY 4.0](LICENSE). Use, adapt, and share these, with credit to Fast Forward.
