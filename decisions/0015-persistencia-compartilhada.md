# 0015 — Persistência compartilhada

- **Data:** a preencher
- **Etapa / Marco:** E3 / M13
- **Status:** Vigente
- **Substitui:** D09 (registrada em docs/00-historico/historico.md)

## Contexto

A decisão D09 estabelecia "web, sem backend, sem login, sem servidor", pensada
para eliminar risco de LGPD e custo de infraestrutura. Ela conflitava com os
marcos M12 e M13, que pedem modelo de banco de dados, arquitetura de back-end e
autenticação — conflito registrado como pendência P07. A adoção do multiplayer
com convite (decisão 0014) tornou a D09 inviável.

## Decisão

Adotar persistência compartilhada em backend gerenciado de camada gratuita, com
log de ações append-only por sessão e estado derivado no cliente. Identidade
anônima gerada no dispositivo, sem e-mail e sem senha.

## Alternativas descartadas

- Manter tudo local e abrir mão do multiplayer
- Backend próprio hospedado pela equipe — custo e manutenção fora do escopo
- Autenticação com conta de usuário — reabre LGPD sem necessidade

## Consequência

Fecha a pendência P07. Os marcos M12 e M13 passam a ter material real em vez de
inventado. Introduz dependência de serviço externo, mitigada pelo fato de o
estado ser derivável do log e o jogo solo funcionar sem rede.
