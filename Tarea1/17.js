/*
Una cadena de supermercados es abastecida por un almacén
central. La mercancía que llega a este almacén es descargada en
turnos nocturnos. Los camiones que se descargan en este almacén
llegan en forma aleatoria de acuerdo a un proceso poisson a
una razón media de (2 camiones por hora). El tiempo que un equipo
de (3 trabajadores) se tarda en descargar un un camión,
sigue una distribución uniforme entre (20 y 30 minutos). Si el número
de trabajadores en el equipo incrementa, entonces la razón de
servicio se incrementa. Por ejemplo, si el equipo está formado
por (4 trabajadores), el tiempo de servicio está uniformemente
distribuido (entre 15 y 25 minutos); si el equipo está formado
por (5 trabajadores), el tiempo de servicio está uniformemente
distribuido (entre 10 y 20 minutos) y si el equipo está formado por
(6 trabajadores), el tiempo de servicio está uniformemente distribuido
(entre 5 y 15 minutos). Cada trabajador recibe ($25 por hora) durante
el turno nocturo de (8 horas). El costo de tener un camión
esperando se estima en ($50 por hora).

El administrador del almacén desea saber cuál es el tamaño óptimo del equipo.
*/

const probLlegaCamionEnMinuto = 2 / 60; // Si la probabilidad es 2 camiones / 60 minutos
const costoEsperaCamionMinuto = 50 / 60; // $50 por hora
const costoTrabajadorMinuto = 25 / 60; // $25 por hora
const minutosEnElTurnoConst = 8 * 60;
const totalDeCamionesQueLlegaron = [0, 0, 0, 0];
const gastos = [0, 0, 0, 0];

let lastBus = true;
// Generamos los valores random, para poder usar los mismo con las diferentes iteraciones
const random = [];
for (let i = 0; i < minutosEnElTurnoConst; i += 1) random.push(Math.random());

// Hacemos un loop para checar gastos con diferentes números de trabajadores
for (let numTrabajadores = 3; numTrabajadores <= 6; numTrabajadores += 1) {
    // El index de los arreglos en donde se va a guardar la información
    const index = numTrabajadores - 3;
    let minutosEnElTurno = minutosEnElTurnoConst; // El turno es de 8 horas
    const queueCamiones = [];

    // Un loop que corra por tantos minutos como se va a trabajar
    for (let minutos = 0; minutos < minutosEnElTurno; minutos += 1) {
        // Se calculan gastos en pagos a trabajadores
        gastos[index] += numTrabajadores * costoTrabajadorMinuto;

        // TODO: preguntar qué pasa si al final del turno hay camiones en queue y qué pasa si siguen llegando?
        // Cuánto se les paga la hora extra?
        if (minutos === minutosEnElTurno - 1 && queueCamiones[0] && lastBus) {
            minutosEnElTurno += queueCamiones[0];
            lastBus = false;
        }

        // Pasa un minuto de descarga para el primer camión en el queue
        if (queueCamiones.length) {
            queueCamiones[0] -= 1;
            // Calculamos cuánto pagamos por los camiones que están en espera (-1 porque uno sí está siendo descargado)
            gastos[index] += (queueCamiones.length - 1) * costoEsperaCamionMinuto;
            // Si ya paso todo el tiempo de descarga, sale el camión del queue
            if (queueCamiones[0] === 0) queueCamiones.splice(0, 1);
        }

        // Checamos si llega un camión en el minuto
        const randLlegadaCamion = random[minutos];
        if (randLlegadaCamion < probLlegaCamionEnMinuto) {
            totalDeCamionesQueLlegaron[index] += 1;
            // Una fórmula que se me ocurrió para calcular cuánto tardarían dependiendo del número de trabajadores
            const duracionDescarga = (35 - (numTrabajadores * 5)) + Math.floor(Math.random() * 11);
            queueCamiones.push(duracionDescarga);
        }
    }
}

// Función que agerga comas a los números
function numberWithCommas(x) { return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); }

let lowestCostIndex = 0;
let lowestCostValue = gastos[lowestCostIndex];
console.log('-------------------------------------------');
gastos.forEach((gasto, index) => {
    console.log('Número de Trabajadores: ', 3 + index);
    console.log('Total de Camiones: ', totalDeCamionesQueLlegaron[index]);
    console.log('Gastos: $', numberWithCommas(gasto.toFixed(2)));
    console.log('-------------------------------------------');
    if (gasto < lowestCostValue) {
        lowestCostValue = gasto;
        lowestCostIndex = index;
    }
});

console.log(`El equipo óptimo es de ${3 + lowestCostIndex} trabajadores con un costo de $${numberWithCommas(lowestCostValue.toFixed(2))}`);
console.log('-------------------------------------------');
