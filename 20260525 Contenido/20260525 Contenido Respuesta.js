/*
Video: youtube.com/shorts/I_dZ6XprcCU

Se puede mover cada enésimo cliente al final de una línea y mantener el orden relativo por medio de una función personalizada. Considere el siguiente ejemplo. Creamos una sentencia condicional para tratar con el número entero n para que no cause problemas en la función. Creamos dos variables para almacenar matrices: una para los clientes que se quedan fijos y la otra para los que son movidos. Creamos un ciclo for para recorrer los valores en la cola de clientes, y utilizamos sentencias condicionales para determinar cuales se quedarán en su posición y cuales serán movidos. Una vez que todos los clientes han sido evaluados, mandamos las dos matrices a la consola.

Fuente de la pregunta: Cassidy Williams (Cassidoo)
*/

function shuffleLine(cola, n) {
    if (n < 1) { 
        console.log([...cola]);
        return
    }

    let fijo = [];
    let movido = [];

    for (let i = 0; i < cola.length; i++) {
        if ((i + 1) % n === 0) {
            movido.push(cola[i]);
        } else {
            fijo.push(cola[i]);
        }
    }
    console.log([...fijo, ...movido]);
}

shuffleLine(["Ada", "Ben", "Cam", "Diya", "Eli", "Fay"], 3);
shuffleLine(["A", "B", "C", "D", "E"], 2);
shuffleLine(["Mo", "Noah", "Oli"], 1);
