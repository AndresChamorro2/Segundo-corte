import subprocess, sys, os

def ejecutar_script(nombre):
    ruta = os.path.join(os.path.dirname(__file__), nombre)
    subprocess.run([sys.executable, ruta])

def menu_principal():
    while True:
        print('\n=== PARCIAL 2 ===')
        print('1. Calculadora cientifica')
        print('2. Sistema biblioteca')
        print('3. Sistema restaurante')
        print('4. Salir')
        opc = input('Selecciona opcion (1-4): ').strip()
        if opc == '1':
            ejecutar_script('calculadora_cientifica.py')
        elif opc == '2':
            ejecutar_script('sistema_biblioteca.py')
        elif opc == '3':
            ejecutar_script('sistema_restaurante.py')
        elif opc == '4':
            print('Saliendo...'); break
        else:
            print('Opcion invalida')

if __name__ == '__main__':
    menu_principal()
