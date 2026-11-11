"""Verifica a documentacao; nao substitui testes do projeto."""
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

class TesteDocumentacao(unittest.TestCase):
    def test_arquivos(self):
        for nome in ["README.md", "AGENTS.md", "docs/REQUISITOS.md", "docs/ARQUITETURA.md", "docs/UML.puml", "docs/PLANO_TESTES.md"]:
            with self.subTest(nome=nome):
                self.assertTrue((BASE / nome).is_file())

    def test_uml(self):
        conteudo = (BASE / "docs/UML.puml").read_text(encoding="utf8")
        self.assertIn("@startuml", conteudo)
        self.assertIn("@enduml", conteudo)
