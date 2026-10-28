"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Cadenas: recorrido con for
PROPÓSITO:   Recorrer una cadena carácter por carácter, primero por índice y luego
             directamente por cada letra.
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

texto = "Python"

for i in range(len(texto)):
    print(i, texto[i])
    
for letra in texto:
    print(letra)
