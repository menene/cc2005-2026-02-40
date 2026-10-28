"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Cadenas: slicing y ciclo while
PROPÓSITO:   Determinar si las cadenas ingresadas son palíndromos invirtiéndolas
             con slicing, hasta que el usuario escriba "salir".
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

cadena = "lo que se me de la gana!"

while "salir" not in cadena:
    cadena = input("Ingrese una cadena para validar si es palindromo o no: ")
    
    if "salir" not in cadena:
        
        flipped = cadena[::-1]

        if cadena == flipped and len(cadena) >= 3:
            print("Es palindromo")
            
        else:
            print("No es palindromo")
