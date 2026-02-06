"""
Video: youtube.com/shorts/BFg_-6QWMXU

Para crear una función que retorna el mes perfecto más reciente y el siguiente mes perfecto para el año Gregoriano proporcionado, creamos una variable para almacenar el primer día del mes de febrero como un objeto date. Usamos weekday() para obtener el día de la semana de esa fecha y lo almacenamos en otra variable. Creamos una variable para almacenar la cantidad de años que se le necesitan restar al año proporcionado para producir el mes perfecto más reciente. Creamos una sentencia condicional que almacena el año actual en una variable si el primer día del mes de febrero ocurre en lunes o domingo, pero si no satisface esa condición, disminuye el año por uno hasta llegar al año en el que el mes de febrero empieza en lunes. También incrementa la variable que cuenta la cantidad de años que se le están restando por uno. Una vez que el mes perfecto es obtenido, almacena el año en una variable. Le sumamos la cantidad de años que fueron restados más uno para empezar el proceso de obtener el próximo mes perfecto. Usamos otra sentencia condicional con una lógica similar excepto que si el mes no es perfecto, incrementamos el año por uno hasta obtener el año con el mes perfecto y no almacenamos la cantidad de años agregados. Almacenamos el próximo mes perfecto. Después simplemente imprimimos.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
"""

from datetime import date

def nearest_perfect_months(valor_anual):
    primer_dia = date(valor_anual, 2, 1)
    dia_de_la_semana = primer_dia.weekday()
    cambio = 0
    
    if dia_de_la_semana == 0 or dia_de_la_semana == 6:
        anterior = valor_anual
    else:
        while dia_de_la_semana != 0:
            valor_anual -= 1
            primer_dia = date(valor_anual, 2, 1)

            dia_de_la_semana = primer_dia.weekday()
            cambio += 1

        anterior = valor_anual
    
    valor_anual += cambio + 1
    primer_dia = date(valor_anual, 2, 1)
    dia_de_la_semana = primer_dia.weekday()

    if dia_de_la_semana == 0 or dia_de_la_semana == 6:
        proximo = valor_anual
    else:
        while dia_de_la_semana != 0:
            valor_anual += 1
            primer_dia = date(valor_anual, 2, 1)
            dia_de_la_semana = primer_dia.weekday()
        proximo = valor_anual

    print(f'prev: "{anterior}-02", next: "{proximo}-02"')

nearest_perfect_months(2025)
nearest_perfect_months(2026)
