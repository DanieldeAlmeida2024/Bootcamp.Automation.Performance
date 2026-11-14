"""Testes de contrato HTTP contra o WireMock real e os mapeamentos do repositório."""
import json
import pathlib
import socket
import subprocess
import tempfile
import time
import unittest
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

RAIZ = pathlib.Path(__file__).resolve().parents[1]
JAR = RAIZ / "wiremock-standalone-3.9.1.jar"


def requisitar(base, metodo, caminho, dados=None):
    corpo = json.dumps(dados).encode("utf-8") if dados is not None else None
    req = Request(base + caminho, method=metodo, data=corpo,
                  headers={"Content-Type": "application/json"})
    try:
        with urlopen(req, timeout=3) as resposta:
            return resposta.status, json.loads(resposta.read())
    except HTTPError as erro:
        return erro.code, json.loads(erro.read())


class TestesContratoWireMock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not JAR.is_file():
            raise RuntimeError(f"WireMock não encontrado: {JAR}")
        cls.arquivo_log = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
        with socket.socket() as s:
            s.bind(("127.0.0.1", 0))
            porta = s.getsockname()[1]
        cls.base = f"http://127.0.0.1:{porta}"
        cls.processo = subprocess.Popen(
            ["java", "-jar", str(JAR), "--port", str(porta),
             "--root-dir", str(RAIZ), "--bind-address", "127.0.0.1"],
            stdout=cls.arquivo_log, stderr=subprocess.STDOUT, cwd=str(RAIZ),
        )
        try:
            for _ in range(100):
                if cls.processo.poll() is not None:
                    raise RuntimeError(f"WireMock encerrou com código {cls.processo.returncode}.")
                try:
                    codigo, _ = requisitar(cls.base, "GET", "/api/cars")
                    if codigo == 200:
                        break
                except (URLError, TimeoutError, ValueError):
                    pass
                time.sleep(0.2)
            else:
                raise RuntimeError("WireMock não iniciou na porta local em até 20 segundos.")
        except Exception:
            cls.processo.terminate()
            cls.processo.wait(timeout=5)
            cls.arquivo_log.seek(0)
            print(cls.arquivo_log.read()[-3000:])
            cls.arquivo_log.close()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.processo.terminate()
        try:
            cls.processo.wait(timeout=5)
        except subprocess.TimeoutExpired:
            cls.processo.kill()
            cls.processo.wait(timeout=5)
        cls.arquivo_log.close()

    def test_consulta_retorna_cinco_veiculos(self):
        status, corpo = requisitar(self.base, "GET", "/api/cars")
        self.assertEqual(200, status)
        self.assertEqual(5, len(corpo))
        self.assertEqual(("Toyota", "Corolla"), (corpo[0]["brand"], corpo[0]["model"]))
        self.assertEqual(("BMW", "M3"), (corpo[-1]["brand"], corpo[-1]["model"]))

    def test_fusca_retorna_cadastro_ficticio(self):
        status, corpo = requisitar(self.base, "POST", "/api/cars",
                                  {"brand": "Volkswagen", "model": "fusca", "year": 1965})
        self.assertEqual(201, status)
        self.assertEqual("Car successfully registered!", corpo["message"])
        self.assertEqual(6, corpo["carId"])

    def test_up_tsi_retorna_erro_simulado(self):
        status, corpo = requisitar(self.base, "POST", "/api/cars",
                                  {"brand": "Volkswagen", "model": "up tsi", "year": 2020})
        self.assertEqual(500, status)
        self.assertIn("model 'up tsi' is not allowed", corpo["message"])

    def test_modelo_nao_mapeado_retorna_404(self):
        status, corpo = requisitar(self.base, "POST", "/api/cars",
                                  {"brand": "Volkswagen", "model": "jetta", "year": 2022})
        self.assertEqual(404, status)
        self.assertEqual("Vehicle not found.", corpo["message"])

    def test_post_nao_persiste_mudancas_no_mock(self):
        requisitar(self.base, "POST", "/api/cars",
                   {"brand": "Volkswagen", "model": "fusca", "year": 1965})
        status, corpo = requisitar(self.base, "GET", "/api/cars")
        self.assertEqual(200, status)
        self.assertEqual(5, len(corpo))


if __name__ == "__main__":
    unittest.main()
