# Automação de APIs — WireMock + k6

Laboratório didático de **contratos HTTP e cenários de carga curta** para uma API fictícia de veículos. A API é simulada por WireMock; não existe serviço de produção nem banco de dados.

## Iniciar o mock

Requer **Java 17+**. Na raiz do repositório:

```bash
java -jar wiremock-standalone-3.9.1.jar --port 8080 --bind-address 127.0.0.1 --root-dir .
```

Os mapeamentos são carregados de `mappings/` e os dados de `__files/cars.json`. O servidor escuta apenas a máquina local por padrão.

## Contratos exercitados

| Método | Rota | Cenário | Resposta simulada |
| --- | --- | --- | --- |
| GET | `/api/cars` | Consultar catálogo | 200; lista fixa de cinco veículos |
| POST | `/api/cars` | `model: "fusca"` | 201; mensagem de cadastro e `carId: 6` |
| POST | `/api/cars` | `model: "up tsi"` | 500 **intencional**, configurado no stub |
| POST | `/api/cars` | Outro modelo | 404; mensagem de não encontrado |

O POST **não persiste dados**: a resposta de cadastro é fixa e o GET continua com cinco registros.

## Testes reais no GitHub Actions

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

Os testes em `tests/test_contrato_wiremock.py` iniciam o JAR local em uma porta livre, executam requisições HTTP reais e verificam respostas, incluindo o erro 500 esperado. O workflow `contrato-wiremock.yml` usa Java 17 e Python 3.12. Não há chamadas à AWS nem deploy.

## Carga curta validada automaticamente com k6

O workflow [k6-carga-local.yml](.github/workflows/k6-carga-local.yml) instala k6 via Grafana, inicia WireMock em `127.0.0.1:8080` e executa **10 usuários virtuais por 5 segundos** no `GET /api/cars`. Ele só passa se: mais de 99% dos checks estiverem corretos, taxa de requisição falha <1%, p95 <1500 ms, p99 <3000 ms e houver mais de 30 iterações. O resumo `k6-summary.json` fica disponível como artifact da execução. O job não faz upload para Grafana Cloud nem usa serviços externos de aplicação.

**Essa medição é apenas do WireMock no runner do GitHub**, não um benchmark de API real.

## Cenários k6

Instale `k6` na sua máquina e mantenha o WireMock ativo. Então execute:

```bash
k6 run tests/test-consulta.js
k6 run tests/test-sucesso.js
k6 run tests/test-404.js
k6 run tests/test-500.js
k6 run tests/live.js
```

Para outro endereço local: `k6 run -e BASE_URL=http://127.0.0.1:8080 tests/live.js`.

Os scripts exigem aprovação de mais de 99% das verificações (`checks`) e têm limite de 5 segundos por requisição. Os relatórios k6 são exibidos no terminal; foram removidos downloads de JavaScript remoto para gerar HTML.

**Escopo:** os cenários medem latência e vazão **do mock local** em carga curta, não latência, vazão nem capacidade de uma aplicação real. O cenário HTTP 500 confirma um erro **propositalmente simulado**, não uma falha inesperada da plataforma.

[Arquitetura](docs/ARQUITETURA.md) · [Plano de testes](docs/PLANO_TESTES.md) · [UML](docs/UML.puml)
