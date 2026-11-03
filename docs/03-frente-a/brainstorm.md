---
title: "PAC 2026 — Frente A"
subtitle: "Documento de Brainstorm: conceito unificado, possibilidades e decisões em aberto"
date: "Preparado para o encontro de 29/08/2026"
lang: pt-BR
---

# Resumo executivo

**O conceito.** Jogo de tabuleiro digital para celular, jogado sozinho ou com amigos em sessões assíncronas, em que cada jogador percorre um trajeto rumo a uma meta que escolheu, tomando decisões financeiras e enfrentando fraudes misturadas a oportunidades legítimas. O tabuleiro é a moldura; as cartas são o jogo sério.

**A tese de design:** verificar custa recurso, então o jogador escolhe entre avançar rumo à meta e ter segurança — a mesma tensão da vida real, nascida da mecânica e não de um texto.

| § | Conteúdo | Estado |
|:-----|:-------------------------------------------------------------|:---------------|
| 1–2 | Origem das três contribuições e o conceito unificado | Consolidado |
| 3 | Público-alvo: quatro opções, recomendação de 15 a 24 anos | **Em aberto** |
| 4 | Tabuleiro: tipos de casa, bifurcação, dados escolhíveis, eventos | Parcial |
| 5 | **As cartas:** gerador de três camadas, 15 moldes, 10 sinais, ruído | Consolidado |
| 6–7 | Recursos, meta, itens, empréstimo — e o placar duplo | Parcial |
| 8 | Multiplayer: sessões, log de ações, regra anti-abandono, emotes | Parcial |
| 9–10 | Objetivos de aprendizagem, métricas e dificuldades resolvidas | Consolidado |
| 11–12 | Decisões de engenharia e escada de escopo | Proposta |
| 13–14 | Quinze perguntas para o encontro e três cartas de exemplo | — |

**O que já está firme.** O gerador de três camadas, que impede memorização; o placar duplo, que impede ensinar paranoia; o custo da verificação, que torna a resposta óbvia numa decisão difícil; a meta escolhida, que dá direção e condição de vitória; e a corrida paralela sem turno bloqueante, que impede a partida de morrer por abandono.

**As cinco decisões do encontro.** Faixa etária primária — decide repertório, linguagem, valores e canal de validação, e trava todas as demais. Quantos tipos de casa no primeiro jogável. O que a verificação custa: dado, tempo ou dinheiro. Multiplayer no primeiro semestre ou como nível 2. Quem escreve as trinta primeiras cartas, e até quando.

**Dois avisos de produção.** Escrever trinta cartas à mão **antes** de projetar o gerador; e construir o solo como sessão de um participante desde o primeiro dia, senão o multiplayer vira reescrita.

---
---

# Como ler este documento

Este documento reúne, num conceito só, as duas propostas recebidas para a Frente A e a estrutura de tabuleiro discutida em seguida. **Não é uma decisão tomada.** É material de brainstorm: apresenta o que já está razoavelmente firme, o que tem várias saídas possíveis, e o que precisa ser decidido amanhã.

Está escrito para ser lido por quem nunca projetou um jogo. Termos de game design aparecem explicados na primeira vez que surgem, e o *Guia de Apoio* distribuído antes cobre o vocabulário básico. Se alguma parte parecer óbvia demais, pule; se parecer opaca, é falha do documento e vale sinalizar.

**Três avisos antes de começar.**

Primeiro: há muito mais conteúdo aqui do que cabe em dois semestres, **de propósito**. Brainstorm bom precisa de excesso para escolher bem. A seção 12 organiza tudo em escada de escopo e mostra o que entra no primeiro jogável.

Segundo: quase toda seção termina com decisões em aberto, marcadas assim: **⟶ decidir**. São elas que precisam sair da reunião.

Terceiro: onde eu tenho posição, ela está escrita e identificada como recomendação, não como fato. Discordar é o objetivo do encontro.

---
---

# 1. De onde vem o conceito

Três contribuições distintas se somaram, e cada uma resolveu um problema que as outras tinham.

## 1.1 A contribuição de Beatrice — o custo da verificação

A proposta trouxe um simulador de gestão em que o jogador administra orçamento ao longo de ciclos, recebendo estímulos legítimos e fraudulentos misturados, com três ações possíveis: agir direto, ignorar, ou verificar por canal independente.

O achado central está em uma frase da resposta: **verificar custa tempo e ação dentro do ciclo.**

Isso resolve o problema mais difícil de todo o projeto. Sem custo, "verificar" é sempre a resposta certa, o jogador verifica tudo e o jogo acaba na primeira hora. Com custo, cada verificação é uma escolha real — e é exatamente assim na vida: ninguém liga para o banco a cada mensagem recebida, porque tempo e paciência são finitos.

A proposta trouxe também a **escalada por patrimônio**: quanto mais o jogador acumula, mais sofisticadas ficam as tentativas contra ele. É resposta de retenção elegante, tematicamente verdadeira, e barata de implementar.

E trouxe o **patrimônio como projeto visível** — não um número abstrato, mas algo em construção que regride quando o jogador erra.

## 1.2 A contribuição de Gabriele — a meta escolhida

A proposta trouxe uma peça que faltava: **o jogador escolhe um objetivo maior no início** — juntar determinado valor para determinada coisa — e todas as decisões afetam o prazo para chegar lá.

Isso transforma acumulação em direção. Sem meta, o jogador junta dinheiro porque o jogo pede; com meta, ele junta *para alguma coisa*, e a tensão entre satisfação imediata e objetivo distante vira a segunda camada de decisão do jogo. É praticamente de graça em implementação e muda a experiência inteira.

A proposta identificou também a decisão difícil de forma independente: gastar agora ou guardar para a meta. Como as duas respostas convergiram em *Papers, Please* sem combinação prévia, há um sinal razoável de que o formato de julgamento sob pressão é o caminho certo.

## 1.3 A estrutura de tabuleiro

Sobre essas duas propostas veio a estrutura de tabuleiro, inspirada em Mario Party e Banco Imobiliário: percurso com casas de tipos diferentes, dados como recurso diário, eventos, e sessões compartilhadas com amigos.

O tabuleiro resolve quatro coisas de uma vez: dá **ritmo** (a sessão tem começo e fim naturais), dá **progressão espacial** (dá para ver onde se está), dá **variedade** (cada casa é um tipo de situação) e dá **estrutura para multiplayer** (todo mundo no mesmo percurso, comparando avanço).

## 1.4 O que cada peça resolve

| Peça | Problema que resolve |
|:---------------------------|:----------------------------------------------------------|
| Orçamento e patrimônio | Dá ao jogador algo a perder |
| Fraude como ameaça | Dá antagonista a um sistema que seria só planilha |
| Custo da verificação | Transforma a resposta óbvia em decisão difícil |
| Meta escolhida | Dá direção ao acúmulo e cria conflito de curto x longo prazo |
| Tabuleiro | Dá ritmo, variedade e moldura para multiplayer |
| Sessão compartilhada | Dá motivo para voltar depois que a novidade passa |


---


# 2. O conceito unificado

**Um jogo de tabuleiro digital para celular, jogado sozinho ou com amigos em sessões assíncronas, em que cada jogador percorre um trajeto tomando decisões financeiras — e enfrentando tentativas de fraude misturadas a oportunidades legítimas — rumo a uma meta que ele mesmo escolheu.**

Como funciona, em linguagem simples:

Você escolhe uma meta no começo — juntar dinheiro para uma viagem, um curso, uma moto, uma reserva de emergência. Todo dia você recebe alguns dados e usa para avançar pelo tabuleiro. Cada casa em que você para apresenta uma situação: uma cobrança, uma oportunidade, um imprevisto. A situação chega na forma de uma tela realista — uma mensagem, uma ligação, um boleto — e você decide o que fazer: agir, ignorar, ou gastar recurso para verificar se aquilo é verdade.

Algumas dessas situações são golpes. Outras são absolutamente legítimas, e recusá-las custa oportunidade. Você não sabe qual é qual antes de decidir, e o jogo conta seus dois tipos de erro em separado.

Se estiver jogando com amigos, todos percorrem o mesmo tabuleiro com o mesmo baralho, cada um no seu ritmo, vendo o progresso dos outros e reagindo.


---


# 3. Público-alvo

Ainda não decidido, e é a decisão mais importante do encontro porque quase todo o resto depende dela.

## 3.1 As opções

**Opção 1 — Ensino médio, 15 a 18 anos.**
A favor: gancho curricular direto com a BNCC, que já prevê educação financeira como competência transversal; acesso a escolas é a via de validação mais fácil; é o momento em que a pessoa começa a lidar com dinheiro próprio; e jogo com amigos é nativo dessa faixa. Contra: teste com menores exige autorização dos responsáveis e possivelmente aprovação ética, o que consome prazo administrativo. Golpes contra esse público têm perfil próprio — marketplace, contas de jogo, ingressos, vaga de emprego jovem — e o conteúdo precisa refletir isso, não copiar o repertório de golpe contra idoso.

**Opção 2 — Universitários e jovens adultos, 18 a 25 anos.**
A favor: público plenamente autônomo, sem autorização de responsável; é a fase do primeiro cartão de crédito, primeiro salário, primeiro aluguel e primeira dívida; a equipe tem acesso direto pela própria instituição; e a mecânica social funciona muito bem nessa faixa. Contra: não há gancho curricular, e a validação acontece dentro da própria bolha da equipe, o que enfraquece o argumento de extensão à comunidade.

**Opção 3 — Adultos, 26 a 45 anos.**
A favor: é onde os golpes causam maior prejuízo absoluto e onde há maior volume de tentativas registradas. Contra: é o público mais difícil de recrutar para teste, tem menos tempo para sessões, e o formato de tabuleiro com amigos não é natural nessa faixa.

**Opção 4 — Pessoas com 60 anos ou mais.**
Era o público da proposta original antes da estrutura de tabuleiro. **Recomendação: não.** Simulador de gestão com múltiplos recursos, tabuleiro, dados e sessões longas é o oposto do que serve a usuário com pouca autonomia digital. Manter esse público agora significaria abandonar quase tudo que foi construído nas últimas iterações. O gancho da política estadual de SC é real e valioso, mas não sobrevive a este formato.

## 3.2 Recomendação

**15 a 24 anos, com núcleo em 16 a 20.** A faixa aproveita o gancho curricular na ponta de baixo e a autonomia na ponta de cima, permite validar em escola e na universidade, e é onde o multiplayer entre amigos realmente funciona.

Se o grupo escolher trabalhar com menores, três providências entram já:

1. Consultar o orientador ainda esta semana sobre autorização de responsáveis e comitê de ética.
2. Nada de chat de texto livre entre jogadores — ver seção 9.4.
3. Nenhum dado pessoal coletado; identidade anônima gerada no dispositivo.

**⟶ decidir:** faixa etária primária. Tudo depois disso depende dela: repertório de golpes, linguagem das cartas, valores em jogo, duração da sessão, canal de validação.

## 3.3 Persona provisória

Enquanto a decisão não sai, uma persona de trabalho:

*Tem 17 anos, cursa ensino médio, tem celular próprio e conta digital. Recebe mesada ou faz bico. Já comprou em marketplace e já viu golpe em grupo de família. Joga no celular quase todo dia, quase sempre jogos curtos, e joga com os mesmos três ou quatro amigos. Sabe que golpe existe, acha que não cairia em um.*

Essa última frase é a mais importante para o design: **o público não acha que precisa disso.** O jogo precisa ser divertido primeiro e educativo por consequência, nunca o contrário.


---


# 4. O tabuleiro

## 4.1 Por que tabuleiro

O tabuleiro é uma **moldura**: um jeito de organizar a entrega de situações ao longo do tempo. Ele não é onde está a diversão — em Banco Imobiliário a diversão está na negociação, em Mario Party está nos minijogos e no caos. Tabuleiro sozinho é logística.

Aqui, o que precisa ser divertido são as **cartas**. E isso é uma boa notícia, porque as cartas também são onde está o aprendizado. Se as cartas forem boas, o jogo funciona; se forem burocráticas, nenhum tabuleiro salva.

## 4.2 Tipos de casa

Nomeadas por função, não por cor. Cor entrega o resultado antes de o jogador ler; nome ambíguo preserva a decisão.

| Casa | O que acontece | Papel no jogo |
|:---------------|:-----------------------------------------------------|:-------------------------|
| **Oportunidade** | Saca carta que oferece ganho — pode ser real ou golpe | Tentação; onde a ganância é testada |
| **Cobrança** | Saca carta que exige pagamento — pode ser real ou golpe | Medo; onde a pressa é testada |
| **Imprevisto** | Evento inesperado, sem escolha ou com escolha limitada | Ritmo; quebra o padrão |
| **Rotina** | Entrada de renda, pagamento de conta fixa | Respiro; recompõe recursos |
| **Encruzilhada** | Bifurcação: escolha de caminho | Decisão de rota |
| **Mercado** | Compra de itens e serviços | Preparação; ver seção 7 |
| **Praça** | Interação social; eventos coletivos | Onde o multiplayer aparece |

**⟶ decidir:** quantos tipos de casa entram no primeiro jogável. Recomendação: três — Oportunidade, Cobrança e Rotina. Os demais entram depois.

## 4.3 Bifurcação — o que tira o jogador da posição de passageiro

Num percurso único, o dado decide tudo e o jogador só assiste. **Com bifurcação, o dado vira recurso e a rota vira decisão.**

O desenho básico: nas Encruzilhadas o jogador escolhe entre um caminho **curto e arriscado** — mais casas de Oportunidade e Cobrança, chega antes na meta — e um **longo e seguro** — mais Rotina, menos exposição, atrasa a meta.

Isso cria uma decisão estratégica de alto nível que se repete a cada volta, e conversa diretamente com o conteúdo: correr risco para chegar antes é, literalmente, a decisão financeira que se quer ensinar.

Variações possíveis para discutir:

- **Pedágio:** o caminho curto cobra para entrar
- **Rota condicional:** só abre com reserva mínima ou item específico
- **Atalho de uso único** por volta
- **Rota que muda de perfil** conforme a rodada avança

## 4.4 Dados como recurso, não como destino

Três dados por dia, e aqui está a diferença entre um jogo com agência e um jogo de sorte: **o jogador rola os três de uma vez e decide quais usar e em que ordem.**

Isso é o que jogos de tabuleiro modernos chamam de *dice drafting* — em vez de "rolei 4, ando 4", o jogador pensa "tenho 2, 5 e 6; se uso o 6 agora caio na Oportunidade, mas gasto meu único dado alto e não alcanço o Mercado depois". Sorte gera a variedade; a escolha gera o jogo.

Possibilidades a discutir:

- **Guardar dado** para o dia seguinte, com limite
- **Combinar dois dados** num movimento só
- **Gastar dado como ação** em vez de movimento — e é aqui que se conecta o achado de Beatrice: **verificar uma carta custa um dado**
- **Dado extra** como recompensa
- **Dado viciado** como item negativo temporário

**A conexão mais importante do documento:** se verificar custa um dado, o jogador está sempre escolhendo entre *avançar rumo à meta* e *ter segurança*. Essa é a mesma tensão da vida real, e ela nasce da mecânica, não de um texto explicando.

**⟶ decidir:** três dados por dia é o número certo? Verificação custa dado, tempo, ou dinheiro?

## 4.5 Rodadas e eventos de mapa

Uma **rodada** fecha quando todos os jogadores da sessão gastaram suas ações do dia. No fim de cada rodada, o mapa pode se reorganizar: casas mudam de tipo, eventos aparecem, rotas abrem ou fecham.

Isso mantém o tabuleiro vivo sem exigir muitos mapas diferentes, e resolve barato o problema de memorização do percurso.

Eventos possíveis:

- **Onda de golpes** na região: mais cartas fraudulentas por algumas rodadas
- **Alta de preços:** contas fixas sobem
- **Vazamento de dados:** volume de mensagens suspeitas aumenta para todos
- **Feirão:** descontos reais, mas com golpes se disfarçando entre eles
- **Prazo de imposto:** cobrança legítima chegando junto com falsas

Repare que os eventos são **temáticos e verdadeiros**: fraude realmente vem em ondas, e é justamente durante campanha promocional legítima que o golpe se disfarça melhor.

**Cuidado importante:** evento de **contexto** — que afeta todo mundo igual — é ótimo. **Ataque direto** entre jogadores, no estilo Mario Party, não. Perder por decisão de outro jogador remove a agência que o resto do desenho passou tanto tempo construindo, e é o que faz muita gente detestar Mario Party.

---
---

# 5. As cartas — o coração do jogo

Esta é a seção mais importante do documento. Tudo o mais é moldura.

## 5.1 O problema a resolver

Se as cartas forem um baralho fixo, na terceira sessão o jogador decora "a mensagem da empresa tal é golpe" e para de ler. Isso não é só perda de rejogabilidade: **destrói o objetivo de aprendizagem**, porque a habilidade treinada passa a ser memória em vez de leitura de sinais.

A solução não é embaralhar textos prontos. É separar **superfície** de **sinal**.

## 5.2 A arquitetura em três camadas

Uma carta é gerada combinando três coisas independentes:

**Camada 1 — Molde.** A estrutura da situação. Uns quinze cobrem o repertório real:

| # | Molde | Natureza |
|:---|:-------------------------------------------|:--------------------|
| 1 | Cobrança de serviço em atraso | Pode ser legítima ou golpe |
| 2 | Reembolso ou estorno pendente | Pode ser legítima ou golpe |
| 3 | Atualização cadastral obrigatória | Quase sempre golpe |
| 4 | Prêmio ou sorteio ganho | Quase sempre golpe |
| 5 | Oferta de renda extra ou vaga | Pode ser legítima ou golpe |
| 6 | Empréstimo pré-aprovado | Pode ser legítima ou golpe |
| 7 | Contato de conhecido com número novo | Quase sempre golpe |
| 8 | Alerta de compra suspeita pelo banco | Pode ser legítima ou golpe |
| 9 | Encomenda parada com taxa pendente | Quase sempre golpe |
| 10 | Promoção relâmpago | Pode ser legítima ou golpe |
| 11 | Investimento com retorno garantido | Sempre golpe |
| 12 | Multa ou tributo com desconto hoje | Pode ser legítima ou golpe |
| 13 | Assinatura recorrente inesperada | Pode ser legítima ou golpe |
| 14 | Aluguel com sinal antecipado | Pode ser legítima ou golpe |
| 15 | Conta de consumo com valor atípico | Geralmente legítima |

**Camada 2 — Preenchimentos.** Empresa, valor, prazo, canal, horário, nome. Vêm de vocabulários e mudam a cada geração. É o que faz duas cartas do mesmo molde parecerem diferentes.

**Camada 3 — Sinais.** Lista fechada do que efetivamente determina se é golpe:

1. Canal não oficial
2. Pedido de dado sensível ou código
3. Urgência artificial — prazo hoje, últimas horas
4. Taxa antecipada para receber um valor
5. Remetente não verificável
6. Valor incompatível com o histórico do jogador
7. Pedido de sigilo
8. Endereço ou domínio estranho
9. Forma de pagamento atípica
10. Oferta boa demais para ser verdade

**A regra de ouro: a resposta correta é derivada dos sinais presentes, nunca do texto.** A mesma empresa aparece hoje como legítima e amanhã como golpe. Não há o que memorizar; o que se aprende é a ler os sinais — que é exatamente o objetivo de aprendizagem.

## 5.3 Ruído — a peça que quase todo mundo esquece

Você precisa de **cartas legítimas com características estranhas mas inofensivas**: erro de digitação numa mensagem verdadeira, cobrança chegando às 23h, empresa real porém desconhecida, valor alto mas previsto, remetente com nome abreviado.

Sem ruído, o jogador aprende "qualquer coisa esquisita é golpe" e vira paranoico — que é justamente o erro que o placar duplo existe para punir. **A dificuldade escala reduzindo sinais e aumentando ruído**, não aumentando o valor perdido.

## 5.4 As ações disponíveis

| Ação | Custo | Efeito |
|:-----------|:------------------|:-----------------------------------------------|
| **Agir** | O valor em questão | Paga, aceita, responde. Ganho se legítimo, perda se golpe |
| **Ignorar** | Nada | Nada acontece se golpe; perde a oportunidade ou entra em atraso se legítimo |
| **Verificar** | Um dado ou ação | Revela um ou dois sinais; depois ainda é preciso decidir |
| **Usar item** | O item | Efeito próprio — ver seção 7 |

Detalhe importante: **verificar não entrega a resposta**, revela sinais. O jogador continua tendo que julgar. Se verificar respondesse "isso é golpe", o jogo viraria uma questão de ter ou não ter recurso, e não de saber ler.

## 5.5 Determinismo por semente

Numa sessão compartilhada, todos os jogadores precisam enfrentar o mesmo baralho, ou não há comparação justa nem conversa possível.

Solução: a geração é determinística, com semente derivada do identificador da sessão mais o número da rodada. Mesma sessão, mesma rodada, mesmas cartas — sem precisar transmitir baralho nenhum pela rede. Bônus de engenharia: qualquer bug relatado é reproduzível.

## 5.6 Escada de dificuldade

| Faixa | Sinais por carta | Ruído | Característica |
|:-----------|:-----------------|:---------|:----------------------------------------|
| Inicial | 3 a 4 | Nenhum | Golpe evidente; ensina o repertório |
| Média | 2 | Pouco | Exige leitura atenta |
| Avançada | 1 | Bastante | Exige verificação; erro é esperado |
| Difícil | 1 ou 0 aparente | Muito | Sinal só aparece se verificar |

A escalada por patrimônio da proposta de Beatrice entra aqui: quanto mais o jogador acumula, mais a distribuição pende para as faixas avançadas.

## 5.7 Aviso de produção

**Escrevam trinta cartas à mão antes de projetar o gerador.** Os moldes precisam ser extraídos de conteúdo real — Procon, Febraban, imprensa, mensagens que os próprios integrantes receberam — e não imaginados no abstrato. Gerador desenhado antes do conteúdo produz a coisa errada com muita eficiência.

**Ganho colateral relevante:** molde, vocabulário, sinal e carta gerada são entidades com atributos e relacionamentos. Isso é o marco **M12 — Modelar os dados** resolvido com material legítimo, não inventado para cumprir tabela.


---


# 6. Recursos, meta e economia

## 6.1 O que o jogador administra

| Recurso | O que é | Por que existe |
|:--------------|:--------------------------------------------|:-------------------------------|
| **Saldo** | Dinheiro disponível agora | Recurso principal de decisão |
| **Reserva** | Poupança separada, de acesso mais lento | Ensina o conceito de emergência |
| **Dados** | Ações do dia | Tempo e atenção, que são finitos |
| **Progresso da meta** | Quanto falta para o objetivo | Direção e tensão de longo prazo |

Discussões possíveis: acrescentar **Crédito** (reputação que abre empréstimos melhores) e **Tranquilidade** (indicador que cai quando se decide sob pressão). Ambos são bons temas, mas cada recurso novo é uma coisa a mais para o jogador entender.

## 6.2 A meta — contribuição de Gabriele

O jogador escolhe no início. Exemplos: viagem, curso, notebook, moto, reserva de emergência, presente para alguém, mudança de casa.

A meta faz quatro coisas ao mesmo tempo: dá direção ao acúmulo; cria a tensão entre gasto imediato e objetivo distante; **serve como condição de vitória**, que o jogo ainda não tinha; e gera rejogabilidade barata, porque metas diferentes mudam duração e dificuldade sem exigir conteúdo novo.

Possibilidade interessante: **metas com perfis diferentes** — uma barata e rápida, uma cara e longa, uma que exige reserva constante. Isso é dificuldade ajustável quase de graça.

## 6.3 Itens e serviços

Comprados na casa Mercado. Cada item é, ele mesmo, conteúdo educativo.

| Item | Efeito | O que ensina |
|:-------------------------|:-----------------------------------------|:-------------------------------|
| **Seguro** | Cobre uma perda até certo valor | Pagar por proteção que talvez não se use |
| **Consulta** | Revela um sinal extra de uma carta | Verificação tem custo |
| **Reserva automática** | Separa parte da renda sem ação | Automatizar poupança funciona |
| **Adiamento** | Congela uma decisão até a próxima rodada | Pressa é evitável |
| **Segunda opinião** | Consulta outro jogador da sessão | Conferir com alguém é a defesa mais eficaz |

**A condição inegociável para o seguro:** ele **não pode ser sempre a escolha certa**. Se comprar sempre for ótimo, deixa de ser decisão e vira imposto. O preço precisa ser calibrado para que comprar seja errado com alguma frequência — e o jogador precisa terminar rodadas tendo pago por proteção que não usou. Esse desconforto *é* a lição sobre seguro.

## 6.4 Empréstimo entre jogadores

Aqui a recomendação é específica, e a diferença importa.

**Barganha livre — não.** Combinar valores e prazos exige máquina de proposta e contraproposta em modo assíncrono, o que é caro; trava um jogador esperando resposta do outro; e cria cobrança de dívida entre amigos reais, com potencial de constrangimento que um projeto acadêmico não deveria produzir de propósito.

**Empréstimo de termos fixos — sim, e é bom conteúdo.** O sistema define juros e prazo; um jogador oferece, outro aceita ou recusa. Sem negociação. O credor vê o juro entrando, o devedor vê o custo saindo. **Ensinar dívida pelos dois lados simultaneamente é raro e valioso**, e a implementação é uma transação simples em vez de um protocolo.

**⟶ decidir:** empréstimo entra ou fica para depois?


---


# 7. O placar duplo

Princípio já assentado nas iterações anteriores e que merece ser explicado a quem não acompanhou.

O jogo conta **dois tipos de erro em separado**:

- **Caiu no golpe** — agiu sobre algo fraudulento
- **Recusou o legítimo** — ignorou ou bloqueou algo verdadeiro

Existe porque punir só o primeiro ensina desconfiança generalizada, e desconfiança generalizada é dano, não aprendizado: produz gente que não abre mensagem do banco, não aceita cobrança verdadeira, não confia em oportunidade real. Praticamente todo material antifraude existente comete esse erro.

Na tela de resultado, os dois números aparecem lado a lado. Quem termina a partida com zero golpes e sete oportunidades perdidas **não venceu**.


---


# 8. Multiplayer e sessões

## 8.1 O modelo

Sessão identificada por código curto. Vários jogadores no mesmo tabuleiro, com o mesmo baralho gerado pela mesma semente, cada um avançando no próprio ritmo. Um jogador pode manter várias sessões ao mesmo tempo — uma sozinho, uma com a turma, uma com a família.

## 8.2 Arquitetura

O que foi descrito não é peer-to-peer, e isso é uma boa notícia: é cliente-servidor assíncrono, que é ordem de grandeza mais simples. Nada de WebRTC, sinalização, travessia de NAT ou servidor de relay.

O modelo mínimo:

- **Sessão** com código curto
- **Log de ações** append-only; cada ação é um registro pequeno
- **Estado derivado** do log, recalculado no cliente
- **Identidade anônima**, chave gerada no dispositivo, sem e-mail nem senha
- **Assinatura em tempo real** para ver progresso alheio quando o app está aberto

Com um backend gerenciado na camada gratuita, isso é trabalho de duas a três semanas. O log append-only torna a sincronização trivial: não há conflito a resolver, só ordem de chegada.

**Ganho para o cronograma:** isso resolve a pendência P07. A decisão anterior — sem backend, sem login, sem servidor — conflitava com os marcos M12 e M13, que pedem modelo de dados, arquitetura de back-end e autenticação. Com sessões, log e identidade anônima, os dois marcos passam a ter material real. **O multiplayer facilita o cumprimento do cronograma em vez de atrapalhar.** Exige registrar decisão nova substituindo a anterior.

## 8.3 A regra que salva a partida

**Nenhum turno bloqueia ninguém.** Cada jogador gasta seus dados quando quiser; os outros veem o progresso. Corrida paralela, não turno alternado.

Isso não é preferência estética. Partida por turnos entre amigos morre por abandono: se um dos quatro não joga a rodada dele, os outros três ficam parados, e a taxa de partidas abandonadas em jogos assíncronos de tabuleiro no celular é altíssima. A corrida paralela é imune a isso.

## 8.4 Interação social

**Emotes e frases predefinidas, não chat de texto livre.**

Texto livre entre usuários traz moderação de conteúdo, responsabilidade sobre o que é publicado e, se houver menores, tratamento de dado pessoal de criança e adolescente. Nada disso cabe num projeto de graduação. A substituição funciona igualmente bem — é o que Clash Royale e a maioria dos jogos de tabuleiro digitais fazem, exatamente por essa razão.

Repertório possível: reações rápidas, frases de comemoração e lamento, alerta de "cuidado com essa carta", pedido de segunda opinião.

Notificação fora do jogo exige service worker e chaves de push — caminho conhecido, mas não trivial. Dois cuidados: limite de frequência por jogador, senão emote vira ferramenta de perturbação; e notificação para menor merece linha explícita no documento de arquitetura.

## 8.5 Comparação e conquistas

O que dá para mostrar entre jogadores: progresso rumo à meta, placar duplo, sequência de dias jogados, conquistas temáticas.

**Cuidado com o ranking por patrimônio.** Ele premia quem arrisca e dá sorte. Se houver comparação, que seja por qualidade de decisão — proporção de acertos ponderada pela dificuldade — e não por saldo final.


---


# 9. Objetivos de aprendizagem e como medir

## 9.1 O que o jogador deve sair sabendo

1. Identificar os sinais recorrentes de engenharia social: urgência artificial, canal trocado, pedido de dado ou código, taxa antecipada, sigilo.
2. Distinguir situação fraudulenta de legítima **sem recusar o que é verdadeiro**.
3. Nomear a ação de verificação correta para uma situação suspeita.
4. Distinguir gasto essencial de supérfluo dentro de um orçamento com meta.
5. Reconhecer o efeito de juros e dívida em decisões de curto prazo.

## 9.2 Como medir

Instrumento de 10 a 12 itens — metade golpes, metade legítimos — aplicado antes e uma semana depois. Três métricas:

- **Sensibilidade:** proporção de fraudes corretamente rejeitadas
- **Especificidade:** proporção de legítimas corretamente aceitas
- **Ação nomeada:** proporção de casos em que a pessoa cita verificação por canal independente

As duas primeiras separadas evitam o falso sucesso de quem "melhorou" ficando paranoico.

**Vantagem estrutural:** o próprio jogo já registra tudo isso. O log de ações contém cada decisão, e o placar duplo é a métrica. **A avaliação vem embutida na arquitetura**, não é instrumento externo colado depois — o que é excelente material para o marco M17.

---
---

# 10. Dificuldades conhecidas e como resolvê-las

| Dificuldade | Por que acontece | Resolução proposta |
|:-----------------------------|:-------------------------------------|:--------------------------------------|
| Jogador memoriza as cartas | Baralho fixo | Gerador de três camadas (5.2) |
| Verificar vira sempre a resposta certa | Verificação sem custo | Verificar custa um dado (4.4) |
| Jogo ensina paranoia | Só o erro de credulidade é punido | Placar duplo e ruído (5.3, 7) |
| Dado tira a agência | Percurso único | Bifurcação e escolha de dado (4.3, 4.4) |
| Partida morre por abandono | Turno bloqueante | Corrida paralela (8.3) |
| Seguro vira compra automática | Preço baixo demais | Calibrar para errar às vezes (6.3) |
| Tabuleiro fica repetitivo | Mapa estático | Eventos de rodada (4.5) |
| Conteúdo não escala | Cartas escritas uma a uma | Moldes e vocabulários (5.2) |
| Aprendizado vai para o texto | Explicação depois da fase | Consequência visível no patrimônio |
| Moderação e LGPD | Chat livre e dado pessoal | Emotes e identidade anônima (8.4) |
| Motor bloqueia o time todo | Conteúdo depende do jogo pronto | Cartas escritas em paralelo (11.2) |
| Multiplayer vira reescrita | Solo feito com estado local | Solo é sessão de um participante (11.1) |


---


# 11. Duas decisões de engenharia que precisam ser tomadas cedo

## 11.1 Solo é uma sessão de um participante

**Construir o modo solo com a mesma estrutura de sessão e o mesmo log de ações do multiplayer, desde o primeiro dia de código.** Solo é a sessão sem convidados.

Feito assim, o multiplayer vira transporte. Feito com estado local e "adicionamos multiplayer depois", vira refatoração do jogo inteiro. Essa decisão se toma na primeira semana de implementação e define se o segundo semestre é viável.

## 11.2 Conteúdo paraleliza — e isso muda a divisão de trabalho

O projeto precisa de sessenta a noventa cartas, e escrevê-las **não depende do motor existir**. Cinco pessoas escrevem cartas e vocabulários enquanto duas constroem o jogo.

Isso corrige a principal fraqueza organizacional das outras frentes, onde quase todo mundo ficava bloqueado esperando o código. Aqui há trabalho real e paralelo desde a primeira semana, para quem programa e para quem não programa.


---


# 12. Escada de escopo

Somando tudo que este documento levanta, a proposta ficou maior que as três frentes originais juntas. Comercialmente é uma equipe pequena por um ano. Isso não significa cortar as ideias — significa ordená-las, e registrar o que fica de fora é entregável do marco M18.

## Nível 1 — Primeiro jogável

Tabuleiro curto com uma bifurcação · três tipos de casa (Oportunidade, Cobrança, Rotina) · três dados escolhíveis · gerador com cinco moldes e vinte cartas · meta única · placar duplo · sessão de um jogador, **construída como sessão de um participante**.

## Nível 2 — Núcleo completo

Multiplayer assíncrono com código de sessão · emotes · eventos de rodada · quinze moldes e sessenta cartas · três metas com perfis diferentes · casa Mercado com três itens · escada de dificuldade.

## Nível 3 — Se houver tempo

Eventos globais de contexto · conquistas · comparação por qualidade de decisão · seguro com calibragem fina · casa Praça · rotas condicionais.

## Nível 4 — Registrar como visão, não como escopo

Empréstimo entre jogadores · notificações push · módulos de dificuldade separados (a estrutura fácil/médio/difícil proposta por Beatrice, incluindo o simulador de fluxo de caixa de pequeno negócio, que é um jogo inteiro à parte) · personalização · modo professor.

---
---

# 13. Perguntas para o brainstorm

Organizadas por urgência. As cinco primeiras precisam sair da reunião de amanhã.

**Bloqueantes**

1. Faixa etária primária: 15 a 18, 18 a 25, ou os dois?
2. Quantos tipos de casa no primeiro jogável?
3. Verificar custa dado, tempo ou dinheiro?
4. Multiplayer entra no escopo do primeiro semestre ou fica documentado como nível 2?
5. Quem escreve as trinta primeiras cartas à mão, e até quando?

**Importantes, mas podem esperar uma semana**

6. Quantos dados por dia, e é possível guardar de um dia para o outro?
7. A meta é escolhida pelo jogador ou sorteada?
8. Quantas metas diferentes no primeiro jogável?
9. Reserva é recurso separado do saldo, ou simplificamos?
10. Ranking entre jogadores existe? Por qual critério?

**Abertas para discussão livre**

11. O tabuleiro é um circuito fechado, um percurso com fim, ou gerado a cada partida?
12. O jogo tem tema visual próprio — cidade, bairro, trajeto de vida — ou é abstrato?
13. Quanto o jogo deve se afastar da realidade brasileira concreta? Empresas fictícias ou genéricas?
14. Existe condição de derrota, ou só chegar à meta mais devagar?
15. Que nome esse jogo teria?

---
---

# 14. Anexo — três cartas de exemplo

Escritas à mão, para dar concretude ao que a seção 5 descreve em abstrato.

## Carta A — Cobrança, legítima com ruído

> **SMS — 23h14**
> "Sua fatura de energia venceu ontem. Valor R$ 187,40. Evite o corte: pague pelo aplicativo ou nas casas lotéricas."

*Sinais de fraude presentes:* nenhum.
*Ruído:* horário atípico, tom alarmista, o jogador de fato não pagou.
*Resposta correta:* agir. Ignorar gera multa e atraso.
*Armadilha:* o horário e o tom fazem parecer golpe.

## Carta B — Oportunidade, fraudulenta

> **WhatsApp — número desconhecido**
> "Parabéns! Você foi selecionado no programa de cashback do seu banco. Crédito de R$ 340,00 disponível. Para liberar, confirme o pagamento da taxa de processamento de R$ 29,90 neste link até as 18h de hoje."

*Sinais:* taxa antecipada para receber; urgência artificial; canal não oficial; remetente não verificável.
*Resposta correta:* ignorar.
*Custo do erro:* perde R$ 29,90 e ainda expõe dados, o que aumenta a frequência de cartas fraudulentas nas próximas rodadas.

## Carta C — Cobrança, ambígua — exige verificação

> **Ligação — identificada como "Central de Atendimento"**
> "Identificamos uma compra de R$ 1.240,00 no seu cartão em outro estado. Se não reconhece, vamos bloquear agora. Confirme os três últimos dígitos do código de segurança para prosseguir."

*Sinais:* pedido de código; urgência.
*Ruído:* bancos realmente ligam sobre compra suspeita, e o jogador pode ter tido movimentação alta recente.
*Resposta correta:* verificar — desligar e ligar no número do cartão.
*Por que é a melhor carta do baralho:* a premissa é verdadeira, o procedimento é falso. Ensina que a pergunta certa não é "isso pode acontecer?", e sim "por qual canal isso deveria chegar?".
