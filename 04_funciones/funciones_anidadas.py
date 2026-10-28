"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Funciones que llaman a otras funciones
PROPÓSITO:   Calcular el área de distintas figuras usando una función principal
             que llama a una función específica para cada figura.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

def area(figura):
    
    if figura == "rectangulo":
        base = int(input("base: "))
        altura = int(input("altura: "))
        
        return rectangulo(base, altura)
    
    elif figura == "triangulo":
        base = int(input("base: "))
        altura = int(input("altura: "))
        
        return triangulo(base, altura)
    
    elif figura == "circulo":
        radio = int(input("radio: "))
        
        return circulo(radio)
    
    else:
        return 0
    
    
def rectangulo(base, altura):
    return base * altura

def triangulo(base, altura):
    return(base * altura) / 2

def circulo(r):
    return 3.141592654 * (r ** 2)



a1 = area("rectangulo")
print(a1)

a2 = area("triangulo")
print(a2)

a3 = area("circulo")
print(a3)
