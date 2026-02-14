/*
Video: youtube.com/shorts/UT4AEEEQ4TM

Para crear un programa en JavaScript que toma una matriz de números enteros y un número proporcionado, y que mueve todos los números de la matriz idénticos al número proporcionado hasta el final sin afectar el orden relativo de los demás números, creamos una función personalizada. Creamos una variable para almacenar la cantidad de veces que se encuentra el número proporcionado en la matriz, y por medio de un ciclo for calculamos esa cantidad. Creamos un ciclo for para remover el número proporcionado de la matriz con el método splice(), y otro ciclo for para agregarlo al final de la matriz con el método push(). Después mandamos el resultado a la consola.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
*/

function moveNums(matriz, n){
  let cuenta_n = 0;

  for (let valor in matriz){
    if (matriz[valor] == n){
      cuenta_n++;
    }
  }

  for (let i = 0; i < cuenta_n; i++){
    let indice = matriz.indexOf(n);
    matriz.splice(indice,1);
  }
    
  for (let i = 0; i < cuenta_n; i++){
    matriz.push(n);
  }

  console.log(matriz);
}

moveNums([0,2,0,3,10], 0);
