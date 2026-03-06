"""
Video: youtube.com/shorts/_3sAwx8a7Uo

Para encontrar el elemento mayoritario de una matriz (aquel que aparece más que n/2 veces) en tiempo de orden lineal O(n) y espacio de orden constante O(1) sin utilizar mapas hash, creamos una función personalizada. Creamos dos variables: una para almacenar el elemento candidato y la otra para almacenar la cuenta. Usamos un ciclo for para pasar los elementos de la matriz por sentencias condicionales. Después imprimimos el elemento mayoritario.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
"""

def majority_element(matriz):
    candidato = None
    cuenta = 0

    for elemento in matriz:
        if cuenta == 0:
            candidato = elemento
            cuenta += 1
        elif elemento == candidato:
            cuenta += 1
        else:
            cuenta -= 1

    print(candidato)

majority_element([2, 2, 1, 1, 2, 2, 1, 2, 2])
majority_element([3, 3, 4, 2, 3, 3, 1])
