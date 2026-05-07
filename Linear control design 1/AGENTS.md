# AGENTS.md

You are building a LaTeX formula collection for the course described by the source material.

## Goal

Create a complete, compact, searchable LaTeX formula collection based on the course source material.

The document must function as a ctrl+f reference during exam preparation.

## Source material

Use files in:

- `source_material/slides/`
- `source_material/exams/`
- `source_material/exercises/`

First infer the course title, lecture structure, notation, and recurring exam concepts from the source material.

Do not assume fixed lecture topics in advance.

Do not invent formulas or topics that are not supported by the source material unless they are standard prerequisites clearly required to solve the exam problems.

If uncertain, mark with:

    % TODO: verify from source

## Output files

Create output files dynamically in:

- `sources/`

Use one `.tex` file per major lecture/topic inferred from the source material.

Use clear numbered filenames such as:

    01_topic_name.tex
    02_topic_name.tex
    03_topic_name.tex

The topic names must be inferred from the slides and exams, not hardcoded.

Do not write large amounts of formula content directly in `main.tex`.

## Style

Follow `prompts/style_guide.md` exactly.

The style must resemble a professional engineering reference handbook:

- section/subsection/subsubsection hierarchy
- centered display equations
- short physical or mathematical explanation after each equation block
- no long prose
- no derivations unless essential
- no examples unless they encode a reusable exam method
- no images
- no Markdown in `.tex` files

## Organization

Organize primarily by lecture topic as inferred from the slides.

Each generated lecture/topic file should contain LaTeX in this form:

    \section{Topic name}

    \subsection{Major concept}

    \subsubsection{Specific formula or definition}
    \[
    ...
    \]
    Short explanation.

If the source material has numbered lectures, preserve that order.

If the source material has thematic slide packs rather than numbered lectures, infer a logical order from prerequisites and exam usage.

## Searchability

Make headings searchable with explicit terms from the source material.

Good:

    \subsubsection{Continuous-time Fourier transform}

Bad:

    \subsubsection{Main result}

Extract common keywords from:

- slide titles
- section headings
- repeated formula names
- exam problem wording
- exercise wording

Use those keywords in headings.

## Work process

Follow this process:

1. Inspect all source material.
2. Infer course title, topic order, notation, and recurring exam concepts.
3. Create or update `reports/coverage_report.md` with:
   - detected source files
   - inferred topic structure
   - proposed `sources/*.tex` files
   - key notation
   - recurring exam concepts
4. Create the `sources/*.tex` files dynamically.
5. Update `main.tex` so it inputs all generated source files.
6. Fill each source file.
7. Compile `main.tex`.
8. Fix LaTeX errors.
9. Verify coverage against exam sets.
10. Create or update `reports/exam_verification_report.md`.

## Verification

After writing the formula collection, inspect all exam sets.

For each exam problem, determine which formula collection section would help solve it.

Update `reports/exam_verification_report.md` with a table:

| Exam | Problem | Required concept | Covered in file/section | Missing? |
|---|---|---|---|---|

If something is missing, add it to the relevant `sources/*.tex` file and recompile.

If a new topic is required by exams but not present in slides, create an additional clearly named file such as:

    sources/99_exam_required_extra_topics.tex

and mark the additions with:

    % Added from exam coverage

## LaTeX quality

The final document must compile.

Before finishing:

- run LaTeX build if available
- fix compile errors
- check for undefined references
- check for missing input files
- check for broken math syntax
- ensure `main.tex` inputs all generated files in the correct order

## Do not

- do not assume a fixed course structure
- do not hardcode topics from another course
- do not generate textbook chapters
- do not include long derivations
- do not include unsupported material
- do not duplicate the same formula many times
- do not place raw notes in the final files
- do not remove existing useful content unless replacing it with better equivalent content
