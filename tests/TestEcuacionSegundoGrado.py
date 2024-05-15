import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado


class TestEcuacionSegundoGrado(unittest.TestCase):
    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()

    def tearDown(self):
        self.calculoRaices = None

    def test_calculoESG_dosNumeros_retornaSolucion(self):
        # Arrange
        a = 3
        b = -5
        c = 1
        resultoEsperadoRaiz1 = 1.43
        resultoEsperadoRaiz2 = 0.23

        # Do
        resultoActualRaiz1, resultoActualRaiz2 = self.calculoRaices.calculoESG(a, b, c)

        # Assert
        self.assertAlmostEqual(resultoEsperadoRaiz1, resultoActualRaiz1, 2)
        self.assertAlmostEqual(resultoEsperadoRaiz2, resultoActualRaiz2, 2)

    def test_calculoESG_diccionarioDosNumeros_retornaSolucion(self):
        # Arrange
        items = (
            {"Case": "Caso 01", "a": 3, "b": -5, "c": 1, "RaizEsperada1": 1.43, "RaizEsperada2": 0.23},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 1, "RaizEsperada1": -1.00, "RaizEsperada2": -1.00},
            {"Case": "Caso 03", "a": -1, "b": 2, "c": -1, "RaizEsperada1": 1.0, "RaizEsperada2": 1.00},
            {"Case": "Caso 04", "a": 1, "b": 0, "c": -18, "RaizEsperada1": 4.2, "RaizEsperada2": -4.24},
            {"Case": "Caso 05", "a": 1, "b": 4, "c": 0, "RaizEsperada1": 0.0, "RaizEsperada2": -4.00},
            {"Case": "Caso 06", "a": 1, "b": 4, "c": 4, "RaizEsperada1": -2.0, "RaizEsperada2": -2.00},
            {"Case": "Caso 07", "a": 1, "b": 3, "c": 2, "RaizEsperada1": -1.0, "RaizEsperada2": -2.00},
        )

        # Do
        #resultoActualRaiz1, resultoActualRaiz2 = self.calculoRaices.calculoESG(a, b, c)

        for item in items:
            with self.subTest(item["Case"]):
                resultadoActualRaiz1, resultadoActualRaiz2 = self.calculoRaices.calculoESG(item["a"], item["b"], item["c"])
            resultadoEsperadoRaiz1 = item["RaizEsperada1"]
            resultadoEsperadoRaiz2 = item["RaizEsperada2"]
        # Assert
        self.assertAlmostEqual(resultadoEsperadoRaiz1, resultadoActualRaiz1, 2)
        self.assertAlmostEqual(resultadoEsperadoRaiz2, resultadoActualRaiz2, 2)


if __name__ == '__main__':
    unittest.main()
