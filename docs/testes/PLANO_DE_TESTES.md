# Testes — Teste de carga e cenários de erro em API simulada

**v1.0.0 · 11/11/2026 · base `249aca7aa03654257bb6771254901ed5451e09e7` · análise do código, sem execução de testes neste PR.**

## Casos e critérios de aceitação
| ID | Cenário | Esperado | Estado |
|---|---|---|---|
| PERF-01 | POST /api/cars com fusca/1965 | 201, message correta, carId=6 | Planejado, não executado neste PR |
| PERF-02 | POST com modelo up tsi | 500 e mensagem definida no mapping | Planejado, não executado neste PR |
| PERF-03 | POST com body sem brand | Revisar mapping e status efetivo | Planejado, não executado neste PR |
| PERF-04 | GET /api/cars | Resposta de consulta compatível com test-consulta.js | Planejado, não executado neste PR |
| PERF-05 | 10 VUs por 5 segundos | Sem erros não previstos, relatório k6 | Planejado, não executado neste PR |
| PERF-06 | Mock offline | Falhas de conexão reportadas | Planejado, não executado neste PR |
| PERF-07 | Reporter remoto indisponível | Executar com reporter local ou diagnóstico | Planejado, não executado neste PR |
| PERF-08 | Latência p95 com thresholds definidos | Pendente: threshold precisa ser estabelecido | Planejado, não executado neste PR |

## Estratégia
Isolar as dependências externas do projeto e exercitar os limites citados; preservar dados e hardware. Executar em ambiente adequado:
```bash
k6 run tests/test-sucesso.js
```

A presença de scripts e relatórios HTML não comprova metas de performance, pois não há baseline publicado nem thresholds p95 quantificados.

Registrar por cenário SHA, versão de ferramenta, entrada, resultado observado, evidência e decisão. Teste documental presente em `tests/` não comprova os critérios de domínio.
