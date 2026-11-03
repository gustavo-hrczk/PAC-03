#!/usr/bin/env python3
"""Converte um .md do repositório em .docx com a folha de estilo neutra do projeto.

Os .md daqui são escritos para ler bem no GitHub: um único `#` de título, índice
com links de âncora, nenhuma marcação de impressão. O .docx precisa do contrário —
seções em Heading 1, metadados de capa, quebra de página antes de cada seção.
Este script faz a tradução de um para o outro, para que o markdown continue sendo
a fonte da verdade.

O que ele faz, nesta ordem:

1. lê o título (`# ...`) e a linha de metadados logo abaixo;
2. remove a seção `## Índice` — no .docx ela não navega, só ocupa página;
3. promove os cabeçalhos em um nível, de modo que `##` vire Heading 1;
4. insere quebra de página antes de cada seção;
5. chama o pandoc e depois o `fix-page-breaks.py`.

Arquivos que ainda têm frontmatter YAML são tratados no formato antigo: só a
conversão dos separadores `---`/`---` em quebra de página.

Uso: python3 tools/md2docx.py docs/GDD.md [build/GDD.docx]
"""
import json
import os
import re
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEBRA = '\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'


def tem_frontmatter(texto):
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return None
    linhas = [l for l in m.group(1).split("\n") if l.strip()]
    if linhas and all(re.match(r"^[A-Za-z_][\w-]*:\s", l) for l in linhas):
        return m
    return None


def preparar(texto):
    """Devolve (markdown pronto para o pandoc, metadados).

    Três formatos convivem no repositório:

    - frontmatter YAML — formato antigo, mantido para os documentos de arquivo;
    - `## Índice` presente — convenção atual, descrita no cabeçalho deste arquivo;
    - nenhum dos dois — documento solto, convertido como está.
    """
    legado = tem_frontmatter(texto)
    if legado:
        corpo = texto[legado.end():].replace("\n---\n---\n", QUEBRA)
        return legado.group(0) + corpo, {}

    if not re.search(r"(?m)^## Índice\s*$", texto):
        return texto.replace("\n---\n---\n", QUEBRA), {}

    linhas = texto.split("\n")

    titulo = ""
    for i, linha in enumerate(linhas):
        if linha.startswith("# "):
            titulo = linha[2:].strip()
            linhas = linhas[i + 1:]
            break

    # linha de metadados: primeira linha não vazia, se for texto solto em negrito
    subtitulo = ""
    for i, linha in enumerate(linhas):
        if not linha.strip():
            continue
        if linha.startswith("**") and not linha.startswith("#"):
            subtitulo = re.sub(r"\*+", "", linha).strip()
            linhas = linhas[:i] + linhas[i + 1:]
        break

    corpo = "\n".join(linhas)

    # 2. fora o índice
    corpo = re.sub(r"\n## Índice\n.*?(?=\n## )", "", corpo, flags=re.S)

    # 3. promove os cabeçalhos
    corpo = re.sub(r"^#(#+) ", r"\1 ", corpo, flags=re.M)

    # 4. quebra antes de cada seção, menos a primeira
    partes = re.split(r"(?m)^(?=# )", corpo)
    corpo = partes[0] + QUEBRA.join(partes[1:]) if len(partes) > 1 else corpo

    meta = {"title": titulo, "lang": "pt-BR"}
    if subtitulo:
        partido = [p.strip() for p in subtitulo.split("·")]
        meta["subtitle"] = partido[0]
        if len(partido) > 1:
            meta["date"] = " — ".join(partido[1:])

    # json.dumps dá aspas válidas em YAML mesmo quando o título já tem aspas
    frente = "---\n" + "".join(
        f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in meta.items() if v
    ) + "---\n\n"
    return frente + corpo, meta


def converter(origem, destino=None):
    destino = destino or os.path.join(
        RAIZ, "build", os.path.basename(origem)[:-3] + ".docx"
    )
    os.makedirs(os.path.dirname(destino), exist_ok=True)

    referencia = os.path.join(RAIZ, "build", "reference.docx")
    if not os.path.exists(referencia):
        subprocess.run(
            [sys.executable, os.path.join(RAIZ, "tools", "make-reference.py")],
            check=True,
        )

    with open(origem, encoding="utf-8") as f:
        pronto, _ = preparar(f.read())

    tmp = tempfile.NamedTemporaryFile(
        "w", suffix=".md", delete=False, encoding="utf-8"
    )
    tmp.write(pronto)
    tmp.close()
    try:
        subprocess.run(
            ["pandoc", tmp.name, "-o", destino, f"--reference-doc={referencia}"],
            check=True,
        )
    finally:
        os.unlink(tmp.name)

    subprocess.run(
        [sys.executable, os.path.join(RAIZ, "tools", "fix-page-breaks.py"), destino],
        check=True,
    )
    return destino


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    print("gerado:", converter(*sys.argv[1:3]))
