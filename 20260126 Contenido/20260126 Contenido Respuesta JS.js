/*
Video: youtube.com/shorts/cexm6olJAC0

Para crear un programa con JavaScript que analiza una cadena de caracteres en minúsculas con un espacio entre cada palabra para determinar cuántas vocales existen en la primera palabra, y para invertir las palabras sucesivas que tienen la misma cantidad de vocales, creamos una función personalizada. Creamos una función flecha que retorna la cantidad de vocales que existen en la palabra pasada como argumento. En la función flecha, creamos una variable para almacenar la cuenta de vocales en la palabra, creamos una variable para las vocales del abecedario, y por medio de un ciclo for y una sentencia condicional, se suma la cantidad de vocales que existen en la palabra. Asignamos la primera palabra y la cuenta de sus vocales en sus respectivas variables. Creamos un ciclo for para evaluar las palabras e invertirlas si tienen la misma cantidad de vocales que la primera palabra. Después simplemente mandamos el resultado reunido por medio del método join() a la consola.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
*/

function flippedy(cadena){
  const cuentaVocales = (palabra) => {
    let cuenta = 0;
    const vocales = "aeiou";
    for (let caracter of palabra) {
      if (vocales.includes(caracter)) {
        cuenta++;
      }
    }
    return cuenta;
  };

  let palabras = cadena.split(" ");

  const primeraPalabra = palabras[0];
  const primeraCuenta = cuentaVocales(primeraPalabra);

  for (let i = 1; i < palabras.length; i++) {
    let palabraProc = palabras[i];
    if (cuentaVocales(palabraProc) === primeraCuenta) {
      palabras[i] = palabraProc.split("").reverse().join("");
    }
  }
  
  console.log(palabras.join(" "));
}

flippedy("cat and mice");
flippedy("banana healthy");
