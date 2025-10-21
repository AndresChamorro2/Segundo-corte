import math

def sumar(a,b): return a + b
def restar(a,b): return a - b
def multiplicar(a,b): return a * b
def dividir(a,b):
    if b == 0:
        raise ZeroDivisionError('division por cero')
    return a / b
def potencia(a,b): return a ** b
def raiz(a, n=2):
    if a < 0 and n % 2 == 0:
        raise ValueError('raiz par de numero negativo no permitida')
    return a ** (1.0 / n)
def sin_g(deg): return math.sin(math.radians(deg))
def cos_g(deg): return math.cos(math.radians(deg))
def tan_g(deg): return math.tan(math.radians(deg))

def menu_calculadora():
    while True:
        print('\n=== CALCULADORA CIENTIFICA ===')
        print('1. Sumar')
        print('2. Restar')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Potencia')
        print('6. Raiz n-esima')
        print('7. Trigonometria (grados)')
        print('8. Ejemplo predeterminado')
        print('9. Volver al menu principal')
        opc = input('Selecciona opcion (1-9): ').strip()
        if opc == '1':
            try:
                a = float(input('Ingrese primer numero: '))
                b = float(input('Ingrese segundo numero: '))
                print('Resultado:', sumar(a,b))
            except Exception as e:
                print('Error:', e)
        elif opc == '2':
            try:
                a = float(input('Ingrese primer numero: '))
                b = float(input('Ingrese segundo numero: '))
                print('Resultado:', restar(a,b))
            except Exception as e:
                print('Error:', e)
        elif opc == '3':
            try:
                a = float(input('Ingrese primer numero: '))
                b = float(input('Ingrese segundo numero: '))
                print('Resultado:', multiplicar(a,b))
            except Exception as e:
                print('Error:', e)
        elif opc == '4':
            try:
                a = float(input('Ingrese primer numero: '))
                b = float(input('Ingrese segundo numero: '))
                print('Resultado:', dividir(a,b))
            except Exception as e:
                print('Error:', e)
        elif opc == '5':
            try:
                a = float(input('Base: '))
                b = float(input('Exponente: '))
                print('Resultado:', potencia(a,b))
            except Exception as e:
                print('Error:', e)
        elif opc == '6':
            try:
                a = float(input('Numero: '))
                n = int(input('Indice n (entero >0): '))
                print('Resultado:', raiz(a,n))
            except Exception as e:
                print('Error:', e)
        elif opc == '7':
            try:
                g = float(input('Angulo en grados: '))
                print('sin:', sin_g(g))
                print('cos:', cos_g(g))
                try:
                    print('tan:', tan_g(g))
                except Exception as e:
                    print('tan error:', e)
            except Exception as e:
                print('Error:', e)
        elif opc == '8':
            # ejemplo fijo
            print('Ejemplo: 2 + 3 * sin(45 deg)')
            print('2 + 3*sin(45) =', 2 + 3 * sin_g(45))
        elif opc == '9':
            break
        else:
            print('Opcion invalida')

if __name__ == '__main__':
    menu_calculadora()
