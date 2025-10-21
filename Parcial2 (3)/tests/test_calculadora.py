import unittest
from calculadora_cientifica import sumar, restar, multiplicar, dividir, potencia, raiz, sin_g

class TestCalculadora(unittest.TestCase):
    def test_basicas(self):
        self.assertEqual(sumar(2,3), 5)
        self.assertEqual(restar(5,2), 3)
        self.assertEqual(multiplicar(3,4), 12)
        self.assertAlmostEqual(dividir(10,4), 2.5)
    def test_pot_raiz(self):
        self.assertEqual(potencia(2,3), 8)
        self.assertAlmostEqual(raiz(9), 3)
    def test_trig(self):
        self.assertAlmostEqual(round(sin_g(30),5), 0.5)
if __name__ == '__main__':
    unittest.main()
