import unittest
from sistema_restaurante import Restaurante

class TestRestaurante(unittest.TestCase):
    def setUp(self):
        self.r = Restaurante()
        self.r.cargar_menu_desde_txt('catalogo_inicial/catalogo.txt')
        self.platos = list(self.r.menu.keys())
    def test_pedido(self):
        if not self.platos:
            self.skipTest('menu vacio')
        nombre = self.platos[0]
        total = self.r.registrar_pedido(nombre, 2)
        self.assertEqual(total, self.r.menu[nombre].precio * 2)
        top = self.r.plato_mas_vendido()
        self.assertEqual(top.vendidos, 2)
if __name__ == '__main__':
    unittest.main()
