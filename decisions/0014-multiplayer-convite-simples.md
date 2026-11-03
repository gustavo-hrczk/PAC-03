# 0014 — Multiplayer com convite simples

- **Data:** a preencher
- **Etapa / Marco:** E3 / M06
- **Status:** Vigente
- **Substitui:** —

## Contexto

A estrutura de tabuleiro abriu a possibilidade de sessões compartilhadas. A
discussão envolveu desde P2P com sincronia até modelos sem servidor algum.
Partida por turnos entre amigos morre por abandono quando um jogador para,
o que descartou o modelo de turno bloqueante.

## Decisão

Multiplayer assíncrono com sessão criada por um host, que convida os demais por
código curto. Todos os participantes recebem o mesmo baralho, gerado
deterministicamente pela semente da sessão. Cada jogador age no próprio ritmo,
sem depender da vez dos outros. Sem ranking público e sem matchmaking.
Interação social por reações predefinidas, nunca por texto livre.

## Alternativas descartadas

- P2P via WebRTC — exige sinalização, STUN e TURN; três a cinco semanas só nisso
- Turno alternado bloqueante — mata a partida no primeiro jogador que some
- Estado dentro do link, trocado por mensagem — barato, mas limita o número de jogadores
- Chat de texto livre — moderação, LGPD e responsabilidade sobre conteúdo gerado

## Consequência

Exige persistência compartilhada, o que leva à decisão 0015. Em contrapartida,
fornece material real para os marcos M12 e M13, que pediam modelo de dados,
arquitetura e autenticação.
