"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Listas: remove y count
PROPÓSITO:   Eliminar un elemento de una lista solo si existe, verificándolo
             antes con count().
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

lista1 = ["manzana", "limon", "sandia", "manzana"]

#print(lista1.index("pera"))
if lista1.count("pera") > 0:
    lista1.remove("pera")

else:
    print("No es posible eliminar la pera ya que no existe")
    
print(lista1)
