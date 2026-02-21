"""
Video: youtube.com/shorts/MoMrV-IoxsA

Para escribir una función que se amplía por el factor k >= 2 en un bloque k x k que contiene el mismo valor, creamos una sentencia condicional para determinar si el factor es menor que dos. Si sí es menor que dos, imprime un mensaje indicando que el factor de ampliación k necesita ser mayor o igual a dos y termina la función por medio de return. Creamos una variable para almacenar la nueva matriz. Creamos un ciclo for en el que se crean las filas necesarias y se agregan a la nueva matriz. Después imprimimos la matriz. 

Fuente de la pregunta: Cassidy Williams (Cassidoo)
"""

def zoom(matriz, factor):
    if factor < 2:
        print("El factor necesita ser >= 2")
        return

    ampliado = []
    for fila in matriz:
        fila_ampliada = [celda for celda in fila for _ in range(factor)]
        for _ in range(factor):
            ampliado.append(fila_ampliada)

    print(ampliado)

zoom([[1,2],[3,4]], 2)
zoom([[7,8,9]], 3)
zoom([[1],[2]], 3)
