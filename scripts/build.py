#!/usr/bin/env python3
"""Markdown kaynaklarından sayfaları üretir (paket gerektirmez).

Kullanım: python3 scripts/build.py ../İOS/FormlyStudy/docs/legal/privacy-policy-tr.md
Kaynak FormlyStudy reposunda durur; burada yalnız üretilen HTML yayınlanır.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"([\w.+-]+@formlyapps\.com)", r'<a href="mailto:\1">\1</a>', text)
    return text


def convert(markdown: str) -> tuple[str, str, str]:
    markdown = re.sub(r"<!--.*?-->", "", markdown, flags=re.S).strip()
    lines = markdown.splitlines()
    title, updated, out = "", "", []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("### "):
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("Son güncelleme:"):
            updated = line.strip()
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            head, body = rows[0], rows[1:]
            table = ["<div class=\"table-wrap\"><table><thead><tr>"]
            table += [f"<th>{inline(c)}</th>" for c in head]
            table.append("</tr></thead><tbody>")
            for row in body:
                table.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
            table.append("</tbody></table></div>")
            out.append("".join(table))
            continue
        elif line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{inline(lines[i][2:])}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        else:
            para = [line.strip()]
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r"(#|- |\|)", lines[i + 1]):
                i += 1
                para.append(lines[i].strip())
            out.append(f"<p>{inline(' '.join(para))}</p>")
        i += 1
    return title, updated, "\n".join(out)


def page(title: str, description: str, body: str, home: str = "/") -> str:
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="site"><a class="brand" href="{home}">Formly</a><nav><a href="/formlystudy/destek/">Destek</a><a href="/formlystudy/gizlilik/">Gizlilik</a></nav></header>
<main>
{body}
<footer>© 2026 Süleyman Çayır · <a href="mailto:destek@formlyapps.com">destek@formlyapps.com</a></footer>
</main>
</body>
</html>
"""


def build_privacy(source: Path) -> None:
    title, updated, body = convert(source.read_text(encoding="utf-8"))
    # "Kısaca" listesini öne çıkar.
    body = body.replace("<p>Kısaca:</p>\n<ul>", "<div class=\"summary\"><p><strong>Kısaca</strong></p><ul>", 1)
    body = body.replace("</ul>", "</ul></div>", 1) if "class=\"summary\"" in body else body
    content = f"<h1>{inline(title)}</h1>\n<p class=\"meta\">{inline(updated)}</p>\n{body}"
    target = ROOT / "formlystudy" / "gizlilik" / "index.html"
    target.write_text(page(title, "FormlyStudy'nin hangi verileri işlediği ve senin seçeneklerin.", content), encoding="utf-8")
    print("yazıldı:", target.relative_to(ROOT))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("kullanım: build.py <privacy-policy-tr.md>")
    build_privacy(Path(sys.argv[1]))
