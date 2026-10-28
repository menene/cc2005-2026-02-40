"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Diccionarios: conteo de frecuencias
PROPÓSITO:   Contar cuántos votos recibe cada opción usando un diccionario y get().
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

votos = ["A", "B", "A", "C", "A", "B", "A", "C", "D", "A"]
conteo = {}

for voto in votos:
    print("Antes: ", conteo)
    conteo[voto] = conteo.get(voto, 0) + 1
    print("Después: ", conteo)
    print()

print(conteo)
