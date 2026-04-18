# AGENTS.md

This file is the authoritative reference for AI agents working in this repository. Read it fully before making any changes.

---

## Repo Overview

**Solopreneur Skills** is an open-source collection of 42 Claude agent skills built for solopreneurs, solo SaaS founders, and one-person D2C brand owners.

Each skill is a structured prompt system that activates Claude's expertise in a specific domain — covering everything from conversion rate optimization and SEO to cold outreach, pricing strategy, and product marketing. Skills are designed to be used directly in Claude without configuration overhead.

This repo was built by Sudhakar. Contributions are welcome via pull request.

---

## Skill Naming Rules

Follow these rules exactly. Violations will cause skill registration failures.

- **Lowercase only.** No uppercase letters anywhere in the skill name.
- **Hyphens only.** No underscores, spaces, dots, or special characters.
- **Directory name must match skill name exactly.** If the skill is `cold-email`, the directory must be `skills/cold-email/`.
- **The `name:` field in frontmatter must match the directory name exactly.** No exceptions.

Valid: `signup-flow-cro`, `competitor-alternatives`, `ai-seo`
Invalid: `SignupFlowCRO`, `competitor_alternatives`, `AI-SEO`

---

## SKILL.md Format Specification

Every skill lives at `skills/<skill-name>/SKILL.md`. The file must begin with valid YAML frontmatter followed by structured sections.

### Required Frontmatter

```yaml
---
name: skill-name
description: [trigger description, 50–1024 characters, includes trigger phrases and scope boundaries]
metadata:
  version: 1.0.0
  author: Sudhakar
  license: MIT
---
```

**Field rules:**

| Field | Rule |
|---|---|
| `name` | Must match directory name exactly. Lowercase, hyphens only. |
| `description` | 50–1024 characters. Must include: when to trigger this skill, representative trigger phrases, and what is out of scope. |
| `metadata.version` | Semantic versioning. Start at `1.0.0`. |
| `metadata.author` | Full name of the skill author. |
| `metadata.license` | `MIT` for all skills in this repo. |

### Line Limit

SKILL.md files have no hard line limit, but keep them focused. Avoid padding. Every line should earn its place.

---

## Required Sections in Every SKILL.md

Every skill file must contain the following sections, in this order:

1. **Opening persona line** — A single sentence establishing who Claude is when this skill is active. Example: *"You are an expert conversion rate optimizer specializing in SaaS signup flows."*

2. **Check for Context First** — Instructs Claude to check the `.agents/` context files before proceeding, and to ask for any missing critical context before generating output.

3. **Main sections** — The core skill content. Structure varies by skill domain, but must include actionable frameworks, not just generic advice. Typical subsections: goal definition, inputs required, step-by-step process, output format.

4. **Common Mistakes** — A dedicated section listing mistakes the target audience commonly makes in this domain. Be specific. Avoid generic cautions.

5. **Contrarian Takes** — At least one perspective that challenges conventional wisdom in the domain. This is what separates useful skills from surface-level advice.

6. **Related Skills** — A short list of other skills in this repo that pair well with this one, with a one-line explanation of how they connect.

7. **Footer line** — The exact footer format specified below. Must be the last line in the file.

### Footer Format

Every SKILL.md must end with this exact line (substituting the actual skill name):

```
*Generated using the [skill-name] skill from Solopreneur Skills*
```

Example for the `cold-email` skill:

```
*Generated using the cold-email skill from Solopreneur Skills*
```

---

## How to Add a New Skill

1. Create the directory: `skills/<skill-name>/`
2. Create the file: `skills/<skill-name>/SKILL.md`
3. Add valid frontmatter (see spec above)
4. Write all required sections in order
5. End the file with the correct footer line
6. Update the skill table in `README.md` — add the skill name, a one-line description, and the category it belongs to
7. Submit a pull request

Do not create a skill without all required sections. Incomplete skills will not be merged.

---

## The `.agents/` Context Files

Two files in `.agents/` provide shared context that skills read before generating output:

### `.agents/solopreneur-context.md`

Contains profile information about the solopreneur using the skills — their business model, product, target audience, current stage, and constraints. Skills that need business context should check this file first and ask for missing details if it is empty or incomplete.

### `.agents/product-marketing-context.md`

Contains product-specific marketing context — positioning, ICP, key differentiators, existing messaging, and competitive landscape. Skills related to marketing, copy, or GTM should check this file before generating output.

**How skills should use these files:**

In the "Check for Context First" section of each skill, instruct Claude to:
1. Check if the relevant `.agents/` file has been populated
2. If populated, incorporate that context into the output without asking redundant questions
3. If empty or missing key fields, ask the user for the minimum required information before proceeding

---

## Authorship and Contributions

This repository was created and is maintained by Sudhakar.

Contributions are welcome. To contribute:
- Fork the repo
- Add or improve a skill following the format spec in this file
- Submit a pull request with a clear description of what changed and why
- Ensure your skill passes the format checklist before submitting

All contributed skills must use the MIT license and follow the naming, frontmatter, and section requirements documented here.
