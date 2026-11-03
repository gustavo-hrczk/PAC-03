#!/usr/bin/env python3
"""Gera a folha de estilo neutra usada nos .docx do projeto.

Arial 11, corpo justificado, entrelinha simples, títulos em preto.
Uso: python3 tools/make-reference.py  ->  build/reference.docx
"""
import re, os, shutil, subprocess, zipfile, tempfile

OUT = "build/reference.docx"

def main():
    os.makedirs("build", exist_ok=True)
    tmp = tempfile.mkdtemp()
    base = os.path.join(tmp, "base.docx")
    with open(base, "wb") as f:
        f.write(subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                               capture_output=True).stdout)
    ext = os.path.join(tmp, "ref")
    with zipfile.ZipFile(base) as z:
        z.extractall(ext)

    p = os.path.join(ext, "word/styles.xml")
    s = open(p, encoding="utf-8").read()

    s = re.sub(r'<w:rFonts[^/]*?w:asciiTheme[^/]*?/>',
               '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:eastAsia="Arial" w:cs="Arial"/>', s)
    for a, b in [('<w:sz w:val="24" />', '<w:sz w:val="22" />'),
                 ('<w:szCs w:val="24" />', '<w:szCs w:val="22" />'),
                 ('<w:sz w:val="24"/>', '<w:sz w:val="22"/>'),
                 ('<w:szCs w:val="24"/>', '<w:szCs w:val="22"/>')]:
        s = s.replace(a, b)
    s = re.sub(r'<w:color w:val="(?!auto)[0-9A-Fa-f]{6}"[^/]*/>', '<w:color w:val="000000"/>', s)

    def blk(sid, txt):
        m = re.search(r'<w:style [^>]*w:styleId="%s">.*?</w:style>' % sid, txt, re.S)
        return m.group(0) if m else None

    n = blk("Normal", s)
    if n and "<w:pPr>" not in n:
        s = s.replace(n, n.replace('<w:name w:val="Normal" />',
            '<w:name w:val="Normal" /><w:pPr><w:jc w:val="both"/>'
            '<w:spacing w:line="240" w:lineRule="auto"/></w:pPr>'
            '<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'
            '<w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr>'))

    for sid in ["BodyText", "FirstParagraph", "Compact", "BlockText"]:
        b = blk(sid, s)
        if not b:
            continue
        if "<w:jc " in b:
            s = s.replace(b, re.sub(r'<w:jc w:val="[^"]*"/>', '<w:jc w:val="both"/>', b))
        elif "<w:pPr>" in b:
            s = s.replace(b, b.replace("<w:pPr>", '<w:pPr><w:jc w:val="both"/>', 1))

    # O pandoc marca bloco de código como SourceCode, mas a folha padrão não
    # define esse estilo — ele cai no Normal e sai justificado, o que estica os
    # espaços e desalinha diagrama ASCII (o GDD desenha o core loop assim).
    if 'w:styleId="SourceCode"' not in s:
        s = s.replace("</w:styles>",
            '<w:style w:type="paragraph" w:customStyle="1" w:styleId="SourceCode">'
            '<w:name w:val="Source Code"/><w:basedOn w:val="Normal"/><w:qFormat/>'
            '<w:pPr><w:jc w:val="left"/>'
            '<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>'
            '</w:pPr>'
            '<w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/>'
            '<w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>'
            "</w:style></w:styles>")

    for sid in ["SourceCode", "Verbatim", "PreformattedText"]:
        b = blk(sid, s)
        if not b:
            continue
        if "<w:jc " in b:
            nb = re.sub(r'<w:jc w:val="[^"]*"\s*/>', '<w:jc w:val="left"/>', b)
        elif "<w:pPr>" in b:
            nb = b.replace("<w:pPr>", '<w:pPr><w:jc w:val="left"/>', 1)
        else:
            nb = re.sub(r'(<w:name w:val="[^"]*"\s*/>)',
                        r'\1<w:pPr><w:jc w:val="left"/></w:pPr>', b, count=1)
        s = s.replace(b, nb)

    for sid, sz in [("Heading1","32"),("Heading2","26"),("Heading3","23"),
                    ("Heading4","22"),("Heading5","22"),("Heading6","22"),
                    ("Title","36"),("Subtitle","26")]:
        b = blk(sid, s)
        if not b:
            continue
        nb = re.sub(r'<w:sz w:val="\d+"\s*/>', '<w:sz w:val="%s"/>' % sz, b)
        nb = re.sub(r'<w:szCs w:val="\d+"\s*/>', '<w:szCs w:val="%s"/>' % sz, nb)
        nb = nb.replace("<w:i/>", "").replace("<w:i />", "")
        s = s.replace(b, nb)

    open(p, "w", encoding="utf-8").write(s)

    if os.path.exists(OUT):
        os.remove(OUT)
    subprocess.run(["zip", "-Xrq", os.path.abspath(OUT), "."], cwd=ext, check=True)
    shutil.rmtree(tmp)
    print("gerado:", OUT)

if __name__ == "__main__":
    main()
