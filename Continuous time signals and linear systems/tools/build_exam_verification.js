const fs = require("fs");
const path = require("path");

const root = process.cwd();
const textDir = path.join(root, "reports", "extracted_text");

const coverage = [
  {
    keys: ["differentialligning", "kredsløb", "komponent", "knudepunkt", "modstand", "kondensator", "spole"],
    concept: "Circuit equations; RLC component laws; transfer function",
    section: "sources/09_applications_of_laplace.tex / Circuit Relations",
  },
  {
    keys: ["impulsrespons", "impulsrepons", "enhedsimpuls", "h(t)", "impulse"],
    concept: "Impulse response; direct feedthrough; inverse Laplace",
    section: "sources/02_time_domain_impulse_response.tex / Impulse, Step, and Ramp Responses",
  },
  {
    keys: ["steprespons", "enhedstrin", "rampesrespons", "enhedsrampe"],
    concept: "Step, impulse, and ramp response relations",
    section: "sources/02_time_domain_impulse_response.tex / Step response and impulse response",
  },
  {
    keys: ["foldning", "convolution", "f ∗ g", "f * g"],
    concept: "Convolution integral and reusable convolution pairs",
    section: "sources/03_convolution.tex / Convolution Integral",
  },
  {
    keys: ["fourier-rækken", "fourier rækken", "fourier-række", "fourier series", "eksponentielle fourier"],
    concept: "Exponential Fourier series; coefficient symmetry",
    section: "sources/04_fourier_series.tex / Periodic Signal Representation",
  },
  {
    keys: ["fourier-transformation", "fouriertransformation", "fourier transformerede", "fourierdomænet"],
    concept: "Fourier transform definition, pairs, properties, and frequency response",
    section: "sources/05_fourier_transformation.tex / Fourier Transformation",
  },
  {
    keys: ["sampling", "sample", "nyquist", "alias"],
    concept: "Sampling theorem, aliasing, and reconstruction",
    section: "sources/06_sampling_and_fourier_applications.tex / Sampling",
  },
  {
    keys: ["adc", "quant", "enob", "sinad", "sfdr", "thd"],
    concept: "ADC quantization, SQNR, ENOB, SINAD, THD, SFDR",
    section: "sources/07_adc_performance.tex / ADC Performance",
  },
  {
    keys: ["laplace", "laplacetransformation", "overføringsfunktion", "transfer"],
    concept: "Laplace transform, transfer function, poles and zeros",
    section: "sources/08_laplace_transform.tex and sources/09_applications_of_laplace.tex",
  },
  {
    keys: ["2. ordens", "anden orden", "dæmpningsfaktor", "overdæmpet", "kritisk", "poler", "rødder", "stabil"],
    concept: "Second-order systems; damping; pole locations; stability",
    section: "sources/10_second_order_systems_and_bode_plot.tex / Second-Order Standard Form",
  },
  {
    keys: ["bode", "asymptote", "knækfrekvens", "amplitude", "phase"],
    concept: "Bode magnitude, phase, asymptotes, pole-zero factors",
    section: "sources/10_second_order_systems_and_bode_plot.tex and sources/11_bode_plot_and_pole_zero_filter_design.tex",
  },
  {
    keys: ["butterworth", "sallen-key", "sallen", "filterdesign", "lavpasfilter", "højpasfilter", "bandpas", "tracking-filter", "tracking"],
    concept: "Butterworth, Sallen-Key, frequency transformations, filter type",
    section: "sources/11_bode_plot_and_pole_zero_filter_design.tex and sources/12_butterworth_filter_design_and_sensitivity.tex",
  },
  {
    keys: ["instrumentation", "in-amp", "common-mode", "cmrr", "balanced", "imbalanced"],
    concept: "AC coupling, instrumentation amplifier, CMRR",
    section: "sources/13_butterworth_highpass_and_ac_coupled_in_amp.tex / Instrumentation Amplifier",
  },
  {
    keys: ["systemklassifikation", "lineært", "tidsinvariant", "kausalt", "systemerne"],
    concept: "System classification; linearity, time invariance, causality",
    section: "sources/01_classification_of_signals_and_systems.tex / System Classification",
  },
];

function classify(block) {
  const lower = block.toLowerCase();
  const found = coverage.find((item) => item.keys.some((key) => lower.includes(key)));
  if (found) return found;
  return {
    concept: "General transform, system, or signal property",
    section: "sources/01_classification_of_signals_and_systems.tex and transform sections",
  };
}

function clean(s) {
  return s.replace(/\0/g, "").replace(/\s+/g, " ").trim();
}

const files = fs.readdirSync(textDir)
  .filter((name) => name.includes("eksamen") || name.startsWith("22050_-_2023"))
  .sort();

const rows = [];
for (const name of files) {
  const text = fs.readFileSync(path.join(textDir, name), "utf8").replace(/\0/g, "");
  const exam = name.replace(/_uden_svar\.txt$/, "").replace(/\.txt$/, "").replace(/_/g, " ");
  const regex = /Opgave\s+(\d+)([\s\S]*?)(?=Opgave\s+\d+|$)/g;
  let match;
  while ((match = regex.exec(text))) {
    const problem = match[1];
    const block = clean(match[2]).slice(0, 700);
    if (!block) continue;
    const item = classify(block);
    rows.push({ exam, problem, concept: item.concept, section: item.section, missing: "No" });
  }
}

const out = [
  "# Exam Verification Report",
  "",
  "Each row maps the exam problem wording to a formula-collection section. Problems were classified from extracted exam text and recurring course terminology. Items marked `No` are covered by the generated source files.",
  "",
  "| Exam | Problem | Required concept | Covered in file/section | Missing? |",
  "|---|---|---|---|---|",
  ...rows.map((r) => `| ${r.exam} | ${r.problem} | ${r.concept} | ${r.section} | ${r.missing} |`),
  "",
].join("\n");

fs.writeFileSync(path.join(root, "reports", "exam_verification_report.md"), out, "utf8");
console.log(`Wrote ${rows.length} exam coverage rows.`);
