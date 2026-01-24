"""
Video: https://www.youtube.com/shorts/W2qBeAdVH8Q

Para crear un programa que toma a una cadena de caracteres y que retorna caracteres que pueden ser mapeados de manera biyectiva a los movimientos del código Konami, podemos empezar con crear una función personalizada. En esa función, asignamos el código Konami y sus movimientos individuales a sus respectivas variables. Creamos un ciclo for con la longitud del parámetro de la función personalizada menos la longitud del código Konami más uno como su rango. En ese ciclo for, creamos una variable para almacenar la subcadena que es producida al pasar los caracteres del parámetro. Para determinar si la subcadena tiene la misma cantidad de caracteres únicos que el código Konami, usamos una sentencia condicional. Creamos una variable para almacenar el mapeo y otra para determinar si es biyectivo. Por medio de un ciclo for, la función zip() y una sentencia condicional determinamos si el parámetro se puede mapear de manera biyectiva. Con una sentencia condicional nos aseguramos que ningún carácter comparta movimientos. Después simplemente imprimimos.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
"""

def konami_mapping(cadena):
    codigo_konami = "UUDDLRLRBA"
    movimientos = set(codigo_konami)

    for i in range(len(cadena) - len(codigo_konami) + 1):
        subcadena = cadena[i:i+len(codigo_konami)]
        
        if len(set(subcadena)) == len(movimientos):
            mapeo = {}
            es_biyectivo = True
            for sub_car, konami_car in zip(subcadena, codigo_konami):
                if sub_car not in mapeo:
                    mapeo[sub_car] = konami_car
                elif mapeo[sub_car] != konami_car:
                    es_biyectivo = False
                    break

            if es_biyectivo and len(set(mapeo.values())) == len(mapeo.keys()):
                print(mapeo)

konami_mapping("xx2233454590yy11110")
konami_mapping("sduwahoda22ii0d0dbn")
