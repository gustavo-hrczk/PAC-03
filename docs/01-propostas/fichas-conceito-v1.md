# PAC 2026 — Jogo Sério
## Fichas de Conceito das Propostas — Documento de Discussão

**Semestre:** 3º — Engenharia de Software
**Fase atual:** Concepção (ideação → seleção → GDD → análise de requisitos)
**Encontros:** quinzenais
**Equipe:** 7 integrantes
**Status da coleta:** 5 de 7 propostas recebidas
**Data de compilação:** 18/08/2026

---

## 0. Como ler este documento

### 0.1 Por que padronizar

As respostas do formulário chegaram em profundidades muito diferentes: de propostas com dez campos completos e mecânica detalhada até propostas com quatro campos e uma linha por campo. Discutir nesse estado favorece quem escreveu mais, não quem teve a melhor ideia. Este documento normaliza tudo no mesmo esqueleto para que a comparação seja sobre o mérito da proposta, não sobre o esforço de redação.

### 0.2 Padrão adotado: Ficha de Conceito (Game Concept Sheet)

O artefato escolhido é a **Ficha de Conceito**, que na prática de desenvolvimento antecede o GDD. Ela existe justamente para a fase de decisão: é curta o suficiente para ser lida em reunião e estruturada o suficiente para virar a espinha dorsal do GDD depois. Os 12 campos abaixo são fixos e sempre aparecem na mesma ordem, mesmo quando vazios — um campo vazio é informação (indica risco de imaturidade da proposta).

| # | Campo | Função no GDD futuro |
|---|---|---|
| 1 | Identificação | Capa / controle de versão |
| 2 | High Concept | Seção 1 — Visão geral |
| 3 | Causa social e problema | Seção 2 — Justificativa (obrigatória em jogo sério) |
| 4 | Público-alvo | Seção 3 — Audiência e perfil de jogador |
| 5 | Objetivos de aprendizagem | Seção 4 — Objetivos verificáveis |
| 6 | Pilares de design | Seção 5 — Diretrizes de decisão |
| 7 | Core loop e mecânica | Seção 6 — Gameplay |
| 8 | Progressão e conteúdo | Seção 7 — Estrutura e economia |
| 9 | Escopo do MVP | Seção 8 — Vertical slice / backlog |
| 10 | Plataforma e técnico | Seção 9 — Requisitos técnicos |
| 11 | Riscos e dificuldades | Anexo — Matriz de risco |
| 12 | Validação | Seção 10 — Plano de avaliação |

### 0.3 Convenções de rastreabilidade

| Marcação | Significado |
|---|---|
| Texto normal | Declarado pelo autor na resposta do formulário |
| *(inferido)* | Reconstrução a partir do que o autor escreveu — **precisa de confirmação dele** |
| **[LACUNA]** | Não respondido. O autor precisa preencher antes da votação final |

O campo mais importante de toda ficha de jogo sério é o **7.1 — Alinhamento mecânica ↔ objetivo**. É ali que se decide se a proposta é um jogo sério de verdade ou um questionário com skin de jogo. Uma proposta pode ter causa excelente e falhar aqui.

### 0.4 Escala de maturidade

Aplicada ao final de cada ficha. Não avalia a ideia, avalia o quanto ela está **pronta para virar GDD**.

- **M1 — Semente:** existe um tema, falta mecânica e público definidos.
- **M2 — Conceito:** tema, público e mecânica declarados, sem escopo nem validação.
- **M3 — Conceito viável:** acima + MVP delimitado + caminho de validação identificado.
- **M4 — Pronto para GDD:** acima + objetivos verificáveis + riscos mapeados com mitigação.

---

# PROPOSTA P1 — Educação Financeira Gamificada

### 1. Identificação
- **ID:** P1
- **Título provisório:** *(sem título declarado)* — sugestão de referência interna: **"Meu Primeiro Orçamento"**
- **Autora:** Beatrice Fischer
- **Submissão:** 05/08/2026
- **Gênero:** Quiz / trivia gamificado com simulação de recursos

### 2. High Concept
Jogo de quiz e trivia gamificado no estilo Duolingo em que o jogador completa desafios diários curtos, toma decisões financeiras simuladas e monta orçamentos, para aprender educação financeira básica de forma prática e recorrente.

### 3. Causa social e problema
A falta de educação financeira nas escolas brasileiras. A maioria dos alunos do ensino fundamental e médio termina a educação básica sem noções práticas de orçamento, poupança, juros ou consumo consciente, o que contribui para endividamento e decisões financeiras ruins na vida adulta.

**Ancoragem institucional:** o tema já é previsto na BNCC como competência transversal — a autora usa isso como justificativa de aderência curricular, o que é um ponto forte para negociar entrada em escola.

### 4. Público-alvo
- **Primário:** 11 a 17 anos, ensino fundamental (anos finais) e médio, prioritariamente escola pública.
- **Contexto de uso:** duplo — em sala com orientação do professor e em casa pelo celular.
- **Perfil de jogador:** acostumado a jogos mobile e apps gamificados; pouco ou nenhum contato prévio com conteúdo financeiro estruturado.
- **Secundário:** professores, usando o jogo como apoio em aula.

### 5. Objetivos de aprendizagem (verificáveis)
Depois de jogar, o jogador será capaz de:
1. Montar um orçamento pessoal simples, distinguindo gastos essenciais de supérfluos.
2. Reconhecer os efeitos de juros e dívidas em decisões cotidianas.
3. Tomar decisões financeiras simuladas mais conscientes — poupar vs. gastar, comparar preços, planejar uma compra.

**Nota de avaliação:** os três são operacionalizáveis em pré/pós-teste. É o conjunto de objetivos mais mensurável entre as cinco propostas.

### 6. Pilares de design *(inferidos)*
1. **Consequência antes de explicação** — o jogador descobre a regra pelo resultado.
2. **Hábito por sessões curtas** — lições de poucos minutos, retorno diário.
3. **Situações do cotidiano brasileiro** — decisões reconhecíveis pelo jogador.

### 7. Core loop e mecânica

**Loop declarado:** receber uma situação financeira do dia a dia → tomar uma decisão (gastar, poupar, investir, negociar) → ver a consequência simulada dessa decisão no orçamento, no saldo ou numa meta.

**7.1 Alinhamento mecânica ↔ objetivo**
A autora argumenta que é a repetição decisão-consequência, e não um texto explicando teoria, que cria o hábito de pensar antes de gastar — o aprendizado vem da prática, como no Duolingo, em que o jogador erra, vê o resultado e ajusta.

**Avaliação crítica:** o alinhamento é válido para os objetivos 1 e 3. Para o objetivo 2 (juros compostos), há risco de a mecânica não conseguir mostrar o efeito, porque juros só ficam visíveis em horizonte longo, e sessões curtas comprimem o tempo. Fica como questão de design a resolver no GDD: como tornar o custo do juro sensível dentro de uma sessão de 3 minutos. Há também tensão declarada entre o rótulo "quiz/trivia" e a mecânica de simulação de orçamento — são duas mecânicas distintas, e a equipe precisa decidir qual é a principal.

### 8. Progressão e conteúdo
Sistema de progressão com XP, pontos e streak, organizado em módulos temáticos, cada módulo com lições curtas.
**[LACUNA]** Quantidade total de módulos pretendida e critério de desbloqueio.

### 9. Escopo do MVP
**Dentro:** um módulo único ("Orçamento do mês") com 5 a 10 lições curtas em formato quiz/decisão, sistema simples de pontos e streak, e uma tela de resultado mostrando o orçamento final do jogador.
**Fora (recorte a explicitar):** *(inferido)* múltiplos módulos, investimentos, perfil de responsável, ranking social.
**Justificativa do recorte:** entrega o objetivo de praticar decisão financeira e ver consequência com um único módulo.

### 10. Plataforma e requisitos técnicos
- **Prioritária:** mobile.
- **Secundária:** web.
- **[LACUNA]** Engine/stack pretendida, necessidade de backend para persistir streak e progresso.

### 11. Riscos e dificuldades

| Risco | Descrição (autora) | Severidade *(inferida)* | Mitigação |
|---|---|---|---|
| Técnico | Sistema de progressão, XP e simulação de orçamento com múltiplas variáveis pode ficar complexo no prazo | Média | Reduzir variáveis do simulador a 3 no MVP (renda, gasto fixo, gasto variável) |
| Pesquisa/conteúdo | Precisa de fonte confiável — professor de matemática/economia ou material da BNCC/Banco Central | Média | Usar material do "Meu Bolso em Dia" como base e submeter a um professor para revisão |
| Ético | Tema não é sensível, mas há risco de estigmatizar realidades de pobreza e endividamento dos alunos | **Alta** | Situações não devem punir o jogador por baixa renda; separar "erro de decisão" de "condição socioeconômica" |
| Acesso ao público | Depende de autorização de escola/professor para testar com alunos reais | Média | Iniciar contato imediatamente (aluno menor exige autorização dos responsáveis) |
| Escopo | Risco real de número de lições e mecânicas crescer demais | Média | Congelar MVP em 1 módulo e 10 lições |

**Observação:** o risco ético aqui é subestimado pela autora. Público menor de idade em escola pública com tema de dinheiro exige cuidado redacional em cada situação do jogo — e possivelmente aprovação ética, dependendo do que a coordenação do curso exigir para testes com menores.

### 12. Validação
- **Parceiro possível:** a escola onde um dos membros da equipe estudou — depende de confirmação com professor/coordenação.
- **Método** **[LACUNA]** — não declarado. Sugestão: pré/pós-teste de 8 questões + observação de sessão em sala.
- **Métricas** **[LACUNA]** — sugestão: taxa de acerto em decisões, retenção D1/D7, delta pré/pós.

### Maturidade: **M3 — Conceito viável**
Falta apenas definir método de validação e resolver a ambiguidade quiz vs. simulação para chegar a M4.

---

# PROPOSTA P2 — Gestão de Tempo e Antiprocrastinação

### 1. Identificação
- **ID:** P2
- **Título provisório:** **[LACUNA]**
- **Autora:** Gabi
- **Submissão:** 11/08/2026
- **Gênero:** **[LACUNA]** — não declarado. A resposta traz "produtividade", que é tema, não gênero.

> **Aviso de integridade:** esta é a proposta com menos informação declarada (4 de 10 campos). Quase todo o corpo desta ficha é lacuna. Ela **não está em condição de ser comparada com as demais** hoje. A autora precisa complementar antes de qualquer votação, ou a proposta será eliminada por falta de dados e não por mérito — o que seria injusto com a ideia, que tem um núcleo defensável.

### 2. High Concept
*(reconstruído a partir dos fragmentos)* Jogo de produtividade em que o jogador completa tarefas do dia a dia para aprender a gerenciar o próprio tempo.
**[LACUNA]** Gênero e ação principal não declarados. Não está definido se as tarefas são reais (o jogo espelha a vida do usuário) ou fictícias (o jogo simula uma rotina) — **essa é a decisão que define o projeto inteiro** e não pode ficar aberta.

### 3. Causa social e problema
Declarado: "procrastinação".
**[LACUNA]** Não há caracterização do problema: quem sofre, em que contexto, com que consequência, com que evidência. Procrastinação como tema isolado não configura causa social — precisa ser ancorada em um recorte (evasão escolar? saúde mental de estudantes? desempenho acadêmico?).

### 4. Público-alvo
- **Primário:** crianças, adolescentes e adultos; "qualquer lugar"; hábito de jogo declarado como irrelevante porque não haveria mecânicas complexas.
- **Secundário:** possibilidade de perfil kids + perfil de responsável, a depender de alinhamento.

**Avaliação crítica:** "crianças, adolescentes e adultos em qualquer lugar" é ausência de público-alvo, não um público-alvo amplo. Uma criança de 8 anos e um adulto de 35 têm modelos mentais de tempo, autonomia e recompensa incompatíveis — não existe uma mecânica única que sirva bem aos dois. Este é o principal ponto a resolver com a autora.

### 5. Objetivos de aprendizagem
Declarado: depois de jogar, o jogador passará a gerenciar melhor o tempo livre e priorizar as responsabilidades.
**Avaliação:** é um objetivo, mas não é verificável na forma atual — "gerenciar melhor" não tem instrumento de medida. Precisa virar algo como "será capaz de ordenar 5 tarefas por prioridade usando critério de urgência × importância".

### 6. Pilares de design
**[LACUNA]**

### 7. Core loop e mecânica
**[LACUNA]** — campo não respondido.

**7.1 Alinhamento mecânica ↔ objetivo:** impossível avaliar. Sem mecânica declarada, não há como julgar se o jogo ensina ou apenas registra tarefas. **Risco central:** sem core loop, a proposta tende a virar um to-do list com pontos, que é a armadilha clássica desse tema — a ferramenta cobra a disciplina que deveria ensinar.

### 8. Progressão e conteúdo
**[LACUNA]**

### 9. Escopo do MVP
**[LACUNA]** — não declarado. Sem MVP definido, não há como estimar viabilidade em 2 semestres.

### 10. Plataforma e requisitos técnicos
- **Declarada:** mobile.
- **[LACUNA]** Stack, backend, necessidade de sincronização entre perfis kids/responsável.

### 11. Riscos e dificuldades
**[LACUNA]** — campo não respondido. Riscos identificados por análise externa:

| Risco *(inferido)* | Severidade | Observação |
|---|---|---|
| Público indefinido | **Alta** | Bloqueia definição de mecânica, arte e linguagem |
| Ausência de core loop | **Alta** | Bloqueia estimativa de escopo |
| Sobreposição com P5 (Lucas) | **Alta** | Ver seção comparativa — as duas propostas convergem no mesmo território |
| Ético (se envolver menores + perfil de responsável) | Média | Dados de rotina de criança são dado sensível sob LGPD |
| Verificabilidade do objetivo | Média | Difícil provar mudança de hábito em janela de 1 semestre |

### 12. Validação
**[LACUNA]** — nenhum parceiro, método ou métrica declarados.

### Maturidade: **M1 — Semente**
Tem tema e plataforma. Falta praticamente todo o resto.

---

# PROPOSTA P3 — Mercado Comunitário / Cidade Solidária

### 1. Identificação
- **ID:** P3
- **Título provisório:** *(sem título declarado)* — sugestão de referência interna: **"Vizinho Solidário"** (termo usado pela própria autora)
- **Autora:** Karina Medeiros
- **Submissão:** 12/08/2026
- **Gênero:** Construção/gerenciamento de cidade com progressão por níveis

> **Nota de normalização:** na resposta original, o conteúdo do campo 4 (objetivos do jogador) foi preenchido com a estrutura de níveis e mecânica, e o campo 5 (mecânica) recebeu uma única frase. Realoquei o conteúdo para os campos corretos e sinalizei o objetivo de aprendizagem real como lacuna, porque ele não foi declarado em nenhum campo.

### 2. High Concept
Jogo de construção de cidade em que o jogador realiza doações — registradas em um mercado comunitário físico — e progride por níveis, desbloqueando personagens e elementos para construir a própria cidade.

**Característica estrutural que distingue esta proposta:** é a única em que a ação do jogador ocorre **fora da tela e no mundo real, com efeito material sobre terceiros**. As demais propostas simulam; esta intermedia doações reais. Isso muda a natureza do projeto — de jogo educativo para plataforma de mobilização com camada lúdica.

### 3. Causa social e problema
Pessoas em situação de dificuldade financeira; famílias necessitadas do bairro.
**[LACUNA]** Falta caracterização: qual bairro, qual demanda concreta, existe rede de doação já operando ali, qual a lacuna que o jogo preenche.

### 4. Público-alvo
- **Primário:** "vizinhança no geral" — moradores de bairro dispostos a doar.
- **Beneficiários (categoria distinta do jogador):** famílias necessitadas do bairro.
- **[LACUNA]** Faixa de idade, contexto de uso, hábito de jogo. Não declarados.

**Ponto de atenção conceitual:** aqui há **dois públicos com papéis assimétricos** — quem joga e quem recebe. Nenhuma outra proposta tem essa separação. Ela precisa ser tratada explicitamente no GDD, inclusive para evitar que o beneficiário apareça como recurso do jogo.

### 5. Objetivos de aprendizagem
Declarado apenas: "porque ele vai pensar sempre no próximo".
**[LACUNA]** Nenhum objetivo verificável declarado. Reconstrução possível a validar com a autora: *(inferido)* "depois de jogar, o jogador passará a doar com regularidade e a reconhecer as demandas materiais concretas da própria vizinhança".

### 6. Pilares de design *(inferidos)*
1. **Ação real precede recompensa virtual.**
2. **Progressão por escalada de tipo de doação**, não por volume.
3. **Reconhecimento comunitário** como motivador principal.

### 7. Core loop e mecânica

**Loop reconstruído:** doar item real → levar até o ponto de armazenamento → doação registrada/validada → ganhar progresso → desbloquear elementos e construir a cidade → subir de nível e acessar nova categoria de doação.

**Estrutura de níveis declarada:**
- Nível 1 — itens de cesta básica
- Nível 2 — mudas para horta comunitária
- Nível 3 — produtos de higiene e limpeza
- (continua)
- A cada ~10 doações, o "vizinho solidário" conquista um personagem melhor no jogo

**Elemento físico:** um local que armazenará as doações, onde as pessoas levam os produtos.

**7.1 Alinhamento mecânica ↔ objetivo**
A justificativa declarada é que a mecânica faz o jogador "pensar sempre no próximo". O alinhamento é fraco como formulado: o jogo **recompensa** a doação, não **ensina** sobre a causa. Se o objetivo é conscientização, a mecânica atual pode produzir doação por recompensa e não por consciência — e o comportamento tende a cessar quando a recompensa cessa. Se, por outro lado, o objetivo aceito for **mobilização** (aumentar volume de doações reais no bairro) em vez de aprendizado, a mecânica está adequada e o problema é de enquadramento, não de design. **Essa decisão precisa ser tomada em sala.**

### 8. Progressão e conteúdo
Níveis escalonados por categoria de doação; desbloqueio de personagens a cada ~10 doações; construção incremental da cidade do jogador.
**[LACUNA]** Quantos níveis, o que acontece ao fim, o que sustenta o jogador depois do último nível.

### 9. Escopo do MVP
**[LACUNA]** — não declarado. Recorte mínimo *(inferido)*: cadastro de doador, registro manual de doação por um operador do ponto de coleta, 3 níveis, 5 elementos de cidade desbloqueáveis.

### 10. Plataforma e requisitos técnicos
**[LACUNA]** — não declarada.
**Requisitos que a proposta implica** *(inferidos)*: backend obrigatório, autenticação de usuário, painel de operador para validar doações, persistência de estado de cidade. **É a proposta com maior carga técnica mínima entre as cinco**, porque nada funciona sem servidor e sem um operador humano no ponto de coleta.

### 11. Riscos e dificuldades

| Risco | Severidade | Observação |
|---|---|---|
| Ético (declarado pela autora) | **Alta** | Público vulnerável. Risco de gamificar a pobreza e de expor beneficiários |
| **Dependência operacional externa** *(inferido)* | **Crítica** | O jogo exige um ponto físico de coleta, alguém para operá-lo e um fluxo logístico. Isso não é escopo de software e a equipe não controla |
| **Verificação de doação** *(inferido)* | **Crítica** | Sem forma de comprovar a doação, o sistema é trivialmente burlável. Com forma de comprovar, exige operador presencial constante |
| Institucional (declarado) | Alta | Negociar benefício simbólico de IPTU com a Prefeitura envolve trâmite público fora do prazo de 2 semestres |
| Técnico *(inferido)* | Alta | Backend + painel administrativo + app, com 7 pessoas em 3º semestre |
| Escopo *(inferido)* | Alta | Camada de construção de cidade é, por si só, um jogo completo |

**Avaliação franca:** esta é a proposta com a causa social mais direta e imediata do conjunto — e a de execução mais difícil, porque a maior parte do risco está **fora do software**. A viabilidade depende de existir, já hoje, uma instituição operando coleta no bairro que aceite ser o ponto físico. Se essa instituição existir e aceitar, a proposta ganha muita força. Se não existir, ela não é executável em 2 semestres.

### 12. Validação
- **Instituição citada:** Prefeitura, para negociar redução simbólica de IPTU como benefício.
- **Comunidade:** pessoas do bairro.
- **[LACUNA]** Nome de instituição de coleta, contato, método e métricas. O campo de viabilidade foi respondido apenas com a palavra "avaliável".

### Maturidade: **M2 — Conceito**
Tema, mecânica e níveis declarados; sem escopo, sem plataforma, sem objetivo verificável, sem parceiro confirmado.

---

# PROPOSTA P4 — Investigação de Barreiras de Acessibilidade

### 1. Identificação
- **ID:** P4
- **Título provisório:** *(sem título declarado)* — sugestão de referência interna: **"Denúncia"** ou **"Caso Acessível"**
- **Autora:** Giovanna Lopes Pontes
- **Submissão:** 17/08/2026
- **Gênero:** Investigação e puzzle

### 2. High Concept
Jogo de investigação e puzzle em que o jogador investiga ambientes, encontra evidências e identifica barreiras de acessibilidade, para perceber problemas de inclusão que passam despercebidos no cotidiano e aprender a propor soluções mais acessíveis.

### 3. Causa social e problema
A falta de acessibilidade e a dificuldade de reconhecer barreiras enfrentadas por pessoas com deficiência e outras pessoas com necessidades específicas em ambientes públicos e privados. Muitas barreiras não são imediatamente perceptíveis para quem não é diretamente afetado por elas. A proposta busca mostrar que acessibilidade não envolve apenas a existência de uma rampa, mas também circulação, comunicação, sinalização, acesso à informação e organização dos espaços.

**Força da formulação:** o problema é definido como um **problema de percepção**, não de informação. Isso é raro e é exatamente o que justifica usar um jogo em vez de uma cartilha — barreira invisível é conteúdo que se descobre, não que se lê. A causa também tem respaldo normativo disponível (NBR 9050, Lei Brasileira de Inclusão), o que dá base de conteúdo confiável.

### 4. Público-alvo
- **Primário:** 14 a 24 anos, estudantes de escolas e universidades, com contato casual ou frequente com jogos digitais.
- **Contexto de uso:** individual ou como atividade complementar em instituições de ensino, em ações de cidadania, inclusão e acessibilidade.
- **Secundário:** professores, profissionais da educação e instituições que queiram usar o jogo como ferramenta de conscientização.

### 5. Objetivos de aprendizagem (verificáveis)
Depois de jogar, o jogador será capaz de:
1. Identificar diferentes tipos de barreiras de acessibilidade presentes em ambientes cotidianos.
2. Reconhecer que uma solução aparentemente acessível pode não resolver completamente uma barreira.
3. Relacionar problemas encontrados a possíveis soluções.

**Nota:** o objetivo 2 é o mais sofisticado apresentado por qualquer proposta do grupo — vai além de identificar e chega a avaliar a adequação de uma solução. Também é o mais difícil de ensinar e o mais difícil de medir.

### 6. Pilares de design *(inferidos)*
1. **Descoberta em vez de exposição** — o jogador encontra a barreira, não é informado dela.
2. **Perspectiva de observador, não de simulação** — declarado explicitamente pela autora.
3. **Evidência → diagnóstico → solução** como cadeia obrigatória de raciocínio.

### 7. Core loop e mecânica

**Loop declarado:** receber uma denúncia sobre um local → explorar o ambiente → observar objetos e ambientes, conversar com personagens → registrar evidências → relacionar cada evidência a uma barreira de acessibilidade → escolher ou elaborar uma possível solução → receber resultado da investigação.

**7.1 Alinhamento mecânica ↔ objetivo**
A mecânica ensina por observação e resolução de problemas, fazendo o jogador descobrir as barreiras durante a exploração em vez de receber uma explicação sobre elas.

**Avaliação crítica:** este é o alinhamento mais forte do conjunto. O ato de procurar uma barreira invisível **é** literalmente a habilidade que se quer treinar — mecânica e objetivo de aprendizagem são a mesma coisa, o que é o padrão-ouro de design de jogo sério. A etapa de relacionar evidência a solução cobre o objetivo 3. Há uma ressalva: a fase de "escolher ou elaborar" uma solução, se implementada como escolha múltipla, degrada para quiz e enfraquece o objetivo 2. A distinção entre "escolher" e "elaborar" é uma decisão de design com impacto grande em escopo e precisa ser resolvida no GDD.

**Decisão de design digna de registro:** a autora rejeita explicitamente simular a experiência de uma pessoa com deficiência. Isso é acertado e evita o problema ético mais comum em jogos sobre deficiência (simulação de deficiência tende a produzir pena em vez de compreensão estrutural, e é criticada por organizações do próprio grupo representado).

### 8. Progressão e conteúdo
Progressão por casos de investigação dentro de ambientes.
**[LACUNA]** Quantidade de ambientes e casos na versão completa; se há dificuldade crescente e como.

### 9. Escopo do MVP
**Dentro:** um único ambiente (ex.: uma escola) com três casos de investigação, entregando o ciclo completo — receber denúncia, explorar, encontrar pistas, registrar evidências, identificar barreiras, relacionar a soluções, receber resultado.
**Fora (recorte a explicitar):** *(inferido)* múltiplos ambientes, diálogo ramificado complexo, elaboração livre de solução.
**Justificativa do recorte:** a versão mínima já entrega o objetivo principal, pois permite praticar a identificação de barreiras por investigação.

**Avaliação:** é o MVP melhor delimitado entre as cinco propostas — tem fronteira clara e o ciclo listado passo a passo é praticamente um backlog inicial.

### 10. Plataforma e requisitos técnicos
- **Declarada:** web ou desktop.
- **[LACUNA]** Engine e definição entre web e desktop (decisão relevante: web facilita muito a distribuição em escola, que é o contexto de validação pretendido).
- **Carga de conteúdo** *(inferida)*: alta em arte de ambiente e baixa em sistemas. Um jogo de observação exige cenário detalhado e legível — é aqui que o esforço se concentra, não em programação.

### 11. Riscos e dificuldades

| Risco | Severidade | Observação |
|---|---|---|
| Escopo (declarado pela autora) | Alta | Jogos de investigação escalam por conteúdo; cada caso é conteúdo novo, não reuso de sistema |
| Volume de arte *(inferido)* | Alta | Ambiente precisa ser rico o suficiente para esconder barreiras de forma justa. É o gargalo real |
| Precisão técnica do conteúdo *(inferido)* | Média | Barreiras e soluções precisam estar corretas conforme NBR 9050 / LBI — erro aqui desinforma |
| Representação *(inferido)* | Média | Mesmo sem simular deficiência, personagens com deficiência precisam ser escritos com cuidado. Idealmente com consulta a uma pessoa com deficiência |
| Design de justiça do puzzle *(inferido)* | Média | Barreira invisível demais frustra; óbvia demais não ensina. Exige iteração e playtest |
| Acesso ao público | Baixa | O público (14–24, escola/universidade) é o mais acessível do conjunto — inclui a própria turma |

### 12. Validação
- **Parceiro possível:** instituição de ensino, escola, associação ou projeto voltado à inclusão e acessibilidade; possível parceria com profissionais da área ou professores de educação inclusiva.
- **[LACUNA]** Nome concreto de instituição e contato — a autora indica caminho, não nome.
- **[LACUNA]** Método e métricas. Sugestão: teste em que o participante lista barreiras de uma foto de ambiente real antes e depois de jogar — contagem de barreiras identificadas é métrica direta e limpa.

### Maturidade: **M3 — Conceito viável** (a mais próxima de M4)
Falta nome de parceiro e método de validação. Tudo o mais está no lugar.

---

# PROPOSTA P5 — Idle com Missões Reais e Controle Parental

### 1. Identificação
- **ID:** P5
- **Título provisório:** **[LACUNA]**
- **Autor:** Lucas de Carvalho Ziele
- **Submissão:** 17/08/2026
- **Gênero:** Idle / clicker com progressão

### 2. High Concept
Jogo idle em que a criança completa missões para progredir, sendo que as missões são cadastradas pelo pai ou responsável através de uma variação de controle parental do mesmo jogo — tarefas reais dão recompensas dentro do jogo.

**Arquitetura de duas faces:** app da criança + painel do responsável. Junto com P3, é uma das duas propostas com mais de um tipo de usuário no sistema.

### 3. Causa social e problema
Ensinar à criança a relação entre esforço e recompensa, além de incentivá-la a efetivamente cumprir tarefas.
**[LACUNA]** Não há caracterização de problema social — está formulado como benefício pedagógico individual e familiar. Para um jogo sério de PAC com "causa social", isso pode ser insuficiente e precisa de ancoragem: rotina e autorregulação infantil, tempo de tela, corresponsabilidade doméstica, ou desenvolvimento de função executiva. Sem esse enquadramento, a proposta é um app de produtividade familiar, não um jogo de causa social.

### 4. Público-alvo
- **Primário:** crianças de cerca de 5 a 6 anos, já habituadas a telas.
- **Secundário:** os pais ou responsáveis, que operam o cadastro de missões.
- **[LACUNA]** Contexto de uso (casa, presumivelmente) e frequência de jogo não declarados.

**Ponto crítico:** 5–6 anos é uma faixa muito específica e muito restritiva. Crianças nessa idade em geral **não leem com fluência** — isso praticamente elimina interface baseada em texto e obriga a design por ícone, cor, som e feedback visual. É a proposta com a maior restrição de acessibilidade de interface e isso não aparece nos riscos declarados.

### 5. Objetivos de aprendizagem
Declarado: depois de jogar, o jogador deve ser capaz de entender melhor o pensamento de que esforço gera recompensa, e o comportamento de criar bons hábitos.
**Avaliação:** é objetivo comportamental, não cognitivo, e por isso é o **mais difícil de verificar** de todas as propostas. Formação de hábito exige semanas de observação e o relato depende dos pais, não do jogo. Reformulação sugerida a validar com o autor: *(inferido)* "após 4 semanas, a criança inicia tarefas cadastradas sem solicitação do responsável em X% dos casos" — mensurável via painel do responsável.

### 6. Pilares de design *(inferidos)*
1. **Recompensa virtual atrelada a esforço real.**
2. **Baixa carga cognitiva** — poucos estímulos, adequado a 5–6 anos.
3. **Responsável no controle do conteúdo**, criança no controle do jogo.

### 7. Core loop e mecânica

**Loop declarado:** responsável cadastra missões separadas por nível de dificuldade → criança realiza a tarefa real → recompensa in-game → criança se empenha ou cria o hábito de buscar completar as missões → progresso idle e desbloqueio de minigames por pontos.

**7.1 Alinhamento mecânica ↔ objetivo**
O autor argumenta que a estrutura de missões com níveis de dificuldade faz o jogador se empenhar para atingir recompensas in-game, criando o hábito.

**Avaliação crítica — e este é o ponto que precisa ser discutido em sala:** existe uma tensão conhecida entre a mecânica e o objetivo declarado. Recompensa externa por tarefa é **motivação extrínseca**, e há literatura consolidada indicando que ela pode **reduzir** a motivação intrínseca a médio prazo (efeito de superjustificação) — ou seja, o jogo pode ensinar "eu faço tarefa se houver prêmio" em vez de "esforço gera resultado". Isso não invalida a proposta, mas significa que o design precisa endereçar isso deliberadamente (por exemplo, transição de recompensa para reconhecimento, ou recompensa variável decrescente). Se o grupo escolher esta ideia, esse é o problema de design central do GDD e é um **excelente** problema para um projeto acadêmico — dá muito o que fundamentar.

**Segundo ponto:** gênero idle é uma escolha discutível. Idle recompensa **passagem de tempo**, o objetivo é ensinar **esforço**. Há contradição estrutural entre a mecânica do gênero e a mensagem pretendida. Vale perguntar ao autor se idle é essencial ou se foi escolhido por simplicidade de implementação.

### 8. Progressão e conteúdo
Missões separadas por níveis de dificuldade; minigames desbloqueados com pontos; progressão idle.
**[LACUNA]** Quantidade de minigames, economia de pontos, o que a criança faz entre as missões.

### 9. Escopo do MVP
**Dentro:** alguns minigames desbloqueáveis com pontos.
**[LACUNA]** O MVP declarado não inclui explicitamente o **painel do responsável**, que é a metade indispensável do sistema — sem ele não há missão real, e sem missão real não há proposta. Recorte mínimo *(inferido)*: painel do responsável com cadastro e validação de missão + tela de progresso da criança + 2 minigames.
**Nota:** minigames são conteúdo caro e não são o núcleo. O núcleo é o ciclo missão-validação-recompensa.

### 10. Plataforma e requisitos técnicos
- **Declarada:** mobile.
- **[LACUNA]** Se painel do responsável é app separado, área no mesmo app ou web.
- *(inferido)* Backend e vínculo entre contas responsável↔criança são obrigatórios. Duas interfaces distintas para dois perfis muito diferentes de usuário dobram o trabalho de UI.

### 11. Riscos e dificuldades

| Risco | Severidade | Observação |
|---|---|---|
| Acesso ao público (declarado) | Alta | Testar com crianças de 5–6 anos exige consentimento dos responsáveis e possivelmente aprovação ética |
| **LGPD / dados de menor** *(inferido)* | **Crítica** | Dados de criança são categoria especialmente protegida (art. 14 da LGPD, consentimento específico de um dos pais). Rotina doméstica de menor é dado sensível |
| Interface para pré-leitores *(inferido)* | Alta | 5–6 anos exige design sem dependência de texto — restrição forte não prevista |
| Efeito de superjustificação *(inferido)* | Alta | A mecânica pode contrariar o objetivo. Precisa ser tratada no design |
| Contradição gênero × mensagem *(inferido)* | Média | Idle recompensa tempo, não esforço |
| Duas interfaces *(inferido)* | Média | Dobra a carga de UI/UX |
| Verificabilidade do objetivo *(inferido)* | Alta | Mudança de hábito não é medível na janela do semestre sem instrumentação via pais |

**Mitigação de acesso declarada pelo autor:** validar com famílias em que os filhos já têm acesso a celular.

### 12. Validação
- **Método declarado:** teste com famílias cujos filhos já possuem acesso ao celular.
- **[LACUNA]** Nome de família, instituição ou escola. Nenhum parceiro concreto citado.
- **[LACUNA]** Métricas — sugestão: taxa de conclusão de missão por semana e tempo entre cadastro e conclusão, ambos já coletáveis pelo painel do responsável.

### Maturidade: **M2/M3 — Conceito**
Mecânica e público claros; falta enquadramento da causa social, MVP correto (com painel) e parceiro.

---

# PROPOSTAS P6 e P7 — Pendentes

**[LACUNA]** Duas propostas não foram submetidas até 18/08/2026 — incluindo a do compilador deste documento.

Recomendação: se as duas não entrarem antes da discussão, registrar em ata que a seleção foi feita sobre 5 propostas e que os dois integrantes abriram mão de submeter ideia própria. Isso protege o grupo de retrabalho depois ("mas eu tinha uma ideia melhor" após a decisão tomada).

---

# 13. Matriz comparativa

## 13.1 Parâmetros lado a lado

| Parâmetro | P1 Financeira | P2 Tempo | P3 Solidária | P4 Acessibilidade | P5 Idle Missões |
|---|---|---|---|---|---|
| Gênero | Quiz + simulação | *não decl.* | Construção de cidade | Investigação/puzzle | Idle |
| Idade-alvo | 11–17 | "todas" | *não decl.* | 14–24 | 5–6 |
| Contexto | Escola pública + casa | *não decl.* | Bairro | Escola/universidade | Casa |
| Plataforma | Mobile → web | Mobile | *não decl.* | Web/desktop | Mobile |
| Tipos de usuário | 1 (+prof.) | 1 ou 2 | 2 assimétricos | 1 (+prof.) | 2 |
| Backend obrigatório | Provável | Provável | **Sim** | Não | **Sim** |
| Objetivos verificáveis | 3, bons | 1, vago | 0 declarados | 3, excelentes | 1, difícil |
| MVP delimitado | Sim | Não | Não | **Sim, o melhor** | Parcial |
| Parceiro nomeado | Quase (escola de membro) | Não | Não (Prefeitura genérica) | Não (caminho indicado) | Não |
| Dependência externa ao software | Baixa | Baixa | **Crítica** | Baixa | Média (famílias) |
| Público envolve menores | Sim (11–17) | Possivelmente | Possivelmente | Parcialmente (14+) | **Sim (5–6)** |
| Gargalo principal | Escopo de conteúdo | Falta de definição | Operação física | Volume de arte | LGPD + interface infantil |
| Maturidade | **M3** | M1 | M2 | **M3** | M2/M3 |

## 13.2 Pontuação sugerida (1–5)

Esta pontuação é uma **proposta de ponto de partida para o debate**, não um veredito. Cada integrante deve pontuar por conta e comparar — divergência grande em um critério é justamente onde a discussão rende.

| Critério | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| Clareza e força da causa social | 4 | 2 | **5** | **5** | 2 |
| Alinhamento mecânica ↔ objetivo | 4 | 1 | 2 | **5** | 2 |
| Objetivos verificáveis | **5** | 2 | 1 | **5** | 2 |
| Viabilidade técnica em 2 semestres | 4 | 3 | 1 | 4 | 3 |
| Acesso real ao público-alvo | 3 | 3 | 2 | **5** | 2 |
| Risco ético/LGPD controlável | 3 | 3 | 2 | 4 | 1 |
| Maturidade da proposta hoje | 4 | 1 | 2 | **5** | 3 |
| **Total (máx. 35)** | **27** | **15** | **15** | **33** | **15** |

## 13.3 Observações para a discussão

**Sobreposição P2 × P5.** As duas propostas ocupam o mesmo território — completar tarefas do mundo real para obter recompensa virtual, com possível perfil de responsável. A diferença é a idade-alvo e o gênero. Faz pouco sentido debatê-las separadamente: convém tratá-las como uma única linha de proposta e pedir que Gabi e Lucas as fundam, escolhendo uma faixa de idade e um gênero. Uma proposta fundida e bem definida provavelmente pontuaria melhor que as duas isoladas.

**Agrupamento temático.** As cinco propostas caem em três famílias:
- **Percepção/conscientização:** P4 — o jogo muda como o jogador vê o mundo.
- **Competência prática:** P1 — o jogo treina uma habilidade aplicável.
- **Mudança de comportamento:** P2, P3, P5 — o jogo tenta alterar o que o jogador faz fora dele.

A terceira família é a mais difícil em projeto acadêmico de 2 semestres, porque mudança de comportamento não é verificável na janela de tempo disponível. Isso não é motivo para descartar, mas o grupo deve saber que escolher dessa família significa **aceitar que a avaliação de eficácia será indireta** — e isso costuma pesar na banca.

**Sobre menores de idade.** Quatro das cinco propostas envolvem menores. Vale confirmar hoje com o professor orientador quais são as exigências do curso para teste com menores (autorização dos responsáveis, comitê de ética, anonimização). Se a exigência for pesada, isso muda o ranking — P4, com público de 14 a 24 que inclui a própria universidade, é a menos afetada.

## 13.4 Encaminhamentos sugeridos para o encontro

1. Cada autor apresenta em 5 minutos usando **apenas** os campos 2, 5, 7 e 9 da ficha — high concept, objetivo, core loop, MVP. Sem defender, sem vender.
2. Rodada de pontuação individual na matriz 13.2, em silêncio, antes de qualquer debate. Isso evita ancoragem no primeiro a falar.
3. Discutir só onde houver divergência maior que 2 pontos.
4. Decidir a fusão P2+P5.
5. Selecionar 2 finalistas, não 1. A segunda fica como plano B para o caso de o parceiro da primeira não se confirmar — e a confirmação de parceiro é o risco número um de todas as propostas.
6. Definir prazo de 3 dias para os autores das finalistas fecharem as lacunas marcadas e para P6/P7 submeterem, se ainda houver interesse.
7. Registrar em ata a decisão e a justificativa. O GDD do próximo encontro começa a partir da ficha da proposta vencedora — os 12 campos já mapeiam para as seções do GDD conforme a tabela da seção 0.2.
