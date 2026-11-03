# Selo Falso — Game Design Document

**Mar das Sete Bandeiras** · Versão 1.0 · 3 de novembro de 2026

> **Este documento substitui os anteriores.** Consolida o brainstorm da Frente A, o
> Anexo I temático, as decisões técnicas e as decisões de 03/11. Brainstorm e anexo
> passam a ser material de arquivo.

## Controle do documento

| Campo | Conteúdo |
|:------|:---------|
| Projeto | PAC III — Jogo Sério |
| Instituição | Centro Universitário Católica de Santa Catarina — Jaraguá do Sul |
| Orientação | Luiz Almeida Junior |
| Equipe | Beatrice Fischer, Gabriele Maria Freiberger, Giovanna Lopes Pontes, Gustavo Hreczuck, Karina Medeiros, Lucas de Carvalho Ziele, Raul Schmitz |
| Título | Selo Falso *(provisório)* |
| Mundo | Mar das Sete Bandeiras *(provisório)* |
| Versão | 1.0 |

## Índice

- [1. Visão geral](#1-visão-geral)
  - [1.1 Conceito](#11-conceito)
  - [1.2 A tese de design](#12-a-tese-de-design)
  - [1.3 Ficha técnica](#13-ficha-técnica)
  - [1.4 Público-alvo](#14-público-alvo)
  - [1.5 O problema](#15-o-problema)
- [2. O mundo](#2-o-mundo)
  - [2.1 Regra de contenção](#21-regra-de-contenção)
  - [2.2 As instituições](#22-as-instituições)
  - [2.3 Correspondência com a realidade](#23-correspondência-com-a-realidade)
- [3. Objetivos de aprendizagem](#3-objetivos-de-aprendizagem)
  - [3.1 Os objetivos](#31-os-objetivos)
  - [3.2 Matriz objetivo × mecânica × medição](#32-matriz-objetivo--mecânica--medição)
  - [3.3 Instrumento de avaliação](#33-instrumento-de-avaliação)
- [4. Core loop](#4-core-loop)
  - [4.1 O turno em duas fases](#41-o-turno-em-duas-fases)
  - [4.2 O que o reconhecimento mostra](#42-o-que-o-reconhecimento-mostra)
  - [4.3 Os limites do reconhecimento](#43-os-limites-do-reconhecimento)
- [5. O tabuleiro](#5-o-tabuleiro)
  - [5.1 Natureza](#51-natureza)
  - [5.2 Tipos de casa](#52-tipos-de-casa)
  - [5.3 Bifurcação](#53-bifurcação)
  - [5.4 Janelas do dia](#54-janelas-do-dia)
  - [5.5 Eventos de rodada](#55-eventos-de-rodada)
- [6. Dados e ações](#6-dados-e-ações)
  - [6.1 Os dados](#61-os-dados)
  - [6.2 O dado como recurso duplo](#62-o-dado-como-recurso-duplo)
- [7. As cartas](#7-as-cartas)
  - [7.1 O problema a resolver](#71-o-problema-a-resolver)
  - [7.2 Arquitetura em três camadas](#72-arquitetura-em-três-camadas)
  - [7.3 Os dez sinais](#73-os-dez-sinais)
  - [7.4 Os quinze moldes e a proporção](#74-os-quinze-moldes-e-a-proporção)
  - [7.5 Ruído](#75-ruído)
  - [7.6 Legítima e mau negócio](#76-legítima-e-mau-negócio)
  - [7.7 Faixas de dificuldade](#77-faixas-de-dificuldade)
  - [7.8 Determinismo](#78-determinismo)
- [8. Ações sobre a carta](#8-ações-sobre-a-carta)
  - [8.1 As quatro ações](#81-as-quatro-ações)
  - [8.2 Por que denunciar importa](#82-por-que-denunciar-importa)
  - [8.3 Canais de denúncia](#83-canais-de-denúncia)
  - [8.4 Custo e localização](#84-custo-e-localização)
- [9. Economia](#9-economia)
  - [9.1 Recursos](#91-recursos)
  - [9.2 Contratos](#92-contratos)
  - [9.3 A feira — loja de itens](#93-a-feira--loja-de-itens)
  - [9.4 Itens](#94-itens)
- [10. Reputação](#10-reputação)
  - [10.1 A régua](#101-a-régua)
  - [10.2 Os dois lados](#102-os-dois-lados)
  - [10.3 O equilíbrio](#103-o-equilíbrio)
  - [10.4 Golpe entre jogadores (nível 2)](#104-golpe-entre-jogadores-nível-2)
- [11. Metas, vitória e derrota](#11-metas-vitória-e-derrota)
  - [11.1 Metas](#111-metas)
  - [11.2 Títulos](#112-títulos)
  - [11.3 Derrota](#113-derrota)
- [12. Multiplayer e sessões](#12-multiplayer-e-sessões)
  - [12.1 Modelo](#121-modelo)
  - [12.2 Regras de sessão](#122-regras-de-sessão)
  - [12.3 Interação social](#123-interação-social)
  - [12.4 Comparação](#124-comparação)
- [13. Progressão fora do jogo](#13-progressão-fora-do-jogo)
- [14. Feedback](#14-feedback)
- [15. Interface](#15-interface)
  - [15.1 Telas do MVP](#151-telas-do-mvp)
  - [15.2 Decisões de usabilidade](#152-decisões-de-usabilidade)
  - [15.3 Requisitos de acessibilidade](#153-requisitos-de-acessibilidade)
  - [15.4 Tutorial](#154-tutorial)
- [16. Arte e som](#16-arte-e-som)
- [17. Arquitetura](#17-arquitetura)
  - [17.1 Camadas](#171-camadas)
  - [17.2 Decisão que não pode ser adiada](#172-decisão-que-não-pode-ser-adiada)
  - [17.3 Persistência em níveis](#173-persistência-em-níveis)
  - [17.4 Stack](#174-stack)
- [18. Escopo](#18-escopo)
  - [Nível 1 — MVP](#nível-1--mvp)
  - [Nível 2 — Núcleo completo](#nível-2--núcleo-completo)
  - [Nível 3 — Se houver tempo](#nível-3--se-houver-tempo)
  - [Nível 4 — Visão, não escopo](#nível-4--visão-não-escopo)
- [19. Produção de conteúdo](#19-produção-de-conteúdo)
  - [19.1 Estado](#191-estado)
  - [19.2 Regra de produção](#192-regra-de-produção)
  - [19.3 Formato](#193-formato)
- [20. Decisões de design registradas](#20-decisões-de-design-registradas)
  - [Pendências que afetam este documento](#pendências-que-afetam-este-documento)

## 1. Visão geral

### 1.1 Conceito

**Selo Falso** é um jogo de tabuleiro digital sobre educação financeira e
reconhecimento de fraude, ambientado num arquipélago mercantil fictício da era
das velas.

O jogador é um mercador recém-estabelecido, dono de uma embarcação pequena. Toda
riqueza vem de comprar, transportar e vender. As instituições do mundo — Casa de
Câmbio, Guilda de Seguros, Casa de Crédito, Companhia Mercante, Registro do Porto
— são legítimas, e cada uma pode ser falsificada. **Piratas não abordam:
falsificam.**

A cada dia o jogador recebe dados, escolhe como usá-los, percorre o mapa e enfrenta
propostas que chegam como documentos do mundo. Algumas são oportunidades reais,
outras são golpes, e há legítimas que simplesmente são mau negócio. Ele decide
aceitar, ignorar, verificar ou denunciar — e cada decisão tem consequência visível
no ouro, na meta e na reputação.

### 1.2 A tese de design

> **Verificar custa recurso.** O jogador escolhe o tempo todo entre avançar rumo à
> meta e ter segurança — a mesma tensão da vida real, nascida da mecânica e não de
> um texto explicativo.

### 1.3 Ficha técnica

| Item | Definição |
|:---------------|:-------------------------------------------|
| Gênero | Tabuleiro digital de decisão sob incerteza |
| Plataforma | Web PWA, para celular |
| Público | 18 a 25 anos |
| Sessão | 3 a 5 minutos por dia de jogo |
| Modos | Travessia (solo), Regata (2 a 8), Companhia (cooperativo) |
| Jogadores | 1 a 8 |
| Ritmo | Assíncrono, sem turno bloqueante |
| Arte | Pixel art, produzida pela equipe |
| Idioma | Português do Brasil |

### 1.4 Público-alvo

Jovens adultos, universitários e recém-ingressantes no mercado de trabalho, em
transição para a autonomia financeira — primeiro cartão, primeiro salário,
primeiro aluguel.

**Persona.** Tem 18 anos, cursa o primeiro semestre de um curso noturno e trabalha
de dia. Tem conta digital, primeiro cartão de crédito e paga o próprio plano de
celular. Já comprou e vendeu em marketplace, já recebeu "seu CPF foi usado em
outra compra" por SMS, e já viu a mãe quase cair num golpe do WhatsApp. Joga no
celular quase todo dia, jogos curtos, com o mesmo grupo de amigos. Sabe que golpe
existe; acha que só cai quem não presta atenção.

**Essa última frase é a mais importante do projeto: o público não acha que precisa
disso. O jogo precisa ser divertido primeiro e educativo por consequência.**

### 1.5 O problema

Jovens adultos recebem diariamente cobranças, ofertas e alertas por canais
digitais, e uma parte deles é fraude. Erram de dois jeitos: caem no golpe por
inexperiência e excesso de confiança no ambiente digital, e recusam o legítimo
quando, assustados, passam a desconfiar de tudo. A educação financeira formal
raramente cobre reconhecimento de fraude, e o material antifraude existente ensina
desconfiança indiscriminada — que também é dano.

## 2. O mundo

### 2.1 Regra de contenção

**O mundo é inteiramente fictício.** Nenhuma nação, companhia, rota, evento ou povo
real. Nenhuma mercadoria com carga histórica de exploração humana. Estética de era
das velas; geografia e história inventadas.

Isso não é preciosismo: grandes navegações são também colonização e tráfico de
pessoas, e um jogo sobre prosperar comercialmente nessa era **vai** receber essa
pergunta. Um mundo fictício responde antes de ela ser feita.

### 2.2 As instituições

Cada uma existe porque carrega um conceito financeiro, e cada uma pode ser
falsificada.

| Instituição | Função | Conceito que ensina |
|:-------------------|:--------------------------|:-------------------------|
| **Registro do Porto** | Verifica selos e licenças | Verificação por canal oficial |
| **Casa de Câmbio** | Troca moedas entre portos | Taxa, spread, custo escondido |
| **Guilda de Seguros** | Segura carga; guarda depósito | Prêmio, cobertura, reserva |
| **Casa de Crédito** | Empresta a risco de viagem | Juros, prazo, garantia |
| **Companhia Mercante** | Compra e vende em volume | Contrato, cláusula, reputação |

O **Registro do Porto** é a peça central: é a materialização do canal oficial.
Consultar o Registro é o equivalente exato de desligar e ligar para o número do
cartão — e tê-lo como lugar físico no mundo é mais didático do que seria uma ação
abstrata de "verificar".

### 2.3 Correspondência com a realidade

| No jogo | Hoje | Conceito |
|:-----------------------------|:---------------------------|:--------------------------|
| Seguro de carga | Seguro | Pagar por proteção que talvez não se use |
| Empréstimo a risco de viagem | Crédito com juros | Custo do dinheiro |
| Letra de câmbio | Transferência, garantia | O canal de pagamento importa |
| Cotas de expedição | Investimento | Dividir risco |
| Contrato de fretamento | Contrato de serviço | Ler cláusulas |
| Reputação de casa comercial | Verificar a fonte | Histórico vale mais que promessa |
| Aval a outro mercador | Ser fiador | Emprestar o nome tem custo |
| Selo do Registro | Canal oficial | Verificar pela fonte |
| Adiantamento de frete | Taxa antecipada | Pagar antes de receber é sinal |

## 3. Objetivos de aprendizagem

### 3.1 Os objetivos

| # | Objetivo |
|:-----|:-----------------------------------------------------------|
| OA1 | Identificar os dez sinais recorrentes de engenharia social |
| OA2 | Verificar pela fonte oficial, em vez de responder pelo canal da mensagem |
| OA3 | Distinguir situação legítima com aparência estranha de golpe |
| OA4 | Decidir sob pressão, escolhendo quando vale a pena verificar |
| OA5 | Planejar recursos rumo a uma meta, equilibrando gastar agora e guardar |
| OA6 | Levar o aprendizado para a vida real e pedir segunda opinião |
| OA7 | Reconhecer o canal correto para denunciar cada tipo de fraude |

### 3.2 Matriz objetivo × mecânica × medição

| OA | Mecânica que ensina | Como se mede |
|:----|:---------------------------------------|:--------------------------|
| OA1 | Cartas geradas por sinais; sinais destacados ao resolver | Sensibilidade: fraudes rejeitadas |
| OA2 | Ação Verificar, com custo, consultando o Registro | Proporção que cita verificação por canal independente |
| OA3 | Ruído obrigatório nas legítimas; placar duplo | Especificidade: legítimas aceitas |
| OA4 | Recurso único para mover e verificar | Qualidade de decisão por faixa de dificuldade |
| OA5 | Meta escolhida; contratos com prazo; loja | Meta alcançada dentro da temporada |
| OA6 | Ponte para hoje; diário; segunda opinião na Regata | Desempenho em cartas contemporâneas |
| OA7 | Denúncia com escolha de canal; reputação | Proporção de denúncias no canal correto |

### 3.3 Instrumento de avaliação

Doze itens, metade fraudulentos e metade legítimos, **em linguagem contemporânea**
— SMS, WhatsApp, PIX, boleto —, aplicados antes da sessão e uma semana depois.

Três métricas separadas, mais uma:

- **Sensibilidade:** fraudes corretamente rejeitadas
- **Especificidade:** legítimas corretamente aceitas
- **Ação nomeada:** cita verificação por canal independente
- **Calibração:** distância entre confiança declarada e acerto real

Separar sensibilidade de especificidade é o que impede que "ficou paranoico"
apareça como sucesso.

**Vantagem estrutural:** o log de ações do próprio jogo registra cada decisão. A
avaliação está embutida na arquitetura, não é instrumento colado depois.

## 4. Core loop

### 4.1 O turno em duas fases

Todo turno tem uma fase de **reconhecimento** e uma fase de **ação**. A primeira é
livre e não gasta nada; a segunda gasta dado e produz consequência.

```
                      ┌──────────────── novo dia ─┐
                      ↓                           │
┌─ RECONHECIMENTO ─ livre, não gasta dado ──┐     │
│  meta e ouro · dia, janela e prazos       │     │
│  contratos ativos · eventos em vigor      │     │
│  itens na mochila · minha reputação       │     │
│  os outros: posição e ponto na régua      │     │
└─────────────────────┬─────────────────────┘     │
                      ↓                           │
┌─ AÇÃO ─ gasta dado ───────────────────────┐     │
│  3 dados → escolhe um → move → para casa  │     │
│  saca carta                               │     │
│  aceitar, ignorar, verificar, denunciar   │     │
│  consequência: ouro, meta, reputação      │     │
└─────────────────────┬─────────────────────┘     │
                      └───────────────────────────┘
```

**O bloco da carta é onde 90% do tempo de jogo acontece.** É nele que o esforço de
design e de interface deve se concentrar. O reconhecimento existe para que a
decisão da carta seja informada — não para competir com ela por atenção.

### 4.2 O que o reconhecimento mostra

| Painel | Conteúdo | Por que está aqui |
|:------------------------|:--------------------------------------------------|:-------------------------------------------------------------|
| Meta e ouro | Quanto falta para a meta escolhida; quanto há em caixa | Sem a distância até a meta, "avaliar risco" não tem denominador: risco em relação a quê? |
| Dia, janela e prazos | Dia do jogo, qual das quatro janelas, o que vence quando | Contrato tem prazo em turnos (9.2) e a janela muda o que o tabuleiro favorece (5.4) |
| Contratos ativos | O que foi assumido, valor corrente, turnos restantes | Evento de rodada pode ter alterado o valor de contrato já aceito (9.2) |
| Eventos em vigor | O que está valendo nesta rodada | Evento muda o mapa para todos (5.5); decidir sem ele na tela é decidir no escuro |
| Mochila | Itens comprados e o que cada um faz | Item esquecido é ouro perdido: a apólice só serve se já estiver na mochila quando a perda chega (9.4) |
| Minha reputação | Posição na régua | Define que ofertas aparecem e se uma denúncia minha é acreditada (10.3) |
| Os outros | Última posição conhecida e ponto na régua | Posição sozinha diz pouco; reputação baixa é que indica quem pode prejudicar (10.4) |
| Em trânsito *(nível 2)* | Denúncias enviadas por pombo-correio que ainda não chegaram | É estado pendente do jogador; sem isso ele paga duas vezes pela mesma denúncia (8.4) |

### 4.3 Os limites do reconhecimento

Três regras. Cada uma fecha um jeito de quebrar o jogo.

**É grátis e não revela carta.** Mostra o que o jogador já possui ou o que é
público. Nada sobre a carta que ele vai sacar, nem sobre carta de outro
participante. Se o reconhecimento adiantasse um sinal que fosse, viraria
verificação sem custo e derrubaria junto a primeira decisão de design —
segurança deixaria de competir com progresso pelo mesmo recurso. Existe uma
exceção, e ela é paga: o **Informante** revela um sinal sem gastar dado (9.4).
Ver de graça é privilégio de item comprado, não de painel.

**O que se vê dos outros é o último estado conhecido.** O multiplayer é
assíncrono, com log append-only e estado derivado no cliente (17.1). A posição de
quem não sincronizou é a de antes, e a tela diz isso. É consequência da
arquitetura, não defeito — e é fiel ao assunto do jogo, onde também se decide com
informação defasada.

**Não é fase cronometrada, mas cabe em segundos.** A sessão inteira dura de 3 a 5
minutos (1.3). O reconhecimento é uma tela que se lê de relance, não um menu em
que se mora. Se for preciso navegar para montar o quadro, o desenho está errado.

> **Lacuna L13.** Falta decidir se o **diário** é consultável dentro da partida.
> Ele é referência de moldes já identificados e dos sinais que os caracterizam
> (seção 13). Consultá-lo no turno é o comportamento que o jogo quer ensinar —
> conferir antes de confiar — mas também é um atalho que entrega o molde sem
> gastar dado, e o gerador de três camadas existe justamente para que a resposta
> venha do sinal e não da memória. Enquanto não se decide, o diário fica fora do
> painel de reconhecimento.

## 5. O tabuleiro

### 5.1 Natureza

Mapa náutico com percurso de casas. O tabuleiro é **moldura**, não é onde está a
diversão: ele organiza a entrega de situações ao longo do tempo. O que precisa ser
divertido são as cartas — e isso é conveniente, porque é também onde está o
aprendizado.

### 5.2 Tipos de casa

**Nível 1 — MVP:**

| Casa | Papel | Carta que entrega |
|:--------------|:---------------|:--------------------------------|
| **Porto** | Rotina | Renda pela venda de carga; pagamento de taxas fixas |
| **Entreposto** | Oportunidade | Oferta de ganho, real ou falsificada |
| **Alfândega** | Cobrança | Exigência de pagamento, real ou falsificada |

**Nível 2:** Alto-mar (imprevisto), Praça de Comércio (social e negociação),
Feira (mercado e itens), Encruzilhada (bifurcação de rota).

### 5.3 Bifurcação

Em casas de Encruzilhada o jogador escolhe entre **costa segura** — mais longa,
mais casas de Porto, atrasa a meta — e **mar aberto** — mais curto, mais
Entreposto e Alfândega, mais exposição.

É o que transforma o dado de destino em recurso: a rota é decisão, e correr risco
para chegar antes é literalmente a decisão financeira que o jogo quer ensinar.

### 5.4 Janelas do dia

O dia tem quatro janelas, que são **posições no ciclo, não horas do relógio**.

| Janela | Perfil | Favorece |
|:-----------|:-------------------------------|:---------------|
| Amanhecer | Rotina, renda, contratos chegando | Planejar |
| Meio-dia | Pico de oportunidades e de golpes | Decidir |
| Tarde | Preços oscilam; contratos vencem | Ajustar |
| Anoitecer | Cobranças e prazos finais | Pagar o que deve |

**Por que não relógio real.** Três razões: amarrar janelas a horários fabrica a
urgência que o jogo existe para condenar; torna o jogo impossível de validar numa
sessão de 40 minutos; e na Regata cria injustiça por agenda, não por decisão.

Como opção de nível 3, janelas em relógio real podem existir desde que a
oportunidade **decaia em vez de expirar** — presença vira vantagem, ausência não
vira punição — e sejam configuráveis na criação da partida.

### 5.5 Eventos de rodada

Ao fim de cada rodada o mapa pode mudar: tempestade, bloqueio de rota, alta de uma
especiaria, onda de falsificações. **Eventos afetam todos igualmente; ninguém perde
por decisão alheia.**

Repare que os eventos são temáticos e verdadeiros: fraude vem em ondas, e é durante
uma feira legítima que o golpe se disfarça melhor.

## 6. Dados e ações

### 6.1 Os dados

**Três dados por dia, rolados juntos.** O jogador vê os três valores e decide qual
usar e em que ordem. Dado não usado não acumula.

Isso é o que separa agência de sorte: em vez de "rolei 4, ando 4", o jogador pensa
"tenho 2, 5 e 6; se uso o 6 agora caio no Entreposto, mas gasto meu único dado
alto". Sorte gera variedade; a escolha gera o jogo.

### 6.2 O dado como recurso duplo

O dado move **e** verifica. Cada dado gasto verificando é um dado a menos avançando
rumo à meta. **Segurança e progresso competem pelo mesmo recurso** — e essa é a
tensão central do jogo.

> **Pendência P21.** O custo exato da verificação e a economia geral de recursos
> não estão fechados. O princípio — verificar compete com progresso — é firme; o
> número é provisório até a oficina de economia.

## 7. As cartas

Esta é a seção mais importante do documento. Tudo o mais é moldura.

### 7.1 O problema a resolver

Se as cartas forem um baralho fixo, o jogador decora e para de ler. Isso não é só
perda de rejogabilidade: **destrói o objetivo de aprendizagem**, porque a
habilidade treinada passa a ser memória em vez de leitura de indícios.

A solução não é embaralhar textos prontos. É separar **superfície** de **sinal**.

### 7.2 Arquitetura em três camadas

**Camada 1 — Molde.** A estrutura da situação. Quinze moldes cobrem o repertório.

**Camada 2 — Preenchimento.** Casa comercial, valor, prazo, porto, nome. Vem de
vocabulários e muda a cada geração.

**Camada 3 — Sinais.** Lista fechada de dez. **A resposta correta deriva sempre dos
sinais presentes, nunca do texto nem do molde.**

### 7.3 Os dez sinais

| id | Sinal | Como aparece no mundo |
|:----|:--------------------------|:------------------------------------|
| S01 | Canal não oficial | Proposta na taverna, não no Registro |
| S02 | Pedido de selo pessoal | Pedem o selo ou a senha do cofre |
| S03 | Urgência artificial | "O navio zarpa com a maré" |
| S04 | Taxa antecipada | Adiantamento para liberar carga |
| S05 | Remetente sem registro | Casa comercial sem registro no porto |
| S06 | Valor incompatível | Lucro acima do praticado na rota |
| S07 | Pedido de sigilo | "Não comente com a Guilda" |
| S08 | Entreposto fora das rotas | Enseada fora dos caminhos conhecidos |
| S09 | Pagamento atípico | Só em moeda estrangeira, em mãos |
| S10 | Bom demais para ser verdade | Retorno garantido, sem risco |

### 7.4 Os quinze moldes e a proporção

A natureza é **razão, não rótulo**. Catorze dos quinze aparecem dos dois lados;
só o molde 11 é sempre fraude, porque a regra é a lição.

| Molde | Legítima/fraude | Molde | Legítima/fraude |
|:---------------------------|:------|:---------------------------|:------|
| 1 Cobrança em atraso | 55/45 | 9 Encomenda com taxa | 25/75 |
| 2 Reembolso pendente | 45/55 | 10 Promoção relâmpago | 60/40 |
| 3 Atualização cadastral | 30/70 | 11 Retorno garantido | **0/100** |
| 4 Prêmio ou sorteio | 15/85 | 12 Multa com desconto | 55/45 |
| 5 Renda extra ou vaga | 50/50 | 13 Assinatura recorrente | 60/40 |
| 6 Empréstimo pré-aprovado | 70/30 | 14 Aluguel com sinal | 45/55 |
| 7 Conhecido com canal novo | 20/80 | 15 Conta com valor atípico | 85/15 |
| 8 Alerta de compra suspeita | 55/45 | | |

**Proporção do baralho: 55% legítimas, 45% fraudulentas.** Se a fraude fosse
maioria, recusar tudo seria lucrativo e a lição viraria paranoia. Além disso é
fiel à realidade, onde mensagem verdadeira é muito mais comum que golpe.

### 7.5 Ruído

**Cartas legítimas com aparência estranha mas inofensiva:** aviso deixado ao
anoitecer, tom ameaçador, casa comercial real porém desconhecida, valor alto mas
previsto.

Sem ruído, o jogador aprende que "estranho = golpe", que é paranoia e não
aprendizado. **A dificuldade escala reduzindo sinais e aumentando ruído, nunca
aumentando o valor perdido.**

### 7.6 Legítima e mau negócio

Atributo adicional das cartas legítimas: *bom negócio* ou *mau negócio*.

Separa dois aprendizados que estavam colados: OA1 a OA3 são reconhecimento de
fraude; OA4 e OA5 são julgamento financeiro. Um empréstimo caro é verdadeiro e
ainda assim ruim — recusá-lo é acerto, e **não conta como erro por desconfiança**.

Ganho de medição: verificar uma carta legítima gasta um dado à toa, e isso alimenta
a métrica de OA2. É o único jeito de medir excesso de verificação.

### 7.7 Faixas de dificuldade

| Faixa | Sinais | Ruído | Característica |
|:----------|:-------|:---------|:-----------------------------|
| Inicial | 3 a 4 | Nenhum | Golpe evidente; ensina o repertório |
| Média | 2 | Pouco | Exige leitura atenta |
| Alta | 1 | Bastante | Exige verificação; errar é esperado |
| Avançada | 0 aparente | Muito | O sinal só aparece ao verificar |

A distribuição pende para as faixas avançadas conforme o patrimônio cresce e a
temporada avança — **quanto mais o jogador tem, mais sofisticada a tentativa
contra ele**.

### 7.8 Determinismo

Geração determinística por semente: `semente da sessão + rodada + participante`.
Todos os participantes de uma sessão enfrentam o mesmo baralho, sem transmitir
baralho pela rede, e qualquer bug é reproduzível.

**A semente vem do servidor.** Se o cliente sorteasse, trapacear seria recarregar
até sair o número desejado.

**Limitação conhecida e aceita:** como a geração roda no cliente, um jogador
curioso consegue inspecionar o código e saber a resposta de qualquer carta.
Trapacear só prejudica quem trapaceia, já que o benefício do jogo é aprender.
Geração no servidor fica registrada como evolução, com prioridade maior caso a
Regata com isca entre jogadores entre em escopo.

## 8. Ações sobre a carta

### 8.1 As quatro ações

| Ação | Se for fraude | Se for legítima |
|:--------------|:----------------------------|:---------------------------|
| **Aceitar** | Perde o valor; exposto | Ganha o negócio |
| **Ignorar** | Nada acontece | Perde a oportunidade |
| **Verificar** | Revela sinais; custa recurso | Revela ausência de sinais; recurso gasto à toa |
| **Denunciar** | Evita a perda e **ganha reputação** | Perde a oportunidade e **perde credibilidade** |

Aceitar aparece com o rótulo apropriado ao tipo de carta — cumprir, entregar,
pagar, assinar —, mas é sempre a mesma ação.

### 8.2 Por que denunciar importa

Sem denúncia, recusar o legítimo é erro **passivo**: você ignora e perde uma
oportunidade. É perda fraca, e o lado "desconfiança" do placar duplo nunca dói.

Com denúncia, o jogador faz afirmação **ativa** — "isto é falso" — e errar tem
custo nomeado. Isso cria três posturas distintas e ensina a nuance que faltava:
**você não precisa acusar todo mundo, pode simplesmente não entrar.** Ignorar é a
saída segura e medíocre; denunciar é a jogada de convicção.

E o jogo passa a ensinar **a denunciar** — comportamento cívico de valor real que
nenhum dos materiais analisados no benchmarking ensina.

### 8.3 Canais de denúncia

Cada carta aponta o canal correto, e errar o canal reduz o efeito.

| Tipo de fraude | Canal |
|:---------------------------|:----------------------|
| Selo ou licença falsos | Registro do Porto |
| Fraude em carga ou seguro | Guilda de Seguros |
| Empréstimo ou crédito falso | Casa de Crédito |
| Contrato descumprido | Companhia Mercante |

Isso ensina **qual é o canal certo para cada problema**, que é a dificuldade real
de quem quer denunciar hoje e não sabe se liga para o banco, o Procon, a
plataforma ou a polícia. É a mecânica do OA7.

### 8.4 Custo e localização

**No MVP:** denúncia imediata e gratuita no momento da carta, com escolha de canal.
O custo é o risco de credibilidade, não o recurso.

Isso é deliberado. Aceitar é instantâneo; se denunciar exigisse atravessar o mapa,
o jogador racional denunciaria de menos — e denunciar é o comportamento que o jogo
quer ensinar.

**No nível 2:** entra a geografia. Denúncia presencial no canal correto vale
integral; o **pombo-correio** permite denunciar à distância pagando ouro, com
efeito reduzido. A localização vira profundidade, não barreira.

## 9. Economia

### 9.1 Recursos

| Recurso | O que é | Para que serve |
|:--------------|:-------------------------------|:---------------------|
| **Ouro** | Dinheiro disponível | Decisão principal |
| **Depósito** | Guardado na Guilda; saque lento | Reserva de emergência |
| **Dados** | Ações do dia | Tempo e atenção |
| **Reputação** | Credibilidade acumulada | Acesso e condições |
| **Meta** | Progresso rumo ao objetivo | Direção e vitória |

O **depósito** merece nota: guardar na Guilda de outro porto leva tempo para
chegar. A regra de "reserva de acesso mais lento" deixa de ser convenção
arbitrária e vira consequência do mundo — que é o padrão de um bom jogo sério.

### 9.2 Contratos

Contratos têm **prazo em turnos**. O jogador tem X turnos para cumprir; eventos
podem alterar o valor de contratos ativos, obrigando a reavaliar decisões já
tomadas.

Prazo é a essência de contrato, crédito e frete — é onde o conteúdo financeiro
encosta na mecânica sem esforço.

### 9.3 A feira — loja de itens

Inspirada na loja do Mario Party, com quatro mecanismos adaptados:

**Entrada condicionada.** Inventário limitado a três itens; loja fechada na última
rodada da temporada, para a partida não se decidir numa compra final.

**Estoque que reage à posição.** Quem está atrás vê ofertas melhores **e mais
arriscadas**, com proporção de fraude maior.

Isso é rubber band, e normalmente mereceria ressalva. Aqui não: **o equilíbrio e a
lição coincidem.** É a pessoa em aperto financeiro que recebe as propostas mais
sedutoras e mais perigosas. Equilíbrio de jogo e conteúdo na mesma mecânica.

**Dois mercados de natureza oposta.** Feira legítima e mercado cinzento, separados
por reputação.

**Estoque finito.** Cada item tem unidades limitadas na temporada; esgotado,
ninguém mais compra. Impede estratégia dominante repetida.

### 9.4 Itens

**Regra:** todo item carrega conteúdo financeiro. Item que só dá movimento ou ouro
é decoração e não se justifica num jogo sério.

| Item | Efeito | O que ensina |
|:-------------------|:----------------------------|:---------------------------|
| **Apólice** | Cobre uma perda até certo valor | Pagar por proteção que talvez não se use |
| **Informante** | Revela um sinal sem gastar dado | Verificação tem custo |
| **Adiamento** | Congela uma decisão até a próxima rodada | Pressa é evitável |
| **Aval** | Melhora condição de crédito | Emprestar o nome tem custo |
| **Pombo-correio** | Denuncia à distância *(nível 2)* | Reportar tem custo e vale a pena |

**Condição inegociável da apólice:** ela **não pode ser sempre a escolha certa**.
Se comprar sempre for ótimo, deixa de ser decisão e vira imposto. O preço precisa
ser calibrado para que comprar seja errado com alguma frequência — e o jogador
precisa terminar rodadas tendo pago por proteção que não usou. Esse desconforto
*é* a lição sobre seguro.

## 10. Reputação

### 10.1 A régua

Cinco faixas. O topo é condição de vitória, o que amarra a régua ao objetivo sem
inventar sistema novo.

```
Suspeito  →  Comum  →  Confiável  →  Respeitado  →  Mestre da Guilda
```

### 10.2 Os dois lados

**Reputação alta** destrava o mercado legítimo: desconto em taxas, contratos
melhores, juro menor na Guilda, denúncia aceita sem prova.

**Reputação baixa** destrava o mercado cinzento: iscas contra outros jogadores,
frete sem documentação, carga de procedência duvidosa.

O caminho do vilão é deliberado e tem respaldo no próprio benchmarking da equipe:
o **Bad News** funciona assim, e o aprendizado mais profundo vem de produzir o
ataque, não de detectá-lo. Montar uma isca ensina o que torna um golpe
convincente.

### 10.3 O equilíbrio

**Com reputação baixa, o Registro deixa de aceitar denúncias sem prova.**

O fraudador perde a capacidade de denunciar com credibilidade. É tematicamente
perfeito — quem mente perde o direito de ser acreditado — e se equilibra sozinho,
sem número mágico.

Além disso, reputação baixa custa acesso: contratos recusados, juro punitivo,
menos oportunidades legítimas. O caminho do vilão precisa ser viável e **não
dominante**; se defraudar for mecanicamente mais forte que negociar bem, o
aprendizado vira o oposto.

### 10.4 Golpe entre jogadores *(nível 2)*

Quatro regras:

1. **Toda isca contém ao menos um sinal verdadeiro.** Nenhuma armadilha é
   indetectável. Ensina o mais verdadeiro sobre fraude: golpe sempre deixa rastro
2. **É aposta, não emboscada.** O atacante deposita para armar; se a vítima
   identifica, ela leva o depósito
3. **Mais sutil paga mais, arrisca mais**
4. **Cair revela o que passou despercebido.** Perder ensina; perder não humilha

**Restrição de segurança inegociável:** o jogador monta a isca **por composição**,
escolhendo molde e sinais entre os que já desbloqueou. **Nunca escreve texto
livre.** O texto é gerado pelo mesmo motor. Isso preserva a decisão estratégica e
elimina moderação de conteúdo e produção de material utilizável fora do jogo.

Limite por rodada e por alvo, para que quatro amigos não virem três contra um.

## 11. Metas, vitória e derrota

### 11.1 Metas

O jogador escolhe no início: comprar um navio maior, abrir uma casa comercial,
quitar uma dívida de família. A meta dá direção ao acúmulo, cria a tensão entre
gasto imediato e objetivo distante, e serve de condição de vitória.

Metas com perfis diferentes — barata e rápida, cara e longa, que exige reserva
constante — ajustam duração e dificuldade sem conteúdo novo.

### 11.2 Títulos

Conquistar um título, sempre com licença:

| Título | Condição | O que treina |
|:--------------------|:--------------------------------|:---------------------|
| **Armador** | Alcançar a meta escolhida | Orçamento com meta; curto × longo prazo |
| **Mestre da Guilda** | Reputação máxima, contratos legítimos cumpridos, nenhum calote | Não recusar o legítimo |
| **Vigia do Porto** | Identificar as falsificações da temporada, caindo no máximo em uma | Reconhecer sinais; verificar pela fonte |

- **Travessia:** o jogador escolhe qual título persegue, ou deixa em aberto
- **Regata:** o primeiro a conquistar qualquer título vence; a temporada segue até
  o fim e os demais são classificados por pontuação
- **Companhia:** todos vencem se a meta comum for alcançada

### 11.3 Derrota

**Não há eliminação.** Perde quem termina a temporada sem título; na Regata, todos
menos o vencedor são classificados, com os falidos no fundo.

**Falir endivida, não elimina:** o naufrágio financeiro gera empréstimo de resgate
com juros e renda retida, e o jogador continua jogando, com caminhos para se
reerguer — fretamento, renegociação, e a tentação dos negócios promissores. Quem
quita volta a disputar título.

Todo jogador, vencedor ou não, recebe o mesmo relatório ao fim: título ou não,
pontuação com as três maiores fontes, os dois placares, reputação e o diário —
**e vê por que perdeu**.

## 12. Multiplayer e sessões

### 12.1 Modelo

Sessão identificada por código curto. O host cria e convida. Todos no mesmo
tabuleiro, com o mesmo baralho, cada um no próprio ritmo. Sem ranking público e
sem matchmaking.

O modelo é o de partida por correspondência: **servidor como fonte da verdade**,
cada ação gravada como registro, estado derivado da sequência, jogador podendo
estar ausente por dias e recebendo atualização ao vivo quando presente.

### 12.2 Regras de sessão

**Nenhum turno bloqueia ninguém.** Corrida paralela. Isso não é preferência
estética: partida por turnos entre amigos morre no primeiro jogador que some.

**Entrada tardia** é configurável na criação da partida, com handicap ao
ingressante se necessário.

**Abandono não encerra a partida.** A temporada tem prazo em rodadas; quem parou
não avança e é classificado pelo que fez.

**Configuração na criação:** duração da temporada por presets, entrada tardia,
modo, e — no nível 3 — janelas em relógio real.

### 12.3 Interação social

**Reações e frases predefinidas, nunca texto livre.** Texto livre entre usuários
traz moderação, responsabilidade sobre conteúdo gerado e tratamento de dado
pessoal. A substituição funciona igualmente bem e é o que a maioria dos jogos de
tabuleiro digitais faz, exatamente por isso.

Repertório: comemoração, lamento, alerta ("cuidado com essa carta"), pedido de
segunda opinião.

### 12.4 Comparação

Comparação por **qualidade de decisão** — proporção de acertos ponderada pela
dificuldade — e nunca por saldo, porque saldo premia quem arrisca e dá sorte.

## 13. Progressão fora do jogo

**Cada sessão é única e autocontida.** Reputação, ouro e progresso não atravessam
partidas — o que mantém a Regata justa, sem veteranos entrando já respeitados.

Fora da partida existe uma camada de **registro do jogador**, persistente:

| Elemento | O que guarda |
|:-------------|:--------------------------------------------|
| **Diário do mercador** | Moldes de golpe já identificados, com os sinais que os caracterizam e a correspondência com hoje |
| **Glossário** | Vocabulário de época e termos financeiros, explicados |
| **Progresso** | Temporadas jogadas, títulos conquistados, evolução dos dois placares |

O diário é colecionável, é referência consultável e é **evidência de
aprendizagem exportável** — serve à avaliação do projeto. É justamente por viver
fora da sessão que ele consegue isso: zerado a cada temporada, não mostraria
acúmulo nenhum.

## 14. Feedback

| Momento | O que o jogador vê |
|:-----------------------|:---------------------------------------------|
| Ao resolver a carta | Resultado imediato; sinais presentes destacados no texto; ponte para o golpe de hoje na primeira vez de cada molde |
| No patrimônio | O erro aparece como perda de ouro e atraso visível na meta — consequência em outro sistema, não texto de feedback |
| No placar duplo | Dois contadores sempre visíveis: caiu no golpe; recusou o legítimo |
| No diário | Coleção de golpes identificados, consultável a qualquer momento |
| Na sessão | Progresso dos outros no mapa; emotes e alertas |
| Ao fim da temporada | Relatório com os dois placares, qualidade de decisão por faixa e diário completo |

**Sobre o placar duplo com quatro ações.** Há três tipos de erro — aceitou golpe,
ignorou legítima, denunciou legítima. Na tela ficam **dois contadores**, com
"desconfiança" somando ignorar e denunciar legítimas e a denúncia falsa pesando
mais. O detalhamento em três aparece no relatório final.

## 15. Interface

### 15.1 Telas do MVP

| # | Tela | Elementos essenciais |
|:----|:-------------------|:--------------------------------------|
| T1 | Abertura | Jogar solo, entrar com código, continuar |
| T2 | Escolha de meta | Metas com custo, prazo e dificuldade |
| T3 | Tabuleiro | Percurso, embarcação, recursos no topo, dados na base |
| T4 | Escolha de dado | Valores e destino previsto de cada um |
| T5 | Carta | Enunciado, remetente, quatro ações, custo da verificação |
| T6 | Verificação | Sinais revelados; decisão ainda pendente |
| T7 | Consequência | Efeito nos recursos, motivo, ponte para hoje |
| T8 | Resultado | Placar duplo, progresso da meta, revisão carta a carta |
| T9 | Sessão | Código, participantes, progresso de cada um |
| T10 | Diário | Golpes identificados, sinais, correspondência atual |

### 15.2 Decisões de usabilidade

- **O custo da verificação é mostrado antes de o jogador escolher.** Esconder custo
  é truque, não dificuldade
- **O placar duplo fica visível durante a partida**, porque é o feedback que
  corrige o comportamento
- **Nenhuma ação é cronometrada.** A urgência existe dentro da ficção; o tempo real
  do jogador é ilimitado. Seria incoerente um jogo sobre não ter pressa apressar
  quem joga
- Operável com uma mão, em sessões curtas

### 15.3 Requisitos de acessibilidade

Contraste WCAG AA; corpo de texto a partir de 16px; área de toque mínima de 44px;
operável sem gesto de precisão; linguagem simples e direta nas cartas; vocabulário
de época limitado a lista fechada e explicado no glossário.

### 15.4 Tutorial

**Não há tela de tutorial. A primeira partida é o tutorial.**

Os três primeiros dias usam apenas cartas de faixa inicial, com três a quatro
sinais evidentes, e o resultado aponta explicitamente qual sinal estava ali. É
coerente com a filosofia do projeto: ensinar pela consequência, não pelo texto.

## 16. Arte e som

**Pixel art, produzida pelos integrantes.** Mapa, cartas, interface, ícones das
instituições e a meta em seus estágios — o navio crescendo, a casa comercial
ganhando andares — seguem a mesma linguagem visual.

**A arte não é caminho crítico.** O primeiro jogável usa uma lista fechada de
assets; o que for além segue a escada de escopo.

**Som:** não especificado. Se entrar, entra no nível 3, e sem dependência — o jogo
precisa ser plenamente jogável no silêncio.

## 17. Arquitetura

### 17.1 Camadas

```
┌─────────────────────────────────────────────┐
│  Interface (telas T1–T10)                   │
├─────────────────────────────────────────────┤
│  Motor de jogo                              │
│  · redutor de estado (log → estado)         │
│  · gerador de cartas (determinístico)       │
│  · regras de movimento, economia, reputação │
├─────────────────────────────────────────────┤
│  Conteúdo (arquivos externos)               │
│  · moldes · vocabulários · sinais · metas   │
│  · tabuleiro · itens · eventos              │
├─────────────────────────────────────────────┤
│  Sessão                                     │
│  · identidade anônima local                 │
│  · log de ações append-only                 │
│  · sincronização por ordem de chegada       │
└─────────────────────────────────────────────┘
```

**O motor não sabe o que é um golpe.** Carrega conteúdo, aplica ações e produz
estado. Trocar o tema inteiro é trocar arquivos de conteúdo.

### 17.2 Decisão que não pode ser adiada

**O modo solo é uma sessão de um participante**, com o mesmo log e o mesmo redutor
do multiplayer, desde a primeira linha de código. Feito com estado local e
"multiplayer depois", vira reescrita do jogo inteiro.

### 17.3 Persistência em níveis

| Nível | Entrega | Esforço |
|:---|:------------------------------------------|:-----------|
| 0 | Solo local; fecha e reabre no mesmo aparelho | 2 dias |
| 1 | Sessão no servidor; log; código de convite | 1 a 2 semanas |
| 2 | Acompanhar progresso alheio em tempo real | 2 a 3 dias |
| 3 | Continuidade entre dispositivos | 2 a 3 dias |
| 4 | Notificação fora do aplicativo | 1 semana |
| 5 | Validação de regras no servidor | 2 semanas |

Alvo de 2027/1: níveis 0 a 3. Níveis 4 e 5 se sobrar.

**Continuidade entre dispositivos** por **código de jogador** que o jogador copia,
sem login e sem e-mail. Mantém identidade anônima e não reabre discussão de dado
pessoal. Desvantagem documentada: quem perde o código perde o registro.

### 17.4 Stack

| Camada | Escolha | Justificativa |
|:-------------|:---------------|:-----------------------------------|
| Linguagem | TypeScript | Regras compartilhadas cliente/servidor |
| Interface | React | 90% do produto é interface; mais gente contribui |
| Build | Vite | Configuração mínima; saída estática |
| Tabuleiro | SVG | Mapa estático com peão em posições discretas |
| Estado | Redutor sobre o log | A arquitetura já é um log |
| Remoto | Supabase | Postgres gerenciado, tempo real, camada gratuita |
| Local | IndexedDB | Retomar partida sem rede |
| Empacotamento | PWA; Capacitor depois | Link para validar; loja depois sem reescrever |
| Hospedagem | Vercel ou GitHub Pages | Gratuito, estático, deploy por push |
| Conteúdo | JSON externo | Não-programador edita carta sem tocar em código |

**Godot foi descartado** com três motivos: export web pesado e instável em Safari
móvel, o que colide com "abrir um link e jogar"; quebra a paralelização, porque só
um integrante programaria; e o jogo não precisa de engine — não há física,
renderização contínua nem colisão.

## 18. Escopo

### Nível 1 — MVP

Mapa único com uma bifurcação · três casas (Porto, Entreposto, Alfândega) · três
dados escolhíveis · quatro janelas em tempo de jogo · contratos com prazo · quatro
ações sobre a carta, com denúncia e canais · vinte cartas nas quatro faixas ·
placar duplo · ponte para hoje · uma meta · reputação em cinco faixas · modo
Travessia construído como sessão de um participante · persistência nível 0 a 1 ·
tutorial pela curva.

### Nível 2 — Núcleo completo

Regata · golpe entre jogadores por composição · feira e itens · diário e
glossário completos · casas restantes · denúncia localizada e pombo-correio ·
sessenta cartas · metas múltiplas · eventos de rodada.

### Nível 3 — Se houver tempo

Companhia · janelas em relógio real configuráveis · som · conquistas ·
notificação fora do aplicativo.

### Nível 4 — Visão, não escopo

Validação de regras no servidor · geração de cartas no servidor · publicação em
loja via Capacitor · módulos de dificuldade financeira (orçamento doméstico, fluxo
de caixa de pequeno negócio, investimentos).

## 19. Produção de conteúdo

### 19.1 Estado

| Camada | Situação |
|:--------------------------|:----------------------|
| 60 premissas (15 moldes × 4 casas) | Pronto |
| Sinais atribuídos | Pendente |
| Ruído nas legítimas | Pendente |
| Cartas completas | 6 de 30 |
| Vocabulários | Pendente |
| Pontes por molde | Pendente |

### 19.2 Regra de produção

**Escrever 30 cartas à mão antes de projetar o gerador.** Gerador desenhado antes
do conteúdo produz a coisa errada com eficiência.

### 19.3 Formato

Cada carta registra: molde, casa, natureza, faixa, sinais presentes, ruído,
enunciado, resposta correta, consequência dos três resultados e ponte para hoje.

**O conteúdo paraleliza e o código não.** Cinco pessoas escrevem cartas enquanto
duas constroem o motor — é o que torna o projeto viável com sete integrantes de
experiência desigual.

## 20. Decisões de design registradas

Resumo. O registro completo, com contexto e alternativas descartadas, está em
`docs/00-historico/registro-decisoes-pendencias-lacunas.md`.

| # | Decisão |
|:-----|:----------------------------------------------------|
| D13 | Temática mercantil fictícia |
| D16 | Público 18 a 25 anos |
| D17 | Verificar custa recurso *(valor provisório)* |
| D18 | Casas do nível 1: Porto, Entreposto, Alfândega |
| D19 | Três modos como parâmetros da mesma sessão |
| D20 | Vitória por títulos; sem eliminação |
| D21 | Dificuldade por sinais e ruído, nunca por valor |
| D22 | Comparação por qualidade de decisão |
| D23 | Pixel art pela equipe; arte não é caminho crítico |
| D24 | Três dados por dia, escolhíveis |
| D25 | Corrida paralela; nenhum turno bloqueia |
| D26 | Plataforma: web PWA |
| D27 | Persistência em cinco níveis |
| D28 | Código de jogador para outro aparelho |
| D29 | Semente no servidor |
| D30 | Geração no cliente; trapaça aceita e documentada |
| D31 | Janelas em tempo de jogo |
| D32 | Contratos com prazo em turnos |
| D33 | Stack TypeScript, React, Vite, SVG, Supabase |
| D34 | Godot descartado |
| D35 | Escopo do MVP congelado |
| D36 | Denúncia com canais; gratuita no MVP |
| D37 | Ouro, feira e itens com conteúdo financeiro |
| D38 | Régua de reputação de dois lados |
| D39 | Temporada configurável por presets |
| D40 | Sessão autocontida; diário e glossário fora dela |
| D41 | Entrada tardia configurável; abandono não encerra |
| D42 | Tutorial pela curva, sem tela |
| — | Natureza do molde como proporção; baralho 55/45 |
| — | Legítima e mau negócio como atributo |

### Pendências que afetam este documento

**P21 — oficina de economia.** Custo da verificação, renda por rodada, preços da
feira e calibragem da apólice. Até lá, os números deste GDD são provisórios.

**P22 — reconciliar as casas.** O documento de cartas usa Porto, Alto-mar,
Entreposto e Praça; o nível 1 usa Porto, Entreposto e Alfândega. As premissas de
Alto-mar e Praça ficam para o nível 2.

**L12 — presets de temporada.** Os valores de duração ainda não foram definidos.
