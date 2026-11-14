# Histórico de mudanças — Performance WireMock/k6

## PERF 1.2.0 — contratos completos no CI (14/11/2026)

- Workflow `k6-carga-local.yml` agora executa todos os cinco scripts k6: `live`, `test-consulta`, `test-sucesso`, `test-404` e `test-500`.
- Resumos JSON individuais incluídos no artifact `k6-wiremock-summary`.
- As respostas 404 e 500 são verificadas como **contrato esperado do WireMock**, não contabilizadas como indisponibilidade do backend.
- Nenhuma mudança no simulador HTTP, nas dependências Java ou no ambiente de rede. Teste de backend real permanece pendente.
