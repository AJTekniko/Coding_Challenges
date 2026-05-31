/*
Video: youtube.com/shorts/VkGv9_1DiFo

Se puede cambiar cada letra minúscula a mayúscula y vice versa en una cadena de caracteres s por medio de una función personalizada. Considere el siguiente ejemplo. Creamos una variable que puede ser utilizada como el segundo argumento en caso de que queramos texto alternado. En esa función, creamos una variable para almacenar el resultado. Creamos una sentencia condicional para determinar si la función va a producir texto con las mayúsculas y minúsculas intercambiadas, o si va a producir texto alternado. Si es para texto alternado, en esa sentencia condicional creamos una variable para mantener la cuenta, y creamos un ciclo for para recorrer todos los caracteres de la cadena. En ese ciclo for, creamos una sentencia condicional para recrear el texto del ejemplo de la pregunta. Solamente aumenta la cuenta con las letras de la cadena. Si es determinado que la función va a producir texto con las mayúsculas y minúsculas intercambiadas, creamos un ciclo for para recorrer todos los caracteres de la cadena y por medio de sentencias condicionales, modificamos las letras. Después mandamos el resultado a la consola.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
*/

let alternating = true;

function toggleChar(cadena, alternacion) {
  let resultado = "";
  if (alternacion) {
    let cuenta = 0;
    for (let caracter of cadena) {
      if (cuenta % 2 === 0) {
        resultado += caracter.toUpperCase();
        if (caracter.toLowerCase() !== caracter.toUpperCase()) {
        cuenta += 1
        }
      } else {
        resultado += caracter.toLowerCase();
        if (caracter.toLowerCase() !== caracter.toUpperCase()) {
        cuenta += 1
        }
      }
    }
  } else {
    for (let caracter of cadena) {
      if (caracter === caracter.toUpperCase()) {
        resultado += caracter.toLowerCase();
      } else {
        resultado += caracter.toUpperCase();
      }
    }
  }
  console.log(resultado);
}


toggleChar("Hello, world!");
toggleChar("HeheHeheHEheheHeH");
toggleChar("This will be alternated", alternating);
