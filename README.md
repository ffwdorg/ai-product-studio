# AI Product Studio

AI Product Studio is a free coach that helps nonprofit builders pressure-test a product idea before they build it. It runs inside your own Claude, ChatGPT, or Gemini. In about fifteen minutes it takes you from a story about one real person to a product requirements document (PRD) a builder can work from.

Built by [Fast Forward](https://ffwd.org), the accelerator for tech nonprofits. It uses the same lens Fast Forward uses with the organizations it funds. Fast Forward never sees what you type.

**[Download ai-product-studio.zip](https://github.com/ffwdorg/ai-product-studio/raw/main/ai-product-studio.zip)**

## How it works

Start a chat and describe your idea. The coach runs three stages, asking one question at a time.

1. **Idea.** One real moment, the root cause, how big the problem is, and what would change.
2. **Choices.** Which jobs AI should do, how people will use it, and the five assumptions the plan rests on.
3. **Plan.** A PRD in Fast Forward's template, with a section for whoever builds it.

You can also name a command at any point.

| Command | What it does |
|---|---|
| **Idea** | Starts the session and shows your problem back for you to fix |
| **AI jobs** | Lists what AI can do for the people you serve and marks the best fits |
| **Setup** | Two plain questions on how people will use it and what it runs on |
| **Assumptions** | Five assumptions, ranked by what would sink the product fastest |
| **PRD** | Writes the PRD from the whole session |
| **Grill** | Challenges your idea one question at a time |
| **Review** | Reads a finished PRD as a stranger and tests its five biggest claims |
| **Build plan** | Turns the PRD into a plan a coding agent can work from |

## Install

Pick the AI you already use. Installing takes about a minute.

### Claude (claude.ai or the desktop app)

1. Download [ai-product-studio.zip](https://github.com/ffwdorg/ai-product-studio/raw/main/ai-product-studio.zip).
2. On a Free, Pro, or Max plan, first open **Settings**, then **Capabilities**, and turn on **Code execution and file creation**. Skills do not appear until it is on. Team and Enterprise plans have it on already unless an owner turned it off.
3. In Claude, open **Customize**, then **Skills**.
4. Click **+**, then **Create skill**, then **Upload a skill**, and choose the zip.
5. Start a new chat and describe your idea. The coach takes it from there.

Works on Free, Pro, Max, Team, and Enterprise plans. On Team and Enterprise, you can share it with colleagues from the **...** menu next to it, and an owner can publish it to the whole organization.

### Claude Code

In a terminal:

```
claude plugin marketplace add ffwdorg/ai-product-studio
claude plugin install ai-product-studio@ai-product-studio
```

Inside a Claude Code session, `/plugin marketplace add` and `/plugin install` do the same. Claude Code also gets **Grill**, **Review**, and **Build plan** as separate skills you can run on their own. To pick up a new version, run `claude plugin update ai-product-studio@ai-product-studio`, or turn on auto-update for this marketplace under **Marketplaces** in `/plugin`.

### Gemini

Works at gemini.google.com and in the Gemini app on Mac.

1. Download [ai-product-studio.zip](https://github.com/ffwdorg/ai-product-studio/raw/main/ai-product-studio.zip). No need to unzip it.
2. In Gemini, open **Customize** in the sidebar (under **More** if you don't see it), then **Skills**.
3. Click **Create**, then **Upload**, and choose the zip.
4. Review the skill and click **Create**.
5. Start a new chat and describe your idea, or type `/` to pick the skill.

You need to be 18 or older with **Keep Activity** turned on. To update, upload the new zip again. Gemini cannot pull from GitHub.

### ChatGPT

Works on ChatGPT Business, Enterprise, Healthcare, and Edu. Free, Go, Plus, and Pro plans do not have skills yet.

1. Download [ai-product-studio.zip](https://github.com/ffwdorg/ai-product-studio/raw/main/ai-product-studio.zip).
2. In ChatGPT, open **Plugins** in the sidebar, then the **Skills** tab.
3. Click **Create**, then **Upload from your computer**, and choose the zip.
4. Start a new chat and describe your idea.

ChatGPT scans every uploaded skill before it is available. If your workspace has uploads turned off, ask an admin.

## Before you start

Tell stories, not records. "A single mother in Fresno" works as well as her name. Leave out names, contact details, case records, government ID numbers, and unreleased financials. The coach will stop and ask you to remove them if it sees them, but it is better not to paste them at all.

What you paste stays in your own Claude, ChatGPT, or Gemini account under that provider's terms. Fast Forward does not receive it.

## What it will not do

Pick for you. Invent a statistic, a quote, or a precedent. Write a product plan before you have made the decisions behind it. Name a Fast Forward portfolio organization as an example.

## Staying updated

If you uploaded the zip, you have the version you uploaded. The download link above is always the latest. To update, download it again, remove the old skill, and upload the new one. Claude Code users update with the command above. Ask the coach "what version are you" at any time.

## Help us improve

Something fell flat, a prompt gave bad advice, or a reference is out of date? Email hello@ffwd.org or [open an issue](https://github.com/ffwdorg/ai-product-studio/issues).

## License

[CC BY 4.0](LICENSE). Use it, adapt it, and share it, with credit to Fast Forward.
