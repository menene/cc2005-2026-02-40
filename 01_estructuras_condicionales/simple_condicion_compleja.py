"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Condición simple compleja
PROPÓSITO:   Comprobar si una nota se encuentra entre 75 y 90, mostrando el
             resultado mediante dos formas equivalentes.
AUTOR:       Erick Marroquín
FECHA:       2026-09-03
VERSIÓN:     1.0
=====================================================
"""

nota = 85

if 75 <= nota < 90:
    print("Muy bien")

if (nota >= 75) and (nota < 90):
    print("Muy bien")
