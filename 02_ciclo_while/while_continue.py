"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo while: continue
PROPÓSITO:   Mostrar solo los números impares del 1 al 10, usando continue para
             saltar los pares.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

x = 0

while x < 10:
    x = x + 1
    
    if x % 2 == 0:
        continue
    
    print(x)
