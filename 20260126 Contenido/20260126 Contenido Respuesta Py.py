"""
Video: https://www.youtube.com/shorts/5VoqeGmhwjM

Para crear un programa que analiza una cadena de caracteres en minúsculas con un espacio entre cada palabra para determinar cuántas vocales existen en la primera palabra, y para invertir las palabras sucesivas que tienen la misma cantidad de vocales creamos una función personalizada. Usamos el método split() para separar la cadena en palabras individuales y asignarlas a una variable. Usamos una sentencia condicional para tratar con cadenas vacías. Creamos una variable para almacenar las vocales. Obtenemos la primera palabra de la cadena de caracteres y la almacenamos en una variable. Por medio de la función sum() y una lista de comprensión, obtenemos la cantidad de vocales en la primera palabra. Creamos una lista para almacenar las palabras en la cadena una vez que han sido procesadas. Creamos un ciclo for para evaluar el resto de las palabras e invertirlas si tienen la misma cantidad de vocales que la primera palabra. Después simplemente imprimimos el resultado unido por medio del método join() con un espacio entre cada palabra.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
"""

def flippedy(cadena):
    palabras = cadena.split()
    if not palabras:
        return ""

    vocales = "aeiou"

    primera_palabra = palabras[0]
    primera_cuenta = sum(1 for caracter in primera_palabra if caracter in vocales)

    palabras_proc = [primera_palabra]

    for palabra in palabras[1:]:
        cuenta_vocales = sum(1 for caracter in palabra if caracter in vocales)
        if cuenta_vocales == primera_cuenta:
            palabras_proc.append(palabra[::-1])
        else:
            palabras_proc.append(palabra)

    print(" ".join(palabras_proc))

flippedy("cat and mice") 
flippedy("banana healthy")
