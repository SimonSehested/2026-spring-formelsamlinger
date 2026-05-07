const { compile } = require("node-latex-compiler");

(async () => {
  const result = await compile({
    texFile: "main.tex",
    outputDir: ".",
    outputFile: "main.pdf",
  });
  process.stdout.write(result.stdout || "");
  process.stderr.write(result.stderr || "");
  if (result.status !== "success") {
    console.error(result.error || "LaTeX compilation failed");
    process.exit(result.exitCode || 1);
  }
  console.log(`PDF generated: ${result.pdfPath}`);
})();
