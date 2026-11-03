# Histórico do Projeto — PAC 2026 / Jogo Sério

> Registro cronológico de etapas, artefatos e decisões.
> Documento vivo. Atualizado ao final de cada encontro.

**Versão:** 1.0 · **Atualizado em:** 18/08/2026 · **Marco atual:** M03 / M04 / M05

---

## 1. Identificação

| Campo | Conteúdo |
|---|---|
| Curso | Engenharia de Software — 3º semestre |
| Disciplina | PAC — Projeto Aplicado à Comunidade |
| Tema do ciclo | Desenvolvimento de um jogo sério |
| Duração | Dois semestres |
| Equipe | 7 integrantes |
| Cadência | Encontros quinzenais |
| Repositório | [preencher URL] |
| Responsável pela manutenção | [preencher] |

---

## 2. Finalidade e regras de manutenção

Este documento registra **o que foi feito, o que foi decidido e por quê**, ao longo de todo o ciclo. Não substitui o GDD nem a documentação de requisitos: é o registro cronológico que dá rastreabilidade a ambos.

Existe por três razões. Primeiro, decisão sem registro é decisão que volta: sem histórico, a mesma discussão se repete a cada dois encontros. Segundo, a banca avalia processo, e um projeto que mostra por que descartou alternativas demonstra maturidade que um projeto sem histórico não consegue alegar. Terceiro, com sete pessoas e encontros quinzenais, quem faltar a uma reunião precisa de um lugar único para se atualizar.

**Regras de manutenção:**

1. Atualizado **ao final de cada encontro**, pelo responsável designado, antes do encerramento da reunião. Registro feito depois, de memória, perde as alternativas descartadas — que são a parte mais valiosa.
2. Nada é apagado. Decisão revista recebe status `Substituída`, com referência à decisão que a substituiu. O histórico de mudança de rumo é informação, não vergonha.
3. Todo artefato produzido recebe **ID, versão e data**, e é registrado na seção 5.
4. Toda decisão que altere escopo, público, plataforma ou cronograma recebe **ID de decisão** e entra na seção 6, mesmo que pareça óbvia no momento.
5. Pendências não resolvidas migram de etapa em etapa até serem fechadas, mantendo o ID original.
6. IDs nunca são reaproveitados. Item removido continua ocupando o número.

### Convenções de identificação

| Prefixo | Uso | Exemplo | Onde vive |
|:--------|:-----------------|:--------|:----------|
| `M` | Marco do cronograma oficial | M09 | Seção 3 |
| `E` | Etapa interna (encontro) | E3 | Seção 4 |
| `A` | Artefato | A04 | Seção 5 |
| `D` | Decisão | D09 | Seção 6 |
| `P` | Pendência | P07 | Seção 7 |
| `R` | Risco registrado | R03 | Seção 8 |

---

## 3. Cronograma

### 3.1 Cronograma oficial do semestre

Definido em sala. É a referência mestra do projeto: o registro interno de etapas da seção 4 se subordina a ele.

| # | Marco | Início | Fim | Situação |
|:-----|:-------------------------------------|:-------|:-------|:-------------|
| M01 | Apresentação do PAC e objetivos | — | — | Concluído |
| M02 | Buscar temas de jogos / tema | 04/08 | 18/08 | Concluído |
| M03 | Definir o problema e o propósito do jogo | 18/08 | 18/08 | Em andamento |
| M04 | Entender o público-alvo | 18/08 | 01/09 | Em andamento |
| M05 | Pesquisar jogos sérios e soluções existentes | 18/08 | 01/09 | Não iniciado |
| M06 | Definir o conceito do jogo | 01/09 | 15/09 | Não iniciado |
| M07 | Definir mecânicas e gameplay | 01/09 | 15/09 | Não iniciado |
| M08 | Definir os objetivos de aprendizagem | 15/09 | 29/09 | Não iniciado |
| M09 | Criar requisitos funcionais e não funcionais | 29/09 | 06/10 | Não iniciado |
| M10 | Criar histórias de usuário e backlog | 29/09 | 13/10 | Não iniciado |
| M11 | Prototipar a experiência do usuário | 29/09 | 13/10 | Não iniciado |
| M12 | Modelar os dados | 13/10 | 27/10 | Não iniciado |
| M13 | Definir a arquitetura do software | 13/10 | 27/10 | Não iniciado |
| M14 | Definir tecnologias e ferramentas | 13/10 | 27/10 | Não iniciado |
| M15 | Definir a metodologia de desenvolvimento | 13/10 | 27/10 | Não iniciado |
| M16 | Definir padrões e boas práticas | 27/10 | 10/11 | Não iniciado |
| M17 | Planejar testes e validação | Cíclico | Cíclico | Não iniciado |
| M18 | Planejar o desenvolvimento | 10/11 | 24/11 | Não iniciado |
| M19 | Consolidar a documentação do projeto | 10/11 | 24/11 | Não iniciado |
| M20 | Defesa do projeto / pitch final | 10/11 | 24/11 | Não iniciado |

O escopo detalhado de cada marco consta do plano da disciplina. Quatro merecem transcrição, por definirem entregas que o projeto ainda não tem resolvidas:

- **M12 — Modelar os dados:** entidades, atributos, relacionamentos e modelo conceitual e lógico do banco de dados.
- **M13 — Definir a arquitetura:** front-end, back-end, banco de dados, APIs, autenticação e componentes principais.
- **M17 — Planejar testes e validação:** testes funcionais, usabilidade, critérios de qualidade e, principalmente, **como validar se o jogo cumpre seu objetivo educacional**.
- **M20 — Defesa e pitch final:** apresentação como se a equipe propusesse o desenvolvimento do jogo a um cliente ou investidor.

### 3.2 Leitura do cronograma — três observações estruturais

**O primeiro semestre não tem implementação.** O ciclo termina em documentação consolidada e pitch. Não há marco de codificação, protótipo funcional ou teste com usuário real — M11 é prototipação de experiência (wireframes e fluxos) e M17 é *planejar* testes, não executá-los. Consequência prática: o critério de "cabe em dois semestres" continua valendo para a escolha da frente, mas o risco de execução só se materializa em 2027.

**Outubro concentra sete marcos** (M09 a M15) em quatro semanas, incluindo requisitos, backlog, protótipo, modelo de dados, arquitetura, tecnologias e metodologia. É o gargalo do semestre e precisa de divisão de frentes de trabalho definida antes de 29/09.

**Há tensão entre M12/M13 e a decisão D09.** Os marcos preveem modelo de banco de dados, back-end, APIs e autenticação; a D09 estabeleceu web sem backend, sem login e sem servidor. Isso não é contradição fatal — um modelo conceitual de dados existe mesmo sem banco relacional, e "arquitetura sem back-end" é uma arquitetura legítima e defensável — mas exige alinhamento com o orientador antes de 13/10. Registrado como pendência P07.

### 3.3 Correspondência com o registro interno

| Etapa interna | Período | Marcos atendidos | Situação |
|:-------------------------------------|:---------------|:-------------------|:-----------|
| E0 — Constituição e enquadramento | Ago/2026 | M01, M02 | Concluída |
| E1 — Ideação individual | 04/08 – 18/08 | M02 | Concluída |
| E2 — Normalização e análise | Ago/2026 | M03 (parcial), M05 (parcial) | Concluída |
| E3 — Convergência e desenho de jogo | 18/08 – 01/09 | M03, M04, M05 | Em andamento |
| E4 — Seleção da proposta | Set/2026 | M04, M06 | Planejada |
| E5 — Conceito, mecânicas e aprendizagem | Set/2026 | M06, M07, M08 | Planejada |
| E6 — Requisitos, backlog e protótipo de UX | Set–Out/2026 | M09, M10, M11 | Planejada |
| E7 — Dados, arquitetura, tecnologias e método | Out/2026 | M12, M13, M14, M15 | Planejada |
| E8 — Padrões, planejamento e consolidação | Out–Nov/2026 | M16, M17, M18, M19 | Planejada |
| E9 — Defesa e pitch | Nov/2026 | M20 | Planejada |
| E10 — Implementação e validação em campo | 2027/1 | — | Planejada |

**Antecipações já realizadas.** Alguns marcos futuros já têm decisão tomada, o que é vantagem desde que registrada como provisória: a D09 antecipa parte de M13 e M14; a D12 antecipa a linguagem de M14 para a Frente C; e a análise de referências das três frentes antecipa parte de M05. Todas ficam sujeitas a confirmação formal na data do respectivo marco.

## 4. Registro das etapas

### E0 — Constituição e enquadramento

**Período:** agosto de 2026 · **Marcos:** M01, M02
**Objetivo:** entender o enunciado do ciclo e organizar a equipe.

**Atividades:** leitura do enunciado; definição de que o produto é um jogo sério, isto é, com objetivo construtivo além do entretenimento; estabelecimento da cadência quinzenal; distribuição inicial de papéis.

**Artefatos gerados:** nenhum documento formal.

**Decisões:** D01.

**Pendências abertas:** P01.

### E1 — Ideação individual

**Período:** 04/08 a 18/08/2026 · **Marcos:** M02
**Objetivo:** coletar uma proposta de tema por integrante, em formato comparável.

**Atividades:** elaboração de formulário curto de dez questões cobrindo ideia, problema, público, objetivo, mecânica, benefícios, desafios, viabilidade e referências; distribuição à equipe; coleta ao longo de duas semanas.

**Artefatos gerados:** A01, A02.

**Decisões:** D02, D03.

**Resultado:** nove propostas registradas, com profundidade de resposta bastante desigual — de dez campos completos a quatro campos com uma linha cada.

**Pendências abertas:** P02.

### E2 — Normalização e análise

**Período:** agosto de 2026 · **Marcos:** M03 e M05, parcialmente
**Objetivo:** tornar as propostas comparáveis sem privilegiar quem escreveu mais.

**Atividades:** conversão de todas as respostas para uma estrutura única de ficha; realocação de campos preenchidos fora de lugar; marcação explícita do que foi declarado, do que foi inferido e do que está faltando; levantamento de pontos fortes e fracos por proposta; formulação de perguntas dirigidas a cada autor.

**Artefatos gerados:** A03, A04.

**Decisões:** D04, D05, D06.

**Resultado:** nove fichas padronizadas, cada uma discutível isoladamente.

**Pendências abertas:** P01, P02, P03.

### E3 — Convergência e desenho de jogo *(em andamento)*

**Período:** 18/08 a 01/09/2026 · **Marcos:** M03, M04, M05
**Objetivo:** reduzir as nove propostas a frentes trabalháveis e resolver a lacuna comum a todas — as propostas descreviam aplicativos, não jogos.

**Atividades:** fusão de propostas afins em três frentes temáticas; definição de restrições técnicas comuns; elaboração de formulário de desenho de jogo, com perguntas sobre gênero, core loop, o que está em risco e retorno; preparação para montagem em formulário eletrônico.

**Artefatos gerados:** A05, A06.

**Decisões:** D07, D08, D09, D10, D11, D12.

**Pendências abertas:** P01, P02, P03, P04, P05, P06.

---

## 5. Registro de artefatos

| ID | Artefato | Tipo | Ver. | Data | Etapa | Situação |
|---|---|---|---|---|---|---|
| A01 | Formulário de ideação individual (10 questões) | Instrumento | 1.0 | Ago/2026 | E1 | Encerrado |
| A02 | Planilha de respostas da ideação | Dados | 1.0 | Ago/2026 | E1 | Encerrado |
| A03 | Fichas de conceito das propostas | Documento | 1.0 | Ago/2026 | E2 | Substituído por A04 |
| A04 | Escopos individuais das propostas (P1 a P9) | Documento | 1.1 | Ago/2026 | E2 | Vigente |
| A05 | Conceitos unificados — três frentes | Documento | 1.0 | Ago/2026 | E3 | Vigente |
| A06 | Formulário de desenho de jogo | Instrumento | 1.0 | Ago/2026 | E3 | Em coleta |
| A07 | Histórico do projeto (este documento) | Documento | 1.0 | Ago/2026 | — | Vigente |

**Artefatos previstos, por marco:** respostas do formulário de desenho e ata de seleção (M04, M06); documento de conceito e de mecânicas (M06, M07); objetivos de aprendizagem com matriz mecânica-aprendizado (M08); documento de requisitos funcionais e não funcionais (M09); product backlog com histórias de usuário (M10); wireframes e fluxo de navegação (M11); modelo conceitual e lógico de dados (M12); documento de arquitetura (M13); justificativa de tecnologias (M14); plano de metodologia e sprints (M15); guia de padrões e convenções (M16); plano de testes e de validação educacional (M17); roadmap e plano de desenvolvimento (M18); documentação consolidada (M19); pitch deck (M20).

---

## 6. Registro de decisões

Formato: **contexto → decisão → alternativas descartadas → consequência**. Uma decisão só entra aqui se tiver alternativa descartada; sem alternativa, é apenas uma tarefa.

### D01 — Produto será um jogo sério com causa social explícita
**Etapa:** E0 · **Situação:** Vigente
**Contexto:** o enunciado admite leitura ampla de "jogo sério", incluindo treinamento corporativo e simulação técnica.
**Decisão:** o produto terá causa social explícita e comunidade beneficiária identificável.
**Alternativas descartadas:** jogo de treinamento corporativo; jogo educacional genérico sem público definido.
**Consequência:** toda proposta precisa nomear a comunidade atendida; proposta sem comunidade não é avaliável.

### D02 — Coleta por formulário estruturado, não por brainstorming
**Etapa:** E1 · **Situação:** Vigente
**Contexto:** sete pessoas com disponibilidade e repertório desiguais.
**Decisão:** coletar por formulário escrito de dez questões, com prazo, antes de qualquer discussão coletiva.
**Alternativas descartadas:** brainstorming presencial; discussão livre em grupo.
**Consequência:** evitou ancoragem no primeiro a falar e produziu material comparável. Custo: respostas de profundidade muito desigual, tratado em D04.

### D03 — Uma proposta por integrante na primeira rodada
**Etapa:** E1 · **Situação:** Substituída por D11
**Contexto:** necessidade de garantir participação de todos.
**Decisão:** cada integrante apresenta uma proposta.
**Consequência:** dois integrantes não submeteram no prazo; um integrante apresentou quatro propostas ao longo do processo, o que a regra não previa.

### D04 — Padronizar em ficha de conceito com marcação de origem
**Etapa:** E2 · **Situação:** Vigente
**Contexto:** propostas com profundidade muito desigual favoreceriam quem escreveu mais, não quem teve a melhor ideia.
**Decisão:** converter tudo para estrutura única, marcando o que é declarado, o que é inferido e o que falta.
**Alternativas descartadas:** discutir as respostas como vieram; devolver aos autores para completar antes da análise.
**Consequência:** propostas incompletas seguiram discutíveis, com a lacuna visível e separada do mérito da ideia.

### D05 — Avaliar propostas isoladamente, sem matriz comparativa
**Etapa:** E2 · **Situação:** Vigente
**Contexto:** uma primeira análise incluiu matriz de pontuação comparativa entre propostas.
**Decisão:** remover o comparativo; cada proposta é avaliada por seus próprios méritos.
**Alternativas descartadas:** ranking por critérios ponderados.
**Consequência:** a discussão passa a ser sobre a qualidade interna de cada ideia. Custo: a equipe precisa fazer a comparação mentalmente na reunião.

### D06 — Registrar pontos fracos com franqueza, separando ideia de descrição
**Etapa:** E2 · **Situação:** Vigente
**Contexto:** risco de propostas mal descritas serem eliminadas por falta de dados, não por mérito.
**Decisão:** em cada ficha, distinguir explicitamente fraqueza da ideia de fraqueza da descrição.
**Consequência:** protege autores que escreveram pouco e evita atrito interno na fase de corte.

### D07 — Fundir propostas afins em três frentes temáticas
**Etapa:** E3 · **Situação:** Vigente
**Contexto:** nove propostas são inviáveis de aprofundar em paralelo; várias se sobrepunham.
**Decisão:** consolidar em três frentes — Defesa Financeira, Rotina Compartilhada e Simulador de Robótica e Programação.
**Alternativas descartadas:** votar diretamente entre as nove; eliminar por rodadas sucessivas.
**Consequência:** cada frente reúne o melhor de propostas que se completavam. Custo: perda de autoria individual, tratada em D08.

### D08 — Remover autoria das frentes
**Etapa:** E3 · **Situação:** Vigente
**Contexto:** as frentes resultam de fusão, e manter coautoria nominal poderia enviesar a discussão.
**Decisão:** frentes apresentadas sem autoria; respostas do formulário de desenho compiladas sem identificação.
**Alternativas descartadas:** nomear coautores em cada frente.
**Consequência:** a discussão fica sobre os desenhos, não sobre quem os escreveu.

### D09 — Restrições técnicas comuns a todas as frentes
**Etapa:** E3 · **Situação:** Vigente
**Contexto:** propostas tendiam a escopo incompatível com dois semestres e sete pessoas de terceiro semestre.
**Decisão:** web no navegador; sem backend, login ou servidor; sem multiplayer em tempo real, matchmaking ou ranking online; arte mínima; funcionamento em celular.
**Alternativas descartadas:** aplicativo nativo mobile; arquitetura com backend e contas de usuário.
**Consequência:** elimina LGPD na maior parte dos casos, reduz custo de infraestrutura e torna as propostas comparáveis. Custo: exclui mecânicas que dependem de persistência entre dispositivos.

### D10 — Inverter o foco da Frente B para o responsável, com progresso cooperativo
**Etapa:** E3 · **Situação:** Vigente
**Contexto:** as propostas de origem miravam a criança; a formulação seguinte previa que a criança lembrasse o responsável de interagir.
**Decisão:** o alvo pedagógico é o adulto, e o avanço exige ação das duas partes — nenhum lado progride sozinho.
**Alternativas descartadas:** manter a criança como público; manter a criança como lembrete ativo do adulto.
**Consequência:** preserva o engajamento do responsável sem colocar a criança em papel de cobrança, que produziria culpa e atrito familiar quando o adulto estivesse ausente ou exausto.

### D11 — Permitir múltiplas propostas por integrante no desenho de jogo
**Etapa:** E3 · **Situação:** Vigente · **Substitui:** D03
**Contexto:** limitar a uma proposta por pessoa reduziria material bom na fase em que ele mais importa.
**Decisão:** cada integrante pode enviar quantas propostas quiser, uma por resposta, sem juntar ideias na mesma submissão.
**Consequência:** volume não conta a favor nem contra; cada proposta é avaliada isoladamente.

### D12 — Linguagem da Frente C: Blockly com Python visível
**Etapa:** E3 · **Situação:** Vigente
**Contexto:** a proposta original mencionava Arduino e C#, que pertencem a ecossistemas distintos — Arduino programa em C/C++, não em C#.
**Decisão:** editor de blocos em Blockly, com o código Python equivalente exibido ao lado e atualizado em tempo real.
**Alternativas descartadas:** construir editor de blocos próprio; adotar C/C++ no estilo Arduino como linguagem exibida; adotar C#; exibir duas linguagens no MVP.
**Consequência:** elimina a maior fatia de engenharia do editor e reduz a barreira de entrada. A exibição em C++ do Arduino fica como evolução pós-MVP. Custo: distância maior em relação ao código que o grupo de robótica usa de fato.

---

## 7. Pendências abertas

| ID | Pendência | Aberta em | Bloqueia | Prazo | Responsável |
|---|---|---|---|---|---|
| P01 | Contato institucional real, com nome e telefone, para a comunidade parceira | E0 | M04 | 01/09 | [preencher] |
| P02 | Uma proposta individual não submetida | E1 | — | — | [preencher] |
| P03 | Exigências do curso para teste com menores e com pessoas idosas em equipamento público | E2 | M17 | 27/10 | [preencher] |
| P04 | Público-alvo da Frente A: adolescentes em escola ou adultos 60+ | E3 | M04, M06 | 01/09 | [preencher] |
| P05 | Ritmo de uso: sessão mediada por facilitador ou uso diário autônomo | E3 | M06, M07 | 15/09 | [preencher] |
| P06 | Revisor técnico externo ao grupo, específico por frente | E3 | M08 | 29/09 | [preencher] |
| P07 | Alinhar com o orientador o que M12 e M13 exigem diante da D09 — sem banco, sem back-end e sem autenticação | E3 | M12, M13 | 13/10 | [preencher] |
| P08 | Divisão de frentes de trabalho para o bloco de outubro (M09 a M15) | E3 | M09 | 29/09 | [preencher] |

---

## 8. Riscos registrados

| ID | Risco | Origem | Severidade | Mitigação adotada |
|---|---|---|---|---|
| R01 | Escopo crescer além de dois semestres | E2 | Alta | Restrições de D09; exigência de MVP mínimo em toda proposta |
| R02 | Nenhum parceiro institucional confirmado | E2 | Alta | P01 aberta desde E0; tratada como bloqueio de E4 |
| R03 | Frente C não paralelizar o trabalho entre sete pessoas | E3 | Alta | Registrada na ficha da frente; pesa na decisão de E4 |
| R04 | Produto virar aplicativo sem ser jogo | E3 | Alta | Formulário de desenho de jogo (A06) criado especificamente para isto |
| R05 | Conteúdo perecer antes do fim do ciclo | E3 | Média | Conteúdo em arquivo externo, editável sem recompilar |
| R06 | Teste com público vulnerável exigir aprovação ética fora do prazo | E2 | Média | P03 aberta; verificar com orientador antes de M17 |
| R07 | Concentração de sete marcos em outubro (M09 a M15) | E3 | Alta | P08 aberta; divisão de frentes definida até 29/09 |
| R08 | Divergência entre a arquitetura decidida (D09) e o que M12 e M13 esperam | E3 | Média | P07 aberta; alinhamento com orientador até 13/10 |

---

## 9. Organização do repositório

Este arquivo é o primeiro do diretório e serve de âncora até existir um `README.md`.

```
/
├── HISTORICO.md              ← este arquivo
├── README.md                 ← visão geral, a criar
├── docs/
│   ├── 01-propostas.md       ← escopos individuais (P1 a P9)
│   ├── 02-frentes.md         ← conceitos unificados das frentes A, B e C
│   ├── 03-formulario.md      ← instrumento de desenho de jogo
│   ├── 04-conceito.md        ← M06, a criar
│   ├── 05-mecanicas.md       ← M07, a criar
│   ├── 06-aprendizagem.md    ← M08, a criar
│   ├── 07-requisitos.md      ← M09, a criar
│   ├── 08-backlog.md         ← M10, a criar
│   ├── 09-arquitetura.md     ← M13, a criar
│   └── adr/                  ← uma decisão por arquivo, se a seção 6 crescer demais
├── assets/                   ← wireframes, diagramas, imagens
└── dados/                    ← respostas de formulários exportadas em CSV
```

**Sobre a pasta `adr/`:** enquanto o registro de decisões couber na seção 6 deste arquivo, mantenha-o aqui — arquivo único é mais fácil de ler e de buscar. Se passar de vinte decisões, migre para um arquivo por decisão em `docs/adr/`, mantendo os mesmos IDs.

**Sobre `dados/`:** exportar as respostas dos formulários como CSV e versionar. Planilha na nuvem muda sem deixar rastro; CSV commitado congela o estado no dia da análise, que é o que a banca pode querer conferir.

## 10. Convenções de versionamento

**Formato de commit.** Prefixo por tipo, seguido do ID afetado:

```
hist: registra E4 e decisões D13-D15
doc:  adiciona 04-conceito.md (M06)
dec:  D09 passa a Substituída por D16
dados: importa respostas do formulário de desenho
fix:  corrige data do marco M11
```

**O que justifica um commit separado.** Cada encontro gera pelo menos um commit no `HISTORICO.md`. Decisão que muda escopo, público, plataforma ou cronograma gera commit próprio, com a justificativa no corpo da mensagem — é ali que fica registrado o raciocínio que a seção 6 resume.

**Versão do documento.** Incrementar o campo `Versão` no cabeçalho: `+0.1` a cada etapa registrada, `+1.0` ao fim de cada semestre. Registrar na seção 11.

**Nada é reescrito.** Correção de erro factual pode ser editada no lugar. Mudança de rumo, não: a decisão antiga vira `Substituída` e a nova referencia a antiga. O `git log` guarda o resto.

## 11. Histórico de versões

| Versão | Data | Etapa | Alterações |
|:-------|:-----------|:------|:-----------------------------------------------------|
| 1.0 | 18/08/2026 | E3 | Criação. Registro de E0 a E3, decisões D01 a D12, cronograma oficial M01 a M20, pendências P01 a P08 e riscos R01 a R08 |

## 12. Modelo para as próximas etapas

Copiar ao final de cada encontro, colar na seção 4 e preencher antes de encerrar a reunião.

```markdown
### E[n] — [Título da etapa]

**Período:** [dd/mm a dd/mm] · **Marcos:** [M__]
**Objetivo:**
**Presentes:**

**Atividades realizadas:**

**Artefatos gerados:** [IDs — registrar também na seção 5, com versão e data]

**Decisões:** [IDs — registrar na seção 6 apenas se houver alternativa descartada]

**Pendências fechadas:** [IDs]

**Pendências abertas:** [IDs]

**Riscos novos ou alterados:** [IDs]

**Próximos passos e responsáveis:**
```

### Modelo de decisão

```markdown
### D[nn] — [Título em uma linha]
**Etapa:** E_ · **Situação:** Vigente
**Contexto:**
**Decisão:**
**Alternativas descartadas:**
**Consequência:**
```

Se não houver alternativa descartada, não é decisão: é tarefa, e o lugar dela é a lista de atividades da etapa.
