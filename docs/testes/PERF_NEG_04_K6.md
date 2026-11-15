# PERF-NEG-04 — Métrica de erro em cenários negativos k6

**Revisão:** 15/11/2026 · **Stack:** Grafana k6 + WireMock 3.9.1.

## Achado
Os cenários para `404` e `500` validavam o status e corpo em `checks`, porém o k6, por padrão, marcava **todas** as respostas HTTP 4xx/5xx como `http_req_failed`. Isso produz interpretações equivocadas do resultado caso a mesma métrica seja usada em painéis, enquanto a suíte negativa não definia threshold algum para erros de transporte.

## Correção
- Atribuir `http.expectedStatuses(404)` apenas ao teste 404 e `http.expectedStatuses(500)` apenas ao teste 500.
- Exigir taxa de requisições inesperadamente falhas menor que 1%; manter os checks do status e JSON específicos.
- Validar semanticamente os scripts na suíte Python e executar k6 contra WireMock isolado nos workflows existentes.
- Remover arquivos de estado `.idea` do índice Git; documentação, exemplos e JAR de referência continuam.

## Limitação
Nenhum teste aqui verifica SLA de produção. O HTTP 500 é intencional **somente** no stub de falha; não converter esse comportamento em regra de monitoramento real.

Referência: documentação do Grafana k6 para `setResponseCallback` e `expectedStatuses`.
