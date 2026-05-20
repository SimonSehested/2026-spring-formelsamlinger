# Style Guide for 4-Page Printed Formula Sheet

## Overall style

Write in concise printed exam-reference style.

The formula sheet should look like a clean, dense, readable mathematical safety net.

It should not look like lecture notes.

Each concept should usually be written as:

```tex
\subsection*{Concept or task name}
\[
formula
\]
\textbf{Use:} ...
\textbf{Condition:} ...
\textbf{Trap:} ...
\textbf{Check:} ...
```

Do not force every label if it adds noise.

## Primary design goal

The final PDF must be exactly 4 A4 pages.

It must be readable when printed.

It must be easy to browse visually.

It is not optimized for Ctrl+F.

## Mandatory rules

- Output in `.tex` files must be valid LaTeX only.
- Use `\section*`, `\subsection*`, and occasional `\subsubsection*`.
- Use clear topic headings for visual navigation.
- Put important formulas in display math when space allows.
- Use compact inline math for simple identities.
- Use at most one short explanatory note per formula.
- Prefer labels: `Use`, `Condition`, `Trap`, `Check`, `Units`, `Sign`, `Boundary`.
- Avoid long paragraphs.
- Avoid proofs.
- Avoid long derivations.
- Avoid examples unless they prevent a common error.
- Avoid Markdown in `.tex` files.
- Use tables for compact comparison and lookup.
- Preserve readability over maximal density.

## Explanation style

Good:

```tex
\textbf{Condition:} valid for linear time-invariant systems.
\textbf{Trap:} check sign convention before using the phase.
\textbf{Check:} units of both sides must match.
```

Bad:

```tex
This formula is useful when you are asked to solve problems where you need to calculate the output, and it is important because it often appears in exams.
```

Good:

```tex
\textbf{Boundary:} final value theorem requires stable poles except possibly at zero.
```

Bad:

```tex
Remember this theorem because it can save time in many different kinds of questions.
```

## Layout

Use a compact printable layout.

Recommended starting point:

```tex
\documentclass[9pt,a4paper]{article}
\usepackage[a4paper,margin=0.8cm]{geometry}
\usepackage{multicol}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage[most]{tcolorbox}

\setlength{\parindent}{0pt}
\setlength{\parskip}{1pt}
\setlength{\columnsep}{0.45cm}
\setlist{nosep,leftmargin=*}
```

Use either 2 or 3 columns.

Prefer 3 columns for formula-heavy courses.

Prefer 2 columns if formulas are wide or readability suffers.

## Spacing

Use compact spacing but keep the sheet readable.

Recommended adjustments:

```tex
\setlength{\abovedisplayskip}{2pt}
\setlength{\belowdisplayskip}{2pt}
\setlength{\abovedisplayshortskip}{1pt}
\setlength{\belowdisplayshortskip}{1pt}
```

Avoid large vertical gaps.

Avoid page-breaking that separates a heading from its formula.

## Headings

Use paper-friendly headings.

Good headings:

```tex
\section*{Transforms}
\subsection*{Laplace rules}
\subsection*{Stability checks}
\subsection*{Boundary conditions}
```

Bad headings:

```tex
\subsection*{Keywords for search}
\subsection*{Important}
\subsection*{General theory}
```

## Formula blocks

For central results:

```tex
\[
X(\omega)=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}\,dt
\]
\textbf{Trap:} sign convention may differ between courses.
```

For related identities:

```tex
\[
\begin{aligned}
Y(s)&=H(s)X(s),&
H(s)&=\frac{Y(s)}{X(s)}.
\end{aligned}
\]
```

For small formulas, prefer inline text:

```tex
\textbf{Check:} stable CT system: poles strictly in left half-plane.
```

## Tables

Use tables aggressively for compact lookup.

Good table types:

- formula pairs
- transform pairs
- condition/rule tables
- sign convention tables
- method selection tables
- common traps
- sanity checks
- classification rules
- boundary cases

Recommended format:

```tex
\begin{tabularx}{\linewidth}{@{}lX@{}}
\toprule
\textbf{Case} & \textbf{Rule} \\
\midrule
... & ... \\
\bottomrule
\end{tabularx}
```

Keep table text short.

## Boxes

Use boxes sparingly for high-risk content.

Good box content:

- formulas that are easy to misuse
- common traps
- decision rules
- final answer checks
- sign conventions

Example:

```tex
\begin{tcolorbox}[title=High-risk trap,boxrule=0.3pt,arc=1mm,left=1mm,right=1mm,top=1mm,bottom=1mm]
Check assumptions before applying the theorem.
\end{tcolorbox}
```

Do not overuse boxes, since they consume space.

## Recipes

Recipes should be short.

Use this style:

```tex
\subsection*{Task: name}
\textbf{Use:} recognition cue.
\begin{enumerate}
    \item Step 1.
    \item Step 2.
    \item Step 3.
\end{enumerate}
\textbf{Check:} ...
```

Normally use 2--5 steps.

No long procedural explanations.

## What to include

Include:

- recurring formulas
- high-risk formula variants
- conditions and assumptions
- sign conventions
- domain restrictions
- units and dimensions
- common traps
- sanity checks
- edge cases
- short task recipes
- notation reminders

## What to exclude

Exclude:

- proofs
- long derivations
- motivational explanations
- historical comments
- generic study advice
- rare formulas with low exam value
- content included only for completeness
- repeated explanations
- large worked examples

## Length control

A normal subsection should contain:

- 1 heading
- 1 formula block or compact table
- 0--3 short labels such as `Use`, `Trap`, `Check`

Longer sections are allowed only for:

- transform tables
- classification tables
- decision tables
- compact method summaries
- formula families

## Page count rule

After compiling, check the page count.

The PDF must be exactly 4 pages.

If it is too long, remove or compress content.

If it is too short, add high-value exam backup material.

Never leave the final PDF at 3 pages or 5 pages.
