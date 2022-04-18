import unittest
from src.logica.TingoTango import TingoTango

class TingoTangoPrueba(unittest.TestCase):
    def setUp(self):
        self.TT = TingoTango()
    def tearDown(self):
        self.TT = TingoTango()
    def test_TingoTango_MultiploTres_retornaTingo(self):
        # Arranque
            self.numero1 = 3
            self.resultadoEsperado = "Tingo"
        # Do
            self.resultadoActual = self.TT.textoTingoTango(self.numero1)
        # Assert
            self.assertEqual(self.resultadoEsperado,self.resultadoActual)

    def test_TingoTango_MultiploCinco_retornaTango(self):
        # Arranque
            self.numero1 = 5
            self.resultadoEsperado = "Tango"
        # Do
            self.resultadoActual = self.TT.textoTingoTango(self.numero1)
        # Assert
            self.assertEqual(self.resultadoEsperado,self.resultadoActual)

    def test_TingoTango_MultiploQuince_retornaTingoTango(self):
        # Arranque
            self.numero1 = 15
            self.resultadoEsperado = "TingoTango"
        # Do
            self.resultadoActual = self.TT.textoTingoTango(self.numero1)
        # Assert
            self.assertEqual(self.resultadoEsperado,self.resultadoActual)

    def test_TingoTango_otroNumero_retornaNumero(self):
        # Arranque
            self.numero1 = 7
            self.resultadoEsperado = "7"
        # Do
            self.resultadoActual = self.TT.textoTingoTango(self.numero1)
        # Assert
            self.assertEqual(self.resultadoEsperado,self.resultadoActual)