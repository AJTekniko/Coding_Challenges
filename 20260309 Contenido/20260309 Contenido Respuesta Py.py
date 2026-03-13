"""
Video: youtube.com/shorts/avinti9CIQM

Se puede retornar la cantidad mínima de cambios necesarios para transformar una cadena de caracteres en una cadena alterna, o -1 si es imposible, creando una función personalizada. Calculamos la cantidad de veces que aparecen las dos letras en la cadena y la almacenamos en su respectiva variable. Creamos una lista con el contenido de la cadena de caracteres. Creamos una variable para almacenar la cantidad de cambios necesarios. Usamos una sentencia condicional para determinar si sería posible producir una cadena alterna. Si la diferencia absoluta es mayor que uno, no sería posible y produce -1. Usamos otra sentencia condicional para determinar si la cadena contiene un número par o impar de caracteres. Si es impar, la primera letra necesita ser la letra mayoritaria. Si es par, empezamos la nueva secuencia con la primera letra de la cadena original. Creamos un ciclo for que anticipa letras alternas. Si las letras en la secuencia no cumplen con sus condiciones, calcula la diferencia, la almacena, y mueve las letras a sus posiciones correctas. Después imprimimos la cantidad de cambios necesarios.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
"""

def min_swaps_to_alternate(s):
    cuenta_a = s.count("a")
    cuenta_b = s.count("b")
    serie_cambiada = list(s)
    cambios = 0

    if abs(cuenta_a - cuenta_b) > 1:
        print(-1)
        return

    if len(s) % 2 != 0:
        letra_mayoritaria = max(cuenta_a, cuenta_b)
        letra_anticipada = letra_mayoritaria
    else:
        letra_anticipada = s[0]

    for i in range(len(s)):
        if serie_cambiada[i] == letra_anticipada:
            if letra_anticipada == "a":
                letra_anticipada = "b"
            elif letra_anticipada == "b":
                letra_anticipada = "a"
        else:
            indice = serie_cambiada.index(letra_anticipada, i)
            cambios += indice - i
            letra_removida = serie_cambiada.pop(indice)
            serie_cambiada.insert(i, letra_removida)
            if letra_anticipada == "a":
                letra_anticipada = "b"
            elif letra_anticipada == "b":
                letra_anticipada = "a"

    print(cambios)
    return

min_swaps_to_alternate('aabb')
min_swaps_to_alternate('aaab')
min_swaps_to_alternate('aaaabbbb')
