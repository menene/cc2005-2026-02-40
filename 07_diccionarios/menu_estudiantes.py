"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Funciones, listas y diccionarios
PROPÓSITO:   Administrar estudiantes y sus notas mediante un menú, calculando
             promedios individuales y generales con una función.
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

def calcular_promedio(notas):
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
estudiantes = [
    {"nombre": "Erick", "carnet": "123", "carrera": "Compu", "curso": "cc2005", "notas": [100, 90, 95, 88, 100, 100]},
    {"nombre": "Ana", "carnet": "456", "carrera": "Civil", "curso": "cc2005", "notas": [100, 100, 100, 100, 100, 100]},
    {"nombre": "Jose", "carnet": "987", "carrera": "Civil", "curso": "cc2005", "notas": [10, 20, 30, 40, 50, 60]},
]

while opcion != "6":
    print("\n=== MENU ===")
    print("1. Crear estudiante")
    print("2. Agregar nota")
    print("3. Calcular promedio estudiante")
    print("4. Calcular promedio general")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("\n\n")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        carnet = input("Ingrese el carnet: ")
        carrera = input("Ingrese la carrera: ")
        curso = input("Ingrese el curso: ")
        
        estudiante = {
            "nombre": nombre,
            "carnet": carnet,
            "carrera": carrera,
            "curso": curso,
            "notas": []
        }
        
        estudiantes.append(estudiante)
        
        
    elif opcion == "2":
        carnet = input("Ingrese el carnet para la nota: ")
        found = False
        
        for estudiante in estudiantes:
            
            if estudiante["carnet"] == carnet:
                
                found = True

                nota = int(input("ingrese la nota: "))
                
                estudiante["notas"].append(nota)
                
        if not found:
            print("Estudiante no encontrado")
        
    elif opcion == "3":
        carnet = input("Ingrese el carnet para el promedio: ")
        found = False
        
        for estudiante in estudiantes:
            
            if estudiante["carnet"] == carnet:
                
                found = True
                
                promedio = calcular_promedio(estudiante["notas"])
                
                print("Nombre:", estudiante["nombre"])
                print("Carnet:", estudiante["carnet"])
                print("Carrera:", estudiante["carrera"])
                print("Curso:", estudiante["curso"])
                print("Promedio:", promedio)
    
        
    elif opcion == "4":
        promedios = []
        
        for estudiante in estudiantes:
            promedio = calcular_promedio(estudiante["notas"])
            promedios.append(promedio)
            
        promedio_general = calcular_promedio(promedios)
        
        print("El promedio general es:", promedio_general)
        
    elif opcion == "5":
        print(estudiantes)
        
    elif opcion == "6":
        print("Nos vemos")
        
    else:
        print("\n\nOpcion inválida... intentalo nuevamente\n\n")
