def dias_semana (num:int) -> str:
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    resultado = ""

    if type(num) != int:
        return "Se debe introducir un número entero comprendido entre 1 y 7" 
    else:
        if num > 7 or num < 1:
            return "El número de la semana debe estar comprendido entre 1 y 7"
        else:
            resultado = dias[num - 1]
    
    return resultado



def piramide_invertida(num_filas: int):

    for indice in range(num_filas, 0, -1):
        #print("Indice",indice)
        fila = []
        
        for digito in range(indice, 0, -1):
            #print("Dígito", digito)
            fila.append(str(digito))
        
        print(" ".join(fila))




def compara_dos_numeros(num1:int, num2:int) -> str:
    resultado = ""

    if num1 == num2:
        resultado = "Los 2 números introducidos (" + str(num1) + " y " + str(num2) + ") son iguales."
    else:
        if num1 > num2:
            resultado = "El primer número (" + str(num1) + ") es mayor que el segundo número (" + str(num2) + ")."
        else:
            resultado = "El segundo número (" + str(num2) + ") es mayor que el primer número (" + str(num1) + ")."
        
    return resultado




def contador_de_letras(texto: str, letra: str) -> int:
    
    resultado = 0

    texto_minusculas = texto.lower()
    letra_minusculas = letra.lower()
    
    resultado = texto_minusculas.count(letra_minusculas)

    return resultado




def contador_letras(texto: str) -> dict:

    texto = texto.lower()
    resultado = {}
    
    for letra in texto:
        if letra != " ": # descarto los espacios en blanco, pero procesaremos dígitos y símbolos de caracteres como una letra
            if letra in resultado: #si la letra ya ha sido procesada antes en el diccionario
                resultado[letra] = resultado[letra] + 1 #incrementamos en 1 el valor de su clave
            else: # primera aparición de la letra, 
                resultado[letra] = 1 # creamos la clave de letra inicializando a 1 su valor
                
    return resultado



def actualiza_lista(lista:list, comando:str, elemento=None) -> list:
    
    if comando == "add":
        lista.append(elemento)
    else:
        if comando == "remove":
            if elemento in lista:
                lista.remove(elemento)
            
    return lista




def genera_frase(*palabras: str) -> str:

    resultado = " ".join(palabras)
    return resultado




def fibonacci(n: int) -> int:
    """ 
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
    """

    secuencia = [0, 1] # los dos primeros números de la secuencia

    # añadimos números hasta llegar a la posición n
    while len(secuencia) <= n:
        siguiente_numero = secuencia[-1] + secuencia[-2] # Sumamos los dos últimos números de la lista
        secuencia.append(siguiente_numero)

    print(secuencia)    

    return secuencia[n]



def area_cuadrado(lado:float) -> float:
    resultado = lado*lado # El área de un cuadrado es lado X lado ; o lado al cuadrado
    # resultado = lado**2 
    return resultado

def area_triangulo(base:float, altura:float) -> float:
    resultado = (base*altura) / 2 # El área de un triángulo se calcula multiplicando la base por la altura y dividiendo el resultado entre dos
    return resultado

def area_circulo(radio:float) -> float:
    pi = 3.1416
    resultado = pi * (radio**2) # El área de un círculo se calcula multiplicando el número pi por el cuadrado de su radio
    return resultado