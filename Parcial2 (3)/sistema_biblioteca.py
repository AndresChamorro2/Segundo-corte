from datetime import datetime, timedelta
from collections import defaultdict
import os

class Libro:
    def __init__(self, titulo, autor, copias=1):
        self.titulo = titulo
        self.autor = autor
        self.copias_total = copias
        self.copias_disponibles = copias

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.prestamos_activos = []  # lista de ids de prestamo
        self.historial = []  # lista de ids de prestamo

class Biblioteca:
    def __init__(self, dias_prestamo=14, multa_por_dia=1.0, limite_prestamos=3):
        self.libros = {}  # isbn -> Libro
        self.usuarios = {}  # id -> Usuario
        self.prestamos = {}  # id_prestamo -> dict
        self.conteo_prestamos = defaultdict(int)
        self.dias_prestamo = dias_prestamo
        self.multa_por_dia = multa_por_dia
        self.limite_prestamos = limite_prestamos
        self.hoy = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)

    def cargar_catalogo_txt(self, ruta):
        if not os.path.exists(ruta):
            return False
        with open(ruta, 'r', encoding='utf-8') as f:
            seccion = None
            for linea in f:
                linea = linea.strip()
                if not linea: continue
                if linea.upper().startswith('[LIBROS]'):
                    seccion = 'LIBROS'; continue
                if linea.startswith('['):
                    seccion = None; continue
                if seccion == 'LIBROS':
                    partes = [p.strip() for p in linea.split(',')]
                    if len(partes) >= 3:
                        titulo, autor, copias = partes[0], partes[1], int(partes[2])
                        isbn = str(abs(hash(titulo)))[:13]
                        self.libros[isbn] = Libro(titulo, autor, copias)
        return True

    def listar_libros_disponibles(self):
        return [(isbn, l.titulo, l.autor, l.copias_disponibles) for isbn,l in self.libros.items()]

    def registrar_usuario(self, id_usuario, nombre):
        if id_usuario in self.usuarios:
            raise ValueError('usuario ya registrado')
        self.usuarios[id_usuario] = Usuario(id_usuario, nombre)

    def prestar(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            raise ValueError('usuario no registrado')
        if isbn not in self.libros:
            raise ValueError('isbn no existe')
        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        if libro.copias_disponibles <= 0:
            raise ValueError('no hay copias disponibles')
        if len(usuario.prestamos_activos) >= self.limite_prestamos:
            raise ValueError('limite de prestamos excedido')
        id_prestamo = str(len(self.prestamos)+1)
        fecha_prestamo = self.hoy
        fecha_venc = fecha_prestamo + timedelta(days=self.dias_prestamo)
        self.prestamos[id_prestamo] = {
            'id_prestamo': id_prestamo,
            'isbn': isbn,
            'id_usuario': id_usuario,
            'fecha_prestamo': fecha_prestamo,
            'fecha_vencimiento': fecha_venc,
            'fecha_devolucion': None,
            'multa': 0.0,
            'multa_pagada': False
        }
        libro.copias_disponibles -= 1
        usuario.prestamos_activos.append(id_prestamo)
        usuario.historial.append(id_prestamo)
        self.conteo_prestamos[isbn] += 1
        return id_prestamo

    def devolver(self, id_prestamo, fecha_devolucion=None):
        if id_prestamo not in self.prestamos:
            raise ValueError('prestamo inexistente')
        prest = self.prestamos[id_prestamo]
        if prest['fecha_devolucion']:
            raise ValueError('ya devuelto')
        fecha_dev = fecha_devolucion or self.hoy
        dias_retraso = (fecha_dev - prest['fecha_vencimiento']).days
        multa = 0.0
        if dias_retraso > 0:
            multa = dias_retraso * self.multa_por_dia
        prest['fecha_devolucion'] = fecha_dev
        prest['multa'] = round(multa,2)
        isbn = prest['isbn']
        self.libros[isbn].copias_disponibles += 1
        uid = prest['id_usuario']
        if id_prestamo in self.usuarios[uid].prestamos_activos:
            self.usuarios[uid].prestamos_activos.remove(id_prestamo)
        return {'dias_retraso': dias_retraso, 'multa': multa}

    def usuarios_morosos(self):
        morosos = []
        for uid, u in self.usuarios.items():
            deuda = 0.0
            for pid in u.historial:
                p = self.prestamos.get(pid)
                if p:
                    if p.get('fecha_devolucion') and p.get('multa',0)>0 and not p.get('multa_pagada',False):
                        deuda += p['multa']
                    elif not p.get('fecha_devolucion'):
                        dias = (self.hoy - p['fecha_vencimiento']).days
                        if dias>0:
                            deuda += dias * self.multa_por_dia
            if deuda>0:
                morosos.append((uid, u.nombre, round(deuda,2)))
        return morosos

def menu_biblioteca():
    ruta = os.path.join(os.path.dirname(__file__), 'catalogo_inicial', 'catalogo.txt')
    b = Biblioteca(dias_prestamo=7, multa_por_dia=2.0)
    ok = b.cargar_catalogo_txt(ruta)
    if not ok:
        print('no se encontro catalogo en', ruta)
        return
    # registrar usuarios de ejemplo
    try:
        b.registrar_usuario('U001','Ana')
        b.registrar_usuario('U002','Carlos')
    except Exception:
        pass

    while True:
        print('\n=== SISTEMA BIBLIOTECA ===')
        print('1. Listar libros disponibles')
        print('2. Prestar libro')
        print('3. Devolver libro')
        print('4. Ver usuarios morosos')
        print('5. Ejemplo predeterminado')
        print('6. Volver al menu principal')
        opc = input('Selecciona opcion (1-6): ').strip()
        if opc == '1':
            for isbn,titulo,autor,cop in b.listar_libros_disponibles():
                print(isbn, '-', titulo, '-', autor, '- copias:', cop)
        elif opc == '2':
            try:
                isbn = input('Ingrese ISBN (puede obtenerlo de la lista): ').strip()
                uid = input('ID usuario: ').strip()
                pid = b.prestar(isbn, uid)
                print('Prestamo registrado id:', pid)
            except Exception as e:
                print('Error:', e)
        elif opc == '3':
            try:
                pid = input('ID prestamo: ').strip()
                res = b.devolver(pid)
                print('Devolucion procesada:', res)
            except Exception as e:
                print('Error:', e)
        elif opc == '4':
            mor = b.usuarios_morosos()
            if not mor:
                print('No hay morosos')
            else:
                for uid,nombre,deuda in mor:
                    print(uid, nombre, 'deuda:', deuda)
        elif opc == '5':
            # ejemplo: prestar y devolver con retraso
            isbn = next(iter(b.libros))
            try:
                pid = b.prestar(isbn, 'U001')
                print('Prestado id:', pid, 'titulo:', b.libros[isbn].titulo)
                # adelantar hoy para forzar retraso
                b.hoy = b.hoy + timedelta(days=10)
                res = b.devolver(pid)
                print('Devolucion ejemplo:', res)
            except Exception as e:
                print('Error ejemplo:', e)
        elif opc == '6':
            break
        else:
            print('Opcion invalida')

if __name__ == '__main__':
    menu_biblioteca()
