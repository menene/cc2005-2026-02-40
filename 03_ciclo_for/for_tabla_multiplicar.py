"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo for: tabla de multiplicar
PROPÓSITO:   Mostrar la tabla de multiplicar de un número hasta el límite indicado
             por el usuario.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

numero = int(input("Ingresa el número para ver su tabla: "))
fin = int(input("Ingrese hasta que numero quieres ver la tabla: "))

for i in range(1, fin + 1):
    resultado = numero * i
    
    print(numero, "x", i, "=", resultado)
