# Contributing to Solopreneur Skills

Thanks for considering a contribution. This repo is a collection of 42 marketing and growth skills built for solopreneurs and one-person teams. The goal is sharp, opinionated, practitioner-grade skills — not generic advice.

## How to Contribute

There are three ways to help:

1. **Add a new skill** — fill a gap that solopreneurs actually hit.
2. **Improve an existing skill** — sharpen the writing, update stale benchmarks, add a contrarian take, fix a broken cross-reference.
3. **File an issue** — flag a bug, suggest a skill, or ask a question.

## Before You Start

- Skim `README.md` and the `skills/` directory so you don't propose something that already exists.
- For a brand-new skill, open an issue with the **"New skill proposal"** template first so we can align on scope before you write 400 lines.
- If your idea overlaps with an existing skill, prefer editing that skill over creating a near-duplicate. Cross-linked, focused skills beat sprawling ones.

## Quality Bar

What makes a skill worth merging:

- **Under 500 lines** per `SKILL.md`. If it's longer, you're probably hedging.
- **Opinionated.** Takes a stance. "It depends" is not a skill.
- **Researched.** Cite Reddit and forums for practitioner takes (name the subreddit). Cite named experts for frameworks (CXL, Demand Curve, Lenny's Newsletter, SparkToro, First Round, Common Good, YC, etc.). Cite benchmarks with source and year.
- **Has a "Common Mistakes" section** sourced from real practitioners.
- **Has a "Contrarian Takes" section** — things that push back on conventional advice.
- **Written for solopreneurs**, not VP-of-Marketing-at-a-Series-B.
- **Specific beats generic.** Real numbers, named frameworks, actual examples.

## Required SKILL.md Format

Every skill starts with this frontmatter:

```yaml
---
name: skill-name
description: [Trigger description, 50-1024 chars. Include "when the user wants" + trigger phrases + scope boundaries + cross-references to related skills.]
metadata:
  version: 1.0.0
  author: Your Name
  license: MIT
---
```

First line of the body:

```
You are a [expert role] helping solopreneurs [accomplish X] — [differentiating principle].
```

Required body sections, in order:

1. **When to use**
2. **Check for Context First** — read `.agents/solopreneur-context.md` or `.agents/product-marketing-context.md` if present
3. **Core framework / mindset**
4. **Main content sections** (specific to the skill)
5. **Common Mistakes (What Doesn't Work)** — sourced from Reddit/forums
6. **Contrarian Takes** — where you disagree with the mainstream playbook
7. **Quick wins**
8. **Related Skills** — cross-reference sibling skills

Footer line:

```
*Generated using the [skill-name] skill from Solopreneur Skills*
```

## How to Add a New Skill

1. Fork the repo.
2. Create `skills/<skill-name>/SKILL.md`.
3. Follow the format above.
4. Update the skill table in `README.md`.
5. Add the skill to the `skills` array in `.claude-plugin/marketplace.json`.
6. Add a changelog entry to `VERSIONS.md`.
7. Open a PR using the **"New skill"** template.

## How to Improve an Existing Skill

- **Small fixes** (typos, a better example, a broken link) — direct PR is fine.
- **Major rewrites** — open an issue first so we can agree on direction before you burn a weekend.
- **Bump `version:`** in the frontmatter on any meaningful change.

## Research Standards

- **Reddit voice counts.** Quote practitioners, cite the subreddit (`r/marketing`, `r/SaaS`, `r/Entrepreneur`, etc.).
- **Named experts only.** CXL, Demand Curve, Lenny's, SparkToro, First Round, Common Good, YC, and similar. "Industry experts say" is not a source.
- **Benchmarks need a source and a year.** A 2019 CTR number is a lie in 2026.
- **No AI slop.** If you drafted with AI, rewrite every sentence in your own voice. Editors can smell it.
- **Banned phrases:** "delve", "leverage", "in today's landscape", "unlock the power of", "navigate the complexities", "robust", "seamless".

## Style

- Lowercase hyphenated skill names (`cold-email-outreach`, not `ColdEmailOutreach`).
- Plain markdown. Minimal emoji.
- Tables for comparative data.
- Examples beat abstractions every time.
- Cut ruthlessly. If a paragraph doesn't help a solopreneur ship something this week, delete it.

## Legal

- This repo is MIT licensed.
- You keep copyright of what you contribute. By submitting a PR you agree to license it under MIT.
- Don't include proprietary frameworks, playbooks, or internal data from an employer without permission.

## Community

- **Issues** for bugs, questions, and skill proposals.
- **PRs** for contributions.
- Be kind, be specific, be helpful. Vague criticism isn't useful; a concrete suggestion is.

---

Thanks for making this better. – [Sudhakar](https://www.linkedin.com/in/sudhakaran88/)
