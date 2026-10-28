"""
=====================================================
Algoritmos y Programación Básica

TEMA:        Cadenas: validación de longitud
PROPÓSITO:   Validar que una contraseña ingresada tenga al menos 8 caracteres.
AUTOR:       Erick Marroquín
FECHA:       2026-10-26
VERSIÓN:     1.0
=====================================================
"""

contrasena = input("Escribe tu contraseña (debe tener 8 caracteres): ")

print(len(contrasena))

if len(contrasena) < 8:
    print("La contraseña es demasiado corta.")
    
else:
    print("Contraseña aceptada.")
