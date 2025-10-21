#!/usr/bin/env python3
"""
EJERCICIOS PARA ESTUDIANTES - ESTRUCTURAS DE CONTROL
Completa los siguientes ejercicios mientras exploramos los conceptos confusos.
"""

def ejercicio_1():
    """
    Problema: El siguiente código debería imprimir solo los números impares,
    pero tiene un error porque modifica la lista mientras la recorre.
    Corrígelo para que funcione correctamente.
    """
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Código original con error
    print("Código original (con error):")
    print("numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
    print("for num in numeros:")
    print("    if num % 2 == 0:  # Si es par")
    print("        numeros.remove(num)")
    print("print(numeros)")
    
    print("\nResultado esperado: [1, 3, 5, 7, 9]")
    
    # Tu corrección
    print("\nTu solución:")
    # La solución es iterar sobre una copia de la lista (numeros[:])
    # o crear una nueva lista con los elementos deseados (como en el ejemplo 5)
    
    # Opción 1: Iterar sobre una copia (si queremos modificar la lista original 'in-place')
    # Sin embargo, la forma más Pythonica y segura es crear una nueva lista de impares.
    
    # Opción 2: Usar una comprensión de lista para obtener solo los impares
    numeros_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    impares = [num for num in numeros_original if num % 2 != 0]
    print(impares)

    # Nota: Si el objetivo *era* modificar la lista original, se podría hacer:
    # for num in numeros[:]: # Iterar sobre una COPIA para modificar la original
    #     if num % 2 == 0:
    #         numeros.remove(num)
    # print(numeros) # Si se usa esta opción, se debe redefinir 'numeros' al inicio.
    
    return "¡Ejercicio 1 completado!"

# --------------------------------------------------

def ejercicio_2():
    """
    Problema: Completa el código para generar una tabla de multiplicar
    del 1 al 10 usando bucles anidados.
    """
    print("Tabla de multiplicar del 1 al 10:")
    
    # Completa el código aquí
    # Bucle externo para el multiplicador (de 1 a 10)
    for i in range(1, 11):
        # Bucle interno para el factor (de 1 a 10)
        linea = ""
        for j in range(1, 11):
            producto = i * j
            # Formatear la salida para que se vea como tabla
            linea += f"{producto:3}" # :3 asegura 3 espacios para cada número
        print(f"Fila {i}: {linea}")
    
    return "¡Ejercicio 2 completado!"

# --------------------------------------------------

def ejercicio_3():
    """
    Problema: El siguiente bucle while debería imprimir los números del 1 al 5,
    pero tiene un problema que lo convierte en infinito. Corrígelo.
    """
    print("Bucle while para imprimir números del 1 al 5:")
    
    # Código original con error
    print("Código original (con error):")
    print("contador = 1")
    print("while contador <= 5:")
    print('    print(f"Número: {contador}")')
    print("    # Falta algo aquí")
    
    # Tu corrección
    print("\nTu solución:")
    # El bucle es infinito porque la variable de control (contador) no se actualiza.
    # Se debe incrementar el contador dentro del bucle.
    contador = 1
    while contador <= 5:
        print(f"Número: {contador}")
        # Corrección: Incrementar la variable de control
        contador += 1
    
    return "¡Ejercicio 3 completado!"

# --------------------------------------------------

def ejercicio_4():
    """
    Problema: Usa break y continue adecuadamente para procesar la siguiente lista
    de números: imprime cada número, pero salta los negativos y detén el proceso
    al encontrar un cero.
    """
    numeros = [5, -2, 10, 8, -3, 0, 7, 9]
    
    print(f"Lista de números: {numeros}")
    print("Resultado esperado: Imprime solo positivos y termina al encontrar 0")
    
    # Completa el código aquí
    print("\nProcesando:")
    for num in numeros:
        if num == 0:
            print("¡Cero encontrado! Deteniendo el proceso (usando break).")
            # Detiene completamente el bucle
            break
        
        if num < 0:
            print(f"Saltando número negativo: {num} (usando continue).")
            # Pasa a la siguiente iteración del bucle
            continue
        
        # Este código solo se ejecuta si num no es 0 (termina) y no es negativo (continúa)
        print(f"Número positivo: {num}")
        
    return "¡Ejercicio 4 completado!"

# --------------------------------------------------

def ejercicio_5():
    """
    Problema: Reescribe el siguiente código utilizando una comprensión de lista.
    """
    print("Código original:")
    print("cuadrados_pares = []")
    print("for numero in range(1, 11):")
    print("    if numero % 2 == 0:")
    print("        cuadrados_pares.append(numero ** 2)")
    print("print(cuadrados_pares)")
    
    # Versión con bucle tradicional para comparar
    cuadrados_pares_tradicional = []
    for numero in range(1, 11):
        if numero % 2 == 0:
            cuadrados_pares_tradicional.append(numero ** 2)
    print(f"\nResultado con bucle tradicional: {cuadrados_pares_tradicional}")
    
    # Tu solución con comprensión de lista
    print("\nTu solución con comprensión de lista:")
    # La sintaxis es: [expresion for elemento in iterable if condicion]
    cuadrados_pares_comprension = [numero ** 2 for numero in range(1, 11) if numero % 2 == 0]
    print(cuadrados_pares_comprension)
    
    return "¡Ejercicio 5 completado!"

# --------------------------------------------------

def ejercicio_6():
    """
    Problema: Usa bucles anidados para encontrar todas las combinaciones
    posibles de dos listas. Luego implementa el mismo resultado usando
    comprensión de listas.
    """
    colores = ["rojo", "azul", "verde"]
    tamaños = ["pequeño", "mediano", "grande"]
    
    print(f"Colores: {colores}")
    print(f"Tamaños: {tamaños}")
    print("Combinaciones esperadas: [('rojo', 'pequeño'), ('rojo', 'mediano'), ...]")
    
    # --------------------------------------------------
    print("\n1. Solución con bucles anidados:")
    # Completa el código aquí
    combinaciones_bucle = []
    for color in colores:
        for tamaño in tamaños:
            # Crea una tupla y la añade a la lista
            combinaciones_bucle.append((color, tamaño)) 
    print(combinaciones_bucle)
    
    # --------------------------------------------------
    print("\n2. Solución con comprensión de listas:")
    # Completa el código aquí
    # La sintaxis es: [expresion for elemento1 in iterable1 for elemento2 in iterable2]
    combinaciones_comprension = [(color, tamaño) for color in colores for tamaño in tamaños]
    print(combinaciones_comprension)
    
    return "¡Ejercicio 6 completado!"

# --------------------------------------------------

def menu():
    """
    Muestra un menú para seleccionar qué ejercicio ejecutar.
    """
    print("\n" + "=" * 50)
    print("EJERCICIOS DE ESTRUCTURAS DE CONTROL".center(50))
    print("=" * 50)
    
    print("\nSelecciona un ejercicio:")
    print("1. Corregir iteración y modificación de lista")
    print("2. Tabla de multiplicar con bucles anidados")
    print("3. Corregir bucle while infinito")
    print("4. Uso de break y continue")
    print("5. Convertir bucle a comprensión de lista")
    print("6. Combinaciones con bucles anidados")
    print("0. Salir")
    
    try:
        opcion = int(input("\nIngresa el número del ejercicio (0-6): "))
        return opcion
    except ValueError:
        print("Entrada inválida. Ingresa un número del 0 al 6.")
        return -1

def main():
    """
    Función principal para ejecutar los ejercicios.
    """
    while True:
        opcion = menu()
        
        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            ejercicio_3()
        elif opcion == 4:
            ejercicio_4()
        elif opcion == 5:
            ejercicio_5()
        elif opcion == 6:
            ejercicio_6()
        else:
            print("Opción inválida. Intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()

######PARTE 2
#!/usr/bin/env python3
"""
ESTRUCTURAS DE CONTROL CONFUSAS - Versión Interactiva y Resuelta

Este script resuelve y demuestra los conceptos de estructuras de control,
incluyendo correcciones a errores comunes.
"""
import os

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter(mensaje="Presiona Enter para continuar..."):
    """Espera a que el usuario presione Enter"""
    input(f"\n{mensaje}")

def mostrar_titulo(texto):
    """Muestra un título formateado"""
    print("\n" + "=" * 70)
    print(texto.center(70))
    print("=" * 70 + "\n")

def mostrar_seccion(texto):
    """Muestra un encabezado de sección"""
    print("\n" + "-" * 50)
    print(texto)
    print("-" * 50)

# ===========================================================================
# INICIO DEL PROGRAMA PRINCIPAL
# ===========================================================================
def main_interactivo_resuelto():
    limpiar_pantalla()
    mostrar_titulo("ESTRUCTURAS DE CONTROL EN PYTHON - Sesión Interactiva Resuelta ✅")

    print("¡Bienvenidos! A continuación, se ejecutan las demostraciones y correcciones.")
    esperar_enter()

    # ===========================================================================
    # Ejercicio 1: Modificación de una lista mientras se itera
    # ===========================================================================
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 1: MODIFICACIÓN DURANTE ITERACIÓN (CORRECCIÓN)")

    mostrar_seccion("❌ Código original con error (Demostración):")
    numeros_error = [1, 2, 3, 4, 5]
    print(f"Lista original: {numeros_error}")
    for numero in numeros_error:
        if numero % 2 == 0:
            numeros_error.remove(numero)
    print(f"Resultado incorrecto: {numeros_error}") # Se obtiene [1, 3, 5], el 4 se salva.

    mostrar_seccion("✅ Solución Correcta (Comprensión de lista):")
    numeros_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # La solución más Pythónica: crear una nueva lista con los elementos deseados.
    numeros_filtrados = [num for num in numeros_original if num % 2 != 0]
    print(f"Lista filtrada de impares: {numeros_filtrados}")
    print("\nReflexión: No modificar una colección mientras se itera sobre ella.")
    esperar_enter()

    # ===========================================================================
    # Ejercicio 2: Confusión con range()
    # ===========================================================================
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 2: RANGES CORRECTOS (DEL 1 AL 10)")

    mostrar_seccion("❌ Ejemplo range(1, 10):")
    print("Imprime del 1 al 9 (excluye el 10): ", end="")
    for i in range(1, 10):
        print(i, end=" ")

    mostrar_seccion("\n✅ Solución Correcta (range(1, 11)):")
    print("Imprime del 1 al 10 (incluye el 10): ", end="")
    for i in range(1, 11): # El valor final debe ser 11 para incluir el 10.
        print(i, end=" ")
    print()
    esperar_enter()

    # ===========================================================================
    # Ejercicio 3: Bucle while infinito (Corregido)
    # ===========================================================================
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 3: BUCLE WHILE CORREGIDO")

    mostrar_seccion("❌ Problema: Bucle infinito (no ejecutado por seguridad)")
    print("El código original no actualizaba el contador (`contador += 1`), causando un bucle infinito.")

    mostrar_seccion("\n✅ Solución Correcta:")
    contador = 1
    while contador <= 5:
        print(f"Contador: {contador}")
        contador += 1  # La corrección clave: incrementar la variable de control.
    
    print("Reflexión: En bucles `while`, la condición de salida debe actualizarse.")
    esperar_enter()

    # ===========================================================================
    # Ejercicio 4: Confusión con break vs. continue
    # ===========================================================================
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 4: BREAK Y CONTINUE")

    numeros_proc = [5, -2, 10, 8, -3, 0, 7, 9]
    print(f"Lista de números: {numeros_proc}")
    mostrar_seccion("✅ Solución con break y continue:")
    print("Resultado: Imprime solo positivos, saltando negativos y terminando en 0.")
    
    for num in numeros_proc:
        if num == 0:
            print(f"¡Cero encontrado! Deteniendo el proceso (usando break).")
            # Detiene completamente el bucle for
            break
        
        if num < 0:
            print(f"Saltando número negativo: {num} (usando continue).")
            # Salta a la siguiente iteración
            continue
        
        # Solo se llega aquí si el número es positivo
        print(f"Procesando número positivo: {num}")

    esperar_enter()
    
    # ===========================================================================
    # Ejercicio 5: Bucles anidados y break (Salida elegante)
    # ===========================================================================
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 5: BUCLES ANIDADOS Y SALIDA ELEGANTEMENTE")

    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    objetivo = 6

    mostrar_seccion("❌ Problema: Un 'break' interno no sale del bucle externo.")
    print("El código original seguiría procesando filas después de encontrar el 6.")

    mostrar_seccion("\n✅ Solución Correcta (Usando bandera 'encontrado'):")
    encontrado = False

    for fila in matriz:
        for elemento in fila:
            print(f"Verificando: {elemento}")
            if elemento == objetivo:
                print(f"¡Objetivo {objetivo} encontrado!")
                encontrado = True
                break  # Sale del bucle interno
        
        if encontrado:
            print("Saliendo del bucle externo (gracias a la bandera).")
            break  # Sale del bucle externo

    print(f"Búsqueda terminada. Estado final: {encontrado}")
    esperar_enter()

    # ===========================================================================
    # Ejercicio 6: Comprensiones de lista vs bucles tradicionales
    # ===========================================================================
    limpiar_pantalla()
    mostrar_titulo("EJERCICIO 6: COMPRENSIÓN DE LISTA Y BUCLES ANIDADOS")

    colores = ["rojo", "azul", "verde"]
    tamaños = ["pequeño", "mediano", "grande"]
    
    mostrar_seccion("1. Combinaciones con bucles anidados:")
    combinaciones_bucle = []
    for color in colores:
        for tamaño in tamaños:
            combinaciones_bucle.append((color, tamaño)) 
    print(combinaciones_bucle)
    
    mostrar_seccion("\n2. Combinaciones con comprensión de listas:")
    # Solución de dos bucles anidados en una comprensión de lista.
    combinaciones_comprension = [(color, tamaño) for color in colores for tamaño in tamaños]
    print(combinaciones_comprension)
    
    print("\nReflexión: Las comprensiones son más concisas para crear nuevas colecciones.")
    esperar_enter()

    # ===========================================================================
    # Cierre
    # ===========================================================================
    limpiar_pantalla()
    mostrar_titulo("¡ESTRUCTURAS DE CONTROL RESUELTAS!")
    print("Todos los ejercicios y demostraciones han sido completados.")
    print("Este código es la solución final y funcional.")

if __name__ == "__main__":
    main_interactivo_resuelto()
