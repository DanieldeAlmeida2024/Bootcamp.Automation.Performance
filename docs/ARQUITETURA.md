# Arquitetura — Bootcamp.Automation.Performance

**Objetivo:** Mock HTTP de cadastro e consulta de veículos usando WireMock, com testes didáticos.

**Tecnologias:** Java 11+, WireMock 3.9.1, JavaScript.

Fluxo: entrada → validação → execução do cenário → saída/relatório. Integrações externas são dependências, não são simuladas como fatos operacionais.

Decisões: preservar stack e fontes didáticas, isolar dependências onde viável, manter documentação e testes separados de implementação, validar comportamento em ambiente real antes de publicação.

Limite: Mock não é benchmark de performance; ambiente e cenários reais não foram executados.
