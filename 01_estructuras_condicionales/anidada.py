"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Estructuras condicionales anidadas
PROPÓSITO:   Determinar el tipo de elección en la que puede votar una persona
             según su edad, usando condiciones anidadas.
AUTOR:       Erick Marroquín
FECHA:       2026-09-03
VERSIÓN:     1.0
=====================================================
"""

edad = 21

if edad >= 18:
    print("Eres mayor de edad, puedes votar en las elecciones generales")
    
else:
    
    if edad >= 15:
        print("Eres pubert@, puedes votar en las elecciones pubertas")
        
    else:
        
        if (edad >= 10):
            print("Eres niñ@ Puedes votar en las elecciones infantiles")
        
        else:
            print("No puedes votar")
