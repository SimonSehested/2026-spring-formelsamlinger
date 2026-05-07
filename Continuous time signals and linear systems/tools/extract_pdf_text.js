const fs = require("fs");
const path = require("path");
const { PDFParse } = require("pdf-parse");

const root = process.cwd();
const outDir = path.join(root, "reports", "extracted_text");
fs.mkdirSync(outDir, { recursive: true });

function walk(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  return entries.flatMap((entry) => {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) return walk(full);
    return full.toLowerCase().endsWith(".pdf") ? [full] : [];
  });
}

function slug(name) {
  return name
    .replace(/\.pdf$/i, "")
    .normalize("NFKD")
    .replace(/[^\w.-]+/g, "_")
    .replace(/_+/g, "_")
    .replace(/^_|_$/g, "");
}

(async () => {
  const pdfs = walk(path.join(root, "input")).sort();
  for (const file of pdfs) {
    const rel = path.relative(root, file);
    const parser = new PDFParse({ data: fs.readFileSync(file) });
    const data = await parser.getText();
    const text = [
      `SOURCE: ${rel}`,
      `PAGES: ${data.total}`,
      "",
      data.text.replace(/\r\n/g, "\n"),
    ].join("\n");
    const target = path.join(outDir, `${slug(path.basename(file))}.txt`);
    fs.writeFileSync(target, text, "utf8");
    await parser.destroy();
    console.log(`${rel} -> ${path.relative(root, target)} (${data.total} pages)`);
  }
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
