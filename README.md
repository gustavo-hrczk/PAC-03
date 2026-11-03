# PAC 2026 — Jogo Sério

Repositório de documentação e desenvolvimento do projeto de PAC (Projeto Aplicado à Comunidade), 3º semestre de Engenharia de Software.

## O que é

Jogo de tabuleiro digital para celular sobre educação financeira e reconhecimento de fraude, jogado sozinho ou com amigos em sessões assíncronas.

## Por onde começar

| Se você é… | Leia |
|:--|:--|
| Novo no projeto | `docs/04-apoio/guia-game-design.md`, depois as seções 1 a 4 do [GDD](docs/GDD.md) |
| Vai escrever cartas | GDD, [seção 7](docs/GDD.md#7-as-cartas) e [seção 19](docs/GDD.md#19-produção-de-conteúdo) |
| Vai programar | `CLAUDE.md`, depois GDD [seções 4](docs/GDD.md#4-core-loop), [6](docs/GDD.md#6-dados-e-ações), [8](docs/GDD.md#8-ações-sobre-a-carta) e [17](docs/GDD.md#17-arquitetura) |
| Quer ver o jogo de pé | `prototypes/mapa-animado.html` — abra no navegador |
| Quer o histórico | `docs/00-historico/historico.md` |

## Estrutura

```
CLAUDE.md                     Contexto para sessões de IA — leia antes de qualquer tarefa
docs/GDD.md                   Documento vigente do jogo
docs/espelho-secoes-8-20.md   Conteúdo para o template de acompanhamento do professor
docs/00-historico/     Etapas, artefatos, decisões, pendências e riscos
docs/01-propostas/     As 9 propostas da 1ª rodada e versões arquivadas
docs/02-frentes/       As 3 frentes temáticas e o formulário de desenho
docs/03-frente-a/      Arquivo: brainstorm e Anexo I, já consolidados no GDD
docs/04-apoio/         Guia de game design para quem nunca projetou jogo
decisions/             Registro individual de decisões
content/cards/         Cartas escritas à mão
prototypes/            Protótipos de viabilidade, abertos direto no navegador
tools/                 Scripts de build da documentação
build/                 Saída derivada. Pode apagar; regera com um comando
```

## Documentação

Markdown é a fonte da verdade. Os `.docx` entregues à turma são gerados a partir dele — nunca o contrário, e editar um `.docx` perde a edição no próximo build.

```bash
./tools/build-docs.sh                 # todos os documentos
./tools/build-docs.sh docs/GDD.md     # só um
```

Requer `pandoc`. A folha de estilo neutra (Arial 11, justificado, títulos em preto) é gerada por `tools/make-reference.py`; `tools/md2docx.py` acrescenta capa e quebra de página, que não existem no markdown.

Ao mexer em qualquer cabeçalho do GDD, regere o índice:

```bash
python3 tools/indice.py docs/GDD.md
python3 tools/indice.py --conferir docs/GDD.md   # falha se estiver desatualizado
```

## Estado

- Frente A escolhida; temática mercantil em uso
- GDD consolidado em 03/11/2026, versão 1.0 — substitui brainstorm e Anexo I
- Entrega do 1º semestre em 24/11/2026: documentação e pitch, sem código
- Implementação começa em 2027/1
