# Requisitos — Bootcamp.Automation.Performance

Objetivo: Mock HTTP de cadastro e consulta de veículos usando WireMock, com testes didáticos.

RF01 — Executar o cenário ou exercício principal.

RF02 — Apresentar saída verificável e documentar pré-condições.

RF03 — Sinalizar entradas inválidas e falhas externas.

RNF01 — Executar de forma reproduzível em ambiente de testes.

RNF02 — Não versionar segredos.

RF04 — Executar `GET /api/cars` em uma carga didática de 10 VUs durante 5 segundos em WireMock real local.

RNF03 — Medir latência `http_req_duration`: p95 < 1500 ms e p99 < 3000 ms **somente para o mock local**.

RNF04 — Exigir taxa de erros HTTP < 1%, checks > 99% e ao menos 31 iterações no ensaio.

RNF05 — Gravar relatório JSON de resumo do k6 como artifact do GitHub Actions.

Pendências: mock não representa performance de uma API de produção; não há benchmark de backend real, teste de pico/soak nem TLS/autenticação.

Requisitos inferidos dos arquivos; não são compromissos de produção.
