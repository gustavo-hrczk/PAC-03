# "Confere?" — Propostas finais
## Duas rotas, um molde. Decisão em conjunto.

**Autor:** Gustavo · 18/08/2026
**Status:** documento de decisão. Descreve as duas rotas em estrutura idêntica para que a equipe escolha uma. **A rota não escolhida vira anexo do GDD, não vira escopo.**

---

# PARTE I — O molde compartilhado

As duas propostas usam a mesma casca, inspirada no modelo de jogos diários do LinkedIn. Isso não é detalhe: **a casca é 70% do trabalho de engenharia**, e ela é idêntica nas duas rotas. Só o conteúdo e os tipos de tarefa mudam.

## 1. Formato

- **3 tarefas por dia** (não 5 — ver justificativa em 1.3), de 60 a 90 segundos cada. Sessão total de 3 a 5 minutos.
- **Tipos de tarefa distintos**, rotativos, não repetindo o mesmo formato dois dias seguidos.
- **Resultado imediato** com o motivo, sempre. Nunca só "certo/errado".
- **Placar duplo** em todas as tarefas: erro por acreditar demais e erro por desconfiar demais, contados em separado.
- **Sem cronômetro.** A pressa é o sinal que estamos ensinando a reconhecer; seria incoerente o jogo apressar o jogador.

## 2. A tensão que o formato diário criou — resolver antes de votar

Este é o ponto mais importante deste documento.

O formato diário pressupõe **um usuário que volta sozinho, todo dia, no próprio celular**. A versão anterior da proposta pressupunha **oficina mediada por facilitador em CRAS, com público 60+ e baixo letramento digital**. As duas coisas não convivem sem uma decisão explícita: pessoa com 75 anos e pouca autonomia digital não abre um app diariamente por conta própria.

Três saídas, todas legítimas:

**Saída 1 — "Dia" como unidade de conteúdo, não de calendário.** O jogo é organizado em dias, mas na oficina o grupo joga cinco "dias" em quarenta minutos. Uso doméstico diário existe para quem consegue, como bônus. Preserva o público 60+ e o argumento institucional intacto. **É a mais conservadora e a que eu recomendo se a equipe escolher a rota A.**

**Saída 2 — Mover o público primário para 40 a 65 anos.** Aqui há um dado contraintuitivo e forte: no levantamento da Fundação Seade em São Paulo, a faixa de **45 a 59 anos registrou o maior índice de tentativas de golpe, 92%** — acima dos 82% do grupo 60+. É gente que tem smartphone próprio, autonomia digital, e que **volta ao app sozinha**. O formato diário serve perfeitamente a esse público. Custo: perde-se o gancho da política pública estadual, que é escrita para 60+.

**Saída 3 — Duas trilhas no mesmo produto.** Trilha "oficina" (sessões densas, mediada) e trilha "diária" (leve, autônoma), mesmo conteúdo, ritmos diferentes. Mais completo, mais caro. Só se o motor ficar pronto cedo.

**Decidir isso na reunião, antes de escolher entre A e B.** É uma pergunta de dez minutos que evita um retrabalho de dois meses.

## 3. Quantidade de conteúdo — o problema aritmético

Três tarefas por dia, todo dia, é conteúdo demais para escrever à mão. Trinta dias já são noventa itens; um ano são mais de mil. Nenhum grupo de sete pessoas em dois semestres produz isso.

**A solução é repetição espaçada, e ela é melhor pedagogicamente do que conteúdo infinito.**

Um banco de aproximadamente **60 itens** bem escritos, reapresentados em intervalos crescentes — 1 dia, 3 dias, 1 semana, 3 semanas — sustenta meses de uso. E há razão de aprendizagem, não só de economia: reconhecimento de padrão **decai** com o tempo. Rever o mesmo golpe três semanas depois é exatamente o que consolida. Ninguém reclama de rever uma carta no Anki.

Consequência prática: o entregável de conteúdo do projeto é **um banco de 60 itens etiquetados**, não "conteúdo diário infinito". Isso é estimável, divisível entre quatro pessoas, e defensável em banca.

## 4. Motor comum às duas rotas

Idêntico nas duas propostas. Se a equipe mudar de ideia depois, nada de engenharia se perde.

- Sem backend, sem login, sem coleta de dado pessoal. Progresso e histórico ficam no dispositivo.
- Conteúdo em arquivo de dados externo, editável sem recompilar.
- Web, otimizado para tablet e celular em retrato.
- Acessibilidade como requisito não funcional formal: contraste WCAG AA, corpo de texto a partir de 18px, alvo de toque de 48px, interação de um toque só, operável sem gesto de precisão.
- Agendador de repetição espaçada.
- Exportação do resultado da sessão em PDF, para o facilitador registrar.

---
---

# PARTE II — Rota A
## Treinador diário antifraude financeira

## A1. Conceito
Aplicativo de treino diário em que a pessoa recebe três tarefas curtas sobre situações financeiras suspeitas — mensagem, ligação, boleto, cobrança, oferta — e precisa decidir entre responder, ignorar ou verificar. O objetivo não é decorar golpes: é instalar o reflexo de **duvidar e conferir por canal independente** antes de agir com dinheiro.

## A2. Causa
Golpes financeiros contra pessoas idosas são problema documentado e com política pública já formalizada em Santa Catarina.

- Mais de 72 mil denúncias de golpes financeiros contra pessoas acima de 60 anos no Disque 100 em 2024.
- Mais de 59 mil denúncias de violência patrimonial contra pessoas idosas no Painel da Ouvidoria Nacional de Direitos Humanos em 2025.
- Serasa Experian (2024): maior aumento percentual em tentativas de fraude ocorreu na faixa acima de 60 anos.
- Fundação Seade (2025): 82% das pessoas 60+ em SP já sofreram tentativa de golpe virtual; a faixa de 45 a 59 anos chegou a 92%.
- Procon/SC: aumento de 480% em golpes contra idosos no primeiro trimestre de 2022.
- Consignado apontado como principal crime patrimonial contra aposentados e pensionistas do INSS.
- **PL 522/2025 (Alesc, dep. Antídio Lunelli):** institui política estadual de orientação aos idosos contra fraudes no comércio eletrônico e na internet, prevendo ações educativas e treinamentos. Aprovado na CCJ, em tramitação.
- **Lei 67/2025 de Gaspar/SC:** Política Municipal de Inclusão e Proteção Digital da Pessoa Idosa.

## A3. Público
Primário: 60+ (ou 40 a 65, conforme a saída escolhida na seção 2). Secundário: filhos, netos e cuidadores. Terciário: facilitadores de CRAS e centros de convivência.

## A4. Os cinco tipos de tarefa diária

| Tipo | O que o jogador faz | O que treina |
|---|---|---|
| **Caixa de entrada** | Chega uma mensagem. Responder, ignorar ou verificar | Decisão sob ambiguidade |
| **Onde está o sinal** | Toca no elemento da mensagem que denuncia a fraude | Onde olhar: número, link, pressa, sigilo |
| **E agora?** | Dada uma situação, escolhe a ação de verificação correta | O procedimento — ligar no número do cartão, não no da mensagem |
| **O banco faz isso?** | Prática bancária real ou inventada? | Calibração: saber o que é legítimo, não só o que é golpe |
| **Passa o recado** | Escolhe como explicaria aquilo a um familiar | Retenção por ensino; efeito intergeracional |

O quarto tipo é o que impede o jogo de produzir medo generalizado. Se a pessoa não sabe o que o banco **faz**, ela não tem como saber o que ele **não faz**.

## A5. Objetivos verificáveis
1. Nomear os cinco sinais de engenharia social: urgência artificial, pedido de sigilo, troca de canal, solicitação de dado ou código, cobrança antecipada de taxa.
2. Distinguir mensagem fraudulenta de legítima, sem recusar comunicação verdadeira.
3. Indicar a ação de verificação correta para uma situação suspeita.

## A6. Métricas
Sensibilidade (golpes rejeitados), especificidade (legítimas aceitas), ação correta nomeada, e retenção D1/D7 se houver uso autônomo.

## A7. Pontos fortes
- **Política pública vigente pedindo exatamente isto**, no nosso estado. Chegar num CRAS atendendo a uma política é posição completamente diferente de pedir espaço para testar trabalho de faculdade.
- **Impacto quantificável em reais.** Não é conscientização difusa.
- **Conteúdo de fonte pública, gratuita e confiável:** Febraban, Procon, Banco Central, imprensa. Sem custo de produção de mídia, sem licenciamento.
- **Zero risco de LGPD e zero risco político.** Ninguém é contra ensinar idoso a não ser roubado.
- **Público de validação já reunido** em grupos com encontro fixo.
- **Degrada bem.** Um único tipo de tarefa com dez itens já é produto testável.

## A8. Pontos fracos
- **Uso duplo.** Ensinar como o golpe funciona ensina, em alguma medida, a aplicá-lo. Mitigação: apenas sinais já divulgados em campanha oficial; nunca método operacional.
- **Risco de reabrir ferida.** Parte do público já foi vítima, com vergonha. Exige revisão de tom item a item e ausência total de linguagem que culpe. É o risco mais sério.
- **Acertar no app e errar na vida.** No jogo a pessoa está calma e avisada. O golpe real chega quando ela está sozinha e assustada. Medimos reconhecimento, não imunidade — e isso precisa ser dito no relatório, não escondido.
- **Tema pouco vistoso em banca.** É uma tela de celular com texto.
- **Barreira de letramento digital** limita o uso autônomo no público 60+.

## A9. Validação
Instrumento de 8 itens (4 golpes, 4 legítimas) aplicado antes e uma semana depois. Parceiros candidatos em Jaraguá do Sul: Centro de Convivência da Pessoa Idosa, CRAS, Secretaria de Assistência Social, associações de aposentados, grupos de terceira idade de paróquias, UBS com grupos periódicos. Procon municipal como revisor de conteúdo.

---
---

# PARTE III — Rota B
## Treinador diário de contexto e mídia sintética

**Observação de nomenclatura, importante:** recomendo **não** chamar de "fake news". O termo carrega carga partidária e, num equipamento público municipal, isso fecha portas. "Verificação de contexto e mídia sintética" descreve melhor e não convida disputa.

## B1. Conceito
Aplicativo de treino diário em que a pessoa recebe três tarefas curtas sobre conteúdo circulante — texto, imagem, vídeo, áudio — e precisa decidir se acredita, descarta ou verifica. A tese do produto: **você não consegue distinguir sintético de real olhando, e por isso o caminho é verificar a origem.**

## B2. Causa
Circulação de conteúdo enganoso em grupos familiares e redes, com dois danos simétricos: acreditar no falso e descartar o verdadeiro.

Evidência para o GDD:
- Revisão sistemática com meta-análise de 56 estudos (2024): detecção humana de deepfake fica no nível do acaso em diferentes modalidades.
- *Journal of Cybersecurity* (Oxford, 2023), N=280: acurácia de 60 a 64%, e **nenhuma das três intervenções de ajuda melhorou o resultado**. A confiança dos participantes era alta e **sem relação com a acurácia**.
- *Communications of the ACM* (2025): desempenho próximo do acaso para imagem, áudio, vídeo e audiovisual.
- Ebner et al., *Cognitive Research* (2026): humanos no nível do acaso para imagem; 63% para vídeo, acima dos algoritmos.
- Ressalva honesta: há evidência de que treino focado em impressão global, e não em artefato local, pode quase dobrar a acurácia em rostos — mas é limitado a rostos e a uma geração de geradores.

**Consequência de design que define a rota:** um jogo que treine o olho entrega uma pessoa que erra igual, agora convencida de que sabe. Isso é pior que não fazer nada, e é mensurável — a equipe descobriria na validação sem tempo de corrigir.

## B3. Público
Primário: **decidir na reunião.** O formato diário e o tema favorecem 30 a 60 anos, que é quem repassa conteúdo em grupo de família e volta ao app sozinho. Manter 60+ é possível, mas exige a Saída 1 da seção 2 e perde parte da naturalidade do tema.

## B4. Os cinco tipos de tarefa diária

| Tipo | O que o jogador faz | O que treina |
|---|---|---|
| **Real ou IA + confiança** | Decide e declara o quanto tem certeza | **Calibração** — ver a própria confiança descolada do acerto |
| **Fora de contexto** | Foto verdadeira com legenda. Achar o descasamento de data, lugar ou evento | O caso mais comum e o menos falado |
| **Quem publicou** | Avalia a conta e o histórico, não o conteúdo | Deslocar o julgamento do artefato para a fonte |
| **Qual o primeiro passo** | Dada uma afirmação, escolhe qual verificação fazer primeiro | O procedimento |
| **Manchete × matéria** | Compara título e corpo do texto | Descasamento interno, sem precisar de ferramenta externa |

**O tipo "fora de contexto" é o mais valioso e o menos óbvio.** Boa parte do que circula em grupo de família não é imagem gerada: é foto real de outro país ou outro ano com legenda mentirosa. Nenhum detector de IA pega isso, e olhar a imagem também não. Só verificação de origem pega. Incluir esse tipo é o que mostra que a proposta entendeu o problema em vez de surfar o tema.

**O tipo "Real ou IA + confiança" tem um momento de virada** que só funciona uma vez, na primeira semana: o app mostra as duas colunas lado a lado — acurácia por volta de 55%, confiança por volta de 80% — e diz que esse resultado é o esperado e que ninguém consegue melhor. Para quem já foi enganado e sente vergonha, descobrir que a tarefa é objetivamente impossível é alívio, não derrota. Depois disso, o app passa a treinar procedimento.

## B5. Objetivos verificáveis
1. Reconhecer que inspeção visual não distingue confiavelmente mídia sintética de real.
2. Identificar descasamento de contexto entre um conteúdo e a afirmação que o acompanha.
3. Indicar o primeiro passo de verificação adequado a cada tipo de conteúdo.

## B6. Métricas
Sensibilidade, especificidade, ação correta nomeada — e **calibração**, a distância entre confiança declarada e acurácia real. Reduzir a calibração é objetivo de aprendizagem legítimo, verificável, e que quase nenhum material de mídia mede. Se o relatório final mostrar confiança injustificada caindo enquanto a taxa de verificação sobe, isso é resultado de verdade.

## B7. Pontos fortes
- **Tese contraintuitiva e forte.** "Você não consegue distinguir, e essa é a informação útil" é uma posição que praticamente nenhum material de conscientização assume. Rende defesa em banca.
- **Métrica de calibração é academicamente diferenciada.** Poucos projetos de graduação medem algo além de satisfação.
- **Tema atual e amplo.** Chama atenção, e o público potencial é toda a população conectada.
- **A lição não envelhece.** Verificar origem continua correto independentemente de quanto os geradores melhorem — enquanto qualquer heurística visual expira.
- **Motor idêntico ao da rota A.** Nenhuma engenharia se perde na escolha.

## B8. Pontos fracos
- **Licenciamento de mídia é problema imediato e caro.** Não dá para usar foto de pessoa real, imagem com direitos, nem rosto de figura pública em vídeo falso. Sobra gerar os sintéticos e fotografar os "reais" internamente. É trabalho de produção que entra no cronograma agora.
- **Ética de produzir deepfake.** O grupo vai gerar mídia sintética. Exige regra formal no GDD: nada com rosto de pessoa real identificável, marcação em todo artefato, uso restrito.
- **Perecibilidade acelerada.** Golpe muda em anos; qualidade de geração muda em meses. Artefato de hoje vira obviamente falso rápido — o que ensinaria justamente que dá para perceber.
- **Risco político latente.** Mesmo evitando o termo "fake news", exemplos concretos escorregam para tema partidário com facilidade. Mitigação: usar apenas casos fabricados pela equipe ou históricos e neutros. Nunca material político em circulação.
- **Ausência de política pública correspondente.** Não existe, hoje, lei estadual ou municipal em SC pedindo treinamento nisso. A porta institucional é mais difícil de abrir.
- **Impacto não quantificável em reais.** "Deixou de acreditar em algo falso" não tem valor mensurável como "não perdeu R$ 3.000".
- **O momento de virada é frágil.** Se o texto do resultado errar o tom, desanima em vez de aliviar. Exige teste de tom antes de teste de mecânica.
- **Não existe gabarito neutro para tudo.** Em fraude, o gabarito é objetivo. Em contexto, há casos onde razoáveis discordam — e isso enfraquece a lógica de "certo/errado" de um jogo.

## B9. Validação
Instrumento de 8 itens com declaração de confiança, aplicado antes e uma semana depois, medindo acurácia **e** calibração. Parceiros candidatos: escolas de ensino médio, bibliotecas públicas, cursos de comunicação, grupos de convivência. Revisor de conteúdo: docente de jornalismo ou comunicação.

---
---

# PARTE IV — Decisão

## 4.1 Critérios para a equipe votar

Sugiro decidir por estas perguntas, nesta ordem, e não por preferência de tema:

1. **A equipe consegue abrir uma porta institucional nas próximas três semanas?** Se sim, a rota A já tem a porta aberta pela política estadual. Se não, esse critério não decide nada.
2. **Alguém do grupo topa produzir mídia — gerar sintéticos, fotografar reais, tratar licenciamento?** Se ninguém topar, a rota B não é executável.
3. **A equipe prefere um resultado quantificável ou um resultado conceitualmente ambicioso?** A é a primeira coisa, B é a segunda.
4. **Público final: 60+ mediado por facilitador, ou adulto autônomo em uso diário?** Se a resposta for a segunda, a rota B fica mais natural.

## 4.2 Minha recomendação

**Rota A**, por três razões concretas e uma de risco.

Concretas: existe política pública vigente em SC pedindo exatamente esse material, o que é a coisa mais difícil de conseguir num projeto de extensão e vocês já têm de graça. O conteúdo é gratuito, público e sem licenciamento. E o resultado é quantificável em reais, o que faz o relatório final ter número em vez de impressão.

De risco: a rota B tem dois problemas cujo custo cai inteiro no segundo semestre — produção de mídia com licenciamento resolvido e calibragem de tom de um momento delicado. São exatamente os tipos de trabalho que estouram prazo em equipe de sete pessoas em terceiro semestre, e que não dão para terceirizar nem paralelizar bem.

**Isso dito, a rota B é a ideia mais interessante das duas**, e eu entenderia perfeitamente o grupo escolhê-la. Se escolherem, a condição mínima é que alguém assuma a produção de mídia formalmente nas duas primeiras semanas e que o texto do momento de virada seja escrito e testado antes de qualquer código.

**O que não recomendo:** fazer as duas. Não por escopo apenas, mas porque a tese das duas é a mesma — verificar a origem em vez de julgar o artefato — e ela fica mais forte dita uma vez, bem, do que duas vezes pela metade.

## 4.3 A rota não escolhida

Vai para o GDD como **anexo de evolução do produto**, com conceito, tipos de tarefa e justificativa. Isso mostra à banca que a decisão de escopo foi deliberada e fundamentada, não que ninguém pensou no assunto. É uma página, e ela trabalha a favor de vocês.

## 4.4 Lacunas a fechar antes da próxima reunião

- **[a definir]** Saída 1, 2 ou 3 da seção 2 — público e ritmo
- **[a definir]** Rota A ou B, por voto após os critérios de 4.1
- **[a definir]** Contato institucional real em Jaraguá do Sul, com nome e telefone
- **[a definir]** Exigência do curso para teste com o público escolhido — perguntar ao orientador esta semana
- **[a definir]** Quem revisa o conteúdo tecnicamente
- **[a definir]** Schema do arquivo de conteúdo e do agendador de repetição espaçada — entregável deste semestre
