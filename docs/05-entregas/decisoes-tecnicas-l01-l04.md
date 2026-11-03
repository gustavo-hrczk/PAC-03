---
title: "PAC III — Selo Falso"
subtitle: "Decisões técnicas: plataforma, persistência, stack, MVP e sistema de turnos"
date: "03 de novembro de 2026"
lang: pt-BR
---

# Sumário das recomendações

| Item | Recomendação | Confiança |
|:--------|:-------------------------------------------------|:---------|
| L01 plataforma | Web PWA, com Capacitor como saída para loja depois | Alta |
| L01 persistência | Log de ações no servidor, em cinco níveis incrementais | Alta |
| L01 correspondência | O modelo chess.com se aplica, com duas ressalvas sérias | Alta |
| L02 casas | Adotado: documento oficial tem prioridade | — |
| L04 stack | TypeScript + React + Vite + Supabase; tabuleiro em SVG | Alta |
| L04 engine | **Não usar Godot neste projeto** | Média-alta |
| MVP | Três casas, mapa único, ciclo de ações, 20 cartas | Alta |
| Janelas de evento | **Em tempo de jogo, não em relógio real** | Alta |
| D17 custo | Reclassificada como provisória; oficina de economia pendente | — |

---
---

# 1. D17 — custo da verificação volta a ser lacuna

Aceito e registrado. A D17 estava marcada como decidida porque o documento
oficial descreve "Verificar — gastar um dado", mas o sistema de recursos e custos
não foi fechado, e sem ele o número é arbitrário.

**Reclassificação:** D17 passa a **provisória**. O que permanece firme é o
princípio — *verificar consome um recurso que compete com o progresso* —, porque
é ele que sustenta o objetivo de aprendizagem. Qual recurso e quanto é questão de
balanceamento.

**O que isso trava e o que não trava.** Não trava arquitetura, modelo de dados nem
stack: o log de ações registra `verificar` independentemente do custo. Trava os
requisitos funcionais na granularidade fina e o balanceamento, que é trabalho de
2027/1.

**Nova pendência P21 — oficina de economia do jogo.** Uma sessão dedicada a fechar:
quais recursos existem, o que cada ação custa, qual a renda por rodada, e qual a
razão entre custo de verificação e avanço. Sugestão de prazo: antes do início da
implementação, não antes da entrega de 24/11.

---
---

# 2. L01 — plataforma

## 2.1 As três opções, com trade-offs reais

| | **Web PWA** | **Nativo (RN/Flutter)** | **Híbrido (Capacitor)** |
|:---|:---|:---|:---|
| Como o jogador entra | Abre um link | Baixa da loja | Abre link ou baixa |
| Atrito para validar | **Nenhum** | Alto | Nenhum na web |
| Bases de código | Uma | Uma, com dois builds | Uma |
| Publicação em loja | Não | Sim | Sim, depois |
| Notificação fora do app | Android sim; iOS só se instalado na tela inicial | Plena | Plena |
| Revisão de loja antes da defesa | Não se aplica | **Risco de prazo** | Não se aplica |
| Pixel art e som | Suficiente | Suficiente | Suficiente |
| Conhecimento exigido da equipe | Menor | Maior | Menor |

## 2.2 Recomendação: Web PWA

Três razões decisivas, nesta ordem:

**1. A validação depende de atrito zero.** O público é de 18 a 25 anos na própria
instituição. Pedir que instalem um aplicativo de loja para um teste de 40 minutos
derruba a taxa de participação. Um link funciona em qualquer celular, na hora.

**2. Loja introduz risco de prazo que não se controla.** Revisão da App Store leva
de dias a semanas e pode reprovar por motivos que não têm a ver com o jogo. Num
cronograma que já está apertado, isso é risco desnecessário.

**3. PWA já entrega o essencial do "abrir no navegador ou no celular".** O jogador
abre no navegador do celular, e pode adicionar à tela inicial — passando a ter
ícone, tela cheia e inicialização sem barra de endereço. É a mesma base de código.

**A saída de emergência:** Capacitor empacota a mesma aplicação web como
aplicativo nativo depois, sem reescrever nada. Se em 2027 a equipe quiser loja, o
caminho existe. Documentar isso como decisão é o que diferencia a entrega da
seção 13 — mostra que a escolha foi consciente e reversível.

**A ressalva honesta:** notificação fora do aplicativo é o ponto fraco. No iOS só
funciona se o jogador adicionar à tela inicial. Para um jogo de correspondência
isso importa, e a mitigação é pedir a instalação na tela inicial no primeiro
acesso, explicando o porquê. Não é perfeito, e deve constar como limitação.

**Corrige a inconsistência:** a seção 6 do documento oficial registra "Mobile" e a
seção 4 descreve "jogo web para celular". A decisão é **web mobile (PWA)**, e a
seção 6 precisa ser corrigida.

---
---

# 3. L01 — persistência de sessão

## 3.1 Os cinco níveis, com esforço

Pensar em níveis evita a pergunta errada ("quanto custa fazer multiplayer?") e
permite escolher onde parar.

| Nível | O que entrega | Esforço | Depende de |
|:---|:------------------------------------------|:-----------|:---------|
| 0 | Solo local; fecha e reabre no mesmo aparelho | 2 dias | — |
| 1 | Sessão no servidor; log de ações; código de convite | 1 a 2 semanas | nível 0 |
| 2 | Acompanhar o progresso alheio em tempo real, com o app aberto | 2 a 3 dias | nível 1 |
| 3 | Continuidade entre dispositivos | 2 a 3 dias | nível 1 |
| 4 | Notificação fora do aplicativo | 1 semana | nível 1 |
| 5 | Validação de regras no servidor | 2 semanas | nível 1 + módulo compartilhado |

**Para a entrega de 24/11, documentar até o nível 3 e planejar 4 e 5.** Para a
implementação de 2027/1, níveis 0 a 3 são o alvo realista; 4 e 5 entram se sobrar.

## 3.2 Como funciona o nível 1, concretamente

Três tabelas e uma regra de acesso:

```
sessao        (id, codigo_convite, semente, config, criada_em)
participante  (id, sessao_id, chave_dispositivo, apelido, entrou_em)
acao          (id, sessao_id, participante_id, rodada, tipo, dados, criada_em)
```

`acao` é **append-only**: nada é atualizado nem apagado. Saldo, posição, placar e
progresso da meta são **derivados** da leitura do log. Isso já é o que a
arquitetura acordada descreve, e é a razão pela qual a sincronização fica trivial:
não há conflito a resolver, só ordem de chegada.

## 3.3 Continuidade entre dispositivos — o detalhe que costuma passar

Com identidade anônima presa ao dispositivo, abrir no notebook cria **outro
jogador**. Para o mesmo jogador continuar em outro aparelho, há três caminhos:

| Caminho | Como funciona | Custo | LGPD |
|:-----------|:----------------------------|:------|:------|
| Código de jogador | O jogador copia um código e cola no outro aparelho | Baixo | Nenhum |
| Login com e-mail | Conta de verdade | Médio | Reabre |
| Login social | Google ou similar | Médio | Reabre |

**Recomendação: código de jogador.** Mantém a identidade anônima, custa pouco, e
não reabre a discussão de dado pessoal — que foi justamente o que a decisão D16
e a arquitetura sem login eliminaram. A desvantagem é real e deve ser documentada:
quem perde o código perde o progresso.

---
---

# 4. L01 — o modelo chess.com, validado

## 4.1 O que você pensou está certo, e já é o que está desenhado

Partida por correspondência em chess.com funciona assim: o **servidor é a fonte da
verdade**, cada lance é gravado como registro, o estado do tabuleiro é derivado da
sequência de lances, o jogador pode estar ausente por dias, e quando está presente
recebe atualização ao vivo por assinatura.

Isso é exatamente o log de ações append-only com estado derivado. **A intuição e a
arquitetura coincidem**, o que é um bom sinal. Dois ganhos herdados do modelo:

- Nenhum jogador trava outro: lance registrado é lance aplicado
- Histórico completo da partida fica disponível — e aqui vira instrumento de
  avaliação de aprendizagem, não só replay

## 4.2 Duas diferenças que mudam o projeto

Xadrez tem duas propriedades que este jogo não tem, e ignorá-las custa caro.

**Diferença 1 — xadrez não tem aleatoriedade.** Aqui há dados e geração de cartas.
Se o cliente rola o dado, trapacear é trivial: basta recarregar até sair o número
desejado.

*Solução:* a **semente vem do servidor** e dados e cartas são derivados dela de
forma determinística. O cliente não sorteia nada; calcula a partir da semente
`sessao.semente + rodada + participante`. Isso é barato, e já estava previsto na
decisão de geração determinística — mas precisa estar explícito no modelo de
dados, senão a implementação faz errado.

**Diferença 2 — xadrez não tem informação oculta.** Em xadrez, todo o estado é
público. Aqui, a natureza da carta e os sinais revelados por verificação são
informação que o jogador não deveria ter de graça.

E aqui está o problema que precisa ser dito com clareza: **se a geração de cartas
roda no cliente, um jogador curioso consegue inspecionar o código e saber a
resposta de qualquer carta.** Determinismo é ótimo para sincronizar e péssimo para
esconder.

Três respostas possíveis:

| Resposta | Custo | Efeito |
|:--------------------------|:-------|:------------------------|
| Aceitar e documentar | Zero | Trapacear só prejudica quem trapaceia: o objetivo é aprender, e a nota do jogo não vale nada fora dele |
| Gerar carta no servidor e enviar só o texto | 1 semana | Resolve, mas exige servidor ativo a cada carta |
| Ofuscar o conteúdo no cliente | Alguns dias | Atrasa o curioso, não impede ninguém |

**Recomendação: aceitar e documentar como limitação conhecida**, com a geração no
servidor registrada como evolução. É uma resposta honesta e defensável — e a
justificativa ("quem burla o jogo perde o único benefício que ele oferece, que é
aprender a reconhecer fraude") é exatamente o tipo de raciocínio que a seção 13
pede no campo "justificativas das decisões".

Exceção que merece tratamento: no modo **Regata**, competitivo, com depósito de
isca entre jogadores, trapaça passa a ter consequência sobre terceiros. Se a
Regata entrar no nível 2 de escopo, a geração de carta no servidor sobe de
prioridade junto com ela.

---
---

# 5. Sistema de turnos, contratos e janelas de evento

Esta é a parte da sua mensagem que mais precisa de validação, porque tem uma
contradição interna que é fácil de não ver.

## 5.1 O que funciona bem

**Contratos com prazo em turnos.** Excelente. Dá consequência temporal real, cria
tensão entre aceitar agora e esperar melhor, e amarra o conteúdo financeiro —
prazo é a essência de contrato, crédito e frete. Isso **valida** sem ressalva.

**Oportunidades que alteram valores de contratos ativos.** Também funciona: faz o
jogador reavaliar decisões já tomadas, que é mais interessante do que só decidir
uma vez. E é temático: preço de especiaria oscila mesmo.

**Quatro janelas ao longo do dia.** A estrutura de quatro fases é boa: dá ritmo,
dá previsibilidade com variação, e cria "momentos" na partida.

## 5.2 A contradição — janelas em relógio real

Amarrar as janelas a horários do relógio cria três problemas, e o primeiro é grave.

**Problema 1 — contradiz a tese do jogo.** O objetivo de aprendizagem central é
que **pressa é o sinal**: urgência artificial é o indício número um de golpe, e o
jogo existe para ensinar a desacelerar e verificar. Um sistema que obriga o
jogador a abrir o aplicativo às 12h para não perder a oportunidade **fabrica
exatamente a urgência que o jogo condena**. É incoerente, e um avaliador atento
vai apontar isso.

**Problema 2 — torna o jogo impossível de validar.** O instrumento de avaliação
é uma sessão de pré e pós-teste. Não dá para testar uma estrutura de quatro
janelas diárias numa sessão de 40 minutos se as janelas dependem do relógio. Seria
preciso acompanhar os participantes por dias, o que não cabe no prazo nem no
método.

**Problema 3 — injustiça por agenda no modo competitivo.** Na Regata, quem tem
aula das 8h às 18h perde janelas que o colega de turno da noite pega. A derrota
passa a vir do horário, não da decisão — e isso fere a decisão D22, que define
comparação por qualidade de decisão.

## 5.3 A solução: janelas em tempo de jogo

**As quatro janelas são posições no ciclo do dia, não horas do relógio.**

O "dia" do jogo avança conforme o jogador gasta suas ações. Com três dados e
quatro janelas, a estrutura fica assim:

```
Amanhecer  →  [ação]  →  Meio-dia  →  [ação]  →  Tarde  →  [ação]  →  Anoitecer
   ↑                                                                      ↓
   └──────────────── novo dia, recursos recompostos ←─────────────────────┘
```

Cada janela tem perfil próprio e previsível, que o jogador aprende:

| Janela | Perfil | O que favorece |
|:-----------|:-------------------------------|:-----------------------|
| Amanhecer | Rotina, renda, contratos chegando | Planejar |
| Meio-dia | Pico de oportunidades e de golpes | Decidir |
| Tarde | Preços oscilam; contratos vencem | Ajustar |
| Anoitecer | Cobranças; prazos finais | Pagar o que deve |

Vantagens: todo jogador vive as quatro janelas independentemente do horário; o
ciclo é testável numa sessão única; a previsibilidade do perfil vira estratégia
aprendível; e a urgência existe **dentro da ficção** sem apressar a pessoa real.

**O detalhe que preserva a lição:** a carta pode dizer "decida antes que o navio
zarpe com a maré", e o jogador continua tendo todo o tempo do mundo para pensar.
Urgência ficcional, tempo real ilimitado. É a mesma solução usada no desenho
original.

## 5.4 Se a equipe quiser mesmo tempo real

Há um meio-termo que não quebra nada: **oportunidades não expiram de uma vez, elas
decaem.** Quem está presente na janela pega o preço cheio; quem chega depois pega
pior, mas pega. Presença vira vantagem, ausência não vira punição.

E, se for adotado, que seja **configurável na criação da partida**, como você
propôs, com o padrão em tempo de jogo. Assim a validação acadêmica usa o modo
testável e os amigos podem usar o modo com relógio.

**Recomendação para a documentação:** janelas em tempo de jogo no MVP; janelas em
relógio real como opção de configuração no nível 3 de escopo.

---
---

# 6. L04 — stack

## 6.1 O que este jogo realmente é, tecnicamente

Antes de escolher, vale enxergar a natureza do produto: **cerca de 90% das telas
são interface, não cena de jogo.** Cartas, decisões, recursos, resultado, lista de
sessões, diário, mercado — tudo isso é leitura de texto e toque em botão. Só o
mapa é "de jogo", e mesmo ele é um percurso estático com um peão que se move entre
posições discretas.

Não há física, não há renderização em tempo real, não há animação contínua, não há
colisão. Isso exclui a necessidade de engine de jogo e muda a resposta.

## 6.2 Comparação

| | **React + TS** | **Phaser** | **Godot (web)** |
|:---|:---|:---|:---|
| Telas de interface | Excelente | Ruim | Razoável |
| Mapa e sprites | Bom via SVG/canvas | Excelente | Excelente |
| Pixel art | Suficiente | Ótimo | Ótimo |
| Tamanho do pacote | Pequeno | Médio | **Grande (dezenas de MB)** |
| Navegador móvel | Ótimo | Bom | **Fraco, sobretudo iOS** |
| Regras compartilhadas cliente/servidor | **Sim, mesmo código** | Sim | Não |
| Integração com Supabase | Nativa | Nativa | Manual, via HTTP |
| Quantas pessoas da equipe podem contribuir | Mais | Menos | **Uma** |
| Material em português | Muito | Médio | Muito |

## 6.3 Recomendação

**TypeScript + React + Vite, tabuleiro em SVG, Supabase para persistência,
Capacitor como saída futura para loja.**

O argumento decisivo não é desempenho, é **o módulo de regras compartilhado**.
Escrevendo as regras em TypeScript, o mesmo código roda no cliente (para resposta
imediata) e no servidor (para validar, quando o nível 5 chegar). Nenhuma outra
opção dá isso. Sem ele, as regras seriam implementadas duas vezes, em linguagens
diferentes, e divergiriam.

Segundo argumento: **quantas pessoas podem contribuir**. A equipe tem sete
integrantes com experiência desigual. React tem a maior base de material em
português e o menor custo de entrada.

## 6.4 Sobre Godot — e aqui preciso ser direto

Você conhece Godot e tem pipeline de pixel art nele. A tentação é usá-lo, e eu
recomendo que não, neste projeto, por três motivos:

**O export web é o ponto fraco do Godot.** O pacote fica na casa das dezenas de
megabytes, o carregamento em 4G é lento, e o comportamento em Safari móvel é
historicamente instável quanto a áudio e entrada por toque. Isso colide
frontalmente com a decisão de plataforma — "abrir um link e jogar" é o que torna a
validação possível.

**Quebra a paralelização, que é o pilar organizacional do projeto.** Só você
programaria. O argumento que sustenta a viabilidade com sete pessoas é que o
trabalho se divide; com Godot, a divisão some.

**O jogo não precisa de engine.** Não há nada na lista de mecânicas que exija o
que uma engine oferece. Usar Godot aqui é pagar o custo de uma ferramenta pesada
pelo benefício de um tabuleiro estático.

**Quando Godot seria a escolha certa:** se o projeto fosse nativo desde o início,
ou se tivesse animação e efeitos como parte da proposta. Vale registrar isso como
alternativa descartada com motivo — é exatamente o que a seção 14 pede.

## 6.5 Stack completa, para a seção 14

| Camada | Escolha | Justificativa |
|:-------------|:---------------|:-----------------------------------|
| Linguagem | TypeScript | Regras compartilhadas cliente/servidor; erro aparece antes de rodar |
| Interface | React | 90% do produto é interface; maior base de material; mais gente contribui |
| Build | Vite | Configuração mínima; saída estática |
| Tabuleiro | SVG | Mapa estático com peão discreto; escala sem perda; sprites de pixel art como imagem |
| Estado | Redutor próprio sobre o log | A arquitetura já é um log; biblioteca de estado não acrescenta |
| Persistência remota | Supabase | Postgres gerenciado, assinatura em tempo real, camada gratuita, sem servidor a manter |
| Persistência local | IndexedDB | Retomar partida sem rede |
| Empacotamento | PWA; Capacitor como opção | Link para validar; loja depois, sem reescrever |
| Hospedagem | Vercel ou GitHub Pages | Gratuito, saída estática, deploy por push |
| Versionamento | Git e GitHub | Histórico rastreável |
| Backlog | GitHub Projects | Integrado ao repositório |
| Wireframe | Figma | Gratuito, colaborativo |
| Arte | Aseprite ou Piskel | Pixel art; Piskel é gratuito e roda no navegador |
| Conteúdo | JSON em arquivo externo | Não-programador edita carta sem tocar em código |

---
---

# 7. MVP — escopo congelado (L03)

Sua definição, formalizada. Lembrando que neste semestre o MVP é **especificado**;
construído em 2027/1.

## 7.1 Dentro

- **Mapa único**, percurso fechado, com uma bifurcação
- **Três tipos de casa:** Porto (rotina), Entreposto (oportunidade), Alfândega
  (cobrança) — conforme L02, seguindo o documento oficial
- **Ciclo de ações:** três dados por dia, escolhíveis em ordem
- **Quatro janelas em tempo de jogo:** amanhecer, meio-dia, tarde, anoitecer
- **Contratos com prazo em turnos**, que podem ter valor alterado por eventos
- **Carta ao parar na casa**, com as ações agir, ignorar e verificar
- **Vinte cartas** cobrindo as quatro faixas de dificuldade e os dois lados
- **Placar duplo** visível durante a partida
- **Ponte para hoje** na primeira vez de cada molde
- **Uma meta** escolhida no início, com condição de vitória
- **Modo Travessia (solo)**, construído como sessão de um participante
- Persistência **nível 0 a 1**: retomar partida e sessão no servidor

## 7.2 Fora

- Modos Regata e Companhia
- Golpe entre jogadores
- Mercado e itens
- Diário do mercador
- Janelas em relógio real
- Tipos de casa além dos três
- Notificação fora do aplicativo
- Validação de regras no servidor
- Empréstimo entre jogadores

## 7.3 O corte mais importante

Modo solo no MVP, **mas com a arquitetura de sessão desde a primeira linha de
código**. Não é "fazer solo e depois adicionar multiplayer" — é fazer sessão de um
participante. Essa distinção é o que decide se 2027/1 é viável.

---
---

# 8. Decisões a registrar hoje

| ID | Decisão | Substitui |
|:-----|:------------------------------------------|:---------|
| D26 | Plataforma: web PWA; Capacitor como saída para loja | Corrige seção 6 |
| D27 | Persistência em cinco níveis; documentar até o 3 | — |
| D28 | Identidade anônima com código de jogador para outro aparelho | — |
| D29 | Semente no servidor; cliente deriva dados e cartas | — |
| D30 | Geração de carta no cliente; trapaça aceita e documentada | — |
| D31 | Janelas de evento em tempo de jogo, não em relógio real | — |
| D32 | Contratos com prazo em turnos | — |
| D33 | Stack: TypeScript, React, Vite, SVG, Supabase | — |
| D34 | Godot descartado, com motivo registrado | — |
| D35 | Escopo do MVP congelado conforme seção 7 | Fecha L03 |
| D17 | **Reclassificada como provisória** | — |

**Lacunas fechadas:** L01, L03, L04. L02 fechada por adoção do documento oficial.

**Lacunas que permanecem:** L05 (banco relacional ou documento — respondida de
fato pela escolha de Supabase, que é Postgres; formalizar), L06 (metodologia),
L09 (nome do jogo e do arquipélago), L10 (revisor de conteúdo financeiro).

**Nova pendência P21:** oficina de economia do jogo — recursos, custos e
balanceamento. Antes da implementação, não antes de 24/11.
