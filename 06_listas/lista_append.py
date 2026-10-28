"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Listas: append y recorrido
PROPÓSITO:   Agregar una lista dentro de otra con append(), acceder a sus elementos
             y recorrerla con un ciclo for.
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

lista1 = ["manzana", "limon", "sandia"]
lista2 = ["arroz", "frijol"]


lista1.append(lista2)

print(lista1)

print(lista1[3])
print(lista1[3][0])

for item in lista1:
    print(item)
