"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo for: continue
PROPÓSITO:   Mostrar solo los números pares del 1 al 10, usando continue para
             saltar los impares.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

for x in range(1, 11):
    if x % 2 != 0:
        continue
    print(x)
