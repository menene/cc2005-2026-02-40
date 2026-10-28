"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Diccionarios: items
PROPÓSITO:   Recorrer un diccionario obteniendo llave y valor con items().
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

notas = {"Ana": 85, "Carlos": 90, "María": 78}

print(notas.items())

for nombre, nota in notas.items():
    print(nombre, ":", nota)
