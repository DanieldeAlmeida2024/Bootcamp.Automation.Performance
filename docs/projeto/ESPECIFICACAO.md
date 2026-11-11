# Teste de carga e cenários de erro em API simulada

**v1.0.0 · 11/11/2026 · base `249aca7aa03654257bb6771254901ed5451e09e7` · análise do código, sem execução de testes neste PR.**

## Produto, componentes, contratos e riscos
Laboratório de ensaio HTTP com k6 e respostas mockadas pelo WireMock na porta 8080. O diretório `mappings/` define respostas da API `/api/cars`, incluindo sucesso, 404 e 500, e `__files/cars.json` fornece fixture. Os scripts `tests/test-sucesso.js`, `test-consulta.js`, `test-500.js`, `live.js` testam contratos distintos; relatórios HTML em `report/` são artefatos de execução anterior, não indicadores de resultado atual.

`test-sucesso.js` envia POST de Volkswagen fusca/1965 e verifica HTTP 201, mensagem 'Car successfully registered!' e carId=6, com sleep 1 segundo. `test-500.js` envia Volkswagen up tsi/2020 e espera HTTP 500 e mensagem de rejeição do modelo; configura 10 VUs e duração 5 segundos, com comentário de 30s divergente. `handleSummary` usa bundle externo de reporter, dependência online.

**Risco:** testar desempenho de WireMock mede essencialmente o mock e a rede local, não o desempenho real do backend. É necessário distinguir contrato, erro esperado e limiar de throughput/latência; a suíte não publica métricas p95 obrigatórias no código inspecionado. Não executar carga contra produção sem autorização.

## Entradas, execução e limites
```bash
k6 run tests/test-sucesso.js
```

A presença de scripts e relatórios HTML não comprova metas de performance, pois não há baseline publicado nem thresholds p95 quantificados.

## Relação com os documentos
Os fluxos estão nos diagramas de [UML](../uml/README.md) e os critérios rastreáveis estão em [Testes](../testes/PLANO_DE_TESTES.md). Mudança de regra exige atualizar ambos e o [controle](../controle/VERSIONAMENTO.md).
