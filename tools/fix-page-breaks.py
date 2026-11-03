#!/usr/bin/env python3
"""Converte parágrafos de quebra de página em pageBreakBefore no parágrafo seguinte.

O pandoc emite a quebra como parágrafo vazio, o que gera página em branco quando
a página anterior já está cheia. Este script anexa a quebra ao parágrafo seguinte.

Uso: python3 tools/fix-page-breaks.py arquivo.docx
"""
import re, sys, zipfile, shutil

def fix(path):
    zin = zipfile.ZipFile(path)
    doc = zin.read("word/document.xml").decode("utf-8")
    pat = re.compile(r'<w:p><w:r><w:br w:type="page"\s*/></w:r></w:p>')
    n = 0
    while True:
        m = pat.search(doc)
        if not m:
            break
        head, tail = doc[:m.start()], doc[m.end():]
        nxt = re.search(r"<w:p\b[^>]*>", tail)
        if not nxt:
            doc = head + tail
            continue
        i = nxt.end()
        opening, rest = tail[:i], tail[i:]
        if rest.startswith("<w:pPr>"):
            rest = rest.replace("<w:pPr>", "<w:pPr><w:pageBreakBefore/>", 1)
        else:
            opening += "<w:pPr><w:pageBreakBefore/></w:pPr>"
        doc = head + opening + rest
        n += 1
    tmp = path + ".tmp"
    zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    for it in zin.infolist():
        data = zin.read(it.filename)
        if it.filename == "word/document.xml":
            data = doc.encode("utf-8")
        zout.writestr(it, data)
    zout.close(); zin.close(); shutil.move(tmp, path)
    print(f"{path}: {n} quebras convertidas")

if __name__ == "__main__":
    fix(sys.argv[1])
