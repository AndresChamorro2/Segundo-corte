import os
from collections import defaultdict

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.vendidos = 0

class Restaurante:
    def __init__(self):
        self.menu = {}  # nombre -> Plato
        self.pedidos = []

    def cargar_menu_desde_txt(self, ruta):
        if not os.path.exists(ruta):
            return False
        with open(ruta, 'r', encoding='utf-8') as f:
            seccion = None
            for linea in f:
                linea = linea.strip()
                if not linea: continue
                if linea.upper().startswith('[PLATOS]'):
                    seccion = 'PLATOS'; continue
                if linea.startswith('['):
                    seccion = None; continue
                if seccion == 'PLATOS':
                    partes = [p.strip() for p in linea.split(',')]
                    if len(partes) >= 2:
                        nombre, precio = partes[0], float(partes[1])
                        self.menu[nombre] = Plato(nombre, precio)
        return True

    def registrar_pedido(self, nombre_plato, cantidad=1):
        if nombre_plato not in self.menu:
            raise ValueError('plato no existe')
        plato = self.menu[nombre_plato]
        plato.vendidos += cantidad
        total = plato.precio * cantidad
        self.pedidos.append({'plato': nombre_plato, 'cantidad': cantidad, 'total': total})
        return total

    def total_ventas(self):
        return sum(p['total'] for p in self.pedidos)

    def plato_mas_vendido(self):
        if not self.menu:
            return None
        return max(self.menu.values(), key=lambda p: p.vendidos)

def menu_restaurante():
    ruta = os.path.join(os.path.dirname(__file__), 'catalogo_inicial', 'catalogo.txt')
    r = Restaurante()
    ok = r.cargar_menu_desde_txt(ruta)
    if not ok:
        print('no se encontro catalogo en', ruta)
        return
    while True:
        print('\n=== SISTEMA RESTAURANTE ===')
        print('1. Ver menu')
        print('2. Registrar pedido')
        print('3. Ver total ventas')
        print('4. Ver plato mas vendido')
        print('5. Ejemplo predeterminado')
        print('6. Volver al menu principal')
        opc = input('Selecciona opcion (1-6): ').strip()
        if opc == '1':
            for nombre,pl in r.menu.items():
                print(nombre, '-', pl.precio)
        elif opc == '2':
            try:
                nombre = input('Nombre plato: ').strip()
                cantidad = int(input('Cantidad: '))
                total = r.registrar_pedido(nombre, cantidad)
                print('Pedido registrado. Total:', total)
            except Exception as e:
                print('Error:', e)
        elif opc == '3':
            print('Total ventas:', r.total_ventas())
        elif opc == '4':
            top = r.plato_mas_vendido()
            if top:
                print('Plato mas vendido:', top.nombre, 'ventas:', top.vendidos)
            else:
                print('Menu vacio')
        elif opc == '5':
            # ejemplo: pedir 2 del primer plato
            platos = list(r.menu.keys())
            if not platos:
                print('menu vacio')
            else:
                nombre = platos[0]
                r.registrar_pedido(nombre, 2)
                print('Ejemplo: pedido 2 x', nombre)
                print('Total ventas ahora:', r.total_ventas())
                top = r.plato_mas_vendido()
                print('Plato mas vendido ejemplo:', top.nombre, 'ventas:', top.vendidos)
        elif opc == '6':
            break
        else:
            print('Opcion invalida')

if __name__ == '__main__':
    menu_restaurante()
