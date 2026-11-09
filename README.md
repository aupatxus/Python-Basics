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
````
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
````



<hr>



# Python Basics II: Operaciones, Métodos y Listas

Este repositorio contiene los conceptos teóricos sobre la manipulación de variables, el uso de funciones y métodos integrados, y la introducción a las colecciones de datos a través de las listas en Python.

---

## Índice
1. [Operaciones Aritméticas Avanzadas](#1-operaciones-aritméticas-avanzadas)
2. [Operaciones Comparativas](#2-operaciones-comparativas)
3. [Operaciones con Booleanos (Álgebra de Boole)](#3-operaciones-con-booleanos-álgebra-de-boole)
4. [Funciones Built-in Comunes](#4-funciones-built-in-comunes)
5. [Métodos en Python](#5-métodos-en-python)
6. [Listas](#6-listas)
7. [Gestión de Errores Comunes](#7-gestión-de-errores-comunes)

---

## 1. Operaciones Aritméticas Avanzadas
Además de los operadores aritméticos básicos ya conocidos (`+`, `-`, `*`, `/`, `**`, `//`, `%`), el orden y las reglas de prioridad se mantienen estrictamente fieles a las matemáticas convencionales.

*   **Propiedades algebraicas:** Python respeta las propiedades conmutativa, asociativa y distributiva.
*   **El Paréntesis `()`:** Es el elemento prioritario que permite agrupar operaciones e invalidar el orden de prioridad estándar para forzar un cálculo específico.

### El Módulo `math`
Para realizar operaciones complejas que van más allá del núcleo básico de Python, se requiere importar librerías matemáticas predefinidas utilizando la instrucción `import math`.

Algunas de las funciones más relevantes del módulo son:
*   `math.sqrt(x)`: Calcula la raíz cuadrada de un número (devuelve un float).
*   `math.fabs(x)`: Devuelve el valor absoluto de un número real como float. *(Nota: Python dispone también de la función nativa `abs(x)` que mantiene el tipo original entero o float)*.
*   `math.floor(x)`: Redondea un número hacia abajo, al entero más próximo.
*   `math.ceil(x)`: Redondea un número hacia arriba, al entero más próximo.
*   `math.pi`: Constante matemática que devuelve el valor de π (`3.141592653589793`).

```python
import math

print(math.sqrt(25))  # Resultado: 5.0
print(math.floor(4.7)) # Resultado: 4
print(math.ceil(4.3))  # Resultado: 5
```

---

## 2. Operaciones Comparativas
Las operaciones de comparación evalúan las relaciones entre dos valores y devuelven **siempre** un tipo de dato booleano (`True` o `False`).

*   `==`: Igualdad. *(¡Cuidado! No confundir con el operador de asignación `=`).*
*   `!=`: Desigualdad o diferencia.
*   `>`: Mayor que.
*   `<`: Menor que.
*   `>=`: Mayor o igual que.
*   `<=`: Menor o igual que.

### Comportamientos específicos:
*   **Igualdad e Interferencia de Tipos:** Python considera que el entero `1` es igual al float `1.0` (`1 == 1.0` es `True`), así como `True == 1` y `False == 0` debido a su representación binaria subyacente. Sin embargo, comparar texto con números bajo igualdad simplemente devolverá `False` sin lanzar errores (ej: `6 == "cadena"` es `False`).

---

## 3. Operaciones con Booleanos (Álgebra de Boole)
Cuando se manejan múltiples criterios simultáneos, se recurre a las puertas lógicas que implementan el álgebra booleana. Las tres operaciones fundamentales en Python son:

*   **`and`**: Devuelve `True` **únicamente si todas** las condiciones evaluadas son verdaderas. Si una sola es falsa, el resultado es `False`.
*   **`or`**: Devuelve `True` si **al menos una** de las condiciones evaluadas es verdadera. Solo devuelve `False` si todas lo son.
*   **`not`**: Invierte el valor del booleano (el operador de negación). `not True` se convierte en `False` y viceversa.

### Reglas nemotécnicas de evaluación rápido:
```python
condicion_final = cond_1 and cond_2 and cond_3  # Requiere que TODO sea True
condicion_rapida = cond_1 or cond_2 or cond_3    # Basta con que UNO sea True
```

---

## 4. Funciones Built-in Comunes
Las funciones integradas (*Built-in*) vienen incorporadas por defecto dentro del intérprete de Python sin necesidad de importar librerías. Su sintaxis básica requiere pasar los datos necesarios dentro de sus paréntesis: `nombre_funcion(argumentos)`.

*   **`len(objeto)`**: Devuelve la cantidad de elementos o caracteres que posee una colección o cadena de texto.
*   **`max(argumentos / lista)`**: Identifica y extrae el valor máximo entre un conjunto de números o elementos de una lista.
*   **`min(argumentos / lista)`**: Identifica y extrae el valor mínimo entre un conjunto de números o elementos de una lista.

```python
lista = [23, 5, 8]
print(max(lista))  # Resultado: 23
print(len(lista))  # Resultado: 3
```

---

## 5. Métodos en Python
Un **método** es una función que le pertenece de forma exclusiva a un tipo de objeto o variable en concreto. Se invoca utilizando la sintaxis del punto: `objeto.metodo()`. 

*   **Importante:** Aunque el método no requiera parámetros o argumentos de entrada, **los paréntesis finales `()` son obligatorios** para forzar su ejecución.

### Métodos comunes para Cadenas de Texto (`str`):
*   `.upper()`: Transforma todo el texto a letras mayúsculas.
*   `.lower()`: Transforma todo el texto a letras minúsculas.
*   `.replace(antiguo, nuevo, [max_coincidencias])`: Reemplaza caracteres del string por unos nuevos. Por defecto modifica todas las apariciones a menos que se defina un límite numérico en el tercer argumento.
*   `.split(caracter)`: Divide una cadena de texto en múltiples partes utilizando el carácter indicado como separador, devolviendo los fragmentos guardados dentro de una lista.
*   `.index(caracter)`: Devuelve la posición de la primera coincidencia del carácter buscado dentro de la cadena.

```python
texto = "String de ejemplo"
print(texto.upper())        # "STRING DE EJEMPLO"
print(texto.split(' '))     # ['String', 'de', 'ejemplo']
```

---

## 6. Listas
Las listas son una de las colecciones de datos más versátiles e importantes en Python. Permiten agrupar y almacenar conjuntos de variables u objetos bajo una misma estructura. Sus elementos se separan por comas y se envuelven entre corchetes `[]`.

### Características principales:
1.  **Mutables:** Su contenido puede ser modificado, expandido, reordenado o eliminado después de haber sido creada en memoria.
2.  **Ordenadas:** Cada elemento tiene una posición fija e indexada.

### Reglas de indexación y acceso:
*   **Índice Base Cero:** El conteo de las posiciones de una lista comienza siempre desde el número **`0`**. El primer elemento está en el índice `0`, el segundo en el `1`, etc.
*   **Anidamiento:** Se pueden guardar listas dentro de otras listas. Para acceder a sus elementos internos se concatenan corchetes consecutivamente (ej: `lista[4][2]`).

```python
list_mix = ["texto", 1, 55.78, True]  # Permite almacenar tipos de datos distintos
list_mix[1] = 10                       # Modificación directa de un elemento
```

### Métodos característicos de las Listas:
*   `.append(elemento)`: Añade un elemento al final de la lista. *(Nota: Este método modifica la lista "in-place" y devuelve `None`).*
*   `.index(elemento)`: Devuelve la posición (índice) de la primera aparición del elemento especificado.
*   `.count(elemento)`: Cuenta cuántas veces se repite el elemento indicado dentro de la lista.
*   `.clear()`: Elimina por completo todos los elementos internos, dejando la lista vacía (`[]`).

---

## 7. Gestión de Errores Comunes

*   **`ZeroDivisionError: division by zero`**: Se genera al intentar realizar una división aritmética cuyo denominador sea estrictamente cero `0`. Las indeterminaciones matemáticas provocan caídas del programa.
*   **`ValueError: math domain error`**: Ocurre al solicitar una operación matemática fuera de su dominio real accesible, como intentar calcular la raíz cuadrada de un número negativo utilizando `math.sqrt()`.
*   **`TypeError: '>' not supported between instances...`**: Ocurre al intentar hacer comparaciones lógicas de magnitud (como mayor o menor que) entre variables de tipos incompatibles (ej: comparar un `float` con un `str`).
*   **`TypeError: 'bool' object is not subscriptable`**: Ocurre cuando se intenta utilizar corchetes de indexación `[]` sobre un tipo de dato primitivo que no es una colección (como un booleano o un entero).



<hr>







# Python: Flujos de Control, Bucles y Excepciones

Este repositorio contiene los mecanismos que permiten romper la ejecución puramente secuencial de un programa en Python. Aprenderás a tomar decisiones condicionales, repetir tareas de forma automática, controlar la interrupción de bucles y gestionar errores en tiempo de ejecución sin detener el programa.

---

## Índice
1. [Sintaxis de Línea e Indentación](#1-sintaxis-de-línea-e-indentación)
2. [Estructuras Condicionales (if / elif / else)](#2-estructuras-condicionales-if--elif--else)
3. [Estructura de Patrones (match / case)](#3-estructura-de-patrones-match--case)
4. [Bucle `for`](#4-bucle-for)
5. [Bucle `while`](#5-bucle-while)
6. [Sentencias de Control (`break` / `continue` / `pass`)](#6-sentencias-de-control-break--continue--pass)
7. [Control de Excepciones (try / except / finally)](#7-control-de-excepciones-try--except--finally)

---

## 1. Sintaxis de Línea e Indentación
A diferencia de otros lenguajes de programación que utilizan llaves `{}` o palabras clave como `end` para delimitar los bloques de código, **Python utiliza la indentación (tabulaciones o espacios)**.

*   **Estructura:** Cualquier sentencia que abra un bloque de control (`if`, `for`, `while`, `try`, etc.) termina obligatoriamente con **dos puntos `:`**. Todo el código que pertenezca a ese bloque debe estar desplazado hacia la derecha.
*   **Bloques anidados:** Si metes una estructura dentro de otra, el nivel de indentación se acumula (ej: un `if` dentro de un `for` requerirá doble tabulación).
*   **¿Tabulaciones o espacios?:** Aunque visualmente parecen similares, mezclar tabulaciones y espacios puede corromper el código al cambiar de editor. El estándar dictamina usar **4 espacios**. En entornos modernos como Jupyter Notebook, al pulsar la tecla `Tab`, el IDE lo traduce automáticamente a 4 espacios para mantener la transparencia y compatibilidad.

---

## 2. Estructuras Condicionales (`if` / `elif` / `else`)
Permiten bifurcar el camino que sigue el código evaluando operaciones booleanas. **Únicamente se ejecuta el primer bloque cuya condición devuelva `True`**; en ese instante, Python ignora por completo el resto de condiciones anidadas.

*   **`if`**: Condición inicial obligatoria.
*   **`elif`** (abreviación de *else if*): Permite evaluar nuevas condiciones de forma secuencial si las anteriores resultaron falsas. Se pueden añadir tantos como se necesiten.
*   **`else`**: Bloque opcional de salida por defecto; se ejecuta si y solo si ninguna de las condiciones previas fue verdadera.

### Ejemplo de flujo optimizado:
Al estructurar condicionales de forma secuencial limpia, no es necesario acotar los rangos numéricos por ambos extremos si ya vienen filtrados por el orden superior:

```python
nota = 7.5

if nota < 0 or nota > 10:
    print("Nota errónea") # Anticipación y control de errores
elif nota < 5:
    print("Suspenso")     # Ya sabemos que está entre 0 y 5
elif nota < 7:
    print("Bien")         # Ya sabemos que está entre 5 y 7
elif nota < 9:
    print("Notable")      # Ya sabemos que está entre 7 y 9
else:
    print("Sobresaliente")# Ya sabemos que está entre 9 y 10
```

---

## 3. Estructura de Patrones (`match` / `case`)
Introducido formalmente a partir de **Python 3.10** (*Structural Pattern Matching*), actúa de forma equivalente a la sentencia `switch` de otros lenguajes de programación. Ofrece una alternativa más limpia y legible que una sucesión interminable de bloques `if/elif`.

*   **Sintaxis:** Se evalúa una variable frente a múltiples escenarios (`case`).
*   **Caso por defecto (`case _`):** El guión bajo actúa como un comodín (*wildcard*) para capturar cualquier valor que no haya coincidido con los casos anteriores.

```python
day = "lunes"

match day:
    case "lunes":
        task = "Hacer la compra"
    case "martes":
        task = "Ir al gimnasio"
    case _:
        task = "Día no válido o descanso"
```

---

## 4. Bucle `for`
El bucle `for` se utiliza para **recorrer de forma iterativa los elementos de un objeto iterable** (como listas, tuplas o incluso cadenas de texto). Cuenta con una *variable de ejecución* interna que se actualiza automáticamente tomando el valor del elemento actual en cada vuelta.

### Formas fundamentales de iteración en Python:

1.  **Iteración Directa (`for elemento in lista`):**
    Accede directamente al valor de cada ítem. Es la forma más limpia, eficiente y recomendada si no necesitas conocer la posición numérica del elemento.
    ```python
    for fruta in ["manzana", "banana"]:
        print(fruta)
    ```

2.  **Por Índice (`for i in range(len(lista))`):**
    Utiliza la combinación de la función de longitud `len()` y de rango `range()` para generar una secuencia numérica de índices (0, 1, 2...). El elemento se debe extraer manualmente usando corchetes (`lista[i]`). Es útil si necesitas modificar elementos de la lista original basándote en su posición.
    ```python
    colores = ["rojo", "verde"]
    for i in range(len(colores)):
        print(i, colores[i])
    ```

3.  **Con Enumerate (`for i, elemento in enumerate(lista)`):**
    La forma óptima (*pythónica*) cuando necesitas trabajar tanto con el **índice numérico como con el valor** al mismo tiempo. Devuelve una estructura limpia en forma de tupla desempaquetada por cada iteración.
    ```python
    for index, name in enumerate(["Pedro", "Mariano"]):
        print(f"Posición {index}: {name}")
    ```

### Funciones auxiliares clave:
*   **`range(start, stop, step)`**: Genera un iterable numérico. El límite superior (*stop*) **nunca se incluye**. Admite pasos negativos para realizar cuentas regresivas.
    *   `range(6)` → `[0, 1, 2, 3, 4, 5]`
    *   `range(2, 6)` → `[2, 3, 4, 5]`
    *   `range(0, 6, 2)` → `[0, 2, 4]`
    *   `range(10, -1, -2)` → `[10, 8, 6, 4, 2, 0]`

---

## 5. Bucle `while`
Repite la ejecución de un bloque de código **mientras una condición lógica devuelva `True`**. A diferencia del `for`, el número de iteraciones no está predeterminado por el tamaño de una colección.

### Patrón estándar de implementación:
Para evitar **bucles infinitos** (que saturan el procesador y congelan el entorno de ejecución), se debe seguir rigurosamente este esquema de tres pasos:
1.  Declara e inicializa una **variable de control** fuera del bucle.
2.  Define una **condición límite** lógica en la cabecera del `while`.
3.  **Modifica/actualiza** la variable de control obligatoriamente en el cuerpo interno antes de terminar la iteración.

```python
i = 0  # 1. Inicialización
while i < 5:  # 2. Condición límite
    print(i)
    i = i + 1  # 3. Actualización de la variable
```

---

## 6. Sentencias de Control (`break` / `continue` / `pass`)
Son instrucciones que se colocan estratégicamente dentro de los bucles (`for` o `while`) para alterar el flujo normal de las iteraciones y optimizar el rendimiento del software.

*   **`break`**: Rompe forzadamente la ejecución del bucle por completo. Utilizado para detener búsquedas en colecciones masivas una vez que el objetivo ha sido localizado, evitando procesar miles de datos residuales innecesarios.
*   **`continue`**: Interrumpe la iteración actual y **salta inmediatamente al siguiente elemento del iterable**, ignorando todo el código que quede pendiente por ejecutar debajo de él dentro de esa vuelta.
*   **`pass`**: Una sentencia nula. No realiza ninguna acción operativa; se usa exclusivamente como marcador de posición (*placeholder*) cuando la sintaxis de Python exige tener código escrito en un bloque condicional o función pero aún no se ha implementado la lógica.

---

## 7. Control de Excepciones (`try` / `except` / `finally`)
Cuando ocurre un error crítico en Python (como consultar un índice que no existe con un `IndexError` o invocar una variable no declarada con un `NameError`), el programa detiene su ejecución por completo de forma abrupta. Las estructuras `try/except` permiten **capturar estos errores para controlarlos, tomar decisiones alternativas y dejar que el programa continúe funcionando**.

### Sintaxis Completa:
*   **`try`**: Envuelve el bloque de código sospechoso o impredecible que podría provocar un fallo.
*   **`except`**: Define la respuesta en caso de que ocurra un error dentro del bloque `try`. Se recomienda atrapar errores específicos en lugar de usar un bloque genérico. Se puede instanciar el error usando la palabra clave `as` para analizar su mensaje interno.
*   **`finally`**: Bloque opcional. **Se ejecuta siempre**, sin importar si el código funcionó correctamente o si saltó una excepción. Es sumamente útil para liberar recursos, cerrar conexiones a bases de datos o archivos abiertos.

```python
lista = [1, 2, 3]

try:
    print(lista[5])  # Forzamos un IndexError deliberado
except IndexError as error_detallado:
    print(f"Se ha controlado un error de índice: {error_detallado}")
except NameError:
    print("Error controlado en el nombre de una variable.")
except Exception as e:
    print(f"Cualquier otro tipo de error imprevisto: {e}")
finally:
    print("Fin del bloque de control. Esta línea se imprime pase lo que pase.")

print("El programa continúa su ejecución normal sin caerse.")
```
