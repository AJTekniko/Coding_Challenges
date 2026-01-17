/*
Video: https://www.youtube.com/shorts/6ZlKtAFMVek

Pregunta de Entrevista (Respuesta con JavaScript):

Para crear un programa en JavaScript que toma a una matriz de objetos y que retorna el nombre de los osos más hambrientos que el promedio en orden alfabético, podemos empezar con importar la matriz. Creamos una función personalizada. En esa función, obtenemos la cantidad de osos con la propiedad length y obtenemos la suma de los niveles de hambre por medio de la función reduce(). Almacenamos ambos en su respectiva variable. Después obtenemos el nombre de los osos más hambrientos que el promedio en orden alfabético utilizando los métodos filter(), map(), y sort(). Mandamos el resultado a la consola. Finalmente, llamamos la función personalizada.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
*/

import { osos } from "./ososJS.js";

function ososHambrientos(osos){
  let cantidad = osos.length, suma = osos.reduce((acumulador, osoActual) => {
    return acumulador + osoActual.hambre
  }, 0);
  console.log(osos.filter(oso => oso.hambre > suma/cantidad).map(oso => oso.nombre).sort());
}

ososHambrientos(osos);
