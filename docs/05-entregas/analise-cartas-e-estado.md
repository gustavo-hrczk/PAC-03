---
title: "PAC III — Selo Falso"
subtitle: "Análise do conteúdo de cartas e correção do estado do projeto"
date: "03 de novembro de 2026"
lang: pt-BR
---

# 1. Correção do estado — o plano anterior estava desatualizado

O documento oficial do PAC mostra que o projeto está **mais avançado em design e
menos avançado em documentação** do que o plano de recuperação supunha.

## 1.1 O que já estava fechado e eu tratei como lacuna

| Lacuna que eu apontei | Situação real |
|:--------------------------------|:--------------------------------------|
| L1 — Faixa etária | **Fechada: 18 a 25 anos.** Jovens adultos universitários e recém-ingressantes no mercado. Menores foram descartados explicitamente, para evitar autorização de responsáveis e aprovação ética |
| L2 — Custo da verificação | **Fechada: custa um dado** — o mesmo recurso que move o jogador rumo à meta |
| L3 — Tipos de casa | **Fechada para o nível 1:** Porto (rotina), Entreposto (oportunidade), Alfândega (cobrança). Demais no nível 2 |
| Temática mercantil | **Aprovada.** Título de trabalho "Selo Falso" |
| Multiplayer | **Aprovado**, em três modos: Travessia (solo), Regata (2 a 8, competitivo) e Companhia (cooperativo, nível 3) |

Além disso, já estão definidos: condições de vitória por três títulos (Armador,
Mestre da Guilda, Vigia do Porto), ausência de eliminação, falência tratada por
empréstimo de resgate, escalada de dificuldade em quatro faixas, e identidade
visual em pixel art produzida pelos próprios integrantes.

**M08 está praticamente concluído.** OA1 a OA6 já têm mecânica relacionada,
evidência de aprendizagem e forma de avaliação, sob responsabilidade de Giovanna
e Karina. O que falta é ajuste fino, não construção.

## 1.2 O que está pior do que eu supunha

O meu plano registrou M09, M10 e M11 como "em andamento". **No documento oficial
os três estão "Não iniciado"**, com responsável "Preencher".

Situação real das seções 9 a 20: **doze seções inteiramente vazias**, todas
marcadas "Não iniciado", nenhuma com responsável atribuído. São três semanas
para preencher doze seções.

## 1.3 Duas inconsistências a resolver

**Plataforma.** A seção 6 registra "Mobile"; a seção 4 descreve "jogo web para
celular". São coisas diferentes na hora de escrever M13 e M14 — aplicativo nativo
e web em celular têm arquitetura e stack distintas. A arquitetura acordada
(navegador, sem instalação) aponta para **web mobile**, e a seção 6 deveria dizer
isso.

**Nomes das casas.** O documento de cartas usa Porto, Alto-mar, Entreposto e
Praça. O documento oficial define, para o nível 1, Porto, Entreposto e
**Alfândega** — que não existe na matriz de cartas —, enquanto Alto-mar e Praça
aparecem só no nível 2. Antes de escrever mais carta, os dois documentos precisam
usar o mesmo conjunto.

---
---

# 2. O documento de cartas — avaliação

## 2.1 O que ele é

Uma matriz de **15 moldes × 4 casas = 60 premissas**, consistentes com o mundo e
com bom pareamento entre molde e lugar. Já convertida para
`content/cards/premissas.json`.

É material sólido e vale ser dito com clareza: **é a camada 1 das 3**. O gerador
precisa de molde, preenchimento e sinal; o documento entrega molde e contexto.

## 2.2 O que falta em cada premissa

| Camada | Situação |
|:----------------------|:-------------------------------|
| Molde e contexto | Pronto |
| Preenchimento (vocabulário: nome, valor, prazo, casa comercial) | Ausente |
| Sinais presentes | Ausente |
| Ruído nas legítimas | Ausente |
| Resposta correta | Ausente |
| Consequência dos três resultados | Ausente |
| Ponte para hoje | Ausente |
| Faixa de dificuldade | Ausente |

## 2.3 O problema de design que a matriz revela

A coluna **Natureza** classifica o molde inteiro: nove são "pode ser legítima ou
golpe", quatro "quase sempre golpe", um "sempre golpe" e um "geralmente legítima".

Isso entra em tensão direta com a regra que sustenta o projeto — *a resposta
correta deriva dos sinais presentes, nunca do texto*. Se a natureza está colada ao
molde, o jogador decora o molde: vê "investimento com retorno garantido" e recusa
sem ler. Nesse ponto o gerador de três camadas perde a função.

**Não é para eliminar os moldes sempre-golpe.** Alguns são legítimos como lição:
retorno garantido sem risco realmente não existe, e aprender essa regra é
aprendizado válido. O problema é a proporção.

**Recomendação:** tratar Natureza como **distribuição**, não como rótulo.

| Natureza atual | Moldes | Proposta |
|:-------------------------|:-------|:-----------------------------|
| Pode ser legítima ou golpe | 9 | Manter, com proporção explícita (ex.: 50/50) |
| Quase sempre golpe | 4 | Reduzir para 2; os outros 2 viram mistos com 70/30 |
| Sempre golpe | 1 | Manter — é a lição em si |
| Geralmente legítima | 1 | Manter, com proporção 80/20 |

Com isso, pelo menos doze dos quinze moldes aparecem nos dois lados, e o jogador
não consegue decidir pelo molde.

## 2.4 O que já foi feito aqui

Seis cartas completas, escritas a partir das premissas, em
`content/cards/`. Servem de modelo e cobrem a variação necessária:

| Carta | Molde | Casa | Natureza | Faixa | O que demonstra |
|:---|:---|:---|:---|:---|:---|
| 001 | Cobrança em atraso | Porto | legítima | média | Ruído sem sinal |
| 002 | Reembolso pendente | Praça | fraude | inicial | Quatro sinais acumulados |
| 003 | Recadastro | Porto | fraude | alta | Premissa verdadeira, procedimento falso |
| 004 | Empréstimo | Entreposto | legítima | alta | Legítima e ainda assim mau negócio |
| 005 | Encomenda retida | Alto-mar | fraude | média | Taxa antecipada |
| 006 | Investimento garantido | Praça | fraude | inicial | O molde sempre-golpe, com nota de design |

A carta **003** é a mais importante do conjunto e merece ser lida em voz alta na
reunião: o recadastro existe de verdade, mas o Registro nunca pede o selo em
mãos. Ela ensina que a pergunta certa não é "isso pode acontecer?", e sim "por
qual canal isso deveria chegar?".

A carta **004** demonstra algo que a matriz ainda não previa: **cartas legítimas
que são mau negócio**. Recusá-las não é erro por desconfiança, e verificá-las
gasta um dado à toa — o que alimenta a métrica de OA2 (verificar quando havia
poucos sinais).

---
---

# 3. Pipeline de produção proposto

```
premissas.json        →  carta escrita    →  molde formalizado  →  gerador
15 moldes × 4 casas      NNN-molde-casa.md    regras + slots       2027/1
      PRONTO                 6 de 30            não iniciado      2º semestre
```

**Quem faz o quê, sem depender de código:**

| Tarefa | Depende de quê | Quem pode fazer |
|:---------------------------------|:--------------|:------------------|
| Atribuir sinais a cada premissa | Nada | Qualquer integrante |
| Escrever ruído das legítimas | Nada | Qualquer integrante |
| Escrever as 24 cartas restantes | Modelo pronto | Quatro pessoas em paralelo |
| Escrever as pontes por molde | Pesquisa leve | Dupla de conteúdo |
| Montar vocabulários | Cartas escritas | Dupla de conteúdo |

Vinte e quatro cartas, divididas por quatro pessoas, são seis cartas por pessoa.
Pelo modelo pronto, cada uma leva cerca de quinze minutos.

---
---

# 4. Recomendações para a reunião

**Sobre as cartas:**

1. Reconciliar os nomes das casas entre os dois documentos antes de escrever mais
2. Converter Natureza de rótulo para proporção, conforme a tabela da seção 2.3
3. Adotar o formato das seis cartas-modelo e distribuir as 24 restantes
4. Acrescentar à matriz a categoria "legítima e mau negócio", que hoje não existe

**Sobre o estado do projeto:**

5. Corrigir a plataforma na seção 6 para web mobile, ou justificar nativo
6. Atribuir responsável a cada uma das doze seções vazias — é o que mais trava
7. Fechar M08 formalmente; está a um ajuste de pronto
8. Registrar em ata as decisões já tomadas na prática: temática, multiplayer e
   persistência compartilhada

**O que eu posso preencher a partir do que já está decidido:** M09 (requisitos),
M10 (histórias e backlog), M12 (dados), M13 (arquitetura), M14 (tecnologias),
M15 (metodologia) e M16 (padrões). Com público, custo da verificação, casas,
modos de jogo e condições de vitória já definidos, essas sete seções são
derivação, não criação.
