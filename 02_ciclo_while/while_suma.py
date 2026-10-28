"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo while: acumulador
PROPÓSITO:   Sumar los números desde 1 hasta el número indicado por el usuario.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

numero = 1
total = 0
cantidad = int(input("Ingrese el número al que quiere contar de 1 en 1: "))
 
while numero <= cantidad:
    total = total + numero
    numero = numero + 1
 
print("La suma es:", total)
