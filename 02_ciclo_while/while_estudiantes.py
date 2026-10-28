"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo while con condicionales
PROPÓSITO:   Evaluar a varios estudiantes y determinar si aprueban según su nota
             y su asistencia.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
n = 1

while n <= estudiantes:
    
    print("Evaluando estudiante", n)
    
    nota = int(input("Ingrese la nota del estudiante: "))
    asistencia = int(input("Ingrese la asistencia del estudiante: "))
    
    if (nota >= 61 and asistencia >= 80):
        print("Aprobado")
        
    else:
        print("Reprobado")
        
    n = n + 1
