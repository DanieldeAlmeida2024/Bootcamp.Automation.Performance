# Bootcamp.Automation.Performance

Mock HTTP de cadastro e consulta de veículos usando WireMock, com testes didáticos.

## Tecnologias
Java 11+, WireMock 3.9.1, JavaScript.

## Executar
```bash
java -jar wiremock-standalone-3.9.1.jar
```

**Pré-condições:** Mock não é benchmark de performance; ambiente e cenários reais não foram executados.

## Documentos
- [Requisitos](docs/REQUISITOS.md)
- [Arquitetura](docs/ARQUITETURA.md)
- [UML](docs/UML.puml)
- [Testes](docs/PLANO_TESTES.md)
- [Instruções para IA](AGENTS.md)

## README original preservado

## Projeto de mock da QAZANDO

Esse projeto temos como exemplo uma api de carros.

Temos algumas situações mapeadas no nosso mock que ao registrar algumas massas em específico a gente consegue um determinado valor de resposta.


## Exemplos de massas abaixo:

- Cadastro de veículo: Se o cadastro de veículo for igual a um "fusca" no parâmetro "model". = O mock tem que responder 201
- Cadastro de veículo: Se o cadastro de veículof for igual a um "up tsi" no parâmetro "model" = O mock tem que responder 500

# Como subir o mock.

- baixar o projeto
- Acessar a pasta do projeto
- Rodar o seguinte comando para subir o mock: java -jar wiremock-standalone-3.9.1.jar


OBS: Precisa ter o java instalado em sua máquina na versão 11 pra cima.

## Engenharia de software — documentação v1.0.0

[Projeto](docs/projeto/ESPECIFICACAO.md) · [UML](docs/uml/README.md) · [Testes](docs/testes/PLANO_DE_TESTES.md) · [Versões](docs/controle/VERSIONAMENTO.md)
