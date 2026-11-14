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

## Cenários k6 — execução manual

- `tests/test-consulta.js`: consulta GET e ordem de veículos.
- `tests/test-sucesso.js`: resposta 201 simulada.
- `tests/test-404.js`: modelo não mapeado.
- `tests/test-500.js`: erro 500 proposital.
- `tests/live.js`: 10 VUs por 5 segundos.

Todos possuem critério `checks > 99%`. A CI não instala k6, então **não afirmar que foram executados automaticamente**.

## Fora de escopo

Não mede capacidade real sob carga, SLA, produção, persistência, segurança do backend nem integrações com serviços externos. Relatórios HTML preexistentes são artefatos históricos, não resultado da CI desta revisão.
