#!/usr/bin/env python3
"""Regenerate the submission PDFs (one-pager.pdf, security-privacy.pdf).

These PDFs are committed deliverables (issue #9; attached to the pitch email),
so they must be reproducible from the repo. No pandoc dependency — this renders
Markdown -> styled HTML -> PDF via headless Google Chrome.

Usage:
    python3 submission/render-pdf.py            # renders both docs
    python3 submission/render-pdf.py one-pager  # render one

Requires: `pip install markdown` and Google Chrome installed.
"""
import os
import subprocess
import sys

import markdown  # pip install markdown

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = ["one-pager", "security-privacy"]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: letter; margin: 2.2cm 2cm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif; font-size: 10.5pt; line-height: 1.5; color: #1a1a1a; }
h1 { font-size: 20pt; margin: 0 0 4pt; border-bottom: 2px solid #111; padding-bottom: 6pt; }
h2 { font-size: 13pt; margin: 18pt 0 6pt; color: #111; }
h3 { font-size: 11pt; margin: 12pt 0 4pt; }
p, li { font-size: 10.5pt; }
code { font-family: 'SF Mono', Menlo, monospace; font-size: 9pt; background: #f2f2f2; padding: 1px 4px; border-radius: 3px; }
pre { background: #f6f8fa; border: 1px solid #e2e2e2; border-radius: 6px; padding: 10px 12px; overflow-x: auto; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9.5pt; }
th, td { border: 1px solid #ccc; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #f0f0f0; }
a { color: #0b5cad; text-decoration: none; }
hr { border: none; border-top: 1px solid #ddd; margin: 14pt 0; }
strong { color: #000; }
"""


def render(name: str) -> None:
    md_path = os.path.join(HERE, name + ".md")
    html_path = os.path.join(HERE, name + ".html")
    pdf_path = os.path.join(HERE, name + ".pdf")
    body = markdown.markdown(
        open(md_path).read(),
        extensions=["tables", "fenced_code", "sane_lists"],
    )
    open(html_path, "w").write(
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", f"file://{html_path}"],
        check=True, stderr=subprocess.DEVNULL,
    )
    os.remove(html_path)  # intermediate; not committed
    print(f"rendered {name}.pdf")


if __name__ == "__main__":
    targets = sys.argv[1:] or DOCS
    for t in targets:
        render(t)
