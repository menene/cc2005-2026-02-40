"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Funciones y menús
PROPÓSITO:   Administrar una lista de notas mediante un menú, validando la entrada
             y calculando el promedio con una función.
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

def promedio(notas):
    if len(notas) == 0:
        promedio = 0
        
    else:
        total = 0
        
        for nota in notas:
            total = total + nota
            
        promedio = total / len(notas)
        
    return promedio

# =========================================

opcion = "lo que sea"
notas = []

while opcion != "4":
    print("\n=== MENU ===")
    print("1. Ingresa nota")
    print("2. Calcular promedio")
    print("3. Mostrar notas")
    print("4. Salir")
    print("\n\n")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        #nota = int(input("Ingrese una nota: "))
        nota = input("Ingrese una nota: ")
        
        while not nota.isnumeric():
            nota = input("Ingrese una nota valida: ")            
        
        nota = int(nota)
        notas.append(nota)
        
    elif opcion == "2":
        print("El promedio es", promedio(notas))
        
    elif opcion == "3":
        print(notas)
        
    elif opcion == "4":
        print("Nos vemos")
        
    else:
        print("\n\nOpcion inválida... intentalo nuevamente\n\n")
