"""
Video: https://www.youtube.com/shorts/cKTV3OpEHcg

Pregunta de Entrevista (Respuesta con Python):

Para crear un programa que toma a una matriz de objetos y que retorna el nombre de los osos más hambrientos que el promedio en orden alfabético, podemos empezar con importar la matriz. Creamos una función personalizada. En esa función, obtenemos la suma de los niveles de hambre por medio de la función sum() y una lista de comprensión. También obtenemos la cantidad de osos. Almacenamos ambos en su respectiva variable. Después imprimimos el nombre de los osos más hambrientos que el promedio en orden alfabético, el cual se obtiene por medio de una lista de comprensión anidada dentro de la función sort(). Finalmente, llamamos la función personalizada.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
"""

from osos_py import osos

def osos_hambrientos(osos):
    suma, cantidad = sum(oso['hambre'] for oso in osos), len(osos)
    print(sorted([oso["nombre"] for oso in osos if oso["hambre"] > suma/cantidad]))

osos_hambrientos(osos)
