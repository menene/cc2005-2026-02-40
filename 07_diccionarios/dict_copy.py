"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Diccionarios: copy
PROPÓSITO:   Crear una copia independiente de un diccionario con copy().
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

base = {"Ana": 85, "Carlos": 90}
nuevos = {"María": 78, "Ana": 92}

otro = nuevos.copy()

print(otro)
