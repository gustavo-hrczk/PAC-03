#!/usr/bin/env bash
# Gera os .docx a partir dos .md, com a folha de estilo neutra do projeto.
# O markdown é a fonte da verdade; o .docx é saída derivada e pode ser apagado.
set -euo pipefail
cd "$(dirname "$0")/.."

command -v pandoc >/dev/null || { echo "pandoc não encontrado"; exit 1; }

mkdir -p build
[ -f build/reference.docx ] || python3 tools/make-reference.py

if [ "$#" -gt 0 ]; then
  alvos=("$@")
else
  mapfile -t alvos < <(find docs -name '*.md' | sort)
fi

for md in "${alvos[@]}"; do
  [ -f "$md" ] || continue
  python3 tools/md2docx.py "$md" "build/$(basename "${md%.md}").docx"
done
