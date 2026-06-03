"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
mensaje = "Hola, Mundo!"
print(mensaje)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
mensaje = "Hello world!"
print(mensaje)
#Hemos cambiado la frase Hola mundo al inglés

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
texto = "Banana"
entero = 47
flotante = 19.9
boleano= True
lista = ["perro", "gato", "conejo"]
tupla = ("amarillo", "azul", "rojo")
diccionario ={
    "Nombre": "Irma",
     "Edad": 47,
    "Documento": 2346765
}
animales_domesticos = {"perro", "gato", "conejo", "perro"}

print(texto)
print(type(texto))
print(entero)
print(type(entero))
print(flotante)
print(type(flotante))
print(boleano)
print(type(boleano))
print(lista)
print(type(lista))
print(tupla)
print(type(tupla))
print(diccionario)
print(type(diccionario))
print(animales_domesticos)
print(type(animales_domesticos))






