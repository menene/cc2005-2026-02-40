# CC2005 — Algoritmos y Programación Básica

Repositorio oficial de la clase **CC2005 Algoritmos y Programación Básica**.
Este repositorio contiene ejercicios progresivos en Python diseñados para
practicar los fundamentos de la programación, la resolución de problemas y el
pensamiento algorítmico.

## Temas del curso

- Variables y expresiones
- Tipos de datos básicos
- Entrada y salida de datos
- Operadores aritméticos, relacionales y lógicos
- Estructuras condicionales
- Ciclo while
- Ciclo for
- Funciones
- Cadenas de texto
- Listas
- Diccionarios

## Estructura del repositorio

```text
.
├── 00_varialbes_expresiones/
│   ├── expresiones.py
│   ├── ingreso_datos.py
│   ├── salida_pantalla.py
│   ├── tipos_datos.py
│   └── variables.py
├── 01_estructuras_condicionales/
│   ├── anidada.py
│   ├── compuesta.py
│   ├── simple_condicion_compleja.py
│   ├── simple_if_else.py
│   └── simple_solo_if.py
├── 02_ciclo_while/
│   ├── while_basico.py
│   ├── while_contador.py
│   ├── while_continue.py
│   ├── while_estudiantes.py
│   ├── while_menu.py
│   ├── while_suma.py
│   ├── while_tabla_multiplicar.py
│   ├── while_validacion.py
│   └── while_validacion_rango.py
├── 03_ciclo_for/
│   ├── for_anidado.py
│   ├── for_basico.py
│   ├── for_continue.py
│   ├── for_promedio.py
│   ├── for_promedio_n.py
│   ├── for_range.py
│   ├── for_suma.py
│   └── for_tabla_multiplicar.py
├── 04_funciones/
│   ├── funciones_anidadas.py
│   ├── funciones_basico.py
│   ├── funciones_parametros.py
│   ├── funciones_retorno.py
│   └── notas_plus.py
├── 05_cadenas/
│   ├── longitud_indices.py
│   ├── palindromo.py
│   ├── recorrer_cadena.py
│   └── validar_contrasena.py
├── 06_listas/
│   ├── lista_append.py
│   ├── lista_clear.py
│   ├── lista_doble.py
│   ├── lista_extend.py
│   ├── lista_remove.py
│   └── menu_notas.py
├── 07_diccionarios/
│   ├── conteo_votos.py
│   ├── dict_copy.py
│   ├── dict_for.py
│   ├── dict_get.py
│   ├── dict_items.py
│   ├── lista_diccionarios.py
│   └── menu_estudiantes.py
├── encabezado.py
├── .gitignore
└── README.md
```

> La primera carpeta conserva por ahora su nombre original,
> `00_varialbes_expresiones`, para que los comandos documentados coincidan con
> el repositorio.

## Requisitos

- Python 3.10 o una versión posterior
- No se requieren dependencias externas

Comprueba tu instalación de Python con:

```bash
python3 --version
```

## Ejecutar un ejercicio

Desde la raíz del repositorio, ejecuta cualquier script con Python:

```bash
python3 00_varialbes_expresiones/expresiones.py
python3 01_estructuras_condicionales/simple_if_else.py
```

Algunos ejercicios solicitan datos al usuario. Por ejemplo:

```bash
python3 00_varialbes_expresiones/ingreso_datos.py
python3 01_estructuras_condicionales/compuesta.py
```

## Convenciones de desarrollo

- Mantén cada ejercicio enfocado en un solo concepto de programación.
- Usa nombres descriptivos para las variables y los archivos.
- Sigue la guía de estilo [PEP 8](https://peps.python.org/pep-0008/).
- Mantén el encabezado estándar del proyecto al inicio de cada script de Python.
- Usa el formato `AAAA-MM-DD` para las fechas de los encabezados.
- No subas archivos generados, entornos virtuales ni configuraciones locales.

## Autor

**Erick Marroquín**

Este repositorio se mantiene como el repositorio oficial de trabajo para la
clase CC2005.
