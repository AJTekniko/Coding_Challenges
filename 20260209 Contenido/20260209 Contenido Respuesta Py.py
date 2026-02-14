"""
Video: youtube.com/shorts/oOVYP_u63Jc

Para crear un programa que toma una matriz de números enteros y un número proporcionado, y que mueve todos los números de la matriz idénticos al número proporcionado hasta el final sin afectar el orden relativo de los demás números, creamos una función personalizada. Creamos una variable para almacenar la cantidad de veces que se encuentra el número proporcionado en la matriz, y por medio del método count() calculamos esa cantidad. Creamos un ciclo for para remover el número proporcionado de la matriz con el método remove(), y otro ciclo for para agregarlo al final de la matriz con el método append(). Después imprimimos el resultado.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
"""

def move_nums(matriz, n):
    cuenta_n = matriz.count(n)

    for _ in range(cuenta_n):
        matriz.remove(n)
        
    for _ in range(cuenta_n):
        matriz.append(n)

    print(matriz)

move_nums([0,2,0,3,10], 0)
