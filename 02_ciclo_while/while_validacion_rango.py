"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo while: validación con condición compuesta
PROPÓSITO:   Pedir un número repetidamente hasta que esté entre 1 y 10.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

numero = int(input("Ingresa un número entre 1 y 10: "))

while (numero < 1 or numero > 10):
    print("El número debe ser entre 1 y 10.")
    numero = int(input("Ingresa un número entre 1 y 10: "))

print("Número aceptado:", numero)
