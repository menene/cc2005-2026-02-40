"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo for: promedio de n datos
PROPÓSITO:   Calcular el promedio de una cantidad de notas indicada por el usuario.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

total = 0
n = int(input("Ingrese la cantidad de estudiantes: "))

for i in range(1, n + 1):
    nota = float(input("Ingresa la nota " + str(i) + ": "))
    total = total + nota

promedio = total / n
print("Promedio:", promedio)
