"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Funciones, ciclos y menús
PROPÓSITO:   Calcular el promedio de varios estudiantes mediante un menú y
             determinar si aprueban según su promedio y asistencia.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

def imprimir_menu():
    print()
    print("=== Notas Plus ===")
    print()
    print("1: Calcular promedio de estudiantes")
    print("2: Calcular promedio general")
    print("3: Salir")
    print()
    
def calcular_promedio(suma, n):
    
    if n == 0:
        return 0
    
    x = suma / n
    
    return x

def aprobo(promedio, asistencia):
    
    if (promedio >= 61) and (asistencia >= 80):
        return True
    
    return False
    
    
opcion = "lo que sea"

while opcion != "3":
    
    imprimir_menu()
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        estudiantes = int(input("¿Cuántos estudintes tienes? "))
        notas = int(input("¿Cuántas notas tienes? "))
        
        for estudiante in range(1, estudiantes + 1):
            nombre = input("Ingrese el nombre del estudiante " + str(estudiante) + ": ")
            total = 0
            
            for nota in range(1, notas + 1):
                n = float(input("Ingrese la nota " + str(nota) + " del estudiante " + nombre + ": "))
                
                total = total + n
                
            promedio = calcular_promedio(total, notas)
            
            print("El promedio de", nombre, "es de", promedio)
            
            asistencia = int(input("Ingrese la asistencia de " + nombre + ": "))
            
            if aprobo(promedio, asistencia):
                print("Aprobo el curso 🎓")
                
            else:
                print("Nos vemos el otro año 🥲")
        
        
    elif opcion == "2":
        print("Calcular promedio general")
        
    elif opcion == "3":
        print("Nos vemos 👋")
        
    else:
        print("opción inválida, intentalo nuevamente 🙄")
