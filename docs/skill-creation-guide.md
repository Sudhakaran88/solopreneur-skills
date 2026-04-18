# Skill Creation Guide

How to write a skill that's actually worth installing.

This is not a template — it's the thinking behind a good skill. If you want a starter file, copy any skill in `skills/` and adapt it. This guide is about what separates a skill people use from one they uninstall.

## What makes a great skill

A great skill is four things:

1. **Opinionated.** It tells you what to do, not a menu of options. If the research supports one path, pick it. Hedging is noise.
2. **Specific.** Numbers, formulas, word counts, line thresholds. "Keep subject lines short" is weak. "Subject lines under 50 characters; under 30 if the opener repeats the subject" is a skill.
3. **Research-based.** Every non-obvious claim traces to a source — a study, a practitioner post, a published benchmark. Year the source. If you can't source it, mark it as the author's opinion.
4. **Solopreneur-focused.** No "get buy-in from the VP of Growth." No "loop in your design team." The reader is one person shipping on a Tuesday night. Tools must have free or cheap tiers. Tactics must be doable solo.

Skills that fail these tests get uninstalled fast.

## The research step

Do this before opening the SKILL.md file. It's the difference between a skill and a blog post.

**Four sources, in this order:**

1. **Reddit.** Search `site:reddit.com <topic> what actually worked` and `site:reddit.com <topic> mistake`. Read 30+ comments. You're looking for the gap between the textbook and what practitioners report. That gap is your contrarian section.
2. **Practitioner blogs.** People who ship, not people who sell courses. Rand Fishkin, Kyle Poyar, Kieran Flanagan, Amanda Natividad. Grab frameworks and numbers.
3. **Primary frameworks.** If the topic has a canonical book or paper (Jobs to be Done, Pirate Metrics, Van Westendorp), read the original, not a summary of a summary.
4. **Your own logs.** Screenshots, experiment results, client work. Sanitized, these become the strongest evidence.

**Example queries for an email-sequence skill:**

- `site:reddit.com/r/SaaS onboarding email sequence`
- `site:reddit.com/r/emailmarketing welcome sequence mistakes`
- `"welcome email" open rate benchmark 2024`
- `lifecycle email teardown`

**What to extract from each source:**

- A specific tactic or number
- A common mistake people made
- A claim that disagrees with conventional advice
- A quote or phrase a real founder used (helpful for your voice pass)

You should finish research with a scratch file of 30–50 bullet points before writing a line of the skill.

## Writing the skill

### Frontmatter

```yaml
---
name: email-sequence
description: When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use when the user mentions "email sequence," "drip campaign," "nurture sequence," "onboarding emails," "welcome sequence," "re-engagement emails," "email automation," or "lifecycle emails." For in-app onboarding, see onboarding-cro.
version: 1.0.0
---
```

The `description` is the most load-bearing line in the file. It decides whether the skill triggers. Include:

- The core use case in plain language
- Trigger phrases in quotes
- A cross-reference that disambiguates it from adjacent skills (`For X, see other-skill`)

### Opening line

The first paragraph after the frontmatter is the contract with the reader. State what the skill covers and what it deliberately excludes. Two or three sentences.

Bad opening: "Email sequences are one of the most powerful tools in marketing."

Good opening: "This skill builds 5–9 email sequences for SaaS onboarding, nurture, re-engagement, and win-back. It assumes a solopreneur with one ESP and no design help. It does not cover transactional emails or deliverability setup."

### Structure

A typical skill has this shape:

1. **When to use / when not to use** — bounds the skill
2. **The core framework** — the one mental model the reader should leave with
3. **Step-by-step workflow** — concrete, numbered, with inputs and outputs
4. **Templates or examples** — fill-in-the-blank copy, real numbers
5. **Common Mistakes** (required)
6. **Contrarian Takes** (required)
7. **Related Skills** (required)

Don't pad with a "Conclusion" or "Final Thoughts." The reader leaves when they have what they need.

## The Common Mistakes section

This is the most screenshot-worthy part of the skill. It's also the hardest to write well.

**Format each mistake as:**

- **The mistake in one line** (bold)
- Why people do it (one sentence)
- Why it's wrong (one sentence with a source if you have one)
- What to do instead (one sentence, concrete)

**Bad:**
> Don't send too many emails.

**Good:**
> **Sending the welcome email 24 hours after signup.** Founders delay to "not seem pushy." But Klaviyo's 2024 benchmark data shows welcome emails sent within 60 minutes have 86% higher open rates than those sent 24+ hours later. Send the first email within 15 minutes, triggered on signup event.

Aim for 5–10 mistakes. Each should feel like "oh, I do that."

## The Contrarian Takes section

This is where the skill earns its keep. Textbook advice is everywhere. A contrarian take is when the evidence says the conventional answer is wrong for solopreneurs specifically.

**Format:**

- **The conventional wisdom** (one line)
- **The contrarian take** (one line)
- **Why** (two or three sentences with sources)

**Example:**
> **Conventional:** Personalize cold emails with the prospect's recent LinkedIn activity.
> **Contrarian:** For solopreneurs sending under 200 emails a day, skip personalization variables entirely. Write one great email to a tight segment.
> **Why:** Manual personalization eats 3–5 minutes per email at no measurable reply-rate lift below 200 sends (per Lemlist's 2023 data). Segment tightness does the work personalization is supposed to do.

Three to five contrarian takes is plenty. Don't manufacture controversy — if you can't support it, leave it out.

## The Related Skills section

Skills should cross-reference, not silo. Every skill ends with:

```markdown
## Related Skills

- `onboarding-cro` — For in-app activation after the email kicks them to the product.
- `copywriting` — For the headlines and body copy patterns the emails should echo.
- `churn-prevention` — For win-back sequences specifically.
```

Two-to-five links. Always in backticks. Always with a one-line "use this when" hint.

If your skill has no related skills, you haven't looked hard enough.

## Voice rules

Write like a practitioner talking to another practitioner over a beer. Not a marketer selling marketing.

- **Short sentences.** If it's longer than 25 words, break it.
- **Second person.** "You" not "marketers" or "one."
- **Verbs over nouns.** "Test the CTA" not "run a test on the CTA."
- **Concrete over abstract.** "A $49/month tier" not "a reasonably priced plan."
- **No stakes-raising.** Skip "critical," "essential," "must-have," "non-negotiable." If it's in the skill, it's already important.

Read the draft out loud. If you stumble, the sentence is too long.

## What to avoid

- **AI slop openings.** "In today's fast-paced digital landscape..." Delete. Start with the work.
- **Hedging.** "You might want to consider possibly testing..." Pick a side.
- **Generic advice.** "Make sure your copy is compelling." Useless. Replace with a specific technique.
- **Banned phrases.** `delve`, `leverage`, `unlock`, `supercharge`, `game-changer`, `in today's landscape`, `ever-evolving`, `at the end of the day`.
- **Emoji decoration.** A checkmark in a list is fine. An emoji per section header is theater.
- **The word "simply."** If it were simple, they wouldn't need the skill.
- **Everything-for-everyone framing.** A skill that works for a 500-person company and a solopreneur works for neither.

## Example skills to study

Before writing, read these three end-to-end. They show what "good" looks like in this repo:

- `skills/ai-seo/SKILL.md` — Example of research synthesis and specific tactics (citations, llms.txt, AI Overview optimization).
- `skills/cold-email/SKILL.md` — Example of strong Common Mistakes and Contrarian Takes sections.
- `skills/pricing-strategy/SKILL.md` — Example of opinionated frameworks with math, not vibes.

Read all three. Then write yours.
