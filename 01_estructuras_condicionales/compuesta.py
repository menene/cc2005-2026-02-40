"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Estructuras condicionales compuestas
PROPÓSITO:   Clasificar el tipo de elección en la que puede votar una persona
             según la edad ingresada.
AUTOR:       Erick Marroquín
FECHA:       2026-09-03
VERSIÓN:     1.0
=====================================================
"""

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad, puedes votar en las elecciones generales")

elif edad >= 15:
    print("Eres pubert@, puedes votar en las elecciones pubertas")
    
elif edad >= 10:
    print("Eres niñ@ Puedes votar en las elecciones infantiles")
    
else:
    print("No puedes votar")
