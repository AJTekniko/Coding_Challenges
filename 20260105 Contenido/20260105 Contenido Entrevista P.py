"""
Pregunta de entrevista:

¿Usted puede crear un programa que toma a una matriz de números enteros y suma cada elemento en orden? Suponiendo que el programa pueda reiniciar la calculación solamente una vez durante el proceso, lo que significa que el total actual se vuelve 0 y sigue con los siguientes elementos, por favor escriba un programa que pueda retornar el total máximo posible de cualquier matriz bajo esas condiciones.

Por ejemplo, la primer matriz que usted ve en pantalla debería de retornar 4, la segunda debería de retornar 10 y la última un cero. 

Próximamente se subirá un video con un ejemplo para esta pregunta.

Fuente de la pregunta: Cassidy Williams (Cassidoo)

"""

print("""> total_maximo([2, -1, 2, -5, 2, 2])
// reinicia después de -5
> 4""")

print("""> total_maximo([4, -10, 3, 2, -1, 6])// reinicia después de -10
> 10""")

print("""> total_maximo([-50, -2, -3])
// reinicia después de -3
> 0""")
