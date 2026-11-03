# "Confere?" — v2
## Arquitetura modular

**Autor:** Gustavo · 18/08/2026
**Substitui as seções 1, 5, 6, 7 e 8 da ficha v1.** As seções de causa, público, validação e riscos da v1 continuam válidas e são complementadas ao final.

---

## 1. Veredicto sobre a expansão

**Modularizar: sim.** É a decisão certa, por três razões que valem ser ditas em sala:

1. O motor do jogo já é genérico. O loop é *recebe artefato → inspeciona → decide → consequência + motivo*. Isso serve para mensagem de golpe, imagem gerada, áudio clonado, oferta de emprego falsa e loja fantasma sem alterar uma linha de mecânica. **Um módulo é um pacote de conteúdo, não um jogo novo.**
2. Modularidade é o argumento mais forte que vocês têm para a etapa de análise de requisitos deste semestre. Separar motor de conteúdo, definir o schema de um módulo, especificar extensibilidade — isso é engenharia de software de verdade e rende documentação legítima, não enfeite.
3. Um jogo de módulo único é um trabalho de faculdade. Uma plataforma de treinamento com módulos é algo que uma secretaria de assistência social adota e continua usando depois que vocês colarem grau.

**Mas o módulo "Real ou IA?" precisa de uma correção conceitual antes de entrar.** Ela está na seção 4.

---

## 2. A regra que define o que pode ser módulo

Sem uma regra, "módulos" vira desculpa para escopo infinito. Proponho um critério de admissão, e ele deve ficar registrado no GDD:

> **Um tema só se torna módulo se satisfizer as três condições:**
> **(a)** a resposta correta na vida real é *verificar por canal independente*, e não *julgar o artefato*;
> **(b)** existem os dois erros — acreditar no falso **e** rejeitar o verdadeiro — e ambos causam dano real;
> **(c)** roda no motor existente sem mecânica nova, apenas com conteúdo e regras de inspeção declaradas em dados.

Essa regra faz três coisas: mantém a coerência pedagógica, impede escopo criativo, e dá ao grupo um critério objetivo para dizer "não" a uma sugestão sem discussão de gosto.

---

## 3. A espinha do jogo inteiro

Todos os módulos ensinam **uma única habilidade**, aplicada a artefatos diferentes:

> **Não julgue o artefato. Verifique a origem por um canal que você mesmo escolheu.**

- Mensagem do banco? Não analise a mensagem — desligue e ligue no número do cartão.
- Parente pedindo PIX de número novo? Não analise o texto — ligue no número antigo.
- Imagem de um acidente? Não conte os dedos — procure a mesma imagem em outro lugar, veja quem publicou primeiro.
- Áudio de um político? Não escute o chiado — confira se algum veículo com nome está reportando.

Isso é o que salva a expansão. Sem essa espinha, você tem uma coleção de minijogos temáticos. Com ela, você tem um jogo com uma tese.

---

## 4. Módulo B — "Real ou IA?": a correção

### 4.1 O problema com a versão intuitiva

A forma natural de fazer esse módulo é: mostrar imagem, jogador aponta os pontos suspeitos, jogo dá pontos por acertar os artefatos. **Isso não funciona, e é pior que não fazer nada.**

Evidência para citar no GDD:

- Revisão sistemática com meta-análise de 56 estudos (2024): a detecção humana de deepfake fica no nível do acaso em diferentes modalidades, e é pior para estímulos sintéticos do que para os reais.
- Estudo publicado no *Journal of Cybersecurity* (Oxford, 2023), N=280: acurácia entre 60 e 64%, apenas um pouco acima do acaso, e **nenhuma das três intervenções de ajuda melhorou o resultado**. Achado crítico: a confiança dos participantes era alta e **sem relação com a acurácia**.
- *Communications of the ACM* (2025): desempenho próximo do acaso para imagem, áudio, vídeo e audiovisual.
- Estudo de 2026 em *Cognitive Research* (Ebner et al.): humanos detectam deepfake de imagem só ao nível do acaso, embora tenham ido melhor que os algoritmos em vídeo (63%).
- Há evidência de que treino focado em impressão global — não em artefato local — pode quase dobrar a acurácia em rostos. Vale registrar como ressalva honesta, mas é limitado a rostos e a uma geração de geradores, e envelhece junto com a tecnologia.

Traduzindo para o projeto: **se o módulo treinar o olho, ele entrega uma pessoa que erra na mesma taxa de antes, agora convencida de que sabe distinguir.** Um jogo que aumenta confiança sem aumentar acurácia produz vítima mais fácil, não mais difícil. Seria um resultado de projeto genuinamente ruim, e mensurável — vocês descobririam isso na validação e não teria mais tempo de corrigir.

### 4.2 O que o módulo ensina em vez disso

**A lição do módulo é: você não consegue distinguir, e essa é a informação útil.**

O módulo tem três atos, e essa estrutura *é* o design:

**Ato 1 — A rodada honesta.** Dez artefatos, metade real, metade sintético. O jogador decide "real" ou "IA" e declara a confiança em cada um: *tenho certeza* / *acho que* / *não sei*. Sem feedback nenhum durante a rodada.

**Ato 2 — O espelho.** O resultado aparece em duas colunas: sua acurácia e sua confiança. Quase todo jogador vai ver algo em torno de 55% de acerto com 80% de confiança. O jogo então mostra que esse resultado é o esperado, citando a pesquisa, e diz explicitamente: *não é falha sua. Ninguém consegue. Inclusive quem trabalha com isso.*

Esse é o momento de maior valor do jogo inteiro, e é o oposto de humilhar — é aliviar. A pessoa idosa que caiu num golpe carrega vergonha; descobrir que a tarefa é objetivamente impossível remove a culpa e abre espaço para aprender o procedimento.

**Ato 3 — O procedimento.** Os mesmos dez artefatos voltam, agora com contexto: quem publicou, quando, com qual legenda, o que mais essa conta publica, se o mesmo material aparece em outro lugar. O jogador tem três ações — **acreditar**, **descartar**, **verificar** — e ferramentas de verificação: busca reversa de imagem, checar a conta que publicou, procurar veículo que reportou, conferir data.

Na segunda rodada a acurácia sobe muito. E a lição fica gravada não como frase, mas como experiência: *errei olhando, acertei verificando.*

### 4.3 Placar duplo do módulo B

Igual ao módulo A, com os dois erros pesando:

| Contador | O que mede |
|---|---|
| **Enganado** | Acreditou em conteúdo sintético |
| **Descartou verdade** | Chamou de IA algo que era real |

O segundo contador é o que faz este módulo ser sério. O dano de descrer do que é verdadeiro é tão grave quanto o de crer no falso — foto real de crime descartada como montagem, áudio real de autoridade descartado como clone, diagnóstico real descartado como IA. Um jogo que só pune credulidade produz ceticismo indiscriminado, que é a outra forma de não conseguir pensar.

### 4.4 Conteúdo do módulo B

Cinco dias, escalando por **tipo de dificuldade de verificação**, não por qualidade do sintético:

| Dia | Artefato | Ferramenta de verificação treinada |
|---|---|---|
| 1 | Foto de pessoa que não existe (perfil falso) | Busca reversa; conta sem histórico |
| 2 | Foto real usada fora de contexto | Data e origem — o caso mais comum e o menos falado |
| 3 | Áudio de voz clonada de parente pedindo dinheiro | Retorno por canal conhecido; pergunta que só a pessoa sabe |
| 4 | Vídeo de figura pública dizendo algo | Veículo com nome reportando; canal oficial |
| 5 | Anúncio ou depoimento sintético de produto ou investimento | Registro da empresa; consulta ao Procon |

**Nota de design importante:** o dia 2 é o mais valioso e o menos óbvio. Boa parte da desinformação que circula em grupo de família não é imagem gerada — é foto verdadeira de outro país, de outro ano, com legenda mentirosa. Nenhum detector de IA pega isso, e nenhuma técnica de "olhar a imagem" também. Só verificação de origem pega. Incluir esse dia é o que mostra que a proposta entendeu o problema.

O dia 3 conecta os dois módulos diretamente: voz clonada de parente pedindo PIX é golpe financeiro *e* mídia sintética. A resposta correta é a mesma dos dois módulos: ligar no número que você já tem.

---

## 5. Catálogo de módulos

**Recomendados para a visão completa:**

| ID | Módulo | Status |
|---|---|---|
| A | Golpes financeiros — falso parente, falsa central, boleto e link falso, taxa de liberação, consignado | **Núcleo. Entrega no MVP.** |
| B | Real ou IA — imagem, foto fora de contexto, voz, vídeo, anúncio | **Fatia vertical no MVP, completo depois.** |
| C | Compra e oferta — loja fantasma, oferta de emprego falsa, investimento milagroso | Pós-MVP |

**Recusados pela regra da seção 2:**

- *Fake news política* — falha em (a): não existe canal de verificação neutro e o tema arrasta disputa partidária para dentro de um projeto que precisa entrar em equipamento público. Fica de fora, e é bom que fique.
- *Golpe afetivo / romance scam* — passa na regra, mas o custo emocional para o público 60+ em oficina coletiva é alto demais. Se entrar algum dia, entra em material individual, não em grupo.
- *Segurança de senha e higiene digital* — falha em (b): não tem o erro simétrico. É boa cartilha, não é módulo deste jogo.

---

## 6. Consequência técnica: o motor é o produto

A expansão só é barata se o motor for genérico desde o início. Isso vira requisito arquitetural, e é a parte mais defensável do projeto em banca:

**O motor não sabe o que é um golpe.** Ele sabe carregar um módulo, apresentar artefatos, aceitar decisões, aplicar regras de pontuação e mostrar explicação.

Um módulo é um arquivo de dados declarando:

```
módulo:
  id, título, público-alvo, número de dias
  ações disponíveis: [acreditar/responder, descartar/ignorar, verificar]
  ferramentas de inspeção habilitadas: [remetente, link, data, busca-reversa, ...]
  contadores: [nome do erro tipo 1, nome do erro tipo 2]
  dias:
    - artefatos: [ { tipo, conteúdo, ação_correta, pistas, explicação } ]
```

Consequências práticas:
- Um módulo novo é conteúdo, feito por quem não programa.
- O time de programação trabalha uma vez, no motor, e não a cada tema.
- O schema do módulo é um artefato de requisitos concreto e não trivial — exatamente o que a disciplina pede.
- Instituições parceiras podem, no futuro, propor módulos sem depender de vocês.

---

## 7. Métricas unificadas

Todo módulo reporta o mesmo par, e é isso que torna a plataforma avaliável de forma consistente:

- **Sensibilidade** — proporção de artefatos falsos corretamente rejeitados
- **Especificidade** — proporção de artefatos legítimos corretamente aceitos
- **Ação correta nomeada** — proporção de casos em que a pessoa cita verificação por canal independente

O módulo B acrescenta uma quarta, e ela é a mais interessante academicamente:

- **Calibração** — distância entre confiança declarada e acurácia real

Reduzir a calibração é um objetivo de aprendizagem legítimo, verificável, e que quase nenhum material antifraude mede. Se vocês conseguirem mostrar no relatório final que a confiança injustificada caiu enquanto a taxa de verificação subiu, isso é um resultado bom de verdade — não é "os alunos gostaram do jogo".

---

## 8. Disciplina de escopo: o que realmente entrega

Aqui preciso ser direto, porque expansão de escopo foi o risco que eu apontei nas propostas dos seus colegas e seria incoerente não apontar na sua. **Sete pessoas de terceiro semestre em dois semestres não entregam três módulos completos.** O que salva é a distinção entre arquitetura e entrega:

| Semestre | Entrega |
|---|---|
| **1º (atual)** | GDD com arquitetura modular completa, schema de módulo especificado, catálogo dos três módulos, análise de requisitos, conteúdo escrito do módulo A (25 artefatos) e do dia 1 do módulo B, protótipo de papel testado com 3 a 5 pessoas |
| **2º** | Motor funcional. **Módulo A completo** (5 dias). **Módulo B como fatia vertical** — 1 dia, 6 artefatos, com os três atos funcionando. Roteiro de oficina em PDF. Validação com pré/pós-teste em uma instituição. |
| **Fora do prazo** | Módulo B completo, módulo C, geração procedural, modo facilitador com painel |

A fatia vertical do módulo B é obrigatória e não é concessão: ela é o que **prova a arquitetura**. Um segundo módulo rodando no mesmo motor, com o mesmo loop e placar diferente, demonstra que a modularidade é real e não slide. Sem ela, "arquitetura modular" é promessa.

E se o prazo apertar mais: o módulo A com um único dia já é produto testável. A proposta degrada bem, e isso continua verdade depois da expansão.

---

## 9. Riscos novos que a expansão traz

- **Licenciamento de imagem — o mais imediato.** Vocês não podem usar foto de pessoa real sem autorização, nem imagem com direitos, nem rosto de figura pública em vídeo falso. Isso elimina a maior parte do material que circula. Caminho viável: gerar vocês mesmos os artefatos sintéticos, e usar como "reais" fotos tiradas pelo próprio grupo ou de banco com licença livre. Dá controle total sobre gabarito e evita problema jurídico — mas é trabalho de produção que precisa entrar no cronograma agora, não depois.
- **Ética de produzir mídia sintética.** O grupo vai gerar deepfake para fins didáticos. Regras a fixar no GDD: nada com rosto de pessoa real identificável, nada com figura pública real, marca d'água ou metadado em todo artefato gerado, e uso restrito ao jogo. Vale um parágrafo formal — é o tipo de cuidado que a banca nota.
- **Perecibilidade acelerada.** Golpe financeiro muda em anos; qualidade de geração muda em meses. Um artefato sintético de hoje vira "obviamente falso" rápido, e um jogo com exemplos velhos ensina que dá para perceber — o oposto da lição. Mitigação: o módulo B não pode depender de o artefato *parecer* falso, porque a lição dele não é aparência. Essa é outra razão pela qual a correção da seção 4 é estrutural, e não estética.
- **Desmoralização no ato 2.** Mostrar a alguém que ela acertou 55% pode ser desanimador, especialmente para quem já se sente incapaz diante de tecnologia. O enquadramento tem que ser inequívoco: *a tarefa é impossível para todos, e existe um procedimento que funciona*. Se o ato 2 der errado no tom, o módulo faz mal. Precisa de teste de tom antes de teste de mecânica.
- **Diluição de público.** O módulo B interessa a todo mundo, de 15 a 80 anos. É oportunidade — mas se o grupo começar a projetar para "todos", perde a adaptação de interface para 60+, que é o diferencial real. **Decisão a travar hoje: o público primário continua 60+, e o módulo B é projetado para 60+.** Que um jovem também aproveite é bônus, não requisito.
- **Escopo, de novo.** A regra da seção 2 e a tabela da seção 8 existem para isso. Se alguém do grupo propuser um quarto módulo, a resposta é a regra, não uma discussão.

---

## 10. Como apresentar em sala

**Uma frase:** *"É uma plataforma de treinamento contra engano digital, com módulos. O primeiro é golpe financeiro. O segundo ensina que você não consegue distinguir foto real de foto de IA — e que por isso a saída é verificar a fonte, não apertar os olhos."*

**Se alguém disser "então é só um quiz de imagens":** o jogo mede a sua confiança junto com o seu acerto e mostra a diferença entre as duas. Essa comparação é o conteúdo. Nenhum quiz faz isso.

**Se alguém disser "é escopo demais":** concordo, e por isso a entrega é um módulo completo e uma fatia vertical do segundo. A arquitetura modular é documento; o produto é um módulo e meio. Está na tabela.

**Se alguém disser "vamos fazer o de IA primeiro, é mais atual":** o módulo A é o que abre a porta institucional, porque existe política pública em SC pedindo exatamente aquilo. O módulo B é o que ganha a atenção da banca. Fazer A primeiro e B como fatia entrega os dois.

---

## 11. Lacunas a fechar

Além das da v1:

- **[a definir]** Origem dos artefatos "reais" do módulo B — fotos do próprio grupo ou banco de licença livre
- **[a definir]** Ferramenta de geração dos artefatos sintéticos e regra de marcação
- **[a definir]** Se a busca reversa dentro do jogo é simulada (resultado pré-escrito) ou real (chamada externa). Simulada é mais barata, mais confiável em oficina e funciona offline — recomendo simulada no MVP
- **[a definir]** Texto do ato 2: como comunicar "você acertou 55%" sem desanimar. Testar com 3 pessoas antes de escrever o resto
- **[a definir]** Schema formal do arquivo de módulo — é entregável do 1º semestre
