"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo while: validación de datos
PROPÓSITO:   Pedir un número repetidamente hasta que el usuario ingrese uno positivo.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

numero = int(input("Ingresa un número positivo: "))

while numero <= 0:
    print("El número debe ser positivo.")
    numero = int(input("Ingresa un número positivo: "))

print("Número aceptado:", numero)
