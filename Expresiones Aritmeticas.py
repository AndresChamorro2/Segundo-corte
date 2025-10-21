"""
EXPRESIONES ARITMÉTICAS CONFUSAS - Actividad 1
Este código demuestra errores comunes y confusión con expresiones aritméticas.
Los estudiantes deben identificar los problemas y entender la precedencia de operadores.
"""

print("=" * 60)
print("EXPRESIONES ARITMÉTICAS - Errores Comunes")
print("=" * 60)
print()

# Problema 1: No entender la precedencia de operadores
print("Problema 1: Confusión con Precedencia de Operadores")
print("-" * 40)

# ¿Qué calcula esto?
result1 = 5 + 3 * 2
print(f"5 + 3 * 2 = {result1}")
print("¿Es (5 + 3) * 2 = 16?")
print("¿O es 5 + (3 * 2) = 11?")
print()##La multiplicación tiene prioridad sobre la suma, así que se calcula primero 3 * 2 = 6, luego 5 + 6 = 11.



# Otro ejemplo confuso
result2 = 10 - 2 + 3
print(f"10 - 2 + 3 = {result2}")
print("¿Es 10 - (2 + 3) = 5?")
print("¿O es (10 - 2) + 3 = 11?")
print()##La suma y la resta tienen la misma prioridad, así que se evalúan de izquierda a derecha: 10 - 2 = 8, luego 8 + 3 = 11.



# Problema 2: Confusión con división
print("Problema 2: Tipos de División")
print("-" * 40)

result3 = 7 / 2
result4 = 7 // 2
result5 = 7 % 2

print(f"7 / 2 = {result3}   (¿Qué tipo de división?)")
print(f"7 // 2 = {result4}  (¿Qué significa //?)")
print(f"7 % 2 = {result5}   (¿Qué es %?)")
print()##- 7 / 2 realiza una división estándar y devuelve un número decimal: 3.5,- 7 // 2 hace una división entera, eliminando los decimales: 3,- 7 % 2 devuelve el residuo de dividir 7 entre 2: 1


# Problema 3: Confusión con operador de potencia
print("Problema 3: Operador de Potencia")
print("-" * 40)

result6 = 2 ** 3
result7 = 2 * 3
result8 = 2 ^ 3  # ¡Esto NO es potencia!

print(f"2 ** 3 = {result6}  (¿Es esto potencia?)")
print(f"2 * 3 = {result7}   (¿Es esto potencia?)")
print(f"2 ^ 3 = {result8}   (¿Es esto potencia?)")
print("¡Advertencia: ^ NO es potencia en Python!")
print()###- ** es el operador correcto para potencia: 2 elevado a 3 = 8,- * es multiplicación: 2 por 3 = 6,- ^ no es potencia, es XOR (operación lógica entre bits): 2 ^ 3 = 1


# Problema 4: Expresión compleja sin paréntesis
print("Problema 4: Expresión Compleja")
print("-" * 40)

result9 = 2 + 3 * 4 - 5 / 2
print(f"2 + 3 * 4 - 5 / 2 = {result9}")
print("¿Cómo se evalúa esto?")
print("¿En qué orden ocurren las operaciones?")
print()##- Primero se calcula 3 * 4 = 12,- Luego 5 / 2 = 2.5,- Después se resuelve la expresión completa: 2 + 12 - 2.5 = 11.5



# Problema 5: Confusión con mezcla de tipos
print("Problema 5: Mezcla de Tipos")
print("-" * 40)

result10 = 5 + 3.0
result11 = 10 / 2
result12 = 10 // 2

print(f"5 + 3.0 = {result10}  (tipo: {type(result10).__name__})")
print(f"10 / 2 = {result11}   (tipo: {type(result11).__name__})")
print(f"10 // 2 = {result12}  (tipo: {type(result12).__name__})")
print("¿Por qué los tipos son diferentes?")
print()##- 5 + 3.0 = 8.0 → tipo: float,- 10 / 2 = 5.0 → tipo: float,- 10 // 2 = 5 → tipo: int



# Problema 6: Números negativos y operadores
print("Problema 6: Números Negativos")
print("-" * 40)

result13 = -5 + 3
result14 = 5 + -3
result15 = 5 - -3
result16 = -5 * -3

print(f"-5 + 3 = {result13}")
print(f"5 + -3 = {result14}")
print(f"5 - -3 = {result15}  (¿Por qué es 8?)")
print(f"-5 * -3 = {result16}")
print()##- -5 + 3 da -2 porque se avanza 3 unidades desde -5., 5 + -3 da 2 porque se retrocede 3 unidades desde 5., 5 - -3 da 8 porque restar un negativo es como sumar., -5 * -3 da 15 porque dos negativos multiplicados dan positivo.


# Problema 7: Los paréntesis hacen la diferencia
print("Problema 7: Impacto de Paréntesis")
print("-" * 40)

result17 = 2 + 3 * 4
result18 = (2 + 3) * 4
result19 = 2 + (3 * 4)

print(f"2 + 3 * 4 = {result17}")
print(f"(2 + 3) * 4 = {result18}")
print(f"2 + (3 * 4) = {result19}")
print("¡Mismos números, resultados diferentes!")
print()##- 2 + 3 * 4 = 14 → porque la multiplicación tiene prioridad, (2 + 3) * 4 = 20 → porque los paréntesis obligan a sumar primero, 2 + (3 * 4) = 14 → igual que la primera, pero más claro con paréntesis


# Problema 8: Múltiples divisiones
print("Problema 8: Múltiples Divisiones")
print("-" * 40)

result20 = 20 / 4 / 2
result21 = 20 / (4 / 2)
result22 = (20 / 4) / 2

print(f"20 / 4 / 2 = {result20}")
print(f"20 / (4 / 2) = {result21}")
print(f"(20 / 4) / 2 = {result22}")
print("¿De qué manera se evalúa?")
print()##- En 20 / 4 / 2, Python divide primero 20 entre 4 (da 5) y luego divide ese resultado entre 2, lo que da 2.5., En 20 / (4 / 2), el paréntesis obliga a dividir primero 4 entre 2 (da 2), y luego 20 entre 2, lo que da 10., En (20 / 4) / 2, se agrupa la primera división (20 entre 4 da 5), y luego se divide entre 2, lo que da 2.5.


# Problema 9: Confusión con operador módulo
print("Problema 9: Operador Módulo")
print("-" * 40)

result23 = 17 % 5
result24 = 17 / 5
result25 = 17 // 5

print(f"17 % 5 = {result23}   (¿Qué significa esto?)")
print(f"17 / 5 = {result24}")
print(f"17 // 5 = {result25}")
print("¿Cómo se relacionan?")
print()###- 17 % 5 = 2 → porque 5 cabe 3 veces en 17 (5×3=15) y sobran 2., 17 / 5 = 3.4 → división completa con decimales., 17 // 5 = 3 → división entera, se descartan los decimales.


# Problema 10: Cálculo del mundo real que sale mal
print("Problema 10: Ejemplo del Mundo Real")
print("-" * 40)

# Calcular: (100 + 50) * 0.15 impuesto
wrong_tax = 100 + 50 * 0.15
correct_tax = (100 + 50) * 0.15

print("Calculando impuesto del 15% sobre $150:")
print(f"100 + 50 * 0.15 = ${wrong_tax}")
print(f"(100 + 50) * 0.15 = ${correct_tax}")
print("¿Cuál es correcto?")
print()##- 100 + 50 * 0.15 = 107.5 → cálculo incorrecto por falta de paréntesis, (100 + 50) * 0.15 = 22.5 → cálculo correcto del 15% sobre $150


# Problema 11: Confusión con conversión de temperatura
print("Problema 11: Conversión de Temperatura")
print("-" * 40)

celsius = 25
# Convertir a Fahrenheit: F = C * 9/5 + 32
wrong_fahrenheit = celsius * 9 / 5 + 32
also_wrong = celsius * 9 / (5 + 32)
correct_fahrenheit = (celsius * 9 / 5) + 32

print(f"25°C a Fahrenheit:")
print(f"celsius * 9 / 5 + 32 = {wrong_fahrenheit}")
print(f"celsius * 9 / (5 + 32) = {also_wrong}")
print(f"(celsius * 9 / 5) + 32 = {correct_fahrenheit}")
print("¿Qué fórmula es correcta?")
print()##- celsius * 9 / 5 + 32 = 77 → correcta por precedencia, celsius * 9 / (5 + 32) ≈ 6.08 → incorrecta por agrupar mal, (celsius * 9 / 5) + 32 = 77 → correcta y más clara


# Problema 12: Cálculo de promedio
print("Problema 12: Cálculo de Promedio")
print("-" * 40)

a, b, c = 10, 20, 30
wrong_average = a + b + c / 3
correct_average = (a + b + c) / 3

print(f"Promedio de 10, 20, 30:")
print(f"a + b + c / 3 = {wrong_average}")
print(f"(a + b + c) / 3 = {correct_average}")
print("¿Por qué son diferentes?")
print()

print("=" * 60)
print("¿Puedes identificar todos los problemas?")
print("¿Entiendes por qué cada resultado es lo que es?")
print("=" * 60)## a + b + c / 3 = 40 → incorrecto porque solo se divide el último número, (a + b + c) / 3 = 20 → correcto porque se divide la suma total
