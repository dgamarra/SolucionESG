import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):
    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()

    def tearDown(self):
        self.calculoRaices = None
    def test_calculoESG_dosNumeros_retornaSolucion(self):
        # Arrange
        a= 1
        b= 2
        c= 1
        resultoEsperadoRaiz1 = -1
        resultoEsperadoRaiz2 = -1

        # Do
        resultoActualRaiz1, resultoActualRaiz2 = self.calculoRaices.calculoESG(a,b,c)

        # Assert
        self.assertEqual(resultoEsperadoRaiz1, resultoActualRaiz1)
        self.assertEqual(resultoEsperadoRaiz2, resultoActualRaiz2)


if __name__ == '__main__':
    unittest.main()
