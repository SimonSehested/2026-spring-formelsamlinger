# Style Guide for 22050 Formula Collection

## Overall style

Write in concise engineering handbook style.

The formula collection should look like a clean mathematical reference, not lecture notes.

Each concept should be written as:

    \subsubsection{Concept name}
    \[
    formula
    \]
    Short physical or mathematical explanation.

## Mandatory rules

- Output in `.tex` files must be valid LaTeX only.
- Use `\section`, `\subsection`, and `\subsubsection`.
- One concept per `\subsubsection`.
- Put important formulas in display math.
- After each formula block, write 1-3 concise explanatory sentences.
- Prefer physical/mathematical meaning over procedural explanation.
- Keep wording compact.
- Avoid long paragraphs.
- Avoid bullet lists unless they improve lookup speed.
- Avoid examples unless essential.
- No Markdown in `.tex` files.

## Explanation style

Good:

    The impulse response fully characterizes a continuous-time LTI system in the time domain.

Bad:

    This formula is useful when you are asked to solve problems where you need to calculate the output.

Good:

    The pole locations determine the natural modes and stability of the system.

Bad:

    You should remember this because it often appears in exams.

## Notation

Use consistent notation:

- time variable: \(t\)
- angular frequency: \(\omega\)
- complex frequency: \(s\)
- input signal: \(x(t)\)
- output signal: \(y(t)\)
- impulse response: \(h(t)\)
- transfer function: \(H(s)\)
- frequency response: \(H(j\omega)\)
- Fourier transform: \(X(\omega)\)
- Laplace transform: \(X(s)\)
- unit step: \(u(t)\)
- Dirac impulse: \(\delta(t)\)

## Preferred formatting

Use this style for central results:

    \[
    X(\omega)=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}\,dt
    \]

Use aligned equations when helpful:

    \[
    \begin{aligned}
    Y(s) &= H(s)X(s),\\
    H(s) &= \frac{Y(s)}{X(s)}.
    \end{aligned}
    \]

## Searchability

Use explicit headings.

Good headings:

    \subsubsection{Linearity of systems}
    \subsubsection{Time invariance}
    \subsubsection{Convolution integral}
    \subsubsection{Fourier transform differentiation property}
    \subsubsection{Laplace transform initial value theorem}
    \subsubsection{Bode magnitude asymptotes}

Bad headings:

    \subsubsection{Important formula}
    \subsubsection{Useful theorem}
    \subsubsection{Method}

## Length

A normal `\subsubsection` should contain:

- 1 heading
- 1-2 display equations
- 1-3 short explanatory sentences

Longer sections are allowed only for transform tables, Bode rules, classification tables, and summary tables.

## Tables

Use tables for compact lookup when appropriate.

Examples:

- signal classification
- system properties
- Fourier transform pairs
- Laplace transform pairs
- Bode rules
- filter types

Tables should be compact and searchable.

## Verification language

If source material is unclear, write a LaTeX comment:

    % TODO: verify from lecture slides

Do not silently guess.
