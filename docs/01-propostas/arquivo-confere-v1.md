# P6 — "Confere?"
## Simulador de reconhecimento de golpes digitais para pessoas idosas

**Autor:** Gustavo · Submetido em 18/08/2026
**Gênero:** Simulador de decisão sob engano (referência de estrutura: *Papers, Please*)
**Título provisório:** "Confere?" — alternativas: "Alô, Quem Fala?", "Pode Confiar?"

---

## 1. High concept

Jogo de decisão em que o jogador recebe mensagens, ligações e SMS numa interface de celular simulada — algumas legítimas, algumas golpes — e precisa decidir entre **responder**, **ignorar** ou **verificar por canal independente**, para aprender a reconhecer os sinais de engenharia social sem passar a desconfiar de tudo.

O jogador não é o golpista nem a vítima: é ele mesmo, na própria caixa de entrada, com tempo ilimitado para pensar.

---

## 2. Causa social

Golpes financeiros contra pessoas com 60 anos ou mais são um problema documentado, crescente e caro no Brasil.

- Em 2024, o Disque 100 registrou mais de **72 mil denúncias** de golpes financeiros contra pessoas acima de 60 anos.
- O Painel da Ouvidoria Nacional de Direitos Humanos registrou mais de **59 mil denúncias de violência patrimonial** contra pessoas idosas em 2025.
- Levantamento da Fundação Seade (2025) aponta que **82% das pessoas com 60+ no estado de São Paulo** já sofreram tentativa de golpe virtual por mensagem, e-mail ou ligação.
- Relatório da Serasa Experian (2024) indica que o **maior aumento percentual em tentativas de fraude ocorreu justamente na faixa acima de 60 anos**, o que sugere direcionamento ativo dos criminosos a esse grupo.
- Segundo o IBGE, cerca de **70% dos idosos brasileiros já estão conectados à internet** — a exposição existe e é crescente.
- O empréstimo consignado é apontado como o principal crime patrimonial contra aposentados e pensionistas do INSS, por meio de centrais de atendimento falsas, falsa portabilidade e falsa taxa de liberação.

**Ancoragem local, e este é o ponto mais forte da proposta:**

- O **PL 522/2025**, do deputado Antídio Lunelli, institui em Santa Catarina uma política estadual de orientação aos idosos contra fraudes no comércio eletrônico e na internet. Foi aprovado na Comissão de Constituição e Justiça da Alesc e segue em tramitação nas comissões de Finanças, Direitos da Pessoa Idosa e Educação e Cultura. O texto prevê **ações educativas, campanhas informativas e treinamentos** para o público acima de 60 anos.
- O município de **Gaspar/SC** aprovou a Lei 67/2025, criando Política Municipal de Inclusão e Proteção Digital da Pessoa Idosa. A justificativa do projeto cita o **Procon/SC**, que registrou aumento de 480% em golpes contra idosos no primeiro trimestre de 2022.
- Projetos municipais semelhantes preveem entrega de conteúdo educativo em **CRAS, Casas do Idoso, associações de aposentados e centros comunitários** — exatamente a rede onde este jogo seria usado.

Ou seja: existe demanda institucional formalizada em lei, no nosso estado, por material de treinamento para esse público — e o que essa política prevê hoje é cartilha, palestra e campanha publicitária. **O jogo se posiciona como a ferramenta de treinamento que a política pede e que ainda não existe.**

Fontes a citar formalmente no GDD: Disque 100 / Ouvidoria Nacional de Direitos Humanos, Febraban, Serasa Experian, Procon/SC, Alesc (PL 522/2025), IBGE.

---

## 3. Público-alvo

**Primário:** pessoas de 60 anos ou mais, usuárias de WhatsApp e de aplicativo bancário, com pouca ou nenhuma experiência com jogos digitais. Contexto de uso: grupos de convivência, CRAS, Centro de Convivência da Pessoa Idosa, associações de aposentados, UBS, igrejas — sempre com **facilitador presente**, em tablet ou notebook.

**Secundário — e aqui há uma decisão de design importante:** filhos, netos e cuidadores. O jogo é curto e desconfortável de um jeito produtivo para quem tem 25 anos e acha que "nunca cairia nessa". Uma sessão de dez minutos jogada por um neto muda a forma como ele conversa com o avô sobre o assunto — e é o neto quem, na prática, é chamado quando a mensagem suspeita chega.

**Terciário:** o próprio facilitador (assistente social, agente de saúde), que ganha um roteiro de oficina pronto.

---

## 4. Objetivos de aprendizagem

Após jogar, o jogador será capaz de:

1. **Nomear os cinco sinais recorrentes de engenharia social:** urgência artificial, pedido de sigilo, troca de canal, solicitação de dado ou código, e cobrança antecipada de taxa para liberar um valor.
2. **Distinguir mensagem fraudulenta de mensagem legítima**, sem recusar comunicação verdadeira — medido por duas taxas separadas: acerto em golpes e falso positivo em mensagens legítimas.
3. **Indicar a ação de verificação correta** para uma mensagem suspeita: encerrar o contato e ligar no número oficial, não usar o link recebido, conferir com um familiar.

O objetivo 3 é o que muda comportamento de verdade. O jogo não ensina "desconfie" — ensina **o que fazer** quando desconfiar.

---

## 5. Pilares de design

1. **A urgência é ficcional; o tempo do jogador é real.** As mensagens gritam "você tem 10 minutos". O jogador tem tempo ilimitado para decidir. Essa contradição é a lição central: pressa é o sinal, e você tem o direito de parar e conferir.
2. **Discriminação, não desconfiança.** Metade do conteúdo é legítimo. Ignorar uma consulta médica remarcada ou um aviso real do banco também é erro, e também custa pontos.
3. **A vítima nunca é ridicularizada.** Muitos jogadores já foram golpeados de verdade. Errar no jogo produz explicação e um caminho de ação, nunca deboche, nunca "game over".
4. **A interface é o conteúdo.** A tela do jogo imita WhatsApp, SMS e tela de chamada. Praticar no jogo é praticar na ferramenta real.

---

## 6. Core loop

**Chega uma mensagem → o jogador lê e inspeciona → escolhe uma de três ações → vê a consequência → recebe o motivo.**

Três ações, sempre disponíveis:

| Ação | Quando é correta |
|---|---|
| **Responder** | Mensagem legítima que exige resposta |
| **Ignorar / Bloquear** | Golpe evidente, sem custo em ignorar |
| **Verificar** | A maioria dos casos ambíguos — liga no número oficial, confere com familiar, abre o app pelo ícone e não pelo link |

**Inspeção antes de decidir:** o jogador pode tocar em elementos da mensagem para examinar — número do remetente, endereço do link, nome do contato, foto de perfil, erro de escrita, horário. Cada elemento examinado é uma pista, e é aqui que se aprende *onde olhar*.

**Estrutura de sessão:** um "dia" tem de 4 a 6 mensagens. Uma sessão completa tem 5 dias. Cada dia introduz uma família de golpe nova e repete as anteriores misturadas a mensagens legítimas — dificuldade crescente por acúmulo, não por velocidade.

**Placar duplo, mostrado ao final:**
- **Golpes evitados** — quantos você identificou
- **Oportunidades perdidas** — quantas mensagens legítimas você bloqueou por engano

O segundo número existe para impedir que o jogador aprenda a estratégia burra de recusar tudo. Quem zera bloqueando tudo termina a sessão com o placar mostrando que perdeu a consulta do cardiologista, o aviso real de compra suspeita no cartão e a mensagem da filha.

**Por que a mecânica ensina, e não um texto:** o golpe funciona porque *parece* legítimo no momento em que chega. Ler uma cartilha que diz "desconfie de urgência" não treina nada, porque na cartilha a mensagem já vem rotulada como golpe. No jogo, ela vem sem rótulo, junto de mensagens verdadeiras, e o jogador tem que decidir. É a única forma de treinar reconhecimento: **expor ao engano em ambiente seguro.** É a mesma lógica de um simulador de voo — você erra onde errar não custa nada.

---

## 7. Conteúdo e progressão

Famílias de golpe, todas documentadas publicamente por Febraban, Procon e imprensa:

| Dia | Família | Sinal principal a treinar |
|---|---|---|
| 1 | Falso parente com número novo pedindo PIX | Troca de canal + urgência |
| 2 | Falsa central do banco / falso funcionário | Pedido de dado ou código |
| 3 | Falso benefício, prêmio ou indenização com taxa de liberação | Cobrança antecipada |
| 4 | Falso boleto, link de recadastramento, falsa prova de vida | Endereço do link |
| 5 | Consignado e falsa portabilidade / empréstimo não solicitado | Autorização e assinatura |

Cada dia inclui de 2 a 3 mensagens legítimas plausíveis: consulta remarcada pela UBS, aviso real do banco, mensagem de neto pelo número já conhecido, cobrança verdadeira.

**Escalabilidade barata:** o conteúdo é texto e dados, não código nem arte. Cada golpe novo é um arquivo de configuração. O jogo aceita conteúdo indefinidamente sem crescer em complexidade técnica — e conteúdo é o que sete pessoas conseguem produzir em paralelo.

---

## 8. Escopo do MVP

**Dentro:**
- Uma sessão completa de 5 dias, 4 a 6 mensagens por dia, aproximadamente 25 mensagens
- Cinco famílias de golpe + mensagens legítimas misturadas
- Três ações e inspeção por toque em elementos
- Tela de resultado com placar duplo e revisão caso a caso
- Interface adaptada: fonte grande, alto contraste, alvos de toque amplos, sem tempo cronometrado, sem áudio obrigatório
- Conteúdo em arquivo de dados externo, editável sem recompilar

**Fora do MVP:**
- Simulação de ligação com áudio
- Modo facilitador com painel de turma
- Geração procedural de mensagens
- Conquistas, ranking, progressão de longo prazo
- Versão para o público jovem

**Deliverable adicional de baixo custo e alto valor:** um **roteiro de oficina de 40 minutos** em PDF, para o facilitador conduzir a sessão em grupo. Isso transforma o software num material utilizável e é o que faz uma instituição adotar em vez de só testar.

---

## 9. Plataforma e requisitos técnicos

- **Web (HTML/CSS/JS ou Godot exportado para web)**, otimizado para tablet em modo retrato. Web porque o facilitador abre um link no tablet do CRAS sem instalar nada e sem loja de aplicativos.
- **Sem backend, sem login, sem coleta de dado pessoal.** Toda a sessão é local. Resultado exportável em PDF ou tela, se o facilitador quiser registrar.
- **Sem arte de personagem, sem animação, sem física.** O trabalho visual é de interface: tipografia, contraste, hierarquia. Isso é UI, não asset art.
- Requisito de acessibilidade tratado como requisito não funcional formal: contraste mínimo WCAG AA, corpo de texto a partir de 18px, área de toque mínima de 48px, operável sem gesto de precisão.

**Distribuição de trabalho para 7 pessoas** — argumento a usar em sala:

| Frente | Pessoas | Habilidade necessária |
|---|---|---|
| Front-end e lógica de decisão | 2 | Programação |
| Redação de mensagens e curadoria de golpes | 2 | Pesquisa e escrita |
| UI e acessibilidade | 1 | Design |
| Requisitos, GDD e documentação | 1 | Documentação |
| Contato institucional, oficina e teste | 1 | Articulação |

Nenhuma frente fica bloqueada esperando outra. Só duas pessoas precisam programar bem.

---

## 10. Validação

**Método:** teste com o mesmo instrumento antes e depois. Apresentar 8 mensagens impressas ou em tela — 4 golpes e 4 legítimas — e pedir que a pessoa classifique e diga o que faria. Aplicar antes da sessão e uma semana depois.

**Métricas:**
- Sensibilidade: proporção de golpes corretamente identificados
- Especificidade: proporção de mensagens legítimas corretamente aceitas
- Ação correta nomeada: proporção de casos em que a pessoa cita verificação por canal independente

Duas métricas separadas evitam o falso sucesso de alguém que "melhorou" simplesmente ficando paranoico.

**Parceiros possíveis em Jaraguá do Sul — confirmar contato:** Centro de Convivência da Pessoa Idosa, CRAS municipais, Secretaria de Assistência Social, associações de aposentados, grupos de terceira idade de paróquias, UBS com grupo de hipertensos e diabéticos (público 60+ já reunido periodicamente). Também o Procon municipal, como validador de conteúdo.

Vantagem prática: esses grupos **já se reúnem em horário fixo**. Não é preciso convocar ninguém — é preciso pedir 40 minutos de uma reunião que já acontece.

---

## 11. Pontos fortes

- **Utilidade imediata e mensurável em reais.** Não é conscientização difusa: uma pessoa que reconhece a falsa central do banco deixa de perder o que tem na conta. O impacto é verificável e o valor evitado é quantificável.
- **Demanda institucional já formalizada em lei estadual e municipal em SC.** A política existe e prevê treinamento; o material que ela prevê hoje é cartilha e palestra. Chegar numa instituição pública com uma ferramenta que atende a uma política vigente é uma posição muito diferente de pedir espaço para testar um trabalho de faculdade.
- **Mecânica idêntica à habilidade.** Decidir sobre uma mensagem sem rótulo é exatamente o que a pessoa faz na vida real. Não há tradução entre o que se joga e o que se aprende.
- **O placar duplo resolve o problema pedagógico que quase todo material antifraude tem.** Campanha de conscientização tende a produzir medo generalizado, e medo generalizado isola a pessoa idosa e a torna dependente. Medir falso positivo como erro é o diferencial conceitual da proposta.
- **Custo de produção baixo e previsível.** Sem backend, sem arte de personagem, sem sistemas complexos. O esforço está em interface e em texto, que são as duas coisas que este grupo consegue produzir.
- **Escala por dados, não por código.** Golpe novo é linha nova em arquivo de configuração. Depois do MVP, o jogo continua útil sem manutenção de engenharia.
- **Zero risco de LGPD.** Sem login, sem backend, sem coleta. Público maior de idade. É a única configuração possível que elimina esse risco por completo em vez de mitigá-lo.
- **Público de validação que já está reunido.** Grupos de convivência têm encontro fixo semanal ou quinzenal. O acesso é uma ligação, não uma negociação.
- **Trabalho paralelizável entre sete pessoas com habilidades desiguais.** Quem não programa produz conteúdo, que é metade do produto.
- **A restrição de acessibilidade é conteúdo acadêmico, não obstáculo.** Fonte grande, contraste, alvo de toque e ausência de pressão temporal viram requisitos não funcionais formais e bem justificados — material direto para a etapa de análise de requisitos do semestre.
- **Sobrevive ao corte.** Se o prazo apertar, um único dia com seis mensagens já é um produto testável e útil. Poucas propostas degradam com essa elegância.

---

## 12. Pontos fracos

- **Uso duplo do conteúdo.** Um jogo que ensina como golpes funcionam ensina, em alguma medida, como aplicá-los. Mitigação: usar apenas padrões já divulgados em campanha pública de Febraban, Procon e imprensa, e nunca detalhe operacional — nada de como mascarar número, montar página falsa ou obter lista de contatos. O jogo mostra o **sinal**, não o **método**.
- **Risco de reabrir ferida.** Parte do público já foi vítima, muitas vezes com vergonha e sem ter contado a ninguém. Uma mensagem parecida com a que a pessoa recebeu pode ser dolorosa. Isso exige revisão de tom em cada texto, alerta prévio dado pelo facilitador e ausência total de linguagem que culpe o jogador. **É o risco mais sério da proposta e precisa de tratamento explícito no GDD, não de nota de rodapé.**
- **A barreira de letramento digital é anterior ao jogo.** Parte do público não opera tablet com autonomia. Mitigação: interação de um toque só, sem arrastar, sem gesto de precisão, e uso sempre mediado por facilitador. Mas isso significa que o jogo **não funciona como app baixado em casa**, e essa limitação precisa ser assumida desde o começo.
- **A pessoa pode acertar no jogo e errar na vida.** No jogo ela está calma, sentada, avisada de que há golpes ali. O golpe real chega quando ela está sozinha, ansiosa, e acredita que a filha está em apuros. A transferência do aprendizado para a situação real é limitada e não temos como medir isso em dois semestres. É honesto reconhecer que medimos reconhecimento, não imunidade.
- **Conteúdo perece.** Padrões de golpe mudam rápido, e agora com voz e imagem sintética. O jogo precisa ser fácil de atualizar — daí a decisão de conteúdo em arquivo externo — mas ainda assim envelhece.
- **Precisão do conteúdo é obrigação.** Se o jogo classificar como golpe algo que o banco realmente faz, ele ensina a pessoa a recusar comunicação legítima. Exige revisão por Procon ou por alguém de segurança bancária.
- **Nenhum parceiro confirmado ainda.** Há uma lista de candidatos plausíveis e um argumento forte para abrir a porta, mas nada assinado. Teste com pessoas idosas em equipamento público pode exigir autorização da Secretaria de Assistência Social e possivelmente aprovação ética — prazo administrativo a levantar já nesta semana.
- **Pouco apelo visual em apresentação.** O jogo é uma tela de celular. Em banca, uma cidade sendo construída ou um ambiente ilustrado impressiona mais à primeira vista. A defesa tem que vir do dado de validação e do parceiro institucional, não do print de tela.
- **É pouco "jogo" para parte do grupo.** Alguém vai dizer que é um questionário sofisticado. A resposta: a diferença entre questionário e simulador é que no questionário a pergunta vem rotulada como pergunta. Aqui a mensagem chega disfarçada, no meio de mensagens verdadeiras, e é isso que treina.

---

## 13. Por que funciona como coringa

A proposta se diferencia em cinco eixos ao mesmo tempo:

1. **Faixa de idade.** É a única voltada a 60+. Nenhuma outra passa dos 24 anos.
2. **Natureza da utilidade.** As outras ensinam ou mobilizam. Esta **protege** — evita perda financeira concreta.
3. **Gênero.** Não é quiz, exploração, construção nem idle. É simulador de decisão sob engano, com o jogador exposto a informação deliberadamente enganosa.
4. **Perfil de custo.** É a única com carga de arte praticamente nula e carga de texto alta — perfil oposto ao das demais, o que também significa que exige um conjunto diferente de talentos do grupo.
5. **Respaldo legal existente.** É a única em que já existe política pública aprovada ou em tramitação, no nosso estado, demandando exatamente o tipo de material que o projeto entrega.

**Como apresentar em sala, em uma frase:** *"É um jogo em que você recebe mensagens de golpe misturadas com mensagens verdadeiras e tem que decidir em qual confiar — e você perde ponto tanto por cair no golpe quanto por bloquear sua própria filha."*

Essa segunda metade da frase é o que faz a ideia parar de parecer óbvia.

---

## 14. Perguntas que vão me fazer, e as respostas

**"Idoso não joga."**
Não precisa jogar sozinho, nem se identificar como jogador. É uma atividade de oficina de 40 minutos com facilitador, em tablet, num grupo que já se reúne. E o público secundário — filhos e netos — joga sim, e é quem é chamado quando a mensagem suspeita chega.

**"Isso é um quiz."**
No quiz a pergunta vem rotulada. Aqui a mensagem chega sem rótulo, misturada a mensagens legítimas, e o jogador é punido tanto por confiar demais quanto por desconfiar demais. Essa segunda punição é o que nenhum quiz faz.

**"Não é um jogo bonito."**
Não é. A defesa desta proposta é o dado de validação e a carta de uma instituição pública dizendo que vai usar. Se o grupo quer um projeto que impressione visualmente, esta não é a escolha — e é justo dizer isso na hora de decidir.

**"E se ensinar a golpista?"**
O jogo mostra sinais de reconhecimento já publicados em campanha oficial de banco e de Procon, não método operacional. Quem quer aprender a aplicar golpe não precisa de nós.

---

## 15. Lacunas a fechar

- **[a definir]** Contato real com instituição em Jaraguá do Sul, com nome e telefone
- **[a definir]** Exigência do curso para teste com pessoas idosas em equipamento público — perguntar ao orientador esta semana
- **[a definir]** Revisor de conteúdo: Procon municipal, agente bancário, ou docente da área
- **[a definir]** Godot exportado para web ou HTML/JS puro — decidir pela facilidade de manutenção do conteúdo
- **[a definir]** Texto exato das 25 mensagens do MVP e do instrumento de 8 itens do pré/pós-teste
