# Contexto do projeto

Leia este arquivo inteiro antes de qualquer tarefa. Ele resume um projeto que já passou por várias rodadas de decisão, e boa parte do que parece arbitrário aqui foi decidido por um motivo específico que está registrado.

## O que é

**PAC — Projeto Aplicado à Comunidade**, 3º semestre de Engenharia de Software, Centro Universitário Católica de Santa Catarina, Jaraguá do Sul. Equipe de 7 pessoas, encontros quinzenais, dois semestres.

Entrega: um **jogo sério** — jogo com objetivo construtivo além do entretenimento, e com causa social identificável.

**O primeiro semestre não tem implementação.** Termina em documentação consolidada e pitch, em 24/11/2026. Código é segundo semestre (2027/1). Ver `docs/00-historico/historico.md`, seção 3, para o cronograma oficial com os 20 marcos.

## O jogo

Jogo de tabuleiro digital para celular, jogado sozinho ou com amigos em sessões assíncronas. O jogador é um mercador num arquipélago fictício da era das velas. Escolhe uma meta financeira, recebe dados por dia, percorre o tabuleiro e enfrenta situações que chegam como cartas — contratos, ofertas, cobranças. Algumas são fraude; outras são legítimas e recusá-las custa oportunidade.

**Tema em uso, formalização pendente.** A ambientação mercantil do Anexo I está em uso — o título provisório "Selo Falso" vem dela. Falta registrar a decisão formal (D13). As mecânicas não dependem do tema.

## As quatro decisões que sustentam o design

Não altere nenhuma delas sem que o usuário peça explicitamente. Cada uma resolve um problema concreto.

**1. Verificar custa recurso.** O jogador escolhe entre agir, ignorar ou verificar. Verificar consome um dado. Sem esse custo, verificar é sempre a resposta certa e o jogo acaba na primeira hora.

**2. Placar duplo.** Cair no golpe e recusar o legítimo contam como erros separados. Punir só o primeiro ensina desconfiança generalizada, que é dano e não aprendizado. Qualquer mecânica nova precisa preservar os dois contadores.

**3. Gerador de cartas em três camadas.** Molde + preenchimento + sinal. A resposta correta deriva **sempre** dos sinais presentes, nunca do texto. Isso impede memorização e é o que faz o jogo ensinar leitura de indícios em vez de decoreba. São 10 sinais fechados e ~15 moldes. Ver `docs/03-frente-a/brainstorm.md` seção 5.

**4. Meta escolhida pelo jogador.** Dá direção ao acúmulo, cria a tensão curto x longo prazo e serve de condição de vitória.

## Regras rígidas de conteúdo

- **Ruído é obrigatório:** cartas legítimas com aparência estranha mas inofensiva. Sem elas o jogo ensina paranoia.
- **Pirata falsifica, não aborda.** Nada de combate naval. Perda por violência é azar; perda por engano é o objeto de aprendizagem.
- **Mundo inteiramente fictício.** Nenhuma nação, companhia, rota, evento ou povo real. Nenhuma mercadoria com carga histórica de exploração humana.
- **Ponte explícita.** Ao resolver uma carta, uma linha liga o golpe do jogo ao golpe de hoje. É a condição que preserva a transferência de aprendizado.
- **Golpe entre jogadores é por composição, nunca por escrita.** O jogador monta a isca escolhendo molde e sinais. Nunca digita texto livre — isso evitaria moderação de conteúdo e produção de phishing utilizável fora do jogo.

## Restrições técnicas

- Web, rodando no navegador, funcionando em celular. **Stack: TypeScript, React, Vite, SVG** (D33). Godot foi descartado, reaberto em 03/11 por causa de animação, e reconfirmado como descartado com o protótipo na mão (D36) — não reabra sem motivo novo
- Animação e efeito gráfico saem de SVG e CSS. O degrau seguinte, se faltar, é PixiJS; ele não troca linguagem nem stack. Ver `prototypes/mapa-animado.html`
- Sem multiplayer em tempo real, sem matchmaking, sem ranking online
- Arte mínima; não há artista dedicado no grupo
- Identidade anônima, chave no dispositivo, sem e-mail nem senha
- Multiplayer assíncrono via log de ações append-only; estado derivado no cliente
- Geração de cartas determinística por semente (sessão + rodada), para todos os jogadores enfrentarem o mesmo baralho

**Nota:** a decisão original era "sem backend". Ela foi revista quando o multiplayer entrou — ver decisão D09 e pendência P07 no histórico. Backend gerenciado em camada gratuita é aceitável.

## Decisão de engenharia que não pode ser adiada

**O modo solo é uma sessão de um participante.** Mesmo modelo de estado, mesmo log de ações do multiplayer, desde a primeira linha de código. Se o solo for feito com estado local e o multiplayer "adicionado depois", vira reescrita do jogo inteiro.

## Como o trabalho se divide

O conteúdo paraleliza e o código não. São precisas 60 a 90 cartas, e escrevê-las não depende do motor existir. Cinco pessoas escrevem cartas e vocabulários enquanto duas constroem o jogo. Isso é o que torna o projeto viável com 7 pessoas de habilidades desiguais.

**Ordem de produção:** escrever 30 cartas à mão **antes** de projetar o gerador. Gerador desenhado antes do conteúdo produz a coisa errada com eficiência.

## Onde está cada coisa

```
docs/GDD.md                   Documento vigente do jogo. Substitui o brainstorm e o Anexo I
docs/espelho-secoes-8-20.md   Conteúdo pronto para colar no template do professor
docs/00-historico/     Histórico do projeto: etapas, artefatos, decisões, pendências, riscos
docs/01-propostas/     As 9 propostas da 1ª rodada e os arquivos das versões descartadas
docs/02-frentes/       As 3 frentes temáticas e o formulário de desenho de jogo
docs/03-frente-a/      Arquivo: brainstorm e Anexo I, consolidados no GDD
docs/04-apoio/         Guia de game design para integrantes sem experiência
docs/05-entregas/      Plano de recuperação e rascunhos dos marcos M08 a M16
decisions/             Registro de decisões em formato individual
content/cards/         Cartas escritas à mão
prototypes/            Protótipos de viabilidade, abertos direto no navegador
tools/                 Geração dos .docx a partir dos .md
build/                 Saída derivada. Pode ser apagada e regerada
```

**Comece sempre por** `docs/00-historico/historico.md` — é o registro cronológico e contém pendências e riscos abertos com ID. Depois `docs/GDD.md`, que é o documento vigente do jogo. O brainstorm da Frente A é material de arquivo: foi consolidado no GDD e não deve ser editado.

## Estado atual — 03/11/2026

- Título provisório: **Selo Falso**. Orientação: Luiz Almeida Junior
- Frente A escolhida; temática mercantil em uso
- **Multiplayer definido:** host cria a partida e convida por código; sem ranking e sem matchmaking
- Nenhuma carta escrita ainda — é o gargalo de produção
- Nenhum código escrito ainda (correto: implementação é 2027/1)
- **Projeto atrasado:** 9 marcos pendentes (M08 a M16), 3 semanas até a entrega de 24/11
- Plano de recuperação e rascunhos de cada marco em `docs/05-entregas/plano-recuperacao-m08-m16.md`
- Lacunas que travam o plano: faixa etária, custo da verificação, tipos de casa, duplas por marco
- Decisões a formalizar: D13 (temática), D14 (multiplayer), D15 (persistência, substitui D09)
- Engine fechada em SVG e React (D36), com protótipo de mapa animado como evidência

## Convenções

- Documentação em **português do Brasil**
- Markdown é a fonte da verdade; `.docx` é saída derivada, gerada por `tools/build-docs.sh`. Nunca edite um `.docx` — a edição se perde no próximo build
- Documento mantido em git segue a convenção do `docs/GDD.md`: um único `#` de título, linha de metadados abaixo dele, seção `## Índice` com links de âncora, seções em `##` e subseções em `###`. Nenhuma marcação de impressão no markdown — quem insere capa e quebra de página é o `tools/md2docx.py`, que põe uma quebra antes de cada seção
- Ao mexer em cabeçalho, regere o índice: as âncoras seguem a regra do GitHub, onde um travessão vira dois hífens (`9.3 A feira — loja de itens` → `#93-a-feira--loja-de-itens`)
- Decisões registradas no formato **contexto → decisão → alternativas descartadas → consequência**. Uma decisão só entra no registro se tiver alternativa descartada; sem isso é tarefa, não decisão
- Nada é apagado do histórico. Decisão revista recebe status `Substituída`, com referência à que a substituiu
- Seções argumentativas abrem com **Origem**, indicando de onde veio o questionamento — proposta de integrante, consequência de decisão anterior, risco identificado em análise, ou reversão de posição

## Ao trabalhar neste repositório

- Não proponha mecânicas que violem as quatro decisões da seção acima sem sinalizar explicitamente que está propondo revisá-las
- Ao sugerir features, verifique contra a escada de escopo (brainstorm, seção 12). O projeto já tem mais ideia do que cabe em dois semestres; o problema é cortar, não gerar
- Escopo em leque é o risco número um registrado. Largura é perigosa; profundidade não
- Ao escrever cartas, siga o formato do anexo do brainstorm: enunciado, sinais presentes, ruído, resposta correta, ponte para hoje
