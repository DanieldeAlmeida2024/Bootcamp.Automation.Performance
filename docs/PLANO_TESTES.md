# Plano de testes — WireMock + k6

Versão 1.1.0 — 14/11/2026

## Contrato HTTP — testes automatizados

Executar: `python -m unittest discover -s tests -p 'test_*.py' -v`.

| ID | Cenário | Resultado esperado |
| --- | --- | --- |
| WM-01 | GET /api/cars | HTTP 200; cinco carros, Corolla primeiro e BMW M3 último |
| WM-02 | POST com model fusca | HTTP 201, mensagem de sucesso e ID estático 6 |
| WM-03 | POST com model up tsi | HTTP 500 simulado e mensagem prevista |
| WM-04 | POST com model jetta | HTTP 404 e mensagem de não encontrado |
| WM-05 | POST fusca seguido de GET | Catálogo continua com cinco carros (mock não persiste) |

O teste inicia o WireMock real com `java -jar`; se o JAR não iniciar ou o stub estiver incorreto, deve falhar. Não é uma inspeção superficial de arquivo.

## Cenários k6 — CI e execução manual

O workflow `.github/workflows/k6-carga-local.yml` usa Java 17, inicia WireMock local, instala k6 com a action oficial Grafana e executa `tests/live.js` em 10 VUs/5 segundos. Os critérios **bloqueiam merge**: `checks > 99%`, `http_req_failed < 1%`, `p95 < 1500ms`, `p99 < 3000ms` e `iterations > 30`. Salva `k6-summary.json` como artifact para revisão.

**KPIs medidos são do mock WireMock no runner GitHub**, não da aplicação de negócios. Os cenários POST 404 e 500 são respostas intencionais e não entram no teste de erro-rate HTTP de carga.

| Caso | Cenário | Resultado esperado |
| --- | --- | --- |
| PERF-01 | 10 usuários virtuais, 5 segundos, GET | Pelo menos 31 iterações |
| PERF-02 | Taxa de checagens HTTP/JSON | >99% |
| PERF-03 | Erros de transporte e status no GET | <1% |
| PERF-04 | Latência de requisição p95/p99 | <1500ms e <3000ms |
| PERF-05 | Resumo da execução | Artifact `k6-wiremock-summary` para auditoria |

## Outros cenários k6 — execução manual

- `tests/test-consulta.js`: consulta GET e ordem de veículos.
- `tests/test-sucesso.js`: resposta 201 simulada.
- `tests/test-404.js`: modelo não mapeado.
- `tests/test-500.js`: erro 500 proposital.
- `tests/live.js`: 10 VUs por 5 segundos.

Todos possuem critério `checks > 99%`. O fluxo de CI executa **somente `tests/live.js`**; os quatro scripts de POST/GET específicos permanecem para execução manual. Nenhum teste de backend real foi executado.

## Fora de escopo

Não mede capacidade real sob carga, SLA, produção, persistência, segurança do backend nem integrações com serviços externos. Relatórios HTML preexistentes são artefatos históricos, não resultado da CI desta revisão.
