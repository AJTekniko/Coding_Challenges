/*
Video: https://www.youtube.com/shorts/fPQlU_ztylQ

Para crear un programa con JavaScript que toma a una cadena de caracteres y que retorna caracteres que pueden ser mapeados de manera biyectiva a los movimientos del código Konami, podemos empezar con crear una función personalizada. En esa función, asignamos el código Konami y sus movimientos individuales a sus respectivas variables. Creamos un ciclo for que comienza en cero y continúa mientras es menor que la longitud del parámetro de la función personalizada menos la longitud del código Konami más uno. En ese ciclo for, creamos variables para almacenar la subcadena que es producida al pasar los caracteres del parámetro y sus movimientos individuales. Para determinar si la subcadena tiene la misma cantidad de caracteres únicos que el código Konami, usamos una sentencia condicional. Creamos variables para almacenar el mapeo, para determinar si la cadena es biyectiva y para almacenar los movimientos que ya han sido usados. Por medio de un ciclo for y sentencias condicionales, determinamos si el parámetro se puede mapear de manera biyectiva y si ningún carácter comparte movimientos, y también almacenamos los caracteres del mapeo. Una vez que eso es confirmado, lo mandamos a la consola.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
*/

function konamiMapping(cadena){
  const codigoKonami = "UUDDLRLRBA";
  const movimientos = new Set(codigoKonami);

  for (let i = 0; i < cadena.length - codigoKonami.length + 1; i++){
    let subcadena = cadena.slice(i, i + codigoKonami.length);

    let subcadenaMovimientos = new Set(subcadena);   
    if (subcadenaMovimientos.length == movimientos.length){
      let mapeo = {};
      let esBiyectivo = true;
      let movimientosUsados = new Set();

      for (let j = 0; j < codigoKonami.length; j++){
        let caracterSC = subcadena[j];
        let movimientoCK = codigoKonami[j];
          
        if (mapeo[caracterSC]) {
          if (mapeo[caracterSC] !== movimientoCK) {
            esBiyectivo = false;
            break;
          }
        } else {
            if (movimientosUsados.has(movimientoCK)) {
              esBiyectivo = false;
              break;
            }
            mapeo[caracterSC] = movimientoCK;
            movimientosUsados.add(movimientoCK);
          }
      }
        
      if (esBiyectivo && movimientosUsados.size === movimientos.size) {
          console.log(mapeo);
        
      }
    }
  }
}

konamiMapping("xx2233454590yy11110")
konamiMapping("sduwahoda22ii0d0dbn")
