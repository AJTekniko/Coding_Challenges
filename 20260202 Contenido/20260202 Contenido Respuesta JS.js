/*
Video: youtube.com/shorts/kHv5cPoOjSA

Para crear una función en JavaScript que retorna el mes perfecto más reciente y el siguiente mes perfecto para el año Gregoriano proporcionado, creamos una variable para almacenar el primer día del mes de febrero como un objeto date en tiempo universal coordinado. Usamos el método getDay() para obtener el día de la semana de esa fecha y lo almacenamos en otra variable. Creamos una variable para almacenar la cantidad de años que se le necesitan restar al año proporcionado para producir el mes perfecto más reciente. Creamos una sentencia condicional que almacena el año actual en una variable si el primer día del mes de febrero ocurre en lunes o domingo, pero si no satisface esa condición, disminuye el año por uno hasta llegar al año en el que el mes de febrero empieza en lunes. También incrementa la variable que cuenta la cantidad de años que se le están restando por uno. Una vez que el mes perfecto es obtenido, almacena el año en una variable. Le sumamos la cantidad de años que fueron restados más uno para empezar el proceso de obtener el próximo mes perfecto. Usamos otra sentencia condicional con una lógica similar excepto que si el mes no es perfecto, incrementamos el año por uno hasta obtener el año con el mes perfecto y no almacenamos la cantidad de años agregados. Almacenamos el próximo mes perfecto. Después simplemente lo mandamos a la consola.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
*/

function nearestPerfectMonths(valorAnual){
  let primerDia = new Date(valorAnual + '-02-01T12:00:00Z');
  let diaDeLaSemana = primerDia.getDay();
  let cambio = 0;
  let anterior;
  let proximo;
    
  if (diaDeLaSemana == 0 || diaDeLaSemana == 1){
    anterior = valorAnual;
  }else{
    while (diaDeLaSemana != 1){
      valorAnual -= 1;
      primerDia = new Date(valorAnual + '-02-01T12:00:00Z');

      diaDeLaSemana = primerDia.getDay();
      cambio += 1;
    }
    anterior = valorAnual;
  }
    
  valorAnual += cambio + 1;
  primerDia = new Date(valorAnual + '-02-01T12:00:00Z');
  diaDeLaSemana = primerDia.getDay();

  if (diaDeLaSemana == 0 || diaDeLaSemana == 1){
    proximo = valorAnual;
  }else{
    while (diaDeLaSemana != 1){
      valorAnual += 1;
      primerDia = new Date(valorAnual + '-02-01T12:00:00Z');
      diaDeLaSemana = primerDia.getDay();
    }
    proximo = valorAnual;
  }

  console.log(`prev: "${anterior}-02", next: "${proximo}-02"`)
}

nearestPerfectMonths(2025);
nearestPerfectMonths(2026);
