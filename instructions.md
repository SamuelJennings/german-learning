# Authoring Instructions for german-learning

These instructions guide content creation for A2, B1, and B2 materials. They define structure, style, templates, and linking conventions so pages remain uniform and easy to learn from.

---

## Scope and folder layout

- Levels: `a2/`, `b1/`, `b2/`
- Per level, three sections:
  - `grammar/` — Short, plain-English explanations of German grammar with many examples.
  - `concepts/` — Communication ideas that help you sound natural (e.g., being polite, hedging). Often link to grammar.
  - `topics/` — Everyday themes and situations (e.g., restaurant, small talk, debate) with phrases and dialogs.
- All pages are Markdown (MyST/Sphinx-compatible). Use headings and blocks consistently (see below).

---

## Writing principles

- Keep explanations short and simple. Prefer examples over theory.
- Avoid technical grammar jargon. Use basic terms when needed and explain them briefly.
- Use clear English for explanations and notes. Keep the German in examples accurate and natural.
- Show variation: formal vs. informal, positive vs. negative, short vs. long.
- Be consistent with headings, sections, and formatting across similar pages.

---

## File naming and titles

- Use lowercase snake_case for filenames. Use ASCII only.
  - ä → ae, ö → oe, ü → ue, ß → ss
  - Examples: `praeposition.md`, `konjunktiv_II.md`, `relativsaetze.md`
- One H1 (`#`) at the top with the German name. Optionally add a short English hint: `# Konjunktiv II`.

---

## Linking rules (always at the top)

Add a small “Related” block at the top of every page so learners can jump between connected ideas.

- Place it right under the H1.
- Include links to the other two sections where relevant (Grammar ↔ Concepts ↔ Topics).
- Use relative paths. Examples:
  - From `a2/grammar/konjunktiv_II.md` to a concept: `../concepts/speaking_politely.md`
  - From a topic to grammar across the same level: `../grammar/relativsaetze.md`
  - Across levels (rare): from `b1/concepts/…` to A2 grammar: `../../a2/grammar/praeteritum.md`

Recommended block style (MyST):

:::{seealso}
Related

- Grammar: [Konjunktiv II](../grammar/konjunktiv_II.md)
- Concepts: [Polite speaking](../concepts/speaking_politely.md)
- Topics: [Restaurant ordering](../topics/restaurant_ordering.md)
:::

Only include categories that make sense for the page; omit empty categories.

---

## Formatting conventions

- Headings: `#` title, then `##` section, `###` subsection. Do not skip levels.
- Separate major sections with `---` (horizontal rule).
- Examples style:
  - Bullet list for example sets.
  - Line 1: German sentence with key part in bold.
  - Line 2: English translation in italics.
  - Optional short note after, or group notes in a `:::{note}…:::` block.
- Use tables when a compact overview helps (patterns, synonyms, phrase banks).
- Use MyST admonitions for brief guidance: `:::{note}`, `:::{tip}`, `:::{warning}`.

Example snippet:

- Ich **würde** gern einen Kaffee.  
  _I’d like a coffee._

---

## Using the custom Sphinx extensions

Two local extensions help make pages interactive and consistently styled:

1. Practice directive (opens a ChatGPT prompt)

- Purpose: add a one-click link for targeted practice based on the page’s content.
- Where (default): one consolidated Practice section at the end of the page. Keep it short (2–5 tasks) and focused.
- When to add more than one: only if a page has clearly distinct sub‑skills that benefit from separate drills (e.g., “wo” vs “wohin” on two‑way prepositions, or “ask about things” vs “ask about people” on W‑Fragen mit Präposition). In that case, add at most one extra practice block right after the relevant subsection and keep the end‑of‑page block.
- Prompt quality: the entire content of the directive is sent to ChatGPT. Make it self‑contained: include a brief summary of what to practice + explicit instructions (format, number of items, level, feedback style). Avoid referring to “above” or “the section” without restating key details.
- Syntax (MyST):

```{practice}
Write 5 polite requests using Konjunktiv II with “würde”. Include translations.
```

- Tips for good prompts:
  - Be specific about the target form and context (level, tone: formal/informal).
  - Summarize the relevant facts/rules so the prompt stands alone.
  - Prefer step‑by‑step interaction: one item at a time with brief feedback.

1. Grammar highlighting roles (consistent styling)

- Purpose: highlight only the grammar elements relevant to the rule you’re teaching.
- Usage in MyST Markdown: use role backticks around text, for example: `{prep}`mit``, `{dativ}`dem``, `{akk}`den``.
- Examples:
  - Prepositions focus: {prep}`mit` {dativ}`dem` {noun}`Freund`
  - Cases focus: Ich sehe {akk}`den` {noun}`Hund`.
  - Word order focus (don’t over-mark nouns if the point is case endings): “..., weil ich {verb}`gehe`.”
- Current roles (from `conf.py: custom_roles`): `noun`, `verb`, `adj`, `adv`, `pronoun`, `prep`, `conj`, `article`, `te`, `ka`, `mo`, `lo`, `subj`, `dativ`, `akk`
- Adding a new role:
  1. Add the role name to `custom_roles` in `conf.py`.
  2. Define its CSS class in `_static/stylesheet.css`.
  3. Use high-contrast colors for both light and dark modes. Example:

     ```css
     /* High-contrast examples; adjust to your palette */
     html[data-theme='light'] .konj2 { color: #8B008B; font-weight: 600; }
     html[data-theme='dark']  .konj2 { color: #FF7BFF; font-weight: 600; }
     ```

- Keep highlights focused: if the lesson is on cases, mark case articles/endings; don’t highlight every noun.

## Templates

Copy one of the templates below when creating a new page. Keep the section order and headings.

### Grammar page template

````markdown
# GRAMMAR NAME (EN hint optional)

:::{note}
Related

- Concepts: [linked_concept](../concepts/linked_concept.md)
- Topics: [linked_topic](../topics/linked_topic.md)
:::

## Quick idea
One–two sentences that say what this grammar lets you do, in simple English.

```{practice}
Give a one-sentence summary of this grammar and 3 micro-examples.
```

## When to use it

- Bullet use-case 1
- Bullet use-case 2

```{practice}
Create 3 short situations where this grammar is appropriate and model one example for each.
```

## How it works (short)

Explain in plain English. Avoid jargon. If a term is needed, define it with a simple sentence.

```{practice}
Explain this rule simply for an A2 learner and generate 3 minimal pairs that contrast correct vs. incorrect.
```

## Patterns

| German Pattern | English Meaning | Notes |
|---|---|---|
| pattern | meaning | short tip |

---

<!-- Optional short section-level practice only when a sub-skill is truly distinct; otherwise omit. -->

## Examples

- German sentence with **focus**.  
  _English translation._
- German sentence with **focus**.  
  _English translation._

<!-- Optional short section-level practice only when a sub-skill is truly distinct; otherwise omit. -->

:::{note}
Short tips, variations, or formality notes.
:::

## Common mistakes

- Mistake → correction (short reason)

<!-- Optional short section-level practice only when a sub-skill is truly distinct; otherwise omit. -->

## Mini practice

- Prompt 1
- Prompt 2

:::{note}
Answer key (if included) can go here or at the end.
:::

## Practice

```{practice}
You are a German tutor working with an <LEVEL> learner on <TOPIC>. Briefly recap the key rules/patterns:
- <one-line rule 1>
- <one-line rule 2>

Design an interactive practice delivered one item at a time with concise feedback. Keep vocabulary <LEVEL>-appropriate.

Tasks:
1) <task>
2) <task>

Constraints: short, concrete, everyday contexts; no rare vocabulary; clear answers.
```
````

### Concept page template

````markdown
# CONCEPT NAME (EN hint optional)

:::{note}
Related

- Grammar: [linked_grammar](../grammar/linked_grammar.md)
- Topics: [linked_topic](../topics/linked_topic.md)
:::

## What this helps you do
One–two sentences in plain English.

```{practice}
Summarize this concept for a learner and propose 3 starter prompts.
```

## When to use it

- Bullet situations where this concept appears

```{practice}
Create 3 situations and one model sentence for each using this concept.
```

## Key phrases

| German | English | Notes |
|---|---|---|
| phrase | meaning | register/nuance |

---

<!-- Optional short section-level practice only when a sub-skill is truly distinct; otherwise omit. -->

## Examples

- German example with **key phrase**.  
  _English translation._

<!-- Optional short section-level practice only when a sub-skill is truly distinct; otherwise omit. -->

## Register and tone

Brief guidance (formal/informal, polite/direct, regional if relevant).

<!-- Optional short section-level practice only when a sub-skill is truly distinct; otherwise omit. -->

## Mini practice

- Rewrite or choose-the-phrase tasks.

## Practice

```{practice}
You are a German tutor working with an <LEVEL> learner on the concept <TOPIC>. Recap the key phrases and when to use them:
- <phrase/pattern>
- <phrase/pattern>

Create 2–4 short interactive tasks (e.g., choose-the-phrase, transform for register, mini-dialog). Provide brief feedback and keep all language <LEVEL>-appropriate.
```
````

### Topic page template

```markdown
# TOPIC NAME

:::{note}
Related

- Grammar: [linked_grammar](../grammar/linked_grammar.md)
- Concepts: [linked_concept](../concepts/linked_concept.md)
:::

## You will learn to
- Goal 1
- Goal 2

## Key phrases
| German | English | Notes |
|---|---|---|
| phrase | meaning | context |

## Model dialog
A short, natural dialog for the situation (2–8 lines). Bold target items.

---

## Vocabulary
| German | English | Notes |
|---|---|---|
| word | meaning | tip |

## Try it
- Role-play prompt 1
- Role-play prompt 2
```

---

## Acceptance checklist (for every new/edited page)

- Top-of-page Related block with at least one meaningful link.
- Clear, short English explanation; minimal jargon.
- Examples: at least 6 for Grammar pages; at least 4 for Concepts/Topics.
- Consistent headings and section order as per the template.
- Tables used where they add clarity (patterns, phrases, vocab).
- Practice section present at end with a single, self‑contained prompt (2–5 tasks).
- Extra section-level practice blocks only when strongly justified by distinct sub‑skills (rare).
- Practice prompts are self‑contained: they include a summary and explicit instructions; no vague references to content “above”.
- Relevant grammar roles applied to highlights; avoid over-marking unrelated words.
- New roles (if introduced) added to `conf.py` and styled in `_static/stylesheet.css` with high-contrast light/dark colors.
- File name follows snake_case ASCII rules.
- Relative links verified (no broken paths).

---

## Examples of style (from existing pages)

- Synonym tables like in `a2/topics/adjectives.md` are welcome for vocabulary-focused pages.
- Use `:::{note}…:::` blocks for short guidance and register notes.
- Separate major sections with `---` for scannability.

---

## Notes for automation (Copilot agent)

- When creating a new page, start from the correct template and fill sections in order.
- Always add the Related block immediately after the H1.
- Prefer short, practical explanations followed by many examples.
- Keep German examples error-free; highlight target forms in bold.
- Do not change unrelated pages when adding one page.
- Keep link text human-friendly: German term plus optional English in parentheses.
