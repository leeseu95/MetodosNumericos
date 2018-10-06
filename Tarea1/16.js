/* eslint no-loop-func: "off" */
/*
Una cierta compañía posee un gran número de máquinas en uso.
El tiempo que dura en operación cada una de estas máquinas,
sigue la siguiente distribución de probabilidad:

Tiempo entre descomposturas (horas) -> Probabilidad
6-8 -> 0.10       TODO: 6-8 es 7?
8-10 -> 0.15
10-12 -> 0.24
12-14 -> 0.26
16-18 -> 0.18
18-20 -> 0.07

El tiempo que un operador se tarda en reparar una máquina,
sigue la siguiente distribución de probabilidad:

Tiempo de reparación (horas) -> Probabilidad
2-4 -> 0.15
4-6 -> 0.25
6-8 -> 0.30
8-10 -> 0.20
10-12 -> 0.10

Si el costo de tener una máquina ociosa durante una hora es de
($500), y el salario por hora para este tipo de operarios es de ($50),
¿cuántas máquinas se deben asignar a cada mecánico para que las atienda?

Sugerencia: Minimice el costo de tener la máquina ociosa,
más el salario del mecánico dividido por el número de maquinas
atendidas.
*/

// CONFIG
const horasDeSimulacion = 1000;
const numMaquinas = 50;

function calcularTiempoAleatorio(whichTime) {
    const numAleatorio = Math.random();
    const rangos = [
        [0.93, 0.75, 0.49, 0.25, 0.10], // Probabilidad de morir
        [0.90, 0.70, 0.40, 0.15], // Probabilidad de reparacion
    ];
    const valores = [
        [19, 17, 13, 11, 9, 7],
        [11, 9, 7, 5, 3],
    ];
    let time = valores[whichTime][0];
    rangos[whichTime].forEach((rango, index) => {
        if (numAleatorio < rango) time = valores[whichTime][index + 1];
    });
    return time;
}

// Creamos las primeras maquinas con el tiempo que van a durar antes de morir
// Si una máquina tiene un valor positivo, quiere decir que está funcionando
// si tiene un valor negativo, quiere decir que la están reparando
let maquinas = [];
for (let i = 0; i < numMaquinas; i += 1) {
    const tiempoAntesDeMorir = calcularTiempoAleatorio(0);
    maquinas.push(tiempoAntesDeMorir);
}

let horasOciosas = 0;
let maxDeadMachines = 0;
const deadMachinesPerHour = [];

// Loop que corre por 1,000 horas con 50 máquinas
for (let horas = 0; horas < horasDeSimulacion; horas += 1) {
    // Contamos cuántas máquinas están descompuestas a la vez
    const deadMachines = maquinas.reduce((acc, cur) => {
        if (cur < 0) return acc + 1;
        return acc;
    }, 0);

    if (deadMachines > maxDeadMachines) maxDeadMachines = deadMachines;
    deadMachinesPerHour.push(deadMachines);

    // Pasa una hora para todas las máquinas
    maquinas = maquinas.map((tiempo) => {
        // Si la máquina está por morir, tenemos que calcular cuánto va a tardar
        // el mecánico en repararla
        if (tiempo === 1) {
            const tiempoDeReparacion = calcularTiempoAleatorio(1);
            return -1 * tiempoDeReparacion;

        // Si la máquina esta por terminar de ser reparada, tenemos que calcular
        // cuánto tiempo va a funcionar antes de morir
        } else if (tiempo === -1) {
            horasOciosas += 1;
            const tiempoAntesDeMorir = calcularTiempoAleatorio(0);
            return tiempoAntesDeMorir;

        // Si el valor es positivo le restamos 1
        } else if (tiempo > 1) {
            return tiempo - 1;
        }

        // Si el valor es negativo le sumamos 1
        horasOciosas += 1;
        return tiempo + 1;
    });
}

function numberWithCommas(x) { return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); }

const costoHorasOciosas = horasOciosas * 500;
const salarioMecanicos = horasOciosas * 50;

console.log('Simulación corrida por 1,000 horas con 50 máquinas:\n');
console.log('Horas Ociosas en Total: ', numberWithCommas(horasOciosas));
console.log('Costo por Horas Ociosas: $', numberWithCommas(costoHorasOciosas));
console.log('Costo del Salario de los mecánicos: $', numberWithCommas(salarioMecanicos));
console.log('maxDeadMachines: ', maxDeadMachines);
