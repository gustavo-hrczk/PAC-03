---
title: "PAC III — Selo Falso"
subtitle: "Registro único de decisões, pendências e lacunas"
date: "Atualizado em 03 de novembro de 2026 — v2"
lang: pt-BR
---

# Como usar este registro

Documento único e vivo. Substitui as listas dispersas no histórico, no plano de
recuperação e na análise de cartas. **Atualizar ao final de cada encontro, antes
de encerrar a reunião** — registro feito depois, de memória, perde as
alternativas descartadas, que são a parte valiosa.

## Os três tipos de item

| Tipo | O que é | Como se resolve |
|:--------------|:----------------------------------------|:-------------------|
| **Decisão (D)** | Escolha já feita, com alternativa descartada | Já resolvida; só se revisa |
| **Lacuna (L)** | Escolha ainda não feita; trava trabalho | Alguém decide |
| **Pendência (P)** | Trabalho a fazer; a escolha já existe | Alguém executa |

A distinção importa: lacuna sem decisão trava pendência, e pendência sem dono
não fecha. Um item só vira decisão se tiver alternativa descartada — sem isso,
é pendência.

## Convenções

- Nada é apagado. Decisão revista recebe status `Substituída`, com referência
- Lacuna fechada vira decisão e sai da lista de lacunas, mantendo o ID original
  como referência cruzada
- Todo item tem dono e prazo, ou não é um item: é uma intenção

---
---

# 1. Painel de estado — as 20 seções

| # | Seção | Prazo | Situação | Responsável |
|:-----|:-------------------------------------|:-------|:-------------|:----------------|
| 1 | Apresentação do PAC e objetivos | — | Concluído | Professor |
| 2 | Buscar temas / tema | 18/08 | Concluído | Alunos |
| 3 | Problema e propósito | 18/08 | Concluído | Alunos |
| 4 | Público-alvo | 01/09 | Concluído | Alunos |
| 5 | Pesquisar jogos sérios | 01/09 | Concluído | Alunos |
| 6 | Conceito do jogo | 15/09 | Concluído | Alunos |
| 7 | Mecânicas e gameplay | 15/09 | Concluído | **sem dono** |
| 8 | Objetivos de aprendizagem | 29/09 | Em andamento | Giovanna e Karina |
| 9 | Requisitos funcionais e não funcionais | 06/10 | **Não iniciado** | **sem dono** |
| 10 | Histórias de usuário e backlog | 13/10 | **Não iniciado** | **sem dono** |
| 11 | Protótipo de UX | 13/10 | **Não iniciado** | **sem dono** |
| 12 | Modelar os dados | 27/10 | **Não iniciado** | **sem dono** |
| 13 | Arquitetura do software | 27/10 | **Não iniciado** | **sem dono** |
| 14 | Tecnologias e ferramentas | 27/10 | **Não iniciado** | **sem dono** |
| 15 | Metodologia de desenvolvimento | 27/10 | **Não iniciado** | **sem dono** |
| 16 | Padrões e boas práticas | 10/11 | **Não iniciado** | **sem dono** |
| 17 | Planejar testes e validação | Cíclico | **Não iniciado** | **sem dono** |
| 18 | Planejar o desenvolvimento | 24/11 | **Não iniciado** | **sem dono** |
| 19 | Consolidar documentação | 24/11 | **Não iniciado** | **sem dono** |
| 20 | Defesa e pitch final | 24/11 | **Não iniciado** | **sem dono** |

**Doze seções vazias, nenhuma com responsável, três semanas até 24/11.**
Atribuir dono a cada uma é o item mais urgente de todo este registro (P09).

---
---

# 2. Decisões tomadas

## 2.1 Índice

| ID | Decisão | Etapa | Status |
|:------|:---------------------------------------------|:-------|:-----------------|
| D01 | Produto é jogo sério com causa social explícita | E0 | Vigente |
| D02 | Coleta por formulário estruturado, não brainstorming | E1 | Vigente |
| D03 | Uma proposta por integrante na 1ª rodada | E1 | Substituída por D11 |
| D04 | Padronizar em ficha de conceito com marcação de origem | E2 | Vigente |
| D05 | Avaliar propostas isoladamente, sem matriz comparativa | E2 | Vigente |
| D06 | Separar fraqueza da ideia de fraqueza da descrição | E2 | Vigente |
| D07 | Fundir nove propostas em três frentes temáticas | E3 | Vigente |
| D08 | Remover autoria das frentes | E3 | Vigente |
| D09 | Web sem backend, sem login, sem servidor | E3 | **Substituída por D15** |
| D10 | Frente B com foco invertido e progresso cooperativo | E3 | Vigente (histórica) |
| D11 | Múltiplas propostas por integrante no desenho de jogo | E3 | Vigente |
| D12 | Linguagem da Frente C: Blockly com Python visível | E3 | Vigente (histórica) |
| D13 | Adoção da temática mercantil | E3 | Vigente |
| D14 | Multiplayer com convite simples | E3 | Vigente |
| D15 | Persistência compartilhada | E3 | Vigente |
| D16 | Público-alvo: 18 a 25 anos | E4 | Vigente |
| D17 | Verificar custa um dado | E4 | **Provisória** |
| D18 | Casas do nível 1: Porto, Entreposto, Alfândega | E4 | Vigente |
| D19 | Três modos: Travessia, Regata, Companhia | E4 | Vigente |
| D20 | Vitória por títulos; sem eliminação | E4 | Vigente |
| D21 | Dificuldade escala por sinais e ruído, nunca por valor | E4 | Vigente |
| D22 | Comparação por qualidade de decisão, não por saldo | E4 | Vigente |
| D23 | Identidade visual em pixel art, produzida pela equipe | E4 | Vigente |
| D24 | Três dados por dia, escolhíveis | E4 | Vigente |
| D25 | Corrida paralela; nenhum turno bloqueia | E4 | Vigente |
| D26 | Plataforma: web PWA; Capacitor como saída para loja | E5 | Vigente |
| D27 | Persistência em cinco níveis; documentar até o nível 3 | E5 | Vigente |
| D28 | Identidade anônima com código de jogador | E5 | Vigente |
| D29 | Semente no servidor; cliente deriva dados e cartas | E5 | Vigente |
| D30 | Geração de carta no cliente; trapaça aceita e documentada | E5 | Vigente |
| D31 | Janelas de evento em tempo de jogo, não em relógio | E5 | Vigente |
| D32 | Contratos com prazo em turnos | E5 | Vigente |
| D33 | Stack: TypeScript, React, Vite, SVG, Supabase | E5 | Vigente |
| D34 | Godot descartado, com motivo registrado | E5 | Vigente — reaberta e reconfirmada, ver D36 |
| D35 | Escopo do MVP congelado | E5 | Vigente |
| D36 | Engine reconfirmada: SVG e React, sem Godot | E5 | Vigente |
| D37 | Turno em duas fases: reconhecimento livre, depois ação | E5 | Vigente |

D01 a D12 estão detalhadas em `historico.md`, seção 6. As novas vêm abaixo.

## 2.2 Decisões novas, detalhadas

### D13 — Adoção da temática mercantil

**Contexto.** A proposta original ambientava o jogo no presente, com telas
imitando aplicativos. Surgiu a preocupação de que isso produziria produto datado.
Na análise, o argumento da obsolescência mostrou-se insuficiente — a superfície já
estava protegida pelo conteúdo em arquivo externo. Três outros argumentos
sustentaram a mudança: a era mercantil é onde os instrumentos financeiros
nasceram, o que amplia o conteúdo; a fraude a ensinar já existia lá; e o público
abre um jogo de mercadores, não uma cartilha.

**Decisão.** Ambientação mercantil fictícia, com três condições: ponte explícita
ao resolver cada carta, mundo inteiramente fictício, e instrumento de avaliação
sempre em linguagem contemporânea. Título de trabalho: **Selo Falso**.

**Alternativas descartadas.** Ambientação contemporânea com empresas fictícias;
transposição sem ponte explícita.

**Consequência.** Perde-se o gancho institucional com órgãos de defesa do
consumidor. Ganha-se adesão do público e a capacidade de ensinar seguro,
contrato, juros e aval naturalmente.

### D14 — Multiplayer com convite simples

**Contexto.** A estrutura de tabuleiro abriu sessões compartilhadas. Partida por
turnos entre amigos morre por abandono quando um jogador para.

**Decisão.** Multiplayer assíncrono; host cria a sessão e convida por código;
todos recebem o mesmo baralho, gerado por semente; cada um age no próprio ritmo.
Sem ranking público, sem matchmaking. Interação por reações predefinidas.
Três modos: Travessia (solo), Regata (2 a 8, competitivo) e Companhia
(cooperativo, nível 3).

**Alternativas descartadas.** P2P via WebRTC; turno alternado bloqueante; estado
dentro do link; chat de texto livre.

**Consequência.** Exige persistência compartilhada (D15). Fornece material real
para as seções 12 e 13.

### D15 — Persistência compartilhada

**Contexto.** A D09 estabelecia "sem backend", o que conflitava com as seções 12
e 13, que pedem banco, back-end e autenticação. A adoção do multiplayer tornou a
D09 inviável.

**Decisão.** Backend gerenciado em camada gratuita, com log de ações append-only
por sessão e estado derivado no cliente. Identidade anônima gerada no
dispositivo, sem e-mail nem senha.

**Alternativas descartadas.** Manter tudo local e abrir mão do multiplayer;
backend próprio hospedado pela equipe; autenticação com conta de usuário.

**Consequência.** Substitui a D09 e fecha a antiga pendência P07.

### D16 — Público-alvo: 18 a 25 anos

**Contexto.** Lacuna aberta desde agosto, travando objetivos de aprendizagem e
instrumento de avaliação.

**Decisão.** Jovens adultos, universitários e recém-ingressantes no mercado, em
transição para a autonomia financeira. O projeto não trabalha com menores, nem
como público, nem como participantes de teste.

**Alternativas descartadas.** Ensino médio de 15 a 18 — exigiria autorização de
responsáveis e aprovação ética fora do prazo; adultos de 26 a 45 — difíceis de
recrutar; 60 anos ou mais — incompatível com tabuleiro, múltiplos recursos e
sessões assíncronas.

**Consequência.** Elimina o risco ético e de prazo administrativo. Perde-se o
gancho curricular com a BNCC. A validação passa a acontecer na própria
instituição.

### D17 — Verificar custa um dado

**Contexto.** Sem custo, verificar é sempre a resposta certa e o jogo acaba na
primeira hora.

**Decisão.** A ação Verificar consulta o Registro do Porto e gasta um dado — o
mesmo recurso que move o jogador rumo à meta. Revela um ou dois sinais, nunca a
resposta.

**Alternativas descartadas.** Verificação gratuita; custo em moedas; custo em
tempo de rodada.

**Consequência.** Segurança e progresso competem pelo mesmo recurso, que é a
tensão central do jogo.

### D18 — Casas do nível 1

**Decisão.** Porto (rotina), Entreposto (oportunidade) e Alfândega (cobrança).
Demais tipos — imprevisto, feira, praça, alto-mar — no nível 2 de escopo.

**Alternativas descartadas.** Sete tipos de casa no primeiro jogável.

**Consequência.** Reduz o conteúdo mínimo. **Entra em conflito com o documento de
cartas, que usa Porto, Alto-mar, Entreposto e Praça** — ver L02.

### D19 a D25 — demais decisões de gameplay

| ID | Decisão | Alternativa descartada |
|:------|:---------------------------------------------|:-----------------------|
| D19 | Três modos como parâmetros da mesma sessão | Jogos separados por modo |
| D20 | Vitória por três títulos (Armador, Mestre da Guilda, Vigia do Porto); sem eliminação; falência gera empréstimo de resgate | Eliminação ao falir; vitória única por saldo |
| D21 | Dificuldade escala reduzindo sinais e aumentando ruído | Escalar aumentando o valor perdido |
| D22 | Comparação por qualidade de decisão ponderada pela dificuldade | Ranking por saldo final — premia quem arrisca e dá sorte |
| D23 | Pixel art produzida pelos integrantes; arte não é caminho crítico | Contratar ou terceirizar arte |
| D24 | Três dados por dia, rolados juntos, escolhíveis em ordem | Um dado por turno |
| D25 | Corrida paralela; nenhum turno bloqueia ninguém | Turno alternado |

---
---

### D36 — Engine reconfirmada: SVG e React

**Origem.** Reversão de posição. A D34 havia descartado o Godot por custo de
bundle e por só uma pessoa do grupo programar nele. Em 03/11 a questão foi
reaberta por um motivo diferente dos originais — animação e efeito gráfico — e o
argumento de regras compartilhadas, usado no descarte, foi retirado por ser
exagerado: validação em servidor não está no escopo.

**Decisão.** Mantida a stack da D33: TypeScript, React, Vite e SVG. O Godot fica
fora do primeiro e do segundo semestre.

**Como se decidiu.** Com evidência em vez de discussão. O protótipo
`prototypes/mapa-animado.html` entrega o mapa animado, o navio percorrendo a rota
pela própria curva do `<path>`, as casas reagindo e o ciclo das quatro janelas —
em 18 KB de SVG e CSS, sem engine, sem build e sem instalação. A dúvida que
reabriu a lacuna estava respondida na tela.

**Alternativas descartadas.**

- **Godot 4 com export para web.** Resolveria animação com folga e exporta PWA.
  Descartado porque o protótipo mostrou que a folga não é necessária, e porque o
  custo real não era técnico: a stack só seria programável por uma pessoa do
  grupo.
- **PixiJS desde já.** Fica registrado como degrau intermediário, não como
  escolha atual. Entra se aparecer necessidade concreta de partícula densa ou
  distorção de água — e, se entrar, não troca linguagem nem stack.

**Consequência.** As seções 17 do GDD e 13 e 14 do espelho permanecem válidas
como estão; nada precisa ser reescrito. Soma-se um critério de decisão que o
grupo pode reusar: **questão de viabilidade visual se resolve com protótipo
pequeno, não com reunião.** E um segundo ganho, que pesou na escolha: React e SVG
são o que os demais acadêmicos usam no resto do curso, então o aprendizado do PAC
se aproveita fora dele.

### D37 — Turno em duas fases

**Origem.** Proposta de integrante. O core loop começava no dado, o que deixava
implícito um momento que todo jogo de tabuleiro tem na mesa e que o digital
costuma esconder: olhar o estado antes de agir.

**Decisão.** O turno passa a ter duas fases. **Reconhecimento** — livre, sem custo
— em que o jogador consulta meta e ouro, dia, janela e prazos, contratos ativos,
eventos em vigor, itens na mochila, a própria posição na régua de reputação e a
última posição conhecida dos demais. **Ação** — a partir do dado, como já estava.

**Alternativas descartadas.**

- **Reconhecimento custando dado.** Descartado: puniria planejar. O recurso
  escasso precisa disputar entre *agir* e *verificar*, que é a tensão do jogo;
  pôr *pensar* na mesma disputa ensina a coisa errada.
- **Reconhecimento revelando algo da carta.** Descartado, e esta é a linha que
  não se cruza: viraria verificação de graça e derrubaria a primeira das quatro
  decisões de design. A exceção já existe e é paga — o item Informante.
- **Deixar implícito, sem seção própria.** Descartado porque informação que não
  está especificada não é implementada. O painel tem conteúdo definido e limites
  definidos, ou cada pessoa da equipe imagina um diferente.

**Consequência.** GDD seção 4 reescrita em 4.1, 4.2 e 4.3. Quatro requisitos
funcionais novos no espelho (RF34 a RF37). Abre a L13. Nenhuma das quatro
decisões de design é afetada: o placar duplo, o custo da verificação, o gerador
em três camadas e a meta escolhida continuam como estão.

# 3. Lacunas abertas — decisões que faltam

Ordenadas por impacto. As quatro primeiras travam seções inteiras.

| ID | Lacuna | Trava | Prazo | Quem decide |
|:------|:----------------------------------------|:-------------|:--------|:----------------|
| L05 | Banco relacional ou de documentos — de fato respondida por D33 (Postgres); formalizar | Seção 12 | 10/11 | Equipe técnica |
| L06 | Metodologia: Kanban ou Scrum adaptado | Seção 15 | 17/11 | Equipe |
| L07 | Natureza do molde: rótulo ou proporção | Cartas | 05/11 | Dupla de conteúdo |
| L08 | Entra a categoria "legítima e mau negócio"? | Cartas, OA2 | 05/11 | Dupla de conteúdo |
| L09 | Nome definitivo do jogo e do arquipélago | Seções 6 e 20 | 17/11 | Equipe |
| L10 | Quem revisa a correção do conteúdo financeiro | Seção 17 | 10/11 | Coordenação |
| L13 | O diário é consultável dentro da partida? | Seções 4 e 13 | 10/11 | Equipe |

## Lacunas fechadas em 03/11

| ID | Como fechou |
|:------|:--------------------------------------------------|
| L01 | D26, D27, D28 — web PWA, persistência em níveis, código de jogador |
| L02 | **O documento oficial tem prioridade.** Vale Porto, Entreposto e Alfândega (D18); o documento de cartas é que se ajusta |
| L03 | D35 — escopo do MVP congelado |
| L04 | D33 e D34 — stack definida, Godot descartado com motivo |
| L12 | D36 — engine reaberta por causa de animação, reconfirmada com protótipo na mão |

Detalhamento em `docs/05-entregas/decisoes-tecnicas-l01-l04.md`.

## Nova lacuna

**L11 — economia do jogo.** Quais recursos existem, o que cada ação custa, qual a
renda por rodada, e qual a razão entre custo de verificação e avanço. A D17 foi
reclassificada como provisória por isso: o princípio (verificar compete com
progresso) é firme, o número é arbitrário enquanto a economia não fechar. Não
trava arquitetura nem stack; trava balanceamento e requisitos finos. Tratada pela
pendência P21, com prazo anterior à implementação, não a 24/11.

**L13 — o diário dentro da partida.** Aberta pela D37. O diário guarda moldes já
identificados com os sinais que os caracterizam. Consultá-lo durante o turno é
exatamente o comportamento que o jogo quer ensinar — conferir antes de confiar —
e é também um atalho que entrega o molde sem gastar dado, contra o gerador de
três camadas, que existe para que a resposta venha do sinal e não da memória.

As duas leituras são defensáveis, e é por isso que é lacuna e não decisão. Há uma
saída intermediária a considerar: o diário consultável, mas listando **sinais sem
a resposta**, do mesmo jeito que a verificação revela sinal sem entregar o
veredito (RF12). Enquanto não se decide, o diário fica fora do painel de
reconhecimento.

---
---

# 4. Pendências abertas — trabalho a executar

| ID | Pendência | Bloqueia | Prazo | Responsável |
|:------|:--------------------------------------------|:---------------|:--------|:---------------|
| P09 | **Atribuir responsável às 12 seções vazias** | Tudo | **hoje** | Coordenação |
| P13 | Escrever as 24 cartas restantes (6 prontas de 30) | Seção 17, 2º sem. | 17/11 | 4 pessoas |
| P12 | Atribuir sinais e ruído às 60 premissas | P13 | 10/11 | Dupla de conteúdo |
| P10 | ~~Reconciliar nomes de casas~~ — resolvida por L02; vira P22 | — | — | — |
| P15 | Fechar a seção 8 formalmente | Seções 9, 17 | 05/11 | Giovanna e Karina |
| P11 | Corrigir plataforma na seção 6 | Seções 13, 14 | 10/11 | Coordenação |
| P06 | Definir revisor externo do conteúdo financeiro | Seção 17 | 10/11 | Coordenação |
| P16 | Preencher seção 1: nome da equipe, papéis, acordos | Seção 19 | 10/11 | Coordenação |
| P17 | Preencher "Evidências e anexos" das seções concluídas | Seção 19 | 17/11 | Coordenação |
| P18 | Escrever o instrumento de pré e pós-teste (12 itens contemporâneos) | Seção 17 | 17/11 | Giovanna e Karina |
| P19 | Registrar D13 a D25 em ata | Seção 19 | 10/11 | Coordenação |
| P20 | Montar o roteiro e a divisão de falas do pitch | Seção 20 | 17/11 | Equipe |
| P21 | Oficina de economia do jogo: recursos, custos, balanceamento | L11, implementação | antes de 2027/1 | Equipe |
| P22 | Ajustar o documento de cartas às casas do nível 1 (Alfândega) | P13 | 05/11 | Dupla de conteúdo |

## Pendências encerradas

| ID | Pendência | Como encerrou |
|:------|:-------------------------------------|:-----------------------------|
| P01 | Contato institucional para validação | Resolvida por D16 — validação na própria instituição |
| P02 | Proposta individual não submetida | Encerrada com o fim do prazo da 1ª rodada |
| P03 | Exigências para teste com menores | Resolvida por D16 — não há menores |
| P04 | Público-alvo indefinido | Fechada por D16 |
| P05 | Ritmo de uso: oficina ou diário | Resolvida nas seções 4, 6 e 7 — sessões curtas diárias em temporadas |
| P07 | Conflito entre D09 e as seções 12 e 13 | Resolvida por D15 |
| P08 | Divisão de frentes de trabalho | Substituída por P09, mais urgente |

---
---

# 5. Riscos registrados

| ID | Risco | Severidade | Mitigação |
|:------|:--------------------------------------|:-------------|:--------------------------|
| R01 | Escopo crescer além do prazo | Alta | Escada de escopo em níveis; L03 pendente |
| R04 | Produto virar aplicativo sem ser jogo | Alta | Resolvido pelo desenho atual; monitorar |
| R07 | Concentração de entregas em novembro | **Crítica** | P09; frentes em paralelo |
| R09 | **Doze seções sem responsável** | **Crítica** | P09 — resolver hoje |
| R10 | Nenhuma carta escrita até 03/11 | Alta | P12 e P13; 6 modelos prontos |
| R11 | Jogador decorar moldes em vez de ler sinais | Alta | L07 — converter natureza em proporção |
| R12 | Conteúdo produzido para casas fora do nível 1 | Média | L02 e P10, antes de escrever mais |
| R13 | Divergência entre documento oficial e repositório | Média | P19; este registro como fonte única |
| R14 | Evidências e anexos vazios na consolidação | Média | P17 |

---
---

# 6. O que precisa sair da reunião de hoje

**Decisões (lacunas a fechar):** L02 (nomes das casas), L07 (natureza como
proporção) e L08 (categoria legítima-mau-negócio). As três destravam a produção
de cartas, que é o gargalo do segundo semestre.

**Atribuições (P09):** dono para cada uma das doze seções vazias. Sem isso,
nenhuma outra decisão desta reunião produz efeito.

**Ratificações (P19):** registrar em ata D13 a D25, que já valem na prática mas
não estão formalizadas. Sem registro, a banca encontra o documento de arquitetura
pedindo banco de dados e a D09 dizendo que não haveria nenhum.

**Encaminhamento:** L01, L03, L04, L05 e L10 têm prazo 10/11 e podem ser
decididas pelas duplas responsáveis assim que P09 estiver resolvida.
