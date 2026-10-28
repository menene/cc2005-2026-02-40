"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclos for anidados
PROPÓSITO:   Mostrar las tablas de multiplicar del 1 al 5 usando un ciclo dentro
             de otro.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

for tabla in range(1, 6):
    
    for i in range(1, 6):
        print(tabla, "x", i, "=", tabla * i)
        
    print("---")
