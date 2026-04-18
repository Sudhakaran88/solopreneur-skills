# Installation

Step-by-step install for each platform. Skills are plain Markdown files with YAML frontmatter — any AI coding tool that reads Markdown context can use them, even if the platform has no native skill format.

Pick the section that matches your tool.

---

## Claude Code

Claude Code has first-class skill support. Two install paths.

### Option A: Marketplace (recommended)

```bash
claude plugin marketplace add Sudhakaran88/solopreneur-skills
claude plugin install solopreneur-skills
```

Skills trigger automatically based on the `description` field in each `SKILL.md`. Test with:

```bash
claude
> write a cold email for my SaaS
```

You should see Claude Code invoke the `cold-email` skill.

### Option B: Direct clone

```bash
git clone https://github.com/Sudhakaran88/solopreneur-skills.git ~/.claude/skills/solopreneur-skills
```

Restart Claude Code. Skills will be auto-discovered from `~/.claude/skills/`.

### Option C: Per-project install

Drop skills into a project's `.claude/skills/` folder if you only want them for one repo:

```bash
cd your-project
git clone https://github.com/Sudhakaran88/solopreneur-skills.git .claude/skills/solopreneur-skills
```

### Updating

```bash
cd ~/.claude/skills/solopreneur-skills
git pull
```

---

## Cursor

Cursor doesn't have a native "skills" concept, but it reads `.cursor/rules/` for project-level AI instructions. Use skills as rule files.

### Install as Cursor rules

```bash
cd your-project
mkdir -p .cursor/rules
git clone https://github.com/Sudhakaran88/solopreneur-skills.git .cursor/rules/solopreneur-skills
```

Cursor reads `.mdc` and `.md` files in `.cursor/rules/` as context. The `SKILL.md` frontmatter is ignored by Cursor but harmless.

### Trigger a skill manually

In Cursor chat, reference the skill file directly:

```
@.cursor/rules/solopreneur-skills/skills/cold-email/SKILL.md
Write a cold email for my SaaS CRM targeting dental practices.
```

Cursor will load the skill into context and follow it.

### Global install

For skills across all projects, put them in a `shared-rules` folder and symlink:

```bash
git clone https://github.com/Sudhakaran88/solopreneur-skills.git ~/cursor-rules
ln -s ~/cursor-rules your-project/.cursor/rules/solopreneur-skills
```

---

## OpenAI Codex CLI

Codex CLI reads `AGENTS.md` and supports context injection.

### Install

```bash
git clone https://github.com/Sudhakaran88/solopreneur-skills.git ~/solopreneur-skills
```

### Use

Reference a skill in your Codex prompt:

```bash
codex "using the guidelines in ~/solopreneur-skills/skills/pricing-strategy/SKILL.md, propose a three-tier pricing structure for my project management SaaS"
```

Or append to your project's `AGENTS.md`:

```markdown
## Marketing skills

See `~/solopreneur-skills/skills/` for marketing skills. When the user asks about cold email, read `cold-email/SKILL.md`. When they ask about pricing, read `pricing-strategy/SKILL.md`. [etc.]
```

---

## GitHub Copilot CLI

Copilot CLI does not auto-load external skill files, but accepts context flags.

### Install

```bash
git clone https://github.com/Sudhakaran88/solopreneur-skills.git ~/solopreneur-skills
```

### Use

Pipe a skill into your prompt:

```bash
cat ~/solopreneur-skills/skills/seo-audit/SKILL.md | gh copilot suggest "using these guidelines, audit the SEO for example.com"
```

Or include in a project's `.github/copilot-instructions.md`:

```markdown
When handling marketing tasks, follow the skills at https://github.com/Sudhakaran88/solopreneur-skills.
```

Copilot reads `copilot-instructions.md` automatically when active in a repo.

---

## Gemini CLI

Gemini CLI supports context files via `GEMINI.md` at project or home root.

### Install

```bash
git clone https://github.com/Sudhakaran88/solopreneur-skills.git ~/solopreneur-skills
```

### Use via GEMINI.md

Add to `~/.gemini/GEMINI.md` (global) or `./GEMINI.md` (project):

```markdown
# Marketing skills

For marketing tasks, reference the skills in `~/solopreneur-skills/skills/`. Match the user's request to the most relevant skill's `description` field and follow its instructions.
```

### Use inline

```bash
gemini "follow ~/solopreneur-skills/skills/launch-strategy/SKILL.md and draft a Product Hunt launch plan for my AI note-taking app"
```

---

## Manual install (any tool)

Every skill is a plain `SKILL.md` file. For tools without native AI-context support, paste the content into your prompt.

### Clone

```bash
git clone https://github.com/Sudhakaran88/solopreneur-skills.git
cd solopreneur-skills
```

### Use

1. Open the skill you want: `skills/<skill-name>/SKILL.md`.
2. Copy the content (everything after the `---` frontmatter).
3. Paste into your AI chat before your task prompt.

Example:

```
[pasted content of skills/cold-email/SKILL.md]

---

Now write a cold email for my SaaS that helps agencies automate client reporting. Target: small agency owners. Goal: book a 15-min call.
```

Works with ChatGPT, Claude.ai, Gemini web, Perplexity, or any LLM chat.

---

## Verifying install

Regardless of platform, verify a skill is active by asking your AI:

> What skills do you have loaded for marketing tasks?

If the tool supports skill listing (Claude Code, some Cursor configs), you'll see the full list. If not, test by asking for a specific task a skill covers (like "write a cold email") and see if the output follows that skill's structure — structured sections, cited sources, and a "Common Mistakes" awareness.

---

## Updating

All platforms except the marketplace install use a git clone. To update:

```bash
cd <wherever-you-cloned-it>
git pull
```

For the Claude Code marketplace install:

```bash
claude plugin update solopreneur-skills
```

---

## Troubleshooting

- **Skill isn't triggering in Claude Code.** Check the `description` field in the skill's `SKILL.md` — if the user's phrasing doesn't match any trigger phrases, it won't load. You can invoke manually with `use the <skill-name> skill`.
- **Cursor ignores the skill.** Make sure the file is under `.cursor/rules/` and Cursor indexed the project after you added it. Reopen the project if needed.
- **File too large for the model context.** Skills are kept under 500 lines, but if you load many at once you may hit context limits. Load only the skill you need.

For issues, open one on GitHub: https://github.com/Sudhakaran88/solopreneur-skills/issues
