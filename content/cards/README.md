# Cartas

## Pipeline de produção

```
premissas.json  →  carta escrita à mão  →  molde formalizado  →  gerador
  (60 prontas)      (NNN-molde-casa.md)      (regras + slots)     (2027/1)
```

O documento "PAC III — Conteúdo de Cartas" já entregou a **camada 1 de 3**:
60 premissas (15 moldes × 4 casas), convertidas para `premissas.json`.

Faltam as camadas 2 e 3 — preenchimento e sinais — além de ruído, resposta
correta e ponte. É isso que cada arquivo de carta adiciona.

## Formato de uma carta

Arquivo `NNN-molde-casa.md`, por exemplo `004-reembolso-porto.md`.

```markdown
# NNN — Título curto

- **Molde:** 2 — Reembolso ou estorno pendente
- **Casa:** Porto
- **Natureza:** fraudulenta | legítima
- **Faixa:** inicial | média | alta | avançada
- **Sinais presentes:** (ids da lista fechada de 10)
- **Ruído:** (características estranhas mas inofensivas)

## Enunciado
O texto como chega ao jogador.

## Resposta correta
agir | ignorar | verificar — e o porquê.

## Consequências
- Acerto:
- Erro por credulidade:
- Erro por desconfiança:

## Ponte para hoje
Uma linha ligando o golpe do mundo ao equivalente contemporâneo.
```

## Os dez sinais (lista fechada)

| id | Sinal | Como aparece no mundo |
|:---|:--------------------------|:-------------------------------------|
| S01 | Canal não oficial | Proposta feita na taverna, não no Registro |
| S02 | Pedido de selo pessoal | Pedem o selo ou a senha do cofre |
| S03 | Urgência artificial | "O navio zarpa com a maré, decida agora" |
| S04 | Taxa antecipada | Adiantamento para liberar carga retida |
| S05 | Remetente sem registro | Casa comercial sem registro no porto |
| S06 | Valor incompatível | Lucro muito acima do praticado na rota |
| S07 | Pedido de sigilo | "Não comente com a Guilda" |
| S08 | Entreposto fora das rotas | Enseada fora dos caminhos conhecidos |
| S09 | Pagamento atípico | Só em moeda estrangeira, em mãos |
| S10 | Bom demais para ser verdade | Retorno garantido, sem risco de viagem |

## Faixas de dificuldade

| Faixa | Sinais | Ruído | Característica |
|:----------|:-------|:---------|:-----------------------------|
| Inicial | 3 a 4 | Nenhum | Golpe evidente; ensina o repertório |
| Média | 2 | Pouco | Exige leitura atenta |
| Alta | 1 | Bastante | Exige verificação; errar é esperado |
| Avançada | 0 aparente | Muito | O sinal só aparece ao verificar |

## Regras invioláveis

1. **A resposta correta deriva dos sinais, nunca do texto nem do molde.**
   Um mesmo molde precisa aparecer legítimo em algumas cartas e fraudulento em
   outras, ou o jogador decora o molde em vez de ler os indícios.
2. **Ruído é obrigatório nas legítimas.** Sem carta verdadeira de aparência
   esquisita, o jogo ensina que "estranho = golpe", que é paranoia e não
   aprendizado.
3. **Toda carta fraudulenta tem ao menos um sinal detectável.** Nenhuma
   armadilha é impossível; na faixa avançada o sinal só aparece ao verificar.
4. **A ponte aparece na primeira vez** que o jogador enfrenta cada molde.
   Depois fica no diário.

## Meta

30 cartas escritas à mão antes de projetar o gerador. Gerador desenhado antes
do conteúdo produz a coisa errada com eficiência.
