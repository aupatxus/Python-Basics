# Python Basics
Python Basics  
https://formacion.thebridge.tech/  

<img src="https://www.codewars.com/users/aupatxus/badges/large"></img>


![Data Science con IA](https://raw.githubusercontent.com/aupatxus/ONLINE_DS_THEBRIDGE_GitHub/refs/heads/main/Vital%20LANBIDE.png)


https://codewars.com  

https://www.kaggle.com/learn/python

https://www.youtube.com/watch?v=nLRL_NcnK-4

<hr>



# Python Basics I: Fundamentos de Python

---

## Índice
1. [Variables](#1-variables)
2. [Función Print](#2-función-print)
3. [Comentarios](#3-comentarios)
4. [Flujos de Ejecución](#4-flujos-de-ejecución)
5. [Eliminación de Variables (del)](#5-eliminación-de-variables-del)
6. [Tipos de Datos](#6-tipos-de-datos)
7. [Conversión de Tipos (Casting)](#7-conversión-de-tipos-casting)
8. [Entrada de Datos (Input)](#8-entrada-de-datos-input)
9. [El Valor Nulo (None)](#9-el-valor-nulo-none)
10. [Sintaxis y Buenas Prácticas](#10-sintaxis-y-buenas-prácticas)
11. [El Zen de Python](#11-el-zen-de-python)

---

## 1. Variables
Las variables son etiquetas que asignamos a los datos en un programa para poder almacenarlos en memoria y reutilizarlos. 

*   **Asignación:** Se utiliza el operador `=` para asignar un valor a una variable.
*   **Tipado Dinámico:** No es necesario especificar el tipo de dato al declarar una variable; Python lo interpreta automáticamente. Sin embargo, Python es **fuertemente tipado**, lo que significa que cada variable tiene un tipo definido y no se permiten operaciones incompatibles de forma implícita.

```python
ingresos = 1300  # Asignación de un número entero
gastos = 405
margen = ingresos - gastos  # Uso de variables para operaciones numéricas
```

---

## 2. Función Print
La función `print()` se utiliza para mostrar información por pantalla u obtener el *output* de una celda de código.

### Formas de formatear texto en un print:
1.  **Separación por comas:** Añade un espacio en blanco automáticamente entre cada elemento.
2.  **Concatenación con operador `+`:** Une cadenas de texto (requiere que todos los elementos sean de tipo string).
3.  **Formateo tradicional (`%s`):** Reemplaza marcadores de posición por variables.
4.  **F-strings (Cadenas literales formateadas):** La opción más moderna y legible, anteponiendo una `f` al string y encerrando las variables entre llaves `{}`.

```python
print("Ingresos: ", ingresos)
print("Los beneficios de %s han sido de %s millones" % ("septiembre", beneficio))
print(f"Los beneficios de {mes} han sido de {beneficio} millones")
```

---

## 3. Comentarios
Los comentarios son fragmentos de texto dentro del código que el intérprete de Python ignora por completo. Son fundamentales para documentar y explicar la lógica del programa a otros desarrolladores o a ti mismo en el futuro.

```python
# Esto es un comentario de una sola línea

'''
Esto es un comentario
multilínea o bloque de texto
'''

"""
También se pueden hacer comentarios
multilínea con comillas dobles.
"""
```

---

## 4. Flujos de Ejecución
Los programas en Python se ejecutan de manera **secuencial** (de arriba a abajo). Por tanto, el orden de las instrucciones es crítico: no puedes operar con una variable antes de haberla declarado.

*   **Fin de línea:** Python interpreta el salto de línea como el final de una instrucción. A diferencia de lenguajes como Java o C++, no requiere obligatoriamente el uso de punto y coma `;`, aunque está permitido para poner varias instrucciones en una misma línea.
*   **Asignación múltiple:** Permite asignar valores a varias variables simultáneamente.

```python
# Asignación múltiple en una línea
x, y, z = 1, 2, 3
altura = 1.80; peso = 75  # Dos instrucciones separadas por punto y coma
```

---

## 5. Eliminación de Variables (`del`)
La sentencia `del` borra una variable del mapa de memoria del programa. Si intentas llamarla después de haberla eliminado, Python lanzará un error de tipo `NameError`.

*   **Uso principal:** Aunque en programas pequeños no suele ser necesario limpiar variables, resulta muy útil al trabajar con grandes volúmenes de datos (como datasets de imágenes) que saturan la memoria del sistema.

```python
altura = 1.8
del altura
# print(altura)  --> Lanzará NameError: name 'altura' is not defined
```

---

## 6. Tipos de Datos
Cada tipo de dato en Python posee propiedades y operaciones específicas asociadas. Para conocer el tipo de dato de cualquier variable, se utiliza la función `type()`.

### Tipos básicos integrados (*Built-in Types*):
*   **Numéricos:**
    *   `int`: Números enteros (positivos o negativos sin decimales). Ej: `22`, `-74`.
    *   `float`: Números reales (con decimales, representados con un punto `.`). Ej: `22.45`, `22.0`.
*   **String (`str`):** Cadenas de texto plano. Se declaran entre comillas simples o dobles. Se pueden usar caracteres de escape como `\n` (salto de línea) o `\t` (tabulación). La función `len()` devuelve su longitud.
*   **Booleano (`bool`):** Lógica binaria. Solo puede tomar los valores `True` o `False` (siempre con la primera letra en mayúscula).

### Operadores aritméticos:
*   Suma: `+`
*   Resta: `-`
*   Multiplicación: `*`
*   División: `/` (Siempre devuelve un `float`)
*   Cociente de la división entera: `//`
*   Resto de la división (Módulo): `%`
*   Exponente (Elevar): `**`

---

## 7. Conversión de Tipos (Casting)
Es el proceso de forzar el cambio de un tipo de dato a otro mediante funciones que comparten el nombre del tipo destino: `int()`, `float()`, `str()`, `bool()`.

### Reglas y consideraciones importantes:
*   **De Float a Int:** Se trunca la parte decimal (se pierden los decimales, no se redondea). Para redondear, se usa la función `round(número, decimales)`.
*   **De String a Número:** Funciona siempre que el string contenga únicamente caracteres numéricos válidos. **Importante:** Python reconoce el punto `.` para los decimales. Si una cadena contiene una coma (ej: `"98,25"`), dará un `ValueError`. Se debe usar `.replace(",", ".")` antes de la conversión.
*   **Conversiones a Booleano:**
    *   En números: El `0` equivale a `False`. Cualquier otro número (positivo o negativo) equivale a `True`.
    *   En strings: Una cadena vacía `""` equivale a `False`. Cualquier cadena con texto equivale a `True`.

```python
num_real = 24.69
num_entero = int(num_real)  # Resultado: 24

# Reemplazo de caracteres para conversión exitosa
numero_comas = "98,25"
numero_puntos = numero_comas.replace(",", ".")
numero_float = float(numero_puntos)  # Resultado: 98.25
```

---

## 8. Entrada de Datos (`input`)
La función `input()` detiene la ejecución del programa para que el usuario introduzca un valor por teclado.

*   **¡Atención!** Por defecto, **todo valor recogido por `input()` es un String (`str`)**. Si necesitas realizar operaciones matemáticas con él, debes transformarlo inmediatamente a `int` o `float`.

```python
# Captura y conversión inmediata a entero
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
resultado = num1 + num2
```

---

## 9. El Valor Nulo (`None`)
`None` es una palabra reservada que representa la ausencia de valor o un valor nulo. Su tipo de dato es `NoneType`.
*   **Diferencia clave:** `None` **no** equivale numéricamente a `0`, tampoco es un string vacío `""`, ni equivale al booleano `False`. Es una entidad propia para representar un conjunto vacío.

---

## 10. Sintaxis y Buenas Prácticas
Para escribir código limpio, legible y evitar errores de sintaxis en Python, se sugieren las siguientes pautas:

*   **Cierre de estructuras:** Todo símbolo abierto (paréntesis `()`, llaves `{}`, corchetes `[]`, comillas) debe cerrarse correspondientemente.
*   **Nombres de variables:**
    *   Se deben usar únicamente letras minúsculas y guiones bajos (`_`) para simular espacios (estilo *snake_case*). Ej: `lista_compra`.
    *   No usar espacios en blanco en los nombres de las variables.
    *   Los números no pueden ir al principio del nombre de una variable (ej: `2009_ingresos` es **incorrecto**; `ingresos_2009` es **correcto**).
    *   **Case Sensitive:** Python distingue entre mayúsculas y minúsculas (`ingresos` e `Ingresos` se consideran variables distintas).
*   **Caracteres especiales:** Evitar el uso de la letra `ñ`, tildes o caracteres especiales (`ª`, `º`, `@`) dentro del código (nombres de variables, funciones, etc.). Limitar su uso solo a comentarios o cadenas de texto.
*   **Constantes:** Aquellas variables cuyo valor nunca cambia a lo largo del programa se escriben completamente en mayúsculas. Ej: `MI_PAIS = "España"`.
*   **Confusiones visuales:** Prestar especial atención a caracteres visualmente similares que puedan inducir a error: el número uno (`1`) frente a la letra ele (`l`), o el número cero (`0`) frente a la letra o (`O`).

---

## 11. El Zen de Python
El *Zen de Python* es una colección de 20 principios de software que guían el diseño y la filosofía de este lenguaje, escritos por Tim Peters. Se pueden consultar ejecutando `import this`.

### Principios destacados:
*   Lo bello es mejor que lo feo (*Beautiful is better than ugly*).
*   Lo explícito es mejor que lo implícito (*Explicit is better than implicit*).
*   Lo simple es mejor que lo complejo (*Simple is better than complex*).
*   La legibilidad cuenta (*Readability counts*).
*   Los errores nunca deberían pasar en silencio (*Errors should never pass silently*).

