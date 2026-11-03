---
title: "PAC 2026 — Jogo Sério"
subtitle: "Escopos Individuais das Propostas — Documento de Discussão"
date: "18 de agosto de 2026"
lang: pt-BR
---

# Identificação do documento

| Campo | Conteúdo |
|---|---|
| Curso | Engenharia de Software — 3º semestre |
| Disciplina | PAC — Projeto Aplicado à Comunidade |
| Fase | Concepção — ideação, seleção, GDD e análise de requisitos |
| Equipe | 7 integrantes · Encontros quinzenais |
| Compilação | 18 de agosto de 2026 |
| Propostas registradas | 7 (P1 a P7) · 1 pendente (P8) |

---

# Como usar este documento

Cada proposta tem uma ficha independente e deve ser discutida por seus próprios méritos. As fichas seguem a mesma estrutura para facilitar a leitura, mas **não há comparação entre elas** — a avaliação de cada ideia é interna a ela: dado o que a proposta pretende fazer, ela consegue?

Nenhuma proposta está pré-selecionada, descartada ou hierarquizada neste documento. Os pontos fortes e fracos registrados são insumo para a discussão, não veredito.

## Convenções de rastreabilidade

| Marcação | Significado |
|---|---|
| Texto normal | Declarado pelo autor no formulário |
| *(inferido)* | Reconstrução a partir do que o autor escreveu — confirmar com ele |
| **[a definir]** | Não respondido — o autor precisa preencher |

Propostas incompletas foram desenvolvidas até onde o material permite. Nesses casos, o campo "pontos fracos" separa **fraqueza da ideia** de **fraqueza da descrição** — são coisas diferentes, e uma ideia boa mal descrita não deve ser julgada como ideia ruim.

## Estrutura de cada ficha

**Escopo** (high concept, causa, público, objetivos de aprendizagem, core loop, progressão, MVP, plataforma, validação) · **Pontos fortes** · **Pontos fracos** · **Perguntas para o autor na discussão**.

## Encaminhamento sugerido para o encontro

Cada autor apresenta a própria ficha em cinco minutos, cobrindo apenas high concept, objetivo, core loop e MVP. Em seguida, o grupo faz ao autor as perguntas listadas ao final da ficha dele. Só então se discute a escolha.

Os campos marcados como **[a definir]** constituem o backlog de concepção: precisam estar preenchidos na proposta escolhida antes de o GDD começar.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# P1 — Educação Financeira Gamificada
**Autora:** Beatrice Fischer · Submetido em 05/08/2026

## Escopo

**High concept**
Jogo de quiz e trivia gamificado no estilo Duolingo em que o jogador completa desafios diários curtos, toma decisões financeiras simuladas e monta orçamentos, para aprender educação financeira básica de forma prática e recorrente.

**Causa**
A ausência de educação financeira na educação básica brasileira. Alunos concluem o ensino médio sem noções práticas de orçamento, poupança, juros ou consumo consciente, o que alimenta endividamento e decisões ruins na vida adulta. O tema já figura na BNCC como competência transversal.

**Público**
Primário: 11 a 17 anos, ensino fundamental (anos finais) e médio, prioritariamente escola pública. Uso em sala com mediação de professor e em casa pelo celular. Perfil familiarizado com apps gamificados, sem contato prévio com conteúdo financeiro estruturado.
Secundário: professores, como apoio de aula.

**Objetivos de aprendizagem**
Após jogar, o jogador será capaz de: (1) montar um orçamento pessoal simples distinguindo gastos essenciais de supérfluos; (2) reconhecer efeitos de juros e dívidas em decisões cotidianas; (3) tomar decisões financeiras simuladas mais conscientes — poupar vs. gastar, comparar preços, planejar uma compra.

**Core loop**
Receber uma situação financeira do dia a dia → tomar uma decisão (gastar, poupar, investir, negociar) → ver a consequência simulada no orçamento, no saldo ou numa meta.

**Progressão**
XP, pontos e streak, organizados em módulos temáticos com lições curtas. **[a definir]** número de módulos e critério de desbloqueio.

**MVP**
Um módulo único — "Orçamento do mês" — com 5 a 10 lições curtas em formato quiz/decisão, sistema simples de pontos e streak, e tela final mostrando o orçamento resultante do jogador.
Fora do MVP *(inferido)*: outros módulos, investimentos, perfil de responsável, ranking social.

**Plataforma**
Mobile como prioridade, web como possibilidade. **[a definir]** stack e necessidade de backend para persistir streak e progresso.

**Validação**
Escola onde um dos membros da equipe estudou, dependente de confirmação com professor ou coordenação. **[a definir]** método e métricas.

## Pontos fortes

- **Objetivos de aprendizagem operacionalizáveis.** Os três são mensuráveis por pré/pós-teste sem instrumento complexo. Isso resolve o problema mais comum de jogo sério acadêmico, que é não conseguir provar que ensinou algo.
- **Aderência curricular como porta de entrada.** Ancorar o tema na BNCC dá argumento pronto para negociar com coordenação de escola — o jogo não é um favor pedido à escola, é apoio a uma competência que ela já precisa cumprir.
- **MVP com fronteira nítida.** Um módulo, dez lições, uma tela de resultado. É estimável e cabe no prazo.
- **Referências bem escolhidas.** A autora identifica a lacuna real do mercado: material do Banco Central é confiável mas pouco engajante; apps engajantes raramente têm rigor de conteúdo. O diferencial está bem posicionado.
- **Conteúdo com fonte pública disponível.** Existe material gratuito e confiável (Meu Bolso em Dia, BNCC) para basear as lições, o que reduz o esforço de pesquisa.

## Pontos fracos

- **Ambiguidade de gênero.** "Quiz/trivia" e "simulação de orçamento" são duas mecânicas distintas com consequências diferentes de escopo e de aprendizado. Quiz é barato de produzir e ensina reconhecimento; simulação é caro e ensina decisão. A proposta oscila entre os dois e precisa escolher qual é o núcleo.
- **O objetivo 2 pode não caber na mecânica.** Juros só ficam sensíveis em horizonte longo, e o formato de sessão curta comprime o tempo. Existe risco real de o jogo *afirmar* que juros são ruins em vez de fazer o jogador *sentir* o efeito — o que reduz esse objetivo a texto explicativo, exatamente o que a proposta quer evitar.
- **Risco ético subestimado.** A autora classifica o tema como não sensível. Mas dinheiro, dívida e escassez com adolescentes de escola pública é terreno delicado: se as situações do jogo punirem o jogador por baixa renda, o jogo pode ensinar que pobreza é resultado de má decisão. Cada situação precisa separar erro de decisão de condição socioeconômica.
- **Escopo com tendência natural de crescimento.** A própria autora aponta. Formato de lição é aditivo por natureza — sempre cabe uma lição mais — e o risco é o grupo produzir conteúdo em vez de fechar o produto.
- **Parceiro ainda não confirmado.** Existe um caminho (escola de um dos membros), mas não uma confirmação. Teste com menores em escola envolve autorização de responsáveis e prazo administrativo.
- **Plano de validação ausente.** Sem método nem métrica definidos, os bons objetivos de aprendizagem correm o risco de não serem aproveitados na avaliação final.

## Perguntas para o autor na discussão

1. Quiz ou simulador? Qual das duas mecânicas some se for preciso cortar?
2. Como o jogador vai *sentir* o efeito de juros dentro de uma sessão de três minutos?
3. Já existe contato aberto com a escola, ou é uma possibilidade não testada?
4. Como uma situação de dívida vai ser escrita sem constranger um aluno que vive aquilo em casa?

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# P2 — Gestão de Tempo e Antiprocrastinação
**Autora:** Gabi · Submetido em 11/08/2026

> **Nota:** foram respondidos 4 dos 10 campos, e o campo de mecânica ficou vazio. A ficha abaixo trabalha com o que existe e marca o resto como pendente. A separação entre fraqueza da ideia e fraqueza da descrição é especialmente importante aqui.

## Escopo

**High concept** *(reconstruído)*
Jogo de produtividade em que o jogador completa tarefas do dia a dia para aprender a gerenciar o próprio tempo.
**[a definir]** gênero e ação principal. E, sobretudo: as tarefas são **reais** (o jogo espelha a rotina do usuário) ou **fictícias** (o jogo simula uma rotina)? Essa única decisão define arquitetura, público, mecânica e escopo do projeto inteiro.

**Causa**
Procrastinação.
**[a definir]** caracterização do problema — quem sofre, em que contexto, com qual consequência. Procrastinação como tema solto não configura causa social; precisa de recorte, por exemplo: desempenho e evasão de estudantes, sobrecarga e ansiedade acadêmica, ou autonomia de rotina infantil.

**Público**
Declarado: crianças, adolescentes e adultos, em qualquer lugar, com hábito de jogo considerado irrelevante por não haver mecânicas complexas. Possível perfil kids + perfil de responsável.

**Objetivo de aprendizagem**
Após jogar, o jogador passará a gerenciar melhor o tempo livre e priorizar responsabilidades.

**Core loop**
**[a definir]** — não respondido.

**MVP**
**[a definir]** — não respondido.

**Plataforma**
Mobile. **[a definir]** stack, backend, sincronização entre perfis.

**Validação**
**[a definir]** — não respondido.

## Pontos fortes

- **O problema é universal e imediatamente reconhecível.** Não precisa convencer ninguém de que procrastinação existe nem de que afeta estudantes — inclusive os sete integrantes do grupo. Isso encurta a etapa de justificativa e facilita recrutar participantes de teste.
- **Público de validação trivialmente acessível.** Se o recorte for estudantes, o grupo tem acesso direto à própria turma e ao próprio campus, sem intermediação institucional nem autorização de responsáveis.
- **A intuição de simplicidade é acertada.** A autora afirma que o jogo não terá mecânicas complexas. Para um projeto de dois semestres com sete pessoas de terceiro semestre, mecânica simples e bem executada é uma escolha madura, não uma limitação.
- **A ideia de perfil kids + responsável mostra percepção de arquitetura.** Ela identificou, sem ser perguntada, que o sistema pode ter dois tipos de usuário com permissões diferentes — o que é um insight de requisitos, não de tema.

## Pontos fracos

- **Público-alvo indefinido.** "Crianças, adolescentes e adultos em qualquer lugar" é ausência de público, não amplitude. Uma criança de 8 anos e um adulto de 35 têm noções de tempo, autonomia e recompensa incompatíveis; nenhuma mecânica única serve bem aos dois. Sem escolher uma faixa, não é possível definir linguagem, arte, complexidade nem forma de recompensa.
- **Ausência de core loop.** Sem a ação central declarada, não há como avaliar se o jogo *ensina* gestão de tempo ou apenas *registra* tarefas. Este é o campo que falta para a proposta ser discutível.
- **Risco estrutural de virar uma lista de tarefas com pontos.** É a armadilha clássica do tema: o produto acaba cobrando do usuário justamente a disciplina que deveria ensinar, e quem procrastina abandona o app na primeira semana. A proposta precisa de uma resposta a isso.
- **Objetivo não verificável na forma atual.** "Gerenciar melhor o tempo" não tem instrumento de medida. Precisaria virar algo observável, como ordenar tarefas por critério de urgência e importância, ou reduzir o intervalo entre receber e iniciar uma tarefa.
- **Escopo inestimável.** Sem MVP declarado, não há como afirmar se cabe em dois semestres.
- **Se envolver menores e rotina real, entra LGPD.** Rotina doméstica de criança com perfil de responsável é dado pessoal de menor, com exigência de consentimento específico.

## Perguntas para o autor na discussão

1. Tarefas reais ou fictícias? Esta é a pergunta que destrava todas as outras.
2. Qual faixa de idade única você escolheria se tivesse que escolher uma agora?
3. Qual é a ação que o jogador repete o tempo todo?
4. Por que alguém que procrastina não abandonaria este app na segunda semana?

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# P3 — Mercado Comunitário / Cidade Solidária
**Autora:** Karina Medeiros · Submetido em 12/08/2026

> **Nota de normalização:** na resposta original, o campo de objetivos recebeu a estrutura de níveis e mecânica, e o campo de mecânica recebeu uma frase. O conteúdo foi realocado aos campos correspondentes — vale confirmar com a autora se a leitura ficou fiel.

## Escopo

**High concept**
Jogo de construção de cidade em que o jogador faz doações reais, registradas num ponto de coleta comunitário, e progride por níveis desbloqueando personagens e elementos para construir a própria cidade.

**Causa**
Pessoas em situação de dificuldade financeira; famílias necessitadas do bairro.
**[a definir]** qual bairro, qual demanda concreta, se já existe rede de doação operando ali.

**Público**
Jogadores: a vizinhança em geral — moradores dispostos a doar.
Beneficiários: famílias necessitadas do bairro. **Categoria distinta do jogador** — quem joga e quem recebe são pessoas diferentes, com papéis assimétricos.
**[a definir]** faixa de idade, contexto de uso, hábito de jogo.

**Objetivo de aprendizagem**
Declarado apenas como "o jogador vai pensar sempre no próximo". **[a definir]** objetivo verificável. Reconstrução possível *(inferida)*: passar a doar com regularidade e reconhecer as demandas materiais concretas da própria vizinhança.

**Core loop** *(reconstruído)*
Doar item real → levar ao ponto de armazenamento → doação registrada e validada → ganhar progresso → desbloquear elementos e construir a cidade → subir de nível e acessar nova categoria de doação.

**Progressão declarada**
Nível 1: itens de cesta básica. Nível 2: mudas para horta comunitária. Nível 3: produtos de higiene e limpeza. A cada dez doações, o "vizinho solidário" conquista um personagem melhor. **[a definir]** total de níveis e o que sustenta o jogador depois do último.

**Elemento físico**
Um local que armazena as doações, onde as pessoas levam os produtos.

**MVP**
**[a definir]**. Recorte mínimo *(inferido)*: cadastro de doador, registro manual de doação por operador do ponto de coleta, três níveis, poucos elementos de cidade desbloqueáveis.

**Plataforma**
**[a definir]**. Requisitos implicados *(inferidos)*: backend, autenticação, painel de operador para validar doações, persistência do estado da cidade.

**Validação**
Prefeitura, para negociar benefício simbólico de redução de IPTU. Comunidade do bairro. O campo de viabilidade foi respondido apenas com "avaliável". **[a definir]** instituição de coleta, contato, método, métricas.

## Pontos fortes

- **A causa é a mais concreta possível.** Não é conscientização sobre um problema — é intervenção nele. Cada partida do jogo corresponde a um item de comida ou higiene chegando a uma família real. Para um Projeto Aplicado à Comunidade, esse vínculo direto com a comunidade é exatamente o que o nome da disciplina pede.
- **Impacto demonstrável sem instrumento de pesquisa.** Não precisa de pré/pós-teste para provar resultado: basta contar quantas doações entraram. É a única forma de avaliação que dispensa medir mudança de percepção.
- **Progressão por categoria, não por volume, é uma escolha inteligente.** Escalonar de cesta básica → mudas de horta → higiene faz o jogador conhecer tipos de necessidade que ele não consideraria sozinho. A estrutura de níveis carrega conteúdo educativo embutido, sem texto.
- **Horta comunitária no nível 2 é um bom achado.** Sai da lógica de assistência e entra na de autonomia — doar semente é diferente de doar comida, e a proposta captura essa progressão de forma natural.
- **A ideia de reconhecimento local tem força real.** "Vizinho solidário" como identidade pública funciona em escala de bairro, onde as pessoas se conhecem. É um motivador que não depende de tecnologia.

## Pontos fracos

- **A maior parte do risco está fora do software.** O jogo exige um ponto físico de coleta, alguém para operá-lo diariamente e um fluxo logístico de armazenamento e distribuição. Nada disso é escopo de engenharia de software, nada disso está sob controle do grupo, e sem isso o produto não funciona nem para demonstração. A viabilidade da proposta depende de já existir hoje uma instituição operando coleta no bairro e disposta a participar.
- **Verificação de doação é um problema sem solução barata.** Se a doação for autodeclarada, o sistema é burlável e a progressão perde sentido. Se exigir validação, alguém precisa estar no ponto de coleta registrando cada entrega — trabalho humano contínuo que o grupo terá de fazer ou terceirizar.
- **Risco de gamificar a pobreza.** A autora sinaliza o risco ético e ele é real. Transformar a necessidade de famílias em conteúdo de progressão exige cuidado: o beneficiário não pode aparecer como recurso ou obstáculo do jogo, e a cidade construída pelo jogador não pode contrastar de forma indecente com a carência que motiva a doação.
- **A recompensa pode substituir a motivação, em vez de formá-la.** O jogo premia a doação, mas não ensina sobre a causa. Existe risco de o comportamento cessar quando a recompensa cessar — e de o jogador doar por personagem, não por consciência. Se o objetivo aceito for mobilização de doações, isso deixa de ser problema; se for conscientização, é o problema central.
- **Carga técnica mínima alta.** Backend obrigatório, autenticação, painel administrativo e app de jogador. É bastante infraestrutura antes de existir jogo.
- **A camada de construção de cidade é, por si só, um jogo completo.** Ela pode consumir todo o tempo disponível e não é o que entrega a causa.
- **Trâmite com Prefeitura não cabe no prazo.** Negociar benefício de IPTU envolve processo administrativo público que não se resolve em dois semestres.
- **Sem objetivo verificável declarado.** É a lacuna mais importante a preencher.

## Perguntas para o autor na discussão

1. Existe hoje, no bairro, uma instituição que já recebe doações e aceitaria ser o ponto de coleta? Com nome?
2. Quem confirma que a doação aconteceu?
3. O objetivo é aumentar doações ou mudar a consciência de quem doa? Se for só o primeiro, o projeto fica mais simples e mais honesto.
4. Se a camada de construção de cidade fosse cortada, a ideia sobrevive?

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# P4 — Investigação de Barreiras de Acessibilidade
**Autora:** Giovanna Lopes Pontes · Submetido em 17/08/2026

## Escopo

**High concept**
Jogo de investigação e puzzle em que o jogador investiga ambientes, encontra evidências e identifica barreiras de acessibilidade, para perceber problemas de inclusão que passam despercebidos no cotidiano e aprender a propor soluções mais acessíveis.

**Causa**
A falta de acessibilidade e a dificuldade de reconhecer barreiras enfrentadas por pessoas com deficiência e outras pessoas com necessidades específicas, em ambientes públicos e privados. Muitas barreiras não são perceptíveis para quem não é afetado por elas. A proposta mostra que acessibilidade não se resume a rampa: envolve circulação, comunicação, sinalização, acesso à informação e organização dos espaços.

**Público**
Primário: 14 a 24 anos, estudantes de escolas e universidades, com contato casual ou frequente com jogos digitais. Uso individual ou como atividade complementar em instituições de ensino, em ações de cidadania, inclusão e acessibilidade.
Secundário: professores, profissionais da educação e instituições interessadas em usar o jogo como ferramenta de conscientização.

**Objetivos de aprendizagem**
Após jogar, o jogador será capaz de: (1) identificar diferentes tipos de barreiras de acessibilidade em ambientes cotidianos; (2) reconhecer que uma solução aparentemente acessível pode não resolver completamente a barreira; (3) relacionar problemas encontrados a possíveis soluções.

**Core loop**
Receber uma denúncia sobre um local → explorar o ambiente → observar objetos e conversar com personagens → registrar evidências → relacionar cada evidência a uma barreira → escolher ou elaborar uma solução → receber o resultado da investigação.

**Decisão de design declarada**
O jogo **não** simula a experiência de uma pessoa com deficiência, e não apresenta o conteúdo como perguntas educativas. O jogador é investigador, não a pessoa afetada.

**MVP**
Um único ambiente — por exemplo, uma escola — com três casos de investigação, entregando o ciclo completo: receber denúncia, explorar, encontrar pistas, registrar evidências, identificar barreiras, relacionar a soluções, receber resultado.

**Plataforma**
Web ou desktop. **[a definir]** qual das duas, e engine. **[a definir]** número de ambientes e casos na versão completa.

**Validação**
Instituição de ensino, escola, associação ou projeto voltado à inclusão; possível parceria com profissionais da área ou professores de educação inclusiva. **[a definir]** nome concreto, método e métricas.

## Pontos fortes

- **A mecânica é a habilidade.** Procurar uma barreira que não salta aos olhos é literalmente o que se quer treinar. Não há distância entre jogar e aprender, o que dispensa qualquer camada de explicação — o jogador não é informado da barreira, ele a encontra. Isso é o desenho mais difícil de acertar em jogo sério e a proposta já acerta na concepção.
- **O problema está formulado como problema de percepção, não de informação.** É justamente o que justifica usar um jogo em vez de uma cartilha. Se fosse falta de informação, um folheto resolveria.
- **A recusa em simular deficiência é uma decisão madura e correta.** Simulação de deficiência é criticada por organizações de pessoas com deficiência porque tende a produzir pena e a distorcer a experiência, em vez de revelar a barreira estrutural. Colocar o jogador como investigador mantém o foco no ambiente, que é onde o problema está.
- **O segundo objetivo é sofisticado.** "Uma solução aparentemente acessível pode não resolver a barreira" vai além de identificar e chega a avaliar adequação. É o tipo de nuance que costuma faltar em material sobre acessibilidade.
- **MVP com fronteira precisa.** Um ambiente, três casos, e o ciclo listado passo a passo. A própria enumeração do loop já funciona como backlog inicial.
- **Público de validação acessível.** A faixa de 14 a 24 anos em escola ou universidade inclui a própria instituição do grupo, e a maior parte é maior de idade ou próxima disso, o que simplifica a logística de teste.
- **Base de conteúdo confiável e pública.** NBR 9050 e a Lei Brasileira de Inclusão dão referência normativa para definir o que é barreira e o que é solução adequada, sem depender de interpretação do grupo.

## Pontos fracos

- **Volume de arte é o gargalo real, e ele não aparece nos riscos declarados.** Um jogo de observação exige ambiente detalhado e legível o bastante para esconder barreiras de forma justa. O esforço se concentra em cenário e assets, não em programação — e isso não escala: cada caso novo é conteúdo novo, sem reuso de sistema.
- **Escopo cresce por conteúdo.** A autora identifica o risco. Jogos de investigação não ganham mais horas com mais código, ganham com mais casos, e cada caso custa arte, redação e teste.
- **"Escolher ou elaborar" solução é uma bifurcação com impacto grande.** Se for escolha múltipla, a etapa final degrada para quiz e enfraquece justamente o objetivo 2. Se for elaboração livre, precisa de sistema de avaliação de resposta aberta, que é caro e difícil de acertar. A decisão precisa ser tomada antes do GDD.
- **Justiça do puzzle exige iteração.** Barreira invisível demais frustra; óbvia demais não ensina nada. Encontrar esse ponto depende de playtest com pessoas de fora do grupo, e quem projetou o cenário nunca consegue avaliar a dificuldade dele.
- **Precisão técnica do conteúdo é obrigação, não detalhe.** Se o jogo apontar como adequada uma solução que na norma não é, ele desinforma sobre o tema que quer ensinar. Exige revisão por alguém da área.
- **Representação de personagens com deficiência exige cuidado.** Mesmo sem simular a deficiência, há personagens envolvidos nas denúncias e nos diálogos. Idealmente com consulta a uma pessoa com deficiência, não apenas a um profissional.
- **Nenhum parceiro nomeado.** A autora indica caminhos plausíveis, mas nenhuma instituição ou pessoa concreta.
- **O objetivo 2 é difícil de medir.** Identificar barreira é fácil de aferir por contagem; avaliar se uma solução é insuficiente exige instrumento mais elaborado.

## Perguntas para o autor na discussão

1. Escolher solução ou elaborar solução? A resposta muda o escopo consideravelmente.
2. Web ou desktop? Se a validação é em escola, web reduz muito o atrito de distribuição.
3. Quem no grupo assume a produção de arte de ambiente, e em qual estilo — pixel art, ilustração vetorial, foto tratada?
4. Existe algum contato real com projeto de acessibilidade ou com uma pessoa com deficiência disposta a revisar o conteúdo?

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# P5 — Idle com Missões Reais e Controle Parental
**Autor:** Lucas de Carvalho Ziele · Submetido em 17/08/2026

## Escopo

**High concept**
Jogo idle em que a criança completa missões para progredir, sendo as missões cadastradas pelo responsável através de uma variação de controle parental do próprio jogo — tarefas reais do mundo geram recompensas dentro do jogo.

**Causa**
Ensinar à criança a relação entre esforço e recompensa e incentivá-la a efetivamente cumprir tarefas.
**[a definir]** ancoragem como causa social. Na forma atual é um benefício pedagógico familiar. Recortes possíveis: desenvolvimento de autorregulação e função executiva na primeira infância, corresponsabilidade doméstica, ou uso intencional de tempo de tela.

**Público**
Primário: crianças de cerca de 5 a 6 anos, já habituadas a telas.
Secundário: pais e responsáveis, que operam o cadastro de missões.
**[a definir]** contexto de uso e frequência.

**Objetivo de aprendizagem**
Após jogar, o jogador deve compreender melhor que esforço gera recompensa e desenvolver o comportamento de criar bons hábitos.

**Core loop**
Responsável cadastra missões separadas por nível de dificuldade → criança realiza a tarefa real → recompensa in-game → criança se empenha e cria o hábito de completar missões → progresso idle e desbloqueio de minigames por pontos.

**Arquitetura**
Duas faces: app da criança e painel do responsável.

**MVP**
Declarado: alguns minigames desbloqueáveis com pontos.
Observação: o painel do responsável não aparece no MVP declarado, mas sem ele não há missão real e a proposta deixa de existir. Recorte mínimo *(inferido)*: painel do responsável com cadastro e validação de missão + tela de progresso da criança + poucos minigames.

**Plataforma**
Mobile. **[a definir]** se o painel do responsável é app separado, área no mesmo app ou web. Backend e vínculo entre contas responsável↔criança são implicados *(inferido)*.

**Validação**
Famílias cujos filhos já possuem acesso a celular. **[a definir]** nome de família, escola ou instituição; método e métricas.

## Pontos fortes

- **A ponte entre mundo real e recompensa virtual é um mecanismo forte.** Ao contrário de jogos que simulam tarefas, aqui a ação acontece de fato: a criança arruma o quarto de verdade. O efeito do jogo existe fora dele, o que é raro e valioso.
- **O painel do responsável resolve o problema de conteúdo de graça.** O grupo não precisa produzir nem manter catálogo de tarefas — cada família cadastra as suas. Isso elimina um custo de conteúdo que costuma inviabilizar projetos parecidos, e adapta o jogo a qualquer realidade doméstica sem trabalho adicional.
- **O painel também é o instrumento de medição.** Como o responsável registra cadastro e conclusão, o sistema já gera os dados de avaliação: taxa de conclusão por semana, tempo entre cadastro e conclusão, evolução ao longo do tempo. A avaliação vem embutida na arquitetura.
- **Público de teste acessível sem intermediação institucional.** Famílias conhecidas do grupo, sem necessidade de negociar com escola ou órgão público.
- **Dois perfis de usuário com permissões distintas é bom material de requisitos.** Para a etapa de análise de requisitos do semestre, essa proposta rende casos de uso, atores e regras de autorização com naturalidade.
- **Gênero idle é honestamente barato de implementar.** Não exige física, IA, nem level design complexo, o que sobra tempo para a parte que importa.

## Pontos fracos

- **A mecânica pode contrariar o objetivo.** Recompensa externa por tarefa é motivação extrínseca, e há literatura consolidada indicando que ela pode reduzir a motivação intrínseca a médio prazo. Existe risco concreto de o jogo ensinar "eu faço se houver prêmio" em vez de "esforço gera resultado" — o oposto do pretendido. Isso não invalida a ideia, mas precisa ser endereçado deliberadamente no design (transição de recompensa para reconhecimento, recompensa decrescente, ou algo equivalente). É, aliás, um problema de design excelente para um projeto acadêmico: rende fundamentação teórica de sobra.
- **Idle recompensa passagem de tempo; o objetivo é ensinar esforço.** Há contradição estrutural entre a lógica do gênero e a mensagem. Vale examinar se o idle é essencial ou foi escolhido pela facilidade de implementação.
- **Cinco a seis anos é uma restrição de interface severa, e ela não está nos riscos declarados.** Crianças nessa faixa em geral não leem com fluência. Isso praticamente elimina qualquer interface baseada em texto e obriga a design por ícone, cor, som e animação — o que é mais difícil, não mais fácil, e exige teste com crianças reais para saber se comunica.
- **LGPD sobre dados de menor é o risco mais pesado da proposta.** Rotina doméstica de criança de cinco anos é dado pessoal de menor, com exigência de consentimento específico de um dos pais e finalidade estritamente delimitada. Precisa de tratamento explícito no projeto, não como nota de rodapé.
- **O MVP declarado está no lugar errado.** Minigames são conteúdo caro e periférico; o núcleo é o ciclo cadastrar → cumprir → validar → recompensar. Se o MVP for os minigames, o grupo pode terminar o semestre com um jogo que não tem missões.
- **Duas interfaces para dois perfis muito distintos dobram o trabalho de UI.** A criança precisa de algo lúdico e sem texto; o adulto precisa de algo funcional e denso. São dois projetos de interface, não um.
- **O objetivo é comportamental e por isso quase inverificável no prazo.** Formação de hábito exige semanas de observação, e o relato depende dos pais. A janela do semestre provavelmente não permite comprovar mudança de hábito — só engajamento.
- **A causa social ainda não está formulada.** Como está, é um app de produtividade familiar. Para um PAC, precisa de enquadramento social explícito.

## Perguntas para o autor na discussão

1. Idle é essencial à ideia ou foi escolha de conveniência técnica?
2. Como uma criança que não lê vai entender qual é a missão do dia?
3. Como o design evita que a criança pare de ajudar em casa quando não há prêmio?
4. Qual é a causa social que sustenta a proposta num PAC?

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# P6 — Treinador Diário Antifraude Financeira
**Autor:** Gustavo · Submetido em 18/08/2026

> **Nota:** este autor apresentou duas propostas, P6 e P7. Elas são alternativas entre si, compartilham o mesmo motor e formato, e **apenas uma deve ser levada adiante**. O Anexo A trata dessa escolha. Cada ficha, porém, deve ser discutida por seus próprios méritos, como as demais.

## Escopo

**High concept**
Aplicativo de treino diário, no molde dos jogos curtos do LinkedIn, em que a pessoa recebe três tarefas rápidas sobre situações financeiras suspeitas — mensagem, ligação, boleto, cobrança, oferta — e decide entre responder, ignorar ou verificar. O objetivo não é decorar golpes, e sim instalar o reflexo de duvidar e conferir por canal independente antes de agir com dinheiro.

**Causa**
Golpes financeiros contra pessoas idosas são problema documentado, crescente, e com política pública já formalizada em Santa Catarina.

- Mais de 72 mil denúncias de golpes financeiros contra pessoas acima de 60 anos no Disque 100 em 2024.
- Mais de 59 mil denúncias de violência patrimonial contra pessoas idosas no Painel da Ouvidoria Nacional de Direitos Humanos em 2025.
- Serasa Experian (2024): o maior aumento percentual em tentativas de fraude ocorreu na faixa acima de 60 anos, o que sugere direcionamento ativo dos criminosos.
- Fundação Seade (2025): 82% das pessoas com 60 anos ou mais no estado de São Paulo já sofreram tentativa de golpe virtual.
- Procon/SC: aumento de 480% em golpes contra idosos no primeiro trimestre de 2022, dado citado na justificativa da Lei 67/2025 de Gaspar/SC.
- IBGE: cerca de 70% dos idosos brasileiros já estão conectados à internet.
- O empréstimo consignado é apontado como o principal crime patrimonial contra aposentados e pensionistas do INSS, por meio de centrais falsas, falsa portabilidade e falsa taxa de liberação.

Ancoragem legal local: o **PL 522/2025**, do deputado Antídio Lunelli, institui em Santa Catarina política estadual de orientação aos idosos contra fraudes no comércio eletrônico e na internet, prevendo ações educativas, campanhas e treinamentos para o público acima de 60 anos. Foi aprovado na Comissão de Constituição e Justiça da Alesc e segue em tramitação. O município de Gaspar/SC já aprovou a Lei 67/2025, criando Política Municipal de Inclusão e Proteção Digital da Pessoa Idosa. Projetos semelhantes preveem entrega de material educativo em CRAS, Casas do Idoso, associações de aposentados e centros comunitários.

**Público**
Primário: pessoas de 60 anos ou mais, usuárias de WhatsApp e de aplicativo bancário, com pouca ou nenhuma experiência com jogos digitais. Ver Anexo B, item 2 — a definição de ritmo e faixa etária ainda está em aberto e precisa ser travada.
Secundário: filhos, netos e cuidadores, que são quem a família consulta quando a mensagem suspeita chega.
Terciário: facilitadores de CRAS e centros de convivência, que ganham roteiro de oficina pronto.

**Objetivos de aprendizagem**
Após usar o aplicativo, a pessoa será capaz de: (1) nomear os cinco sinais recorrentes de engenharia social — urgência artificial, pedido de sigilo, troca de canal, solicitação de dado ou código, cobrança antecipada de taxa; (2) distinguir mensagem fraudulenta de legítima, sem recusar comunicação verdadeira; (3) indicar a ação de verificação correta para uma situação suspeita, como encerrar o contato e ligar no número oficial.

**Core loop**
Chega um artefato → a pessoa inspeciona tocando em elementos (remetente, link, horário, escrita) → escolhe entre responder, ignorar ou verificar → vê a consequência e o motivo.

Cinco tipos de tarefa, rotativos:

| Tipo | O que a pessoa faz | O que treina |
|---|---|---|
| Caixa de entrada | Chega uma mensagem: responder, ignorar ou verificar | Decisão sob ambiguidade |
| Onde está o sinal | Toca no elemento que denuncia a fraude | Onde olhar |
| E agora? | Escolhe a ação de verificação correta | O procedimento |
| O banco faz isso? | Prática bancária real ou inventada? | Calibração do que é legítimo |
| Passa o recado | Escolhe como explicaria aquilo a um familiar | Retenção por ensino |

O quarto tipo é o que impede o produto de gerar medo generalizado: quem não sabe o que o banco faz não tem como saber o que ele não faz.

**Progressão**
Banco de aproximadamente 60 itens etiquetados, reapresentados por repetição espaçada em intervalos crescentes — 1 dia, 3 dias, 1 semana, 3 semanas. Sem cronômetro em nenhuma tarefa. Placar duplo permanente: erro por acreditar demais e erro por desconfiar demais, contados em separado.

**MVP**
Motor de tarefas com três dos cinco tipos, banco inicial de 25 itens cobrindo cinco famílias de golpe — falso parente, falsa central bancária, boleto e link falso, taxa de liberação, consignado — misturados a mensagens legítimas plausíveis. Tela de resultado com placar duplo e revisão caso a caso. Roteiro de oficina de 40 minutos em PDF para o facilitador.
Fora do MVP: os outros dois tipos de tarefa, simulação de ligação com áudio, painel de turma, geração procedural.

**Plataforma**
Web, otimizada para tablet e celular em modo retrato, aberta por link sem instalação nem loja de aplicativos. Sem backend, sem login, sem coleta de dado pessoal — o progresso fica no dispositivo. Sem arte de personagem: o trabalho visual é de interface. Acessibilidade como requisito não funcional formal: contraste WCAG AA, corpo de texto a partir de 18px, alvo de toque de 48px, interação de um toque só.

**Validação**
Instrumento de 8 itens — 4 golpes e 4 mensagens legítimas — aplicado antes da sessão e uma semana depois. Métricas: sensibilidade (golpes rejeitados), especificidade (legítimas aceitas), e proporção de casos em que a pessoa cita verificação por canal independente. Parceiros candidatos em Jaraguá do Sul, a confirmar: Centro de Convivência da Pessoa Idosa, CRAS, Secretaria de Assistência Social, associações de aposentados, grupos de terceira idade de paróquias, UBS com grupos periódicos. Procon municipal como revisor de conteúdo.

## Pontos fortes

- **Existe política pública vigente pedindo exatamente este material, no nosso estado.** Chegar num equipamento público com uma ferramenta que atende a uma política em vigor é posição completamente diferente de pedir espaço para testar um trabalho de faculdade. É a coisa mais difícil de conseguir num projeto de extensão e ela já está dada.
- **Impacto quantificável em reais.** Não é conscientização difusa: quem reconhece a falsa central do banco deixa de perder o que tem na conta. O valor evitado é estimável e o resultado do relatório final tem número, não impressão.
- **Conteúdo gratuito, público e confiável.** Febraban, Procon, Banco Central e imprensa documentam os padrões. Sem custo de produção de mídia e sem qualquer questão de licenciamento.
- **Mecânica idêntica à habilidade.** Decidir sobre uma mensagem sem rótulo é exatamente o que a pessoa faz na vida real. Não há tradução entre o que se joga e o que se aprende.
- **O placar duplo resolve um problema pedagógico que quase todo material antifraude tem.** Campanha de conscientização tende a produzir medo generalizado, e medo generalizado isola a pessoa idosa e a torna mais dependente. Contar o falso positivo como erro é o diferencial conceitual da proposta.
- **Repetição espaçada é solução de conteúdo e de aprendizagem ao mesmo tempo.** Sessenta itens sustentam meses de uso, e rever o mesmo golpe três semanas depois é justamente o que consolida reconhecimento, que é uma habilidade que decai.
- **Zero risco de LGPD e zero risco político.** Sem login, sem backend, sem coleta, público maior de idade, e ninguém é contra ensinar idoso a não ser roubado.
- **Público de validação já reunido.** Grupos de convivência têm encontro fixo. O acesso é uma ligação, não uma negociação.
- **Trabalho paralelizável entre sete pessoas de habilidades desiguais.** Duas programam o motor; as demais produzem conteúdo, interface, documentação e articulação. Nenhuma frente fica bloqueada.
- **Degrada bem.** Um único tipo de tarefa com dez itens já é produto testável e útil.

## Pontos fracos

- **Uso duplo do conteúdo.** Um produto que ensina como golpes funcionam ensina, em alguma medida, como aplicá-los. Mitigação: usar apenas sinais já divulgados em campanha pública de Febraban e Procon, nunca detalhe operacional — nada de mascaramento de número, página falsa ou obtenção de lista de contatos. Mostra-se o sinal, não o método.
- **Risco de reabrir ferida.** Parte do público já foi vítima, muitas vezes com vergonha e sem ter contado a ninguém. Uma tarefa parecida com o golpe que a pessoa sofreu pode doer. Exige revisão de tom item a item, aviso prévio do facilitador e ausência total de linguagem que culpe. É o risco mais sério da proposta e precisa de tratamento explícito no GDD.
- **Acertar no aplicativo e errar na vida.** No treino a pessoa está calma, sentada e avisada de que há golpes ali. O golpe real chega quando ela está sozinha e acredita que a filha está em apuros. A transferência é limitada e não é mensurável em dois semestres: mede-se reconhecimento, não imunidade. Isso precisa ser dito no relatório, não escondido.
- **Barreira de letramento digital anterior ao produto.** Parte do público 60+ não opera tablet com autonomia, o que limita o uso diário doméstico e torna a mediação por facilitador quase obrigatória.
- **Tensão entre formato diário e público mediado.** Jogo diário pressupõe alguém que volta sozinho todo dia; oficina em CRAS pressupõe encontro periódico com facilitador. Ver Anexo B, item 2 — é decisão pendente e precisa ser tomada antes do GDD.
- **Conteúdo perece.** Padrões de golpe mudam, e agora com voz e imagem sintética. O banco de itens precisa ser fácil de atualizar, daí a decisão de conteúdo em arquivo externo, mas ainda assim envelhece.
- **Precisão do conteúdo é obrigação.** Se o produto classificar como golpe algo que o banco realmente faz, ensina a pessoa a recusar comunicação legítima. Exige revisão por Procon ou por profissional de segurança bancária.
- **Nenhum parceiro confirmado ainda.** Há lista de candidatos plausíveis e argumento forte para abrir a porta, mas nada acordado. Teste com pessoas idosas em equipamento público pode exigir autorização da Secretaria de Assistência Social e possivelmente aprovação ética.
- **Pouco apelo visual em banca.** É uma tela de celular com texto. A defesa precisa vir do dado de validação e do parceiro institucional, não do print.

## Perguntas para o autor na discussão

1. Ritmo diário autônomo ou sessão mediada em oficina? A resposta muda o público e a arquitetura.
2. Existe hoje algum contato aberto com CRAS, centro de convivência ou associação, com nome e telefone?
3. Como uma tarefa sobre golpe vai ser escrita sem constranger quem já caiu naquele golpe?
4. Quem revisa tecnicamente se uma prática bancária apresentada como legítima é mesmo legítima?

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# P7 — Treinador Diário de Contexto e Mídia Sintética
**Autor:** Gustavo · Submetido em 18/08/2026

> **Nota:** alternativa à P6, do mesmo autor, com o mesmo motor e formato. Ver Anexo A.
>
> **Nomenclatura:** a proposta evita deliberadamente o termo "fake news", que carrega carga partidária e dificulta a entrada em equipamento público municipal. "Verificação de contexto e mídia sintética" descreve melhor o escopo e não convida disputa.

## Escopo

**High concept**
Aplicativo de treino diário, no mesmo molde de tarefas curtas, em que a pessoa recebe três itens de conteúdo circulante — texto, imagem, vídeo, áudio — e decide entre acreditar, descartar ou verificar. A tese do produto é que **inspeção visual não distingue conteúdo sintético de real, e por isso o caminho é verificar a origem**, não apertar os olhos.

**Causa**
Circulação de conteúdo enganoso em grupos familiares e redes sociais, com dois danos simétricos: acreditar no falso e descartar o verdadeiro. O segundo é menos discutido e igualmente grave — foto real de crime descartada como montagem, áudio real descartado como clonagem, documento real descartado como IA.

Evidência que fundamenta a abordagem:

- Revisão sistemática com meta-análise de 56 estudos (2024): a detecção humana de deepfake fica no nível do acaso em diferentes modalidades, e é pior para estímulos sintéticos do que para os reais.
- *Journal of Cybersecurity* (Oxford, 2023), N=280: acurácia entre 60 e 64%, apenas pouco acima do acaso, e nenhuma das três intervenções de ajuda testadas melhorou o resultado. Achado central: a confiança dos participantes era alta e sem relação com a acurácia.
- *Communications of the ACM* (2025): desempenho próximo do acaso para imagem, áudio, vídeo e audiovisual.
- Ebner e colaboradores, *Cognitive Research* (2026): humanos no nível do acaso para imagem, embora tenham superado os algoritmos em vídeo, com cerca de 63%.
- Ressalva honesta a registrar: há evidência de que treino focado em impressão global, e não em artefato local, pode quase dobrar a acurácia em rostos — resultado limitado a rostos e a uma geração de geradores.

Consequência de design que define a proposta: um produto que treine o olho entrega uma pessoa que erra na mesma taxa de antes, agora convencida de que sabe distinguir. Isso é pior do que não fazer nada, e seria detectado na validação sem tempo hábil de corrigir.

**Público**
Primário: adultos de 30 a 60 anos, autônomos digitalmente, que repassam conteúdo em grupos de família e voltam ao aplicativo por conta própria — perfil que o formato diário atende naturalmente. Manter 60+ como primário é possível, mas exige mediação por facilitador (Anexo B, item 2) e perde parte da naturalidade do tema.
Secundário: estudantes de ensino médio e superior.
Terciário: professores e bibliotecários, como material de atividade.

**Objetivos de aprendizagem**
Após usar o aplicativo, a pessoa será capaz de: (1) reconhecer que inspeção visual não distingue confiavelmente mídia sintética de real; (2) identificar descasamento de contexto entre um conteúdo e a afirmação que o acompanha; (3) indicar o primeiro passo de verificação adequado a cada tipo de conteúdo.

**Core loop**
Chega um artefato → a pessoa inspeciona o contexto (quem publicou, quando, o que mais essa conta publica, se aparece em outro lugar) → escolhe entre acreditar, descartar ou verificar → vê a consequência e o motivo.

Cinco tipos de tarefa, rotativos:

| Tipo | O que a pessoa faz | O que treina |
|---|---|---|
| Real ou IA, com confiança | Decide e declara o quanto tem certeza | Calibração — ver a própria confiança descolada do acerto |
| Fora de contexto | Foto verdadeira com legenda: achar o descasamento de data, lugar ou evento | O caso mais comum e o menos falado |
| Quem publicou | Avalia a conta e o histórico, não o conteúdo | Deslocar o julgamento do artefato para a fonte |
| Qual o primeiro passo | Dada uma afirmação, escolhe qual verificação fazer primeiro | O procedimento |
| Manchete × matéria | Compara título e corpo do texto | Descasamento interno, sem ferramenta externa |

O tipo "fora de contexto" é o mais valioso e o menos óbvio: boa parte do que circula em grupo de família não é imagem gerada, e sim foto real de outro país ou outro ano com legenda mentirosa. Nenhum detector de IA pega isso, e olhar a imagem também não — só verificação de origem pega.

O tipo "Real ou IA, com confiança" tem um momento de virada que ocorre uma vez, na primeira semana: o aplicativo mostra as duas colunas lado a lado — acurácia em torno de 55%, confiança em torno de 80% — e informa que esse resultado é o esperado e que ninguém consegue melhor. Para quem já foi enganado e carrega vergonha, descobrir que a tarefa é objetivamente impossível é alívio, não derrota, e abre espaço para aprender o procedimento.

**Progressão**
Banco de aproximadamente 60 itens etiquetados, com repetição espaçada em intervalos crescentes. Placar duplo permanente: "enganado" (acreditou no sintético) e "descartou verdade" (chamou de IA algo real). Sem cronômetro.

**MVP**
Motor de tarefas com três dos cinco tipos, incluindo obrigatoriamente "Real ou IA, com confiança" e "fora de contexto". Banco inicial de 25 artefatos produzidos internamente. Tela de calibração com as duas colunas. Roteiro de atividade em PDF.
Fora do MVP: verificação reversa real com chamada externa (no MVP a busca é simulada, com resultado pré-escrito — mais barata, confiável em oficina e funciona sem internet), vídeo longo, áudio de alta fidelidade, painel de turma.

**Plataforma**
Mesma da P6: web, sem backend, sem login, sem coleta, conteúdo em arquivo externo, mesmos requisitos de acessibilidade.

**Validação**
Instrumento de 8 itens com declaração de confiança, aplicado antes e uma semana depois, medindo acurácia e também **calibração** — a distância entre confiança declarada e acerto real. Reduzir a calibração é objetivo verificável que quase nenhum material de mídia mede. Parceiros candidatos: escolas de ensino médio, bibliotecas públicas, cursos de comunicação, grupos de convivência. Revisor de conteúdo: docente de jornalismo ou comunicação.

## Pontos fortes

- **A tese é contraintuitiva e forte.** "Você não consegue distinguir, e essa é a informação útil" é posição que praticamente nenhum material de conscientização assume, e é sustentada por literatura sólida. Rende defesa consistente em banca.
- **A métrica de calibração é academicamente diferenciada.** Poucos projetos de graduação medem algo além de satisfação do usuário. Mostrar confiança injustificada caindo enquanto a taxa de verificação sobe é resultado de verdade.
- **A lição não envelhece.** Verificar origem continua correto por mais que os geradores melhorem, enquanto qualquer heurística visual expira em meses.
- **Tema atual, amplo e de alto interesse.** Chama atenção de banca, de imprensa local e de potenciais parceiros de ensino, e o público potencial é toda a população conectada.
- **O tipo "fora de contexto" ataca o problema real.** Endereça o formato de desinformação mais comum em grupos familiares, que nenhuma ferramenta automática resolve.
- **O momento de calibração tem valor humano além do pedagógico.** Remove a culpa de quem já foi enganado, o que é pré-condição para a pessoa aprender em vez de se fechar.
- **Motor idêntico ao da P6**, com os mesmos ganhos de paralelização entre sete pessoas.

## Pontos fracos

- **Licenciamento de mídia é problema imediato e caro.** Não é possível usar foto de pessoa real sem autorização, imagem com direitos, nem rosto de figura pública em vídeo falso — o que elimina a maior parte do material que circula. Caminho viável: gerar internamente os artefatos sintéticos e usar como "reais" fotos do próprio grupo ou de banco com licença livre. Dá controle total do gabarito, mas é trabalho de produção que precisa entrar no cronograma desde a primeira semana.
- **Ética de produzir mídia sintética.** O grupo vai gerar deepfake para fim didático. Exige regra formal no GDD: nada com rosto de pessoa real identificável, nada com figura pública, marcação em todo artefato produzido, uso restrito ao projeto.
- **Perecibilidade acelerada.** Padrão de golpe muda em anos; qualidade de geração muda em meses. Um artefato de hoje vira obviamente falso rápido — e um banco velho ensinaria justamente que dá para perceber, o oposto da tese.
- **Risco político latente.** Mesmo evitando o termo, exemplos concretos escorregam para tema partidário com facilidade, o que fecha portas em equipamento público. Mitigação: apenas casos fabricados pela equipe ou históricos e neutros; nunca material político em circulação.
- **Não há política pública correspondente.** Diferentemente da P6, não existe hoje lei estadual ou municipal em SC demandando este tipo de treinamento. A porta institucional é mais difícil de abrir e depende de relação pessoal.
- **Impacto não quantificável.** "Deixou de acreditar em algo falso" não tem valor mensurável equivalente a "não perdeu três mil reais".
- **O momento de calibração é frágil.** Se o texto errar o tom, desanima em vez de aliviar — especialmente para quem já se sente incapaz diante de tecnologia. Exige teste de tom antes de teste de mecânica.
- **Nem todo item tem gabarito neutro.** Em fraude o certo e o errado são objetivos. Em contexto há casos em que pessoas razoáveis discordam, o que enfraquece a lógica de acerto e erro de um jogo e exige curadoria cuidadosa.
- **Dois custos pesados caem no segundo semestre** — produção de mídia e calibragem de tom — e nenhum deles paraleliza bem.

## Perguntas para o autor na discussão

1. Quem no grupo assume formalmente a produção de mídia, incluindo licenciamento, nas duas primeiras semanas?
2. De onde vêm os artefatos "reais": fotos do próprio grupo ou banco de licença livre?
3. Como o texto do momento de calibração evita desanimar quem descobriu que acerta 55%?
4. Sem política pública para se apoiar, qual é a porta de entrada institucional concreta?

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# P8 — Pendente

Uma proposta ainda não foi submetida até 18/08/2026.

Se não entrar antes da discussão, vale registrar em ata que a seleção considerou sete propostas e que um integrante não apresentou ideia própria, evitando questionamento após a decisão tomada.

Para quem ainda for submeter, o mínimo para a ideia ser discutível é: high concept em uma frase, causa com recorte concreto, faixa etária única, core loop (a ação que se repete) e MVP (o menor recorte jogável que já entrega o objetivo). Os demais campos podem ser desenvolvidos depois.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Anexo A — Nota sobre as propostas P6 e P7

As duas propostas vêm do mesmo autor, compartilham motor, formato, arquitetura técnica e requisitos de acessibilidade, e diferem apenas em tema, tipos de tarefa e conteúdo. **São alternativas, não complementos.** A tese das duas é a mesma — verificar a origem em vez de julgar o artefato — e ela fica mais forte dita uma vez, bem, do que duas vezes pela metade.

Se a equipe selecionar uma delas, a outra vai para o GDD como **anexo de evolução do produto**, com conceito, tipos de tarefa e justificativa registrados. Isso demonstra que a decisão de escopo foi deliberada, e não que o tema não foi considerado. Ocupa uma página e trabalha a favor do grupo em banca.

**Nenhuma das duas está pré-selecionada.** A escolha, se o grupo chegar a elas, sugere-se que seja feita por estas quatro perguntas, nesta ordem, e não por preferência de tema:

1. A equipe consegue abrir uma porta institucional nas próximas três semanas? A P6 já tem o argumento pronto pela política estadual; a P7 depende de relação pessoal a construir.
2. Alguém do grupo assume produzir mídia — gerar sintéticos, fotografar reais, resolver licenciamento? Se ninguém assumir, a P7 não é executável.
3. O grupo prefere um resultado quantificável ou um resultado conceitualmente ambicioso? A P6 entrega o primeiro; a P7, o segundo.
4. O público final é 60+ mediado por facilitador ou adulto autônomo em uso diário? A segunda resposta favorece a P7.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Anexo B — Molde diário compartilhado por P6 e P7

## 1. Formato

- Três tarefas por dia, de 60 a 90 segundos cada, totalizando de 3 a 5 minutos por sessão.
- Tipos de tarefa distintos e rotativos, sem repetir o mesmo formato em dias seguidos.
- Resultado imediato com o motivo, sempre — nunca apenas certo ou errado.
- Placar duplo em todas as tarefas: erro por acreditar demais e erro por desconfiar demais, contados em separado.
- Sem cronômetro. A pressa é justamente o sinal que se quer ensinar a reconhecer; seria incoerente o produto apressar a pessoa.

## 2. Questão em aberto: ritmo e público

O formato diário pressupõe alguém que volta sozinho, todo dia, no próprio celular. A validação em CRAS pressupõe encontro periódico com facilitador e público de baixa autonomia digital. **As duas coisas não convivem sem decisão explícita.** Três saídas, todas legítimas, a decidir com a equipe:

- **Saída 1 — "Dia" como unidade de conteúdo, não de calendário.** Na oficina, o grupo percorre cinco "dias" em quarenta minutos; o uso doméstico diário é bônus para quem consegue. Preserva o público 60+ e o argumento institucional.
- **Saída 2 — Mover o público primário para 40 a 65 anos.** No levantamento da Fundação Seade, a faixa de 45 a 59 anos registrou o maior índice de tentativas de golpe, 92%, acima dos 82% do grupo 60+. É gente com smartphone próprio e autonomia para retornar ao aplicativo. Custo: perde-se o gancho da política pública estadual, escrita para 60+.
- **Saída 3 — Duas trilhas no mesmo produto**, uma de oficina e outra diária, mesmo conteúdo em ritmos diferentes. Mais completo e mais caro; só se o motor ficar pronto cedo.

## 3. Volume de conteúdo

Três tarefas diárias escritas à mão são inviáveis: trinta dias já somam noventa itens. A solução adotada é **repetição espaçada** — banco de aproximadamente 60 itens bem escritos, reapresentados em intervalos crescentes de 1 dia, 3 dias, 1 semana e 3 semanas.

A escolha é de aprendizagem antes de ser de economia: reconhecimento de padrão decai com o tempo, e rever o mesmo item semanas depois é o que consolida. O entregável de conteúdo passa a ser um banco de 60 itens etiquetados — estimável, divisível entre quatro pessoas e defensável em banca.

## 4. Motor comum

Idêntico nas duas propostas; se a equipe mudar de rota, nenhuma engenharia se perde.

- Sem backend, sem login, sem coleta de dado pessoal; progresso e histórico no dispositivo.
- Conteúdo em arquivo de dados externo, editável sem recompilar.
- Web, otimizada para tablet e celular em modo retrato.
- Acessibilidade como requisito não funcional formal: contraste WCAG AA, corpo de texto a partir de 18px, alvo de toque de 48px, interação de um toque só, operável sem gesto de precisão.
- Agendador de repetição espaçada.
- Exportação do resultado da sessão em PDF para registro do facilitador.

O motor não conhece o tema: ele carrega um módulo, apresenta artefatos, aceita decisões, aplica pontuação e mostra explicação. Um tema é um pacote de conteúdo. Especificar esse schema é entregável legítimo da etapa de análise de requisitos deste semestre.
