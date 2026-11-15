"""Contrato dos scripts de k6: erros previstos não são falhas de transporte."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ContratoErrosEsperadosK6(unittest.TestCase):
    def test_404_e_500_possuem_resposta_esperada_e_threshold(self):
        for codigo in (404, 500):
            with self.subTest(codigo=codigo):
                codigo_js = (ROOT / "tests" / f"test-{codigo}.js").read_text(encoding="utf-8")
                self.assertIn(f"http.setResponseCallback(http.expectedStatuses({codigo}))", codigo_js)
                self.assertIn("http_req_failed: ['rate<0.01']", codigo_js)
                self.assertIn("checks: ['rate>0.99']", codigo_js)
                self.assertIn(f"r.status === {codigo}", codigo_js)

    def test_live_continua_recusando_status_erro(self):
        live = (ROOT / "tests" / "live.js").read_text(encoding="utf-8")
        self.assertNotIn("http.setResponseCallback(http.expectedStatuses(500))", live)
        self.assertIn("http_req_failed: ['rate<0.01']", live)


if __name__ == "__main__":
    unittest.main()
