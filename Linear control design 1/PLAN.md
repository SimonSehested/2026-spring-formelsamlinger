# PLAN.md

Build a complete formula collection in one agent run.

## Phase 1: Inspect source material

- List all files in `source_material/slides/`.
- List all files in `source_material/exams/`.
- List all files in `source_material/exercises/`, if present.
- Infer the course title.
- Infer lecture/topic structure from slide titles, filenames, and internal headings.
- Infer recurring exam concepts from exam problems.
- Infer standard notation used in the course.
- Write findings to `reports/coverage_report.md`.

## Phase 2: Propose output structure

- Create a proposed list of `sources/*.tex` files.
- Use one file per major lecture/topic.
- Use numbered filenames in inferred order.
- Do not use hardcoded topics from previous courses.
- Record the proposed structure in `reports/coverage_report.md`.

## Phase 3: Prepare LaTeX structure

- Create missing `sources/*.tex` files.
- Ensure `main.tex` inputs all generated files.
- Keep `main.tex` modular.
- Do not place formula content directly in `main.tex`.

## Phase 4: Generate topic sections

For each inferred lecture/topic:

- create section skeleton
- fill definitions
- fill key formulas
- fill core properties
- keep explanations concise
- follow `prompts/style_guide.md`
- use terminology from the source material

## Phase 5: Compile

- Compile `main.tex`.
- Fix LaTeX errors.
- Repeat until clean or until only non-critical warnings remain.

## Phase 6: Exam verification

- Inspect each exam set.
- Map each problem to required concepts.
- Check formula collection coverage.
- Add missing compact formulas to relevant files.
- If required concepts do not fit existing files, create `sources/99_exam_required_extra_topics.tex`.
- Update `reports/exam_verification_report.md`.

## Phase 7: Final cleanup

- Remove duplicates.
- Ensure consistent notation.
- Ensure headings are ctrl+f searchable.
- Ensure `main.tex` includes all generated files.
- Compile one final time.
