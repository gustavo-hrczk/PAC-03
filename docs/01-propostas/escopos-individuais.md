# PAC 2026 — Jogo Sério
## Escopos Individuais das Propostas

**Fase:** Concepção — ideação, seleção, GDD, análise de requisitos
**Compilado em:** 18/08/2026
**Propostas recebidas:** 5 de 7

---

### Como usar este documento

Cada proposta tem uma ficha independente, discutida por seus próprios méritos. As fichas seguem a mesma estrutura para facilitar a leitura, mas **não há comparação entre elas** — a avaliação de cada ideia é interna a ela: dado o que ela quer fazer, ela consegue?

Convenções:

| Marcação | Significado |
|---|---|
| Texto normal | Declarado pelo autor |
| *(inferido)* | Reconstrução a partir do que o autor escreveu — confirmar com ele |
| **[a definir]** | Não respondido — o autor precisa preencher |

Propostas incompletas foram desenvolvidas até onde o material permite. Nesses casos, o campo "pontos fracos" separa **fraqueza da ideia** de **fraqueza da descrição** — são coisas diferentes, e uma ideia boa mal descrita não deve ser julgada como ideia ruim.

---
---

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

---
---

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

---
---

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

---
---

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

---
---

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

---
---

# P6 e P7 — Pendentes

Duas propostas não foram submetidas até 18/08/2026.

Se não entrarem antes da discussão, vale registrar em ata que a seleção considerou cinco propostas e que dois integrantes não apresentaram ideia própria. Isso evita retrabalho e questionamento depois de a decisão estar tomada.

Para quem ainda for submeter, o mínimo necessário para a ideia ser discutível é: **high concept em uma frase, causa com recorte concreto, faixa de idade única, core loop (a ação que o jogador repete), e MVP (o menor recorte jogável que já entrega o objetivo).** Os demais campos podem ser desenvolvidos depois.

---

## Encaminhamento sugerido

Cada autor apresenta a própria ficha em cinco minutos, cobrindo apenas high concept, objetivo, core loop e MVP. Depois, o grupo faz ao autor as perguntas listadas ao final da ficha dele. Só então se discute a escolha.

Os campos marcados como **[a definir]** são o backlog de concepção: eles precisam estar preenchidos na proposta escolhida antes de o GDD começar.
