import unittest
import math
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado
class PruebaEcuacionSegundoGrado(unittest.TestCase):
    def test_ecuacionSegundoGrado_parametrosNumericos_raicesReales(self):
        # arrange
        a = 3
        b = -5
        c = 1
        x1Esperado = 1.43
        x2Esperado = 0.23

        # Do
        ecuacion = EcuacionSegundoGrado()
        x1Actual, x2Actual = ecuacion.calculoECS(a, b, c)


        # Assert
        precision = math.fabs(x1Esperado - x1Actual)
        self.assertLessEqual(precision,0.01)
        precision = math.fabs(x2Esperado - x2Actual)
        self.assertLessEqual(precision, 0.01)

    def test_ecuacionSegundoGrado_parametrosNumericosMultiple_raicesReales(self):
        # arragbe
        ecuacion = EcuacionSegundoGrado()
        items = (
            {"Case": "Caso 01", "a": 3, "b": -5, "c": 1, "RaizEsperada1": 1.43, "RaizEsperada2": 0.23},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 1, "RaizEsperada1": -1.00, "RaizEsperada2": -1.00},
            {"Case": "Caso 03", "a": -1, "b": 2, "c": -1, "RaizEsperada1": 1.0, "RaizEsperada2": 1.00},
            {"Case": "Caso 04", "a": 1, "b": 0, "c": -18, "RaizEsperada1": 4.2, "RaizEsperada2": -4.24},
            {"Case": "Caso 05", "a": 1, "b": 4, "c": 0, "RaizEsperada1": 0.0, "RaizEsperada2": -4.00},
            {"Case": "Caso 06", "a": 1, "b": 4, "c": 4, "RaizEsperada1": -2.0, "RaizEsperada2": -2.00},
            {"Case": "Caso 07", "a": 1, "b": 3, "c": 2, "RaizEsperada1": -1.0, "RaizEsperada2": -2.00},
        )

        # do
        for item in items:
            with self.subTest(item["Case"]):
                RaizActual1, RaizActual2 = ecuacion.calculoECS(item["a"], item["b"], item["c"])

        # assert
        precision = math.fabs(item["RaizEsperada1"] - RaizActual1)
        self.assertLessEqual(precision, 0.01)
        precision = math.fabs(item["RaizEsperada2"] - RaizActual2)
        self.assertLessEqual(precision, 0.01)
