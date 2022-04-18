import unittest
from src.logica.TingoTango import TingoTango

class TingoTangoPrueba(unittest.TestCase):
    def setUp(self):
        self.TT = TingoTango()
    def tearDown(self):
        self.TT = TingoTango()
    def test_TingoTango_MultipleTres_retornaTingo(self):
        # Arranque
            self.numero1 = 3
            self.resultadoEsperado = "Tingo"
        # Do
            self.resultadoActual = self.TT.textoTingoTango(self.numero1)
        # Assert
            self.assertEqual(self.resultadoEsperado,self.resultadoActual)