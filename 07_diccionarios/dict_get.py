"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Diccionarios: get
PROPÓSITO:   Consultar valores de un diccionario con get() y un valor por defecto
             para evitar errores con llaves inexistentes.
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

notas = {"Ana": 85}

# print(notas["Luis"])

print(notas.get("Luis", 0))
print(notas.get("Ana", 0))

print(notas)
