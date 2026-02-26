"""
Video: youtube.com/shorts/p6SGqRa8_OA

Para encontrar la submatriz contigua de una matriz de números enteros que contiene la suma más grande y retornar dicha suma, creamos dos variables para almacenar la suma actual y la suma máxima; les asignamos cero e infinito negativo respectivamente. Creamos un ciclo for para encontrar el elemento mayor entre dos argumentos por medio de la función max(). Empezamos por comparar el elemento de la submatriz y el valor de la suma actual más el elemento, y le asignamos el mayor valor a la variable que contiene la suma actual. Luego comparamos la variable que contiene la suma máxima y la variable que contiene la suma actual, y le asignamos el mayor valor a la variable que contiene la suma máxima. Después imprimimos la matriz. 

Fuente de la pregunta: Cassidy Williams (Cassidoo)
"""

def max_subarray_sum(matriz):
    suma_actual = 0
    suma_maxima = float("-inf")

    for num in matriz:
        suma_actual = max(num, suma_actual + num)
        suma_maxima = max(suma_maxima, suma_actual)
    
    print(suma_maxima)
    
max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
max_subarray_sum([5])
max_subarray_sum([-1, -2, -3, -4])
max_subarray_sum([5, 4, -1, 7, 8])
