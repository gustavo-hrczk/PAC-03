#!/usr/bin/env python3
"""Regera a seção `## Índice` de um documento, no lugar.

Rode isto sempre que mexer em um cabeçalho. As âncoras seguem a regra do GitHub,
que tem uma pegadinha: o caractere removido deixa os dois espaços vizinhos para
trás, e cada espaço vira um hífen. Por isso `9.3 A feira — loja de itens` vira
`#93-a-feira--loja-de-itens`, com dois hífens, e não um.

Uso:  python3 tools/indice.py docs/GDD.md
      python3 tools/indice.py --conferir docs/GDD.md   # só avisa, não escreve
"""
import re
import sys

CABECALHO = re.compile(r"^(#{2,3}) (.+)$", re.M)


def ancora(texto, vistas):
    """Reproduz o github-slugger: trim, minúsculas, remove pontuação, espaço → hífen."""
    base = re.sub(r"\*+", "", texto).strip().lower()
    base = re.sub(r"[^\w\s-]", "", base, flags=re.UNICODE).replace(" ", "-")
    n = vistas.get(base, 0)
    vistas[base] = n + 1
    return base if n == 0 else f"{base}-{n}"


def montar(texto):
    corpo = re.sub(r"(?s)^.*?\n## Índice\n", "", texto)
    vistas, linhas = {}, []
    for nivel, bruto in CABECALHO.findall(corpo):
        rotulo = re.sub(r"\*+", "", bruto).strip()
        recuo = "" if len(nivel) == 2 else "  "
        linhas.append(f"{recuo}- [{rotulo}](#{ancora(bruto, vistas)})")
    return "\n".join(linhas)


def aplicar(caminho, escrever=True):
    with open(caminho, encoding="utf-8") as f:
        texto = f.read()

    if not re.search(r"(?m)^## Índice\s*$", texto):
        print(f"{caminho}: sem seção '## Índice' — nada a fazer")
        return False

    novo = montar(texto)
    atualizado = re.sub(
        r"(?s)(^## Índice\n\n).*?(?=\n## )",
        lambda m: m.group(1) + novo + "\n",
        texto,
        count=1,
        flags=re.M,
    )

    if atualizado == texto:
        print(f"{caminho}: índice em dia ({novo.count(chr(10)) + 1} entradas)")
        return False

    if escrever:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(atualizado)
        print(f"{caminho}: índice regerado ({novo.count(chr(10)) + 1} entradas)")
    else:
        print(f"{caminho}: índice DESATUALIZADO — rode sem --conferir")
    return True


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    conferir = "--conferir" in args
    alvos = [a for a in args if not a.startswith("--")]
    mudou = [aplicar(a, escrever=not conferir) for a in alvos]
    sys.exit(1 if conferir and any(mudou) else 0)
