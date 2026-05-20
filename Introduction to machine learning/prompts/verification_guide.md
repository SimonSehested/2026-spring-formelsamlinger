# Verification Guide for 4-Page Printed Formula Sheet

After generating the formula sheet, verify it against exam sets and exercises.

The goal is not full coverage.

The goal is the best possible 4-page printed exam backup sheet.

## Verification purpose

For each exam problem, identify whether the sheet supports the student in the moments where they are likely to become uncertain:

- formula choice
- assumptions
- sign conventions
- conditions
- notation
- units
- boundary cases
- common traps
- plausibility checks
- short solution method

Do not solve full exam problems unless needed to identify missing formulas or uncertainty points.

## Verification table

Create or update:

- `reports/exam_verification_report.md`

Use this table format:

| Exam/source | Problem | Required concept or method | Likely uncertainty | Support on sheet | Missing? | Include/exclude decision |
|---|---|---|---|---|---|---|

## Rules

- Focus on coverage under a strict 4-page budget.
- Prefer compact reference formulas over explanations.
- Prefer assumptions, traps, and checks over derivations.
- If a recurring method is missing, add a compact formula, rule, or recipe.
- If a recurring trap is missing, add a short `Trap` or `Check` label.
- If a concept appears in several exams, ensure it has a clear visual heading.
- If a formula is missing from slides but clearly required by recurring exams, add it and mark it with:

    % Added from exam coverage

## Include/exclude decision

When content is missing, decide whether to include it.

Include if:

- it appears repeatedly in exams or exercises
- it is easy to confuse
- a small sign/condition mistake causes wrong answers
- it supports several problem types
- it is hard to derive under time pressure
- it provides a useful sanity check

Exclude if:

- it appears only once
- it is easy to derive
- it is low-value compared with other content
- it is mostly theoretical
- it requires too much space for too little exam benefit
- it would push the sheet beyond 4 pages

Mark excluded items explicitly:

    Excluded: rare / derivable / low value / not worth 4-page space

## Page-count discipline

If verification reveals missing content, do not simply add it.

First decide whether it deserves space.

If adding it makes the PDF longer than 4 pages, remove or compress lower-priority content.

The final PDF must remain exactly 4 A4 pages.

## Final verification checklist

Before finishing, confirm:

- LaTeX compiles.
- The compiled PDF is exactly 4 A4 pages.
- The sheet is readable when printed.
- The layout is visually navigable.
- No section looks like lecture notes.
- No proof or long derivation remains.
- Common traps and assumptions are visible.
- Recurring exam task types have compact support.
- Rare excluded items are documented in the report.
