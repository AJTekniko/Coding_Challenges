/*Pregunta de Entrevista (Respuesta con JavaScript):

Para crear un programa en JavaScript que toma a una matriz de números enteros y suma cada elemento en orden con solamente un reinicio permitido, podemos empezar con crear una función personalizada. Encontramos el valor más bajo de la matriz utilizando el método Math.min() y su posición en la matriz con el método indexOf(). Creamos variables para almacenar la suma y los reinicios permitidos. Creamos un ciclo for para sumar el valor más bajo de la matriz y los valores anteriores. Creamos otro ciclo for para tratar con los números que faltan, pero con una sentencia condicional con tres condiciones: que el siguiente número sea positivo, que la suma actual sea negativa y que la cantidad de reinicios sea mayor que cero. Si se satisfacen esas tres condiciones, usamos el reinicio que tenemos y la suma baja a cero. De otro modo, agregamos el valor a la suma. Una vez que ya sumamos todos los números, evaluamos la suma por medio de una sentencia condicional para saber si es un número negativo y si todavía tenemos un reinicio permitido. Si así es el caso, reiniciamos la suma. Después simplemente lo mandamos a la consola.

Fuente de la pregunta: Cassidy Williams (Cassidoo)*/

function total_maximo(puntos){
    let numero_bajo = Math.min(...puntos);
    let numero_bajo_loc = puntos.indexOf(numero_bajo, 0);
    let suma = 0;
    let reinicios = 1;
    for (let i = 0; i < numero_bajo_loc + 1; i++){
        suma += puntos[i];
    }
    for (let i = numero_bajo_loc + 1; i < puntos.length; i++){
        if (suma + puntos[i] > suma && suma < 0 && reinicios > 0){
            suma = 0;
            reinicios -= 1;
        }
        suma += puntos[i];
    }
    if (suma < 0 && reinicios > 0){
        suma = 0;
        reinicios -= 1;
    }
    console.log(suma)
}

total_maximo([2, -1, 2, -5, 2, 2])
total_maximo([4, -10, 3, 2, -1, 6])
total_maximo([-50, -2, -3])
