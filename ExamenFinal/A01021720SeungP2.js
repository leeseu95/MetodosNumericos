// Seung Hoon Lee Kim
// A01021720
// Hecho en Javascript

// Correr asi : node A01021720SeungP2.js

// Metemos las variables que nos da el problema
const timeBetweenBreakdown = [69, 84, 12, 94, 51, 36, 17, 2, 15, 29, 16, 52, 56, 43, 26, 22, 8, 62];
const repairTimeRequired = [37, 77, 13, 10, 2, 18, 31, 19, 32, 85, 31, 94, 81, 43, 31, 58, 33, 51];
// Counters para el problema
let counterTiempoEntreFallas = 0;
let counterTiempoDeReparacion = 0;

// Tiempo de reparación en hours
function getTiempoReparacion(rand) {
    // const rand = Math.random();
    let hours = 1.5;
    if (rand < 0.80) hours = 1;
    if (rand < 0.28) hours = 0.5;
    counterTiempoDeReparacion += 1;
    return hours;
}

// Tiempo entre fallas de máquinas
function getTiempoEntreFallas(rand) {
    // const rand = Math.random();
    let hours = 3;
    if (rand < 0.81) hours = 2.5;
    if (rand < 0.60) hours = 2;
    if (rand < 0.27) hours = 1.5;
    if (rand < 0.11) hours = 1;
    if (rand < 0.05) hours = 0.5;
    counterTiempoEntreFallas += 1;
    return hours;
}

const costOneRepairmen = 4320; // El precio del mantenimiento con 1 sólo reparador
const sueldoPorHoraReparador = 30;
const costoPorHoraDescompostura = 75;
const duracionSimulacion = 15; // 15 descomposturas

let hours = 0; // Contador de hours
let hoursBroken = 0;

//Queue y tiempos de compostura
const tiemposDescomposturas = [];
const queue = [];

// Generamos los tiempos entre las 15 descomposturas que durará la simulación
for (let i = 0; i < duracionSimulacion; i += 1) {
    // El primero lo metemos directo
    if (tiemposDescomposturas.length === 0) tiemposDescomposturas.push(getTiempoEntreFallas(timeBetweenBreakdown[counterTiempoEntreFallas]));

    // Los demás les tenemos que sumar el tiempo pasado
    else tiemposDescomposturas.push(getTiempoEntreFallas(timeBetweenBreakdown[counterTiempoEntreFallas]) + tiemposDescomposturas[i - 1]);
}

while (tiemposDescomposturas.length || queue.length) {
    hours += 0.5;

    // Checamos si hay máquinas por ser reparadas
    if (queue.length) {
        hoursBroken += queue.length * 0.5;
        queue[0] -= 0.5;
        if (queue[0] === 0) queue.splice(0, 1);
    }

    // Checamos si se descompone una máquina
    if (tiemposDescomposturas.length) {
        if (tiemposDescomposturas[0] === hours) {
            queue.push(getTiempoReparacion(repairTimeRequired[counterTiempoDeReparacion]));
            tiemposDescomposturas.splice(0, 1);
        }
    }
}
const costTwoRepairmen = hours * 2 * sueldoPorHoraReparador;
const costBrokenMachines = hoursBroken * costoPorHoraDescompostura;


console.log('\n\nSimulacion (25 puntos)-------------------------')
console.log('Gastos por maquinas descompuestas: $', costBrokenMachines);
console.log('Gastos por salarios de 2 reparadores: $', costTwoRepairmen);

console.log(`El costo total de simulacion con 1 reparador es de $ ${costOneRepairmen}`);
console.log(`El costo de simulacion de 2 reparadores es de $ ${costTwoRepairmen + costBrokenMachines}`);
console.log('-----------------------------------------------------------------------------')

console.log('\n\nDeberia Three Hills agregar un segundo tecnico? (15 puntos)-----------')
if (costOneRepairmen < (costTwoRepairmen + costBrokenMachines)) {
    console.log('No lo deberia hacer ya que es mas barato tener 1 reparador\n');
} else {
    console.log('Si lo deberia hacer ya que es mas barato tener 2 reparadores\n');
}