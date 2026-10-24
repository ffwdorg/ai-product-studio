#!/usr/bin/env python3
"""Build the Fast Forward Sector Tools from their sources.

Source, under src/<tool>/ (edit these):
  tool.json            name, title, description, version, status, references
  persona.md           who the coach is, how it behaves, and the rules for this tool
  prompts/NN-slug.md   one prompt per file. Header lines, then a blank line, then the body:
                         description: one sentence (goes in the router table)
                         trigger: how a user asks for it, e.g. "Hear my pitch"
                         heading: optional, shown as the prompt's title
                         internal: yes   (optional) staff-only; never published
                         skill: <name>   (optional) also publish this prompt as its own skill,
                                         for a command that can run cold from pasted material
                         input: what it runs cold from, e.g. "a pasted PRD" (required with skill:)
  knowledge/*.md       reference files specific to this tool
src/shared/            files more than one tool reads (the lens, the playbooks)

persona.md may wrap text in <!-- router-only --> ... <!-- /router-only -->: orientation and step
routing that belongs in the main skill only. Standalone skills get the persona and rules without it.
tool.json may set "compatibility": one line on where the skill runs, stamped into every SKILL.md.

Generated (never edit by hand; the next build overwrites them):
  plugins/<tool>/skills/<tool>/SKILL.md        the skill: persona, rules, router, reference list
  plugins/<tool>/skills/<tool>/prompts/*.md    one file per prompt, read on demand
  plugins/<tool>/skills/<tool>/references/*.md the knowledge files, copied in
  plugins/<tool>/skills/<name>/SKILL.md        one per `skill:` prompt: persona, rules, the prompt inline
                                               (Claude Code plugin only; the zip carries the main skill)
  plugins/<tool>/.claude-plugin/plugin.json    Claude Code plugin manifest
  dist/<tool>.zip                              the skill folder, for upload to Claude or Gemini
  .claude-plugin/marketplace.json              one marketplace listing every public tool
  README.md tools table                        between the TOOLS markers

Only tools with "status": "public" in tool.json are published. Run:

  python3 build.py            # all tools
  python3 build.py ai-product-studio
"""
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
PLUGINS = ROOT / "plugins"
DIST = ROOT / "dist"
REPO = "ffwdorg/ffwd-sector-tools"
MARKETPLACE = "ffwd-sector-tools"
OWNER = {"name": "Fast Forward", "url": "https://ffwd.org"}
LICENSE = "CC-BY-4.0"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def fail(msg):
    sys.exit(f"build.py: {msg}")



# Each tool is sealed: it may read only its own knowledge/ and what tool.json lists from src/shared.
# Signature words tell the tools apart; a tool that starts using another tool's words is drifting.
SIGNATURES = {
    "pitch-coach": r"\b(pitch(es|ed|ing)?|elevator|stranger|pitch camp|ninety seconds)\b",
    "ai-product-studio": r"\b(founder|PRD|AI job|studio|intake|pre-mortem|configuration)\b",
    "ai-grant-writing-coach": r"\b(proposal|funder|grant|RFP|program officer|reviewer)\b",
}
TITLES = {"pitch-coach": "Pitch Coach", "ai-product-studio": "AI Product Studio",
          "ai-grant-writing-coach": "AI Grant Writing Coach"}


def check_drift(tool_dir, info, ref_names):
    """Hard errors stop the build; warnings print. Keeps one tool's edits from leaking into another."""
    name = info["name"]
    errors, warns = [], []
    files = [tool_dir / "persona.md"] + sorted((tool_dir / "prompts").glob("*.md"))
    for f in files:
        text = f.read_text(encoding="utf-8")
        # a. every references/ path must exist for THIS tool
        for ref in set(re.findall(r"`references/([^`]+)`", text)):
            if ref not in ref_names:
                errors.append(f"{f.relative_to(tool_dir)} cites references/{ref}, which this tool does not ship")
        # b. another tool's title inside a prompt (the persona may route, prompts may not)
        for other, title in TITLES.items():
            if other != name and title in text and f.name != "persona.md":
                errors.append(f"{f.relative_to(tool_dir)} names {title}")
        # c. another tool's signature vocabulary, beyond a stray word
        for other, pat in SIGNATURES.items():
            if other == name:
                continue
            hits = len(re.findall(pat, text, re.I))
            if hits >= 4:
                warns.append(f"{f.relative_to(tool_dir)} uses {other} vocabulary {hits} times")
    for w in warns:
        print(f"  warning: {name}: {w}")
    if errors:
        fail(f"{name} drift check failed:\n  " + "\n  ".join(errors))


def parse_prompt(path):
    text = path.read_text(encoding="utf-8")
    head, _, body = text.partition("\n\n")
    meta = {}
    for line in head.splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    for k in ("description", "trigger"):
        if k not in meta:
            fail(f"{path}: missing '{k}:' header line")
    slug = re.sub(r"^\d+-", "", path.stem)
    meta["slug"] = slug
    meta["internal"] = meta.get("internal", "").lower() in ("yes", "true")
    meta["body"] = body.strip()
    return meta


def frontmatter(info, skill_name, desc):
    desc = desc.replace('"', "'")
    if len(desc) > 1024:
        desc = desc[:1020].rsplit(" ", 1)[0] + "..."
    meta = {
        "author": OWNER["name"],
        "version": info["version"],
        "homepage": info.get("homepage", OWNER["url"]),
        "generatedBy": f"build.py from src/{info['name']}; edit the source, not this file",
    }
    lines = ["---", f"name: {skill_name}", f'description: "{desc}"', f"license: {LICENSE}"]
    if info.get("compatibility"):
        lines.append(f'compatibility: "{info["compatibility"]}"')
    lines.append("metadata:")
    lines += [f"  {k}: \"{v}\"" for k, v in meta.items()]
    lines.append("---")
    return "\n".join(lines) + "\n"


def persona_for(persona, router):
    """The router skill keeps the <!-- router-only --> block; a standalone skill drops it."""
    block = re.compile(r"<!-- router-only -->\n?(.*?)\n?<!-- /router-only -->\n*", re.S)
    if router:
        return block.sub(lambda m: m.group(1) + "\n\n", persona).strip()
    return block.sub("", persona).strip()


def references_section(ref_lines, info):
    return (
        f"## Reference files\n\n"
        f"Read the files in `references/` before coaching. Use their vocabulary and facts; do not recite them.\n\n"
        + "\n".join(ref_lines)
        + f"\n\n## Version\n\n{info['title']} {info['version']}, by Fast Forward. "
        f"If the user asks what version this is or whether there is a newer one, say so and point to "
        f"https://github.com/{REPO}/releases.\n"
    )


def build_standalone(info, p, persona, refs, ref_lines):
    """A prompt with a `skill:` header also ships as its own skill: the persona and rules, that one prompt
    inline, and the same references. It must run cold, from pasted material, with no earlier step in the chat."""
    sname = p["skill"]
    if not NAME_RE.match(sname):
        fail(f"{info['name']}: skill name '{sname}' must be lowercase-hyphenated")
    if not p.get("input"):
        fail(f"{info['name']}: prompt '{p['slug']}' has skill: but no input: header")
    sdir = PLUGINS / info["name"] / "skills" / sname
    (sdir / "references").mkdir(parents=True)
    for r in refs:
        shutil.copy(r, sdir / "references" / r.name)
    desc = (f'{p["description"]} Runs on its own from {p["input"]}. Part of {info["title"]} by Fast Forward. '
            f'Use when the user says "{p["trigger"]}" or asks for this in their own words.')
    heading = p.get("heading") or p["trigger"]
    body = (
        f"{persona_for(persona, router=False)}\n\n---\n\n"
        f"## This command\n\n"
        f"This is the **{p['trigger']}** command from {info['title']}, packaged to run on its own. "
        f"It works from {p['input']}, or from what is already in this conversation. "
        f"If there is nothing to work from, ask for it in one line before starting. "
        f"Where the instructions below point to another command, say in one line that it is part of the full {info['title']}.\n\n"
        f"# {heading}\n\n{p['body']}\n\n"
        + references_section(ref_lines, info)
    )
    (sdir / "SKILL.md").write_text(frontmatter(info, sname, desc) + "\n" + body, encoding="utf-8")


def router_table(prompts):
    rows = ["| Command | What it does | Open |", "|---|---|---|"]
    for p in prompts:
        rows.append(f'| **{p["trigger"]}** | {p["description"]} | `prompts/{p["slug"]}.md` |')
    return "\n".join(rows)


def build_tool(tool_dir):
    info = json.loads((tool_dir / "tool.json").read_text(encoding="utf-8"))
    name = info["name"]
    if not NAME_RE.match(name) or name != tool_dir.name:
        fail(f"{tool_dir}: tool.json name must be lowercase-hyphenated and match the folder")
    if info.get("status") != "public":
        print(f"  {name}: status {info.get('status', 'unset')}, not published")
        return None

    persona = (tool_dir / "persona.md").read_text(encoding="utf-8").strip()
    prompts = [parse_prompt(p) for p in sorted((tool_dir / "prompts").glob("*.md"))]
    public = [p for p in prompts if not p["internal"]]
    if not public:
        fail(f"{tool_dir}: no public prompts")

    # reference files: the tool's own knowledge/ plus whatever tool.json lists from src/shared
    refs = sorted((tool_dir / "knowledge").glob("*.md")) if (tool_dir / "knowledge").is_dir() else []
    for rel in info.get("references", []):
        p = SRC / rel
        if not p.is_file():
            fail(f"{tool_dir}: reference not found: {rel}")
        refs.append(p)

    check_drift(tool_dir, info, {r.name for r in refs})

    skill = PLUGINS / name / "skills" / name
    if (PLUGINS / name).exists():
        shutil.rmtree(PLUGINS / name)
    (skill / "prompts").mkdir(parents=True)
    (skill / "references").mkdir()

    for p in public:
        heading = p.get("heading") or p["trigger"]
        (skill / "prompts" / f"{p['slug']}.md").write_text(f"# {heading}\n\n{p['body']}\n", encoding="utf-8")
    for r in refs:
        shutil.copy(r, skill / "references" / r.name)

    ref_lines = []
    for r in refs:
        first = next((l.strip() for l in r.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")), "")
        first = re.split(r"(?<=[.!?])\s", first)[0]
        ref_lines.append(f"- `references/{r.name}`: {first[:200]}")

    body = (
        f"{persona_for(persona, router=True)}\n\n---\n\n"
        f"## Prompts\n\n"
        f"Each command is a file in `prompts/`. When the user names one, open that file and follow it exactly. "
        f"If they paste material and name a command in the same message, run it; the name is the request. "
        f"If they describe the job in their own words, match it to the closest command. "
        f"If they have not named one, orient them as the persona describes.\n\n"
        f"{router_table(public)}\n\n"
        + references_section(ref_lines, info)
    )
    triggers = ", ".join(p["trigger"] for p in public)
    desc = f'{info["description"]} Commands: {triggers}. Also use when the user describes any of those jobs in their own words.'
    (skill / "SKILL.md").write_text(frontmatter(info, name, desc) + "\n" + body, encoding="utf-8")

    # the router keeps every prompt; a prompt marked `skill:` is also published as its own skill
    standalone = [p for p in public if p.get("skill")]
    for p in standalone:
        build_standalone(info, p, persona, refs, ref_lines)

    manifest = {
        "name": name,
        "description": info["description"],
        "version": info["version"],
        "author": OWNER,
        "homepage": info.get("homepage", OWNER["url"]),
        "repository": f"https://github.com/{REPO}",
        "license": LICENSE,
    }
    (PLUGINS / name / ".claude-plugin").mkdir()
    (PLUGINS / name / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    # eval suite travels with the plugin (results/ is gitignored)
    if (tool_dir / "evals").is_dir():
        shutil.copytree(tool_dir / "evals", PLUGINS / name / "evals", ignore=shutil.ignore_patterns("results"))

    DIST.mkdir(exist_ok=True)
    zpath = DIST / f"{name}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill.rglob("*")):
            if f.is_file():
                z.write(f, f"{name}/{f.relative_to(skill)}")

    n_prompts = len(public)
    print(f"  {name} {info['version']}: {n_prompts} prompts, {len(refs)} references, {zpath.stat().st_size // 1024} KB zip")
    info["_prompts"] = public
    return info


def write_marketplace(tools):
    mp = {
        "name": MARKETPLACE,
        "owner": OWNER,
        "metadata": {"description": "Fast Forward Sector Tools: coaches for tech nonprofit builders."},
        "plugins": [
            {
                "name": t["name"],
                "source": f"./plugins/{t['name']}",
                "description": t["description"],
            }
            for t in tools
        ],
    }
    (ROOT / ".claude-plugin").mkdir(exist_ok=True)
    (ROOT / ".claude-plugin" / "marketplace.json").write_text(json.dumps(mp, indent=2) + "\n", encoding="utf-8")


def write_readme_table(tools):
    readme = ROOT / "README.md"
    if not readme.exists():
        return
    text = readme.read_text(encoding="utf-8")
    start, end = "<!-- TOOLS:START -->", "<!-- TOOLS:END -->"
    if start not in text or end not in text:
        return
    rows = ["| Tool | What it does | First command | Download |", "|---|---|---|---|"]
    for t in tools:
        first = t["_prompts"][0]["trigger"]
        rows.append(f'| **{t["title"]}** | {t["description"].split(". ", 1)[1] if ". " in t["description"] else t["description"]} | **{first}** | [{t["name"]}.zip](https://github.com/{REPO}/raw/main/dist/{t["name"]}.zip) |')
    table = "\n".join(rows)
    new = text[: text.index(start) + len(start)] + "\n" + table + "\n" + text[text.index(end):]
    readme.write_text(new, encoding="utf-8")


def main(argv):
    wanted = set(argv)
    tool_dirs = [d for d in sorted(SRC.iterdir()) if d.is_dir() and d.name != "shared" and (d / "tool.json").exists()]
    if wanted:
        tool_dirs = [d for d in tool_dirs if d.name in wanted]
    if not tool_dirs:
        fail("no tools found")
    print("Building:")
    tools = [t for t in (build_tool(d) for d in tool_dirs) if t]
    if not wanted:  # full build regenerates the shared files
        write_marketplace(tools)
        write_readme_table(tools)
    print("Done.")


if __name__ == "__main__":
    main(sys.argv[1:])
