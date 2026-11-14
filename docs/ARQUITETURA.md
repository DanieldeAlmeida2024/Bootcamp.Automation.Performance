# Arquitetura — automação de APIs fictícias

Versão 1.1.0 — 14/11/2026

## Componentes e limites

- **WireMock 3.9.1**: servidor HTTP local a partir do JAR versionado; utiliza os arquivos `mappings/` e a resposta estática `__files/cars.json`.
- **Mapeamentos de contrato**: GET 200, POST 201 para `fusca`, POST 500 simulado para `up tsi`, POST 404 para outros modelos.
- **Testes Python/unittest**: criam uma instância real de WireMock em porta efêmera e fazem requisições com `urllib.request`; verificam os stubs sem bibliotecas HTTP externas.
- **k6**: cinco cenários independentes, URLs configuráveis por `BASE_URL`, thresholds de `checks`. Os scripts não importam relatórios JavaScript remotamente.

Os resultados de POST são **determinísticos e não persistentes**. O caminho feliz 201 não significa que o catálogo foi modificado.

## Segurança e implantação

O comando de desenvolvimento vincula a interface a `127.0.0.1`; não exponha o mock publicamente. O cenário 500 é parte de um teste negativo, não um bug a corrigir no WireMock. Este laboratório não implementa autenticação e não serve como backend real.

## Evolução

- v1.0: arquivos WireMock, scripts k6 e relatórios de exemplo, sem CI que exercesse a API.
- v1.1: contrato automatizado com servidor real local, checks k6 com thresholds, remoção de script externo para relatório e documentação de comportamento.
