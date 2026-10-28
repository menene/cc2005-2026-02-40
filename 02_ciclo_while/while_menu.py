"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo while: menú de opciones
PROPÓSITO:   Mostrar un menú que se repite hasta que el usuario elija salir.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

opcion = "lo que sea"

while opcion != "3":
    print()
    print("=== MENU PRINCIPAL ===")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    print()
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("¡Hola!")
        
    elif opcion == "2":
        print("¡Adiós!")
        
    elif opcion == "3":
        print("Terminando ejecución...")
        
    else:
        print("Opción invalida... intentalo nuevamente")

print("Programa terminado.")
