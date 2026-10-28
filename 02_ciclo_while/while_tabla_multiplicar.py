"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Ciclo while: tabla de multiplicar
PROPÓSITO:   Mostrar la tabla de multiplicar de un número hasta el límite indicado
             por el usuario.
AUTOR:       Erick Marroquín
FECHA:       2026-10-27
VERSIÓN:     1.0
=====================================================
"""

numero = int(input("Ingresa el número para ver su tabla: "))
fin = int(input("Ingrese hasta que numero quieres ver la tabla: "))
actual = 1

while actual <= fin:
    resultado = numero * actual
    
    print(numero, "x", actual, "=", resultado)
    
    actual = actual + 1
