import unittest
from sistema_biblioteca import Biblioteca

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.b = Biblioteca(dias_prestamo=7, multa_por_dia=1.0)
        self.b.cargar_catalogo_txt('catalogo_inicial/catalogo.txt')
        self.uid = 'UTEST'
        self.b.registrar_usuario(self.uid, 'Test User')
        self.isbn = next(iter(self.b.libros))
    def test_prestar_devolver(self):
        pid = self.b.prestar(self.isbn, self.uid)
        self.assertIn(pid, self.b.prestamos)
        res = self.b.devolver(pid)
        self.assertIn('multa', res)
    def test_moroso(self):
        pid = self.b.prestar(self.isbn, self.uid)
        # avanzar hoy para causar retraso
        self.b.hoy = self.b.hoy + __import__('datetime').timedelta(days=20)
        mor = self.b.usuarios_morosos()
        self.assertTrue(any(m[0]==self.uid for m in mor))
if __name__ == '__main__':
    unittest.main()
