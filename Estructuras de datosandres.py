#!/usr/bin/env python3
"""
EJERCICIOS PARA ESTUDIANTES - ESTRUCTURAS CONDICIONALES
Completa los siguientes ejercicios mientras exploramos los conceptos confusos.
"""

def ejercicio_1():
    """
    Completa este código para que evalúe correctamente si un número es:
    - Positivo (mayor que 0)
    - Negativo (menor que 0)
    - Cero
    """
    try:
        numero = int(input("Introduce un número entero: "))
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
        return

    # Completa el código aquí
    if numero > 0:
        print(f"El número {numero} es Positivo.")
    elif numero < 0:
        print(f"El número {numero} es Negativo.")
    else: # Por descarte, si no es positivo ni negativo, es cero.
        print(f"El número {numero} es Cero.")

    return "¡Ejercicio 1 completado!"

def ejercicio_2():
    """
    El siguiente código contiene errores en las condiciones.
    Encuentra y corrige los errores.
    """
    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
        return

    # Código original con errores:
    # 1. 'if edad = 18:' usa el operador de asignación (=) en lugar del de comparación (==).
    # 2. 'elif edad < 18' le falta el signo de dos puntos (:) al final de la línea.
    
    # Corrige el código aquí
    if edad == 18:
        print("Tienes exactamente 18 años")
    elif edad < 18: # Corrección: añadir ':'
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")
    
    return "¡Ejercicio 2 completado!"

def ejercicio_3():
    """
    Reescribe este código condicional anidado usando operadores lógicos (and, or)
    para hacerlo más legible.
    """
    llueve = input("¿Está lloviendo? (s/n): ").lower() == "s"
    frio = input("¿Hace frío? (s/n): ").lower() == "s"
    
    # Código original anidado (para referencia)
    print("Versión original anidada:")
    if llueve:
        if frio:
            print("Lleva paraguas y abrigo")
        else:
            print("Lleva paraguas")
    else:
        if frio:
            print("Lleva abrigo")
        else:
            print("Disfruta el día")
    
    # Tu versión mejorada usando operadores lógicos
    print("\nTu versión mejorada:")
    # Completa el código aquí
    if llueve and frio:
        print("Lleva paraguas y abrigo")
    elif llueve: # Si llueve Y NO hace frío
        print("Lleva paraguas")
    elif frio: # Si NO llueve Y SÍ hace frío
        print("Lleva abrigo")
    else: # Si NO llueve Y NO hace frío
        print("Disfruta el día")
    
    return "¡Ejercicio 3 completado!"

def ejercicio_4():
    """
    Corrige el orden de las condiciones para que funcione correctamente.
    Queremos mostrar el nivel de alerta según la temperatura:
    - Peligro extremo: más de 40°C
    - Alerta alta: entre 30°C y 40°C
    - Precaución: entre 25°C y 30°C
    - Normal: menos de 25°C
    """
    try:
        temperatura = float(input("Introduce la temperatura actual: "))
    except ValueError:
        print("Entrada inválida. Debe ser un número.")
        return

    # Este código tiene el orden incorrecto de condiciones
    print("Código original (incorrecto):")
    # El problema es que `temperatura > 25` es verdadero para 35, 45, etc.,
    # por lo que las condiciones más específicas nunca se evalúan.
    if temperatura > 25:
        print("Nivel: Precaución")
    elif temperatura > 30:
        print("Nivel: Alerta alta")
    elif temperatura > 40:
        print("Nivel: Peligro extremo")
    else:
        print("Nivel: Normal")
    
    # Corrige el orden de las condiciones
    # La solución es evaluar de la condición más ESTRICTA a la menos estricta
    print("\nTu versión corregida:")
    if temperatura > 40:
        print("Nivel: Peligro extremo")
    elif temperatura > 30: # Implica que es > 30 y <= 40
        print("Nivel: Alerta alta")
    elif temperatura > 25: # Implica que es > 25 y <= 30
        print("Nivel: Precaución")
    else: # Implica que es <= 25
        print("Nivel: Normal")
    
    return "¡Ejercicio 4 completado!"

def ejercicio_5():
    """
    Simplifica los siguientes condicionales usando el operador ternario.
    """
    try:
        puntuacion = int(input("Introduce tu puntuación (0-100): "))
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
        return
    
    # Versión con if-else
    print("Versión con if-else:")
    if puntuacion >= 60:
        resultado_if_else = "Aprobado"
    else:
        resultado_if_else = "Suspenso"
    print(resultado_if_else)
    
    # Tu versión con operador ternario
    # La sintaxis es: [valor_si_verdadero] if [condición] else [valor_si_falso]
    print("\nTu versión con operador ternario:")
    resultado_ternario = "Aprobado" if puntuacion >= 60 else "Suspenso"
    print(resultado_ternario)
    
    return "¡Ejercicio 5 completado!"

def ejercicio_6():
    """
    Crea una función que determine si un año es bisiesto.
    Un año es bisiesto si:
    - Es divisible por 4
    - No es divisible por 100, a menos que también sea divisible por 400
    """
    try:
        año = int(input("Introduce un año: "))
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
        return
    
    # Completa esta función
    def es_bisiesto(año):
        # Es divisible por 4 Y (no divisible por 100 O divisible por 400)
        return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
    
    if es_bisiesto(año):
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")
    
    return "¡Ejercicio 6 completado!"

def menu():
    """
    Muestra un menú para seleccionar qué ejercicio ejecutar.
    """
    print("\n" + "=" * 50)
    print("EJERCICIOS DE ESTRUCTURAS CONDICIONALES".center(50))
    print("=" * 50)
    
    print("\nSelecciona un ejercicio:")
    print("1. Evaluar si un número es positivo, negativo o cero")
    print("2. Corregir errores en condiciones")
    print("3. Simplificar condicionales anidados")
    print("4. Corregir orden de condiciones")
    print("5. Usar operador ternario")
    print("6. Determinar si un año es bisiesto")
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

####PARTE 2
#!/usr/bin/env python3
"""
EJERCICIOS RESUELTOS - ESTRUCTURAS DE CONTROL Y CONDICIONALES
Este script contiene las soluciones a todos los ejercicios propuestos.
"""
import os
import sys

# ===========================================================================
# UTILIDADES GENERALES
# ===========================================================================

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter(mensaje="Presiona Enter para continuar..."):
    """Espera a que el usuario presione Enter"""
    input(f"\n{mensaje}")
    print() # Añade una línea extra para mejor separación

# ===========================================================================
# EJERCICIOS DE ESTRUCTURAS DE CONTROL (BUCLES)
# ===========================================================================

def ejercicio_control_1():
    """
    Problema: Corregir la modificación de una lista mientras se itera.
    """
    print("--- 1. Corregir iteración y modificación de lista ---")
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Lista original: {numeros}")

    # Solución: Usar una comprensión de lista para crear la nueva lista de impares
    impares = [num for num in numeros if num % 2 != 0]
    print(f"Resultado corregido (Solo impares): {impares}")
    print("Corrección: Se evita modificar la lista original usando una comprensión de lista.")

def ejercicio_control_2():
    """
    Problema: Generar una tabla de multiplicar con bucles anidados.
    """
    print("--- 2. Tabla de multiplicar del 1 al 10 ---")
    for i in range(1, 11):
        linea = ""
        for j in range(1, 11):
            producto = i * j
            # Formatear la salida para la tabla
            linea += f"{producto:4}" # :4 asegura 4 espacios para cada número
        print(f"Tabla del {i:2}: {linea}")

def ejercicio_control_3():
    """
    Problema: Corregir un bucle while infinito.
    """
    print("--- 3. Corregir bucle while infinito ---")
    print("Resultado esperado: Números del 1 al 5")
    
    contador = 1
    while contador <= 5:
        print(f"Número: {contador}")
        # Corrección: Incrementar la variable de control
        contador += 1
    
    print("Corrección: Se añadió 'contador += 1' para salir del bucle.")

def ejercicio_control_4():
    """
    Problema: Uso de break y continue.
    """
    print("--- 4. Uso de break y continue ---")
    numeros = [5, -2, 10, 8, -3, 0, 7, 9]
    print(f"Lista: {numeros}")
    
    for num in numeros:
        if num == 0:
            print(f"¡Cero encontrado! Deteniendo el proceso (usando break).")
            break
        
        if num < 0:
            print(f"Saltando número negativo: {num} (usando continue).")
            continue
        
        print(f"Procesando número positivo: {num}")

def ejercicio_control_5():
    """
    Problema: Reescribir un bucle tradicional con una comprensión de lista.
    """
    print("--- 5. Convertir bucle a comprensión de lista ---")
    
    # Versión con bucle tradicional para referencia
    cuadrados_pares_tradicional = []
    for numero in range(1, 11):
        if numero % 2 == 0:
            cuadrados_pares_tradicional.append(numero ** 2)
    print(f"Bucle tradicional: {cuadrados_pares_tradicional}")
    
    # Solución con comprensión de lista
    cuadrados_pares_comprension = [numero ** 2 for numero in range(1, 11) if numero % 2 == 0]
    print(f"Comprensión de lista: {cuadrados_pares_comprension}")

def ejercicio_control_6():
    """
    Problema: Combinaciones con bucles anidados y comprensión de listas.
    """
    print("--- 6. Combinaciones con bucles anidados y comprensión ---")
    colores = ["rojo", "azul", "verde"]
    tamaños = ["pequeño", "mediano", "grande"]
    
    # 1. Solución con bucles anidados
    combinaciones_bucle = []
    for color in colores:
        for tamaño in tamaños:
            combinaciones_bucle.append((color, tamaño)) 
    print(f"1. Bucles anidados: {combinaciones_bucle}")
    
    # 2. Solución con comprensión de listas
    combinaciones_comprension = [(color, tamaño) for color in colores for tamaño in tamaños]
    print(f"2. Comprensión de listas: {combinaciones_comprension}")

# ===========================================================================
# EJERCICIOS DE ESTRUCTURAS CONDICIONALES
# ===========================================================================

def ejercicio_condicional_1():
    """
    Problema: Evaluar si un número es positivo, negativo o cero.
    """
    print("--- 1. Evaluar Positivo, Negativo o Cero ---")
    try:
        numero = int(input("Introduce un número entero: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if numero > 0:
        print(f"El número {numero} es Positivo.")
    elif numero < 0:
        print(f"El número {numero} es Negativo.")
    else: 
        print(f"El número {numero} es Cero.")

def ejercicio_condicional_2():
    """
    Problema: Corregir errores de sintaxis en condiciones.
    """
    print("--- 2. Corregir errores de sintaxis ---")
    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        print("Entrada inválida.")
        return
    
    # Errores originales: 'if edad = 18:' y 'elif edad < 18' (falta ':')
    
    if edad == 18: # Corrección: usar '==' para comparación
        print("Tienes exactamente 18 años")
    elif edad < 18: # Corrección: añadir ':'
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")

def ejercicio_condicional_3():
    """
    Problema: Simplificar condicionales anidados con operadores lógicos.
    """
    print("--- 3. Simplificar condicionales anidados ---")
    llueve = input("¿Está lloviendo? (s/n): ").lower() == "s"
    frio = input("¿Hace frío? (s/n): ").lower() == "s"
    
    # Versión mejorada con operadores lógicos
    if llueve and frio:
        print("Lleva paraguas y abrigo")
    elif llueve: # Implica que NO hace frío
        print("Lleva paraguas")
    elif frio: # Implica que NO llueve
        print("Lleva abrigo")
    else: # Ni llueve ni hace frío
        print("Disfruta el día")

def ejercicio_condicional_4():
    """
    Problema: Corregir el orden de las condiciones (de más a menos estricta).
    """
    print("--- 4. Corregir orden de condiciones ---")
    try:
        temperatura = float(input("Introduce la temperatura actual: "))
    except ValueError:
        print("Entrada inválida.")
        return

    # Corrección: Evaluar de la condición más estricta (mayor número) a la menos estricta
    if temperatura > 40:
        print("Nivel: Peligro extremo")
    elif temperatura > 30: # Implica (30 < T <= 40)
        print("Nivel: Alerta alta")
    elif temperatura > 25: # Implica (25 < T <= 30)
        print("Nivel: Precaución")
    else: # Implica (T <= 25)
        print("Nivel: Normal")

def ejercicio_condicional_5():
    """
    Problema: Simplificar if-else con el operador ternario.
    """
    print("--- 5. Usar operador ternario ---")
    try:
        puntuacion = int(input("Introduce tu puntuación (0-100): "))
    except ValueError:
        print("Entrada inválida.")
        return
    
    # Solución con operador ternario
    # Sintaxis: [valor_si_verdadero] if [condición] else [valor_si_falso]
    resultado = "Aprobado" if puntuacion >= 60 else "Suspenso"
    print(f"Resultado (Ternario): {resultado}")

def ejercicio_condicional_6():
    """
    Problema: Determinar si un año es bisiesto.
    """
    print("--- 6. Determinar si un año es bisiesto ---")
    try:
        año = int(input("Introduce un año: "))
    except ValueError:
        print("Entrada inválida.")
        return
    
    def es_bisiesto(año):
        # Es divisible por 4 Y (no por 100 O por 400)
        return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
    
    if es_bisiesto(año):
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")

# ===========================================================================
# MENÚ PRINCIPAL
# ===========================================================================

MENU_OPS = {
    # (Grupo, Función a ejecutar)
    1: ("Control", ejercicio_control_1),
    2: ("Control", ejercicio_control_2),
    3: ("Control", ejercicio_control_3),
    4: ("Control", ejercicio_control_4),
    5: ("Control", ejercicio_control_5),
    6: ("Control", ejercicio_control_6),
    7: ("Condicional", ejercicio_condicional_1),
    8: ("Condicional", ejercicio_condicional_2),
    9: ("Condicional", ejercicio_condicional_3),
    10: ("Condicional", ejercicio_condicional_4),
    11: ("Condicional", ejercicio_condicional_5),
    12: ("Condicional", ejercicio_condicional_6),
    0: ("Salir", lambda: sys.exit(0))
}

def menu():
    """Muestra el menú y obtiene la selección del usuario."""
    limpiar_pantalla()
    print("=" * 60)
    print("EJERCICIOS RESUELTOS - ESTRUCTURAS DE CONTROL Y CONDICIONALES".center(60))
    print("=" * 60)
    
    print("\n--- ESTRUCTURAS DE CONTROL (BUCLES) ---")
    print("1. Corregir iteración y modificación de lista")
    print("2. Tabla de multiplicar con bucles anidados")
    print("3. Corregir bucle while infinito")
    print("4. Uso de break y continue")
    print("5. Convertir bucle a comprensión de lista")
    print("6. Combinaciones con bucles anidados")
    
    print("\n--- ESTRUCTURAS CONDICIONALES ---")
    print("7. Evaluar positivo, negativo o cero")
    print("8. Corregir errores de sintaxis en condiciones")
    print("9. Simplificar condicionales anidados")
    print("10. Corregir orden de condiciones")
    print("11. Usar operador ternario")
    print("12. Determinar si un año es bisiesto")

    print("\n0. Salir")
    
    try:
        opcion = int(input("\nIngresa el número del ejercicio (0-12): "))
        return opcion
    except ValueError:
        print("Entrada inválida. Ingresa un número del 0 al 12.")
        return -1

def main():
    """Función principal para ejecutar los ejercicios."""
    while True:
        opcion = menu()
        
        if opcion in MENU_OPS:
            _, func = MENU_OPS[opcion]
            if opcion != 0:
                print(f"\nEJECUTANDO EJERCICIO {opcion}...")
                func()
                esperar_enter()
            else:
                # La función de salida ya está definida en MENU_OPS[0]
                func()
        elif opcion != -1:
            print("Opción inválida. Intenta de nuevo.")
            esperar_enter()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n¡Hasta luego!")
        sys.exit(0)