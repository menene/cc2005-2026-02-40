"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Funciones con valor de retorno
PROPÓSITO:   Calcular un área con una función que retorna un valor y validar el
             resultado con otra función.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

def area(base, altura):
    
    a = base * altura
    
    return a
    
def validar_area(area):
    
    if (area > 100):
        print("Cuidado, el área es muy grande")
        
    elif (area < 10):
        print("Cuidado, el área es muy pequeña")
    
    
    
    
# print(area(10, 11))
a1 = area(10, 11)
print(a1)
validar_area(a1)

area(3, 6)
area(1, 2)

#total = area(10, 11) + area(3, 6) + area(1, 2)

# a1 = area(10, 11)
# a2 = area(3, 6)
# a3 = area(1, 2)
# 
# total = a1 + a2 + a3
# 
# print(total)
