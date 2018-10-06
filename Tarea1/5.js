/*
 * La demanda diaria de un cierto artículo está regida por una
 * distribución binomial con parámetros n = 6 y theta = 1/2. El tiempo
 * de entrega en días es una variable aleatoria poisson con
 * lambda = 3. El costo de mantener una unidad en inventario es de
 * ($1 / día), el costo del faltante es de $10 por unidad, y el costo de
 * odernar es de $50 por orden. Se desea comparar dos políticas
 * para llevar el inventario: 1) Ordenar cada 8 días hasta tener 30
 * artículos en el inventario y 2) Odernar hasta 30 artículos cuando el
 * nivel del inventario sea menor o igual a 10. Si se asume que las
 * unidades faltantes en un ciclo son surtidas por la nueva orden
 * que arriba en el próximo ciclo, ¿cuál de las dos políticas
 * desritas es más económica?
 *
 * Probabilidad de demanda:
 * cantidad -> probabilidad
 * 0 -> 0.015625
 * 1 -> 0.09375
 * 2 -> 0.234375
 * 3 -> 0.3125
 * 4 -> 0.234375
 * 5 -> 0.09375
 * 6 -> 0.015625
 */

const duracionSimulacion = 5000; // días
const costoFaltante = 10; // $10 por unidad
const costoOrdenar = 50; // $50 por orden
const lambda = 3;

// Política 1
let inventario1 = 0; // Unidades en el inventario
let gastos1 = 0; // Gastos totales
const pedido1 = {
    espera: 0,
    unidades: 0,
};

// Política 2
let inventario2 = 0;// Unidades en el inventario
let gastos2 = 0; // Gastos totales
const pedido2 = {
    espera: 0,
    unidades: 0,
};

// Helper function para calcular la variable random con la distribución de poisson
// https://gist.github.com/yuanyan/997516
function poisson(expectvalue) {
    let n = 0;
    const limit = Math.exp(-expectvalue);
    let x = Math.random();
    while (x > limit) {
        n += 1;
        x *= Math.random();
    }
    return n;
}

// La probabilidad de demanda se calculó usando una distribución binomial con los parámetros dados en el problema
const probDemanda = [[0.015625, 0], [0.09375, 1], [0.234375, 2], [0.3125, 3], [0.234375, 4], [0.09375, 5], [0.015625, 6]];

console.log(`Los siguientes son los resultados de correr una simulación por ${duracionSimulacion} días.`);

for (let dia = 0; dia < duracionSimulacion; dia += 1) {
    // Checamos cuál es la demanda del día
    const random = Math.random();
    const demanda = probDemanda.reduce((acc, cur) => {
        const maxRange = acc[0] + cur[0];
        if (random >= acc[0] && random < maxRange) return [maxRange, cur[1]];
        return [maxRange, acc[1]];
    }, [0, -1])[1];

    /*
     * -----------------------------------------------------------
     * -----------------------------------------------------------
     * ------------------ Política 1 -----------------------------
     * -----------------------------------------------------------
     * -----------------------------------------------------------
     */
    // Cada 8 días vamos a pedir las unidades faltantes para llegar a 30 unidades
    if (dia % 8 === 0) {
        pedido1.unidades = 30 - inventario1;
        // Hacemos una orden si hay unidades a Pedir
        gastos1 += costoOrdenar;
        pedido1.espera = poisson(lambda);
    }

    // Calculamos los gastos por las unidades que tenemos en el inventario
    if (inventario1 > 0) gastos1 += inventario1;

    // Si ya pasó el tiempo que tardaría la orden, entran las nuevas unidades al inventario
    if (!pedido1.espera) {
        inventario1 += pedido1.unidades;
        pedido1.unidades = 0;
    }

    // Pasa un día para las órdenes realizadas que no han llegado
    if (pedido1.espera) pedido1.espera -= 1;

    // Si la demanda es mayor al inventario
    if (demanda > inventario1) {
        // Surtimos lo que tenemos y pagamos multas por lo demás
        if (inventario1 > 0) gastos1 += (demanda - inventario1) * costoFaltante;

        // Si no tenemos ni un producto pagamos multas por toda la demanda
        else gastos1 += demanda * costoFaltante;
    }

    // Actualizamos el inventario
    inventario1 -= demanda;

    /*
     * -----------------------------------------------------------
     * -----------------------------------------------------------
     * ------------------ Política 2 -----------------------------
     * -----------------------------------------------------------
     * -----------------------------------------------------------
     */
    // Cada día checamos si tenemos 10 o menos unidades y no hemos pedido producto, si sí, pedimos más
    if (inventario2 <= 10 && pedido2.unidades === 0) {
        pedido2.unidades = 30 - inventario2;
        // Hacemos una orden si hay unidades a Pedir
        gastos2 += costoOrdenar;
        pedido2.espera = poisson(lambda);
    }

    // Calculamos los gastos por las unidades que tenemos en el inventario
    if (inventario2 > 0) gastos2 += inventario2;

    // Si ya pasó el tiempo que tardaría la orden, entran las nuevas unidades al inventario
    if (!pedido2.espera) {
        inventario2 += pedido2.unidades;
        pedido2.unidades = 0;
    }

    // Pasa un día para las órdenes realizadas que no han llegado
    if (pedido2.espera) pedido2.espera -= 1;

    // Si la demanda es mayor al inventario
    if (demanda > inventario2) {
        // Surtimos lo que tenemos y pagamos multas por lo demás
        if (inventario2 > 0) gastos2 += (demanda - inventario2) * costoFaltante;

        // Si no tenemos ni un producto pagamos multas por toda la demanda
        else gastos2 += demanda * costoFaltante;
    }

    // Actualizamos el inventario
    inventario2 -= demanda;
}

function numberWithCommas(x) { return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); }

console.log('Gastos Política 1: $', numberWithCommas(gastos1));
console.log('Gastos Política 2: $', numberWithCommas(gastos2));

