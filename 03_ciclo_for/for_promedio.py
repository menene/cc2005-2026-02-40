"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo for: promedio
PROPÓSITO:   Calcular el promedio de 5 notas ingresadas por el usuario.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

total = 0

for i in range(1, 6):
    nota = float(input("Ingresa la nota " + str(i) + ": "))
    total = total + nota

promedio = total / 5
print("Promedio:", promedio)
