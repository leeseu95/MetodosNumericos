/*
Una tienda pequeña tiene un lote de estacionamiento con (6 lugares)
disponibles. Los clientes llegan en forma aleatoria de acuerdo
a un proceso poisson a una razón media de (10 clientes por hora), y se van
inmediatamente si no existen lugares disponibles en el estacionamiento.
El tiempo que un auto permanece en el estacionamiento sigue una
distribución uniforme (entre 10 y 30 minutos).

a. Qué porcentaje de los clientes es perdido por no tener más lugares disponibles?
b. Cuál es la probabilidad de encontrar un lugar disponible en el estacionamiento?
c. Cuál es el porcentaje promedio de espacios disponibles?
*/

const probLlegaCliente = 1 / 6; // 10 clientes / 60 minutos -> (1/6) clientes / 1 minuto
const minutosEnUnDia = 60 * 24;
const numLugares = 6;
let lugares = []; // Cada elemento representa los minutos faltantes para que se libere un lugar
let totalDeCoches = 0;
let cochesQueSeVan = 0;
const lugaresLibresPorMinuto = [];

for (let minutos = 0; minutos < 60 * 24; minutos += 1) {
    // Descomentar esto para mostrar estado de los lugares minuto a minuto
    // console.log('-------- Minuto: ', minutos);
    // lugares.forEach(current => console.log('mins: ', current));
    const rand = Math.random();

    // Pasa un minuto para los coches que están ya en la tienda
    lugares = lugares.map(tiempo => tiempo - 1);
    lugares = lugares.filter(tiempo => tiempo > 0);

    // Si llega un cliente
    if (rand < probLlegaCliente) {
        totalDeCoches += 1;
        // Si hay lugares disponibles
        if (lugares.length < numLugares) {
            // console.log('-> llego alguien');
            const tiempoEnTienda = 10 + Math.floor(Math.random() * 21);
            lugares.push(tiempoEnTienda);

        // Si no hay lugares disponibles
        } else cochesQueSeVan += 1;
    }

    lugaresLibresPorMinuto.push(numLugares - lugares.length);
}

// Tenemos que hacer Math.floor() porque no podemos tener fracciones de lugares disponibles.
const promedioLugaresLibresPorMinuto = Math.floor(lugaresLibresPorMinuto.reduce((acc, curr) => acc + curr, 0) / minutosEnUnDia);

console.log(`Porcentaje de los clientes perdido por no tener lugares disponibles: (${cochesQueSeVan}/${totalDeCoches}) -> ${((cochesQueSeVan / totalDeCoches) * 100).toFixed(2)} %`);
console.log(`Probabilidad de encontrar un lugar disponible en el estacionamiento: (${totalDeCoches - cochesQueSeVan}/${totalDeCoches}) -> ${((totalDeCoches - cochesQueSeVan) / totalDeCoches).toFixed(2)}`);
console.log(`Porcentaje promedio de espacios disponibles: (${promedioLugaresLibresPorMinuto}/6) -> ${((promedioLugaresLibresPorMinuto / 6) * 100).toFixed(2)} %`);
