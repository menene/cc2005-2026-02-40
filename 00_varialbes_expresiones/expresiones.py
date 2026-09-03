"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Expresiones
PROPÓSITO:   Resolver expresiones aritméticas, relacionales y lógicas, y
             mostrar sus resultados.
AUTOR:       Erick Marroquín
FECHA:       2026-09-03
VERSIÓN:     1.0
=====================================================
"""

numero_a = 10
numero_b = 3

suma = numero_a + numero_b
resta = numero_a - numero_b
multiplicacion = numero_a * numero_b
division = numero_a / numero_b
modulo = numero_a % numero_b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)

print("\nOperadores relacionales")
print("¿A es mayor que B?", numero_a > numero_b)
print("¿A es menor que B?", numero_a < numero_b)
print("¿A es igual a B?", numero_a == numero_b)
print("¿A es diferente de B?", numero_a != numero_b)
print("¿A es mayor o igual que B?", numero_a >= numero_b)
print("¿A es menor o igual que B?", numero_a <= numero_b)

print("\nOperadores lógicos")
es_positivo = numero_a > 0
es_par = numero_a % 2 == 0
print("¿A es positivo y par?", es_positivo and es_par)
print("¿A es positivo o B es par?", es_positivo or numero_b % 2 == 0)
print("¿A no es negativo?", not numero_a < 0)
