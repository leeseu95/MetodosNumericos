// Números 'aleatorios' predefinidos
const numAleatorioLlegada = [0, 0.48355, 0.98977, 0.06533, 0.45128, 0.15486, 0.19241, 0.15997, 0.6794, 0.90872, 0.58997, 0.68691, 0.73488, 0.23423, 0.86675, 0.56856];
const numAleatorioDuracionServicio = [0.83761, 0.14387, 0.51321, 0.72472, 0.05466, 0.84609, 0.29735, 0.59076, 0.76355, 0.29549, 0.61958, 0.17267, 0.10061, 0.45645, 0.86754, 0.35340];
const gastosTotales = [];
let eventos = []; // Arreglo donde guardamos todos los eventos
let yaComieron = -1; // Flag utilizado para implementar la pausa de la comida, representa el index del arreglo de eventos en el cual comieron

const horarios = {
    abren: {
        hora: 11,
        minutos: 0,
    },
    cierran: {
        hora: 7,
        minutos: 30,
    },
};

// Función para comparar lo que me inventé como horarios
function time1GreaterThanOrEqualTime2(time1, time2) {
    if (time1.hora > time2.hora) {
        return true;
    } else if (time1.hora === time2.hora) {
        if (time1.minutos >= time2.minutos) return true;
    }
    return false;
}

class Evento {
    constructor(numeroAleatorioLlegada, numeroAleatorioDuracionServicio, numeroTrabajadores) {
        // Definimos el tiempo entre llegadas
        this.tiempoEntreLlegada = 60;
        if (numeroAleatorioLlegada < 0.97) this.tiempoEntreLlegada = 55;
        if (numeroAleatorioLlegada < 0.92) this.tiempoEntreLlegada = 50;
        if (numeroAleatorioLlegada < 0.82) this.tiempoEntreLlegada = 45;
        if (numeroAleatorioLlegada < 0.67) this.tiempoEntreLlegada = 40;
        if (numeroAleatorioLlegada < 0.47) this.tiempoEntreLlegada = 35;
        if (numeroAleatorioLlegada < 0.22) this.tiempoEntreLlegada = 30;
        if (numeroAleatorioLlegada < 0.10) this.tiempoEntreLlegada = 25;
        if (numeroAleatorioLlegada < 0.02) this.tiempoEntreLlegada = 20;
        if (numeroAleatorioLlegada === 0) this.tiempoEntreLlegada = 0;

        if (numeroTrabajadores === 3) {
            // Definimos el tiempo que durará el servicio
            this.tiempoDuracionServicio = 60;
            if (numeroAleatorioDuracionServicio < 0.96) this.tiempoDuracionServicio = 55;
            if (numeroAleatorioDuracionServicio < 0.90) this.tiempoDuracionServicio = 50;
            if (numeroAleatorioDuracionServicio < 0.82) this.tiempoDuracionServicio = 45;
            if (numeroAleatorioDuracionServicio < 0.72) this.tiempoDuracionServicio = 40;
            if (numeroAleatorioDuracionServicio < 0.60) this.tiempoDuracionServicio = 35;
            if (numeroAleatorioDuracionServicio < 0.35) this.tiempoDuracionServicio = 30;
            if (numeroAleatorioDuracionServicio < 0.15) this.tiempoDuracionServicio = 25;
            if (numeroAleatorioDuracionServicio < 0.05) this.tiempoDuracionServicio = 20;
        }

        if (numeroTrabajadores === 4) {
            // Definimos el tiempo que durará el servicio
            this.tiempoDuracionServicio = 55;
            if (numeroAleatorioDuracionServicio < 0.99) this.tiempoDuracionServicio = 50;
            if (numeroAleatorioDuracionServicio < 0.95) this.tiempoDuracionServicio = 45;
            if (numeroAleatorioDuracionServicio < 0.87) this.tiempoDuracionServicio = 40;
            if (numeroAleatorioDuracionServicio < 0.75) this.tiempoDuracionServicio = 35;
            if (numeroAleatorioDuracionServicio < 0.60) this.tiempoDuracionServicio = 30;
            if (numeroAleatorioDuracionServicio < 0.40) this.tiempoDuracionServicio = 25;
            if (numeroAleatorioDuracionServicio < 0.20) this.tiempoDuracionServicio = 20;
            if (numeroAleatorioDuracionServicio < 0.05) this.tiempoDuracionServicio = 15;
        }


        if (numeroTrabajadores === 5) {
            // Definimos el tiempo que durará el servicio
            this.tiempoDuracionServicio = 50;
            if (numeroAleatorioDuracionServicio < 0.97) this.tiempoDuracionServicio = 45;
            if (numeroAleatorioDuracionServicio < 0.92) this.tiempoDuracionServicio = 40;
            if (numeroAleatorioDuracionServicio < 0.86) this.tiempoDuracionServicio = 35;
            if (numeroAleatorioDuracionServicio < 0.78) this.tiempoDuracionServicio = 30;
            if (numeroAleatorioDuracionServicio < 0.68) this.tiempoDuracionServicio = 25;
            if (numeroAleatorioDuracionServicio < 0.50) this.tiempoDuracionServicio = 20;
            if (numeroAleatorioDuracionServicio < 0.28) this.tiempoDuracionServicio = 15;
            if (numeroAleatorioDuracionServicio < 0.10) this.tiempoDuracionServicio = 10;
        }


        if (numeroTrabajadores === 6) {
            // Definimos el tiempo que durará el servicio
            this.tiempoDuracionServicio = 45;
            if (numeroAleatorioDuracionServicio < 0.98) this.tiempoDuracionServicio = 40;
            if (numeroAleatorioDuracionServicio < 0.94) this.tiempoDuracionServicio = 35;
            if (numeroAleatorioDuracionServicio < 0.88) this.tiempoDuracionServicio = 30;
            if (numeroAleatorioDuracionServicio < 0.80) this.tiempoDuracionServicio = 25;
            if (numeroAleatorioDuracionServicio < 0.68) this.tiempoDuracionServicio = 20;
            if (numeroAleatorioDuracionServicio < 0.53) this.tiempoDuracionServicio = 15;
            if (numeroAleatorioDuracionServicio < 0.27) this.tiempoDuracionServicio = 10;
            if (numeroAleatorioDuracionServicio < 0.12) this.tiempoDuracionServicio = 5;
        }

        this.tiempoDeLlegada = { hora: 0, minutos: 0 };
        this.iniciacionDelServicio = { hora: 0, minutos: 0 };
        this.terminacionDelServicio = { hora: 0, minutos: 0 };
        this.ocioDelPersonal = { hora: 0, minutos: 0 };
        this.tiempoEsperaDelCamion = { hora: 0, minutos: 0 };
    }

    calculateTerminacionServicio() {
        const mins = this.iniciacionDelServicio.minutos + this.tiempoDuracionServicio;
        this.terminacionDelServicio.hora = this.iniciacionDelServicio.hora;
        if (mins >= 60) this.terminacionDelServicio.hora += 1;
        this.terminacionDelServicio.minutos = mins % 60;
    }

    calculateTiempoLlegada(index) {
        const mins = this.tiempoEntreLlegada + eventos[index - 1].tiempoDeLlegada.minutos;
        this.tiempoDeLlegada.hora = eventos[index - 1].tiempoDeLlegada.hora;
        if (mins >= 60) this.tiempoDeLlegada.hora += 1;
        this.tiempoDeLlegada.minutos = mins % 60;
    }

    calculateData(index) {
        // Valores por default de la espera del camión
        this.tiempoEsperaDelCamion.hora = 0;
        this.tiempoEsperaDelCamion.minutos = 0;

        // Cuando estamos tratando con el primer evento, las operaciones son diferentes
        if (index === 0) {
            this.tiempoDeLlegada.hora = horarios.abren.hora;
            this.tiempoDeLlegada.minutos = horarios.abren.minutos;

            this.iniciacionDelServicio.hora = horarios.abren.hora;
            this.iniciacionDelServicio.minutos = horarios.abren.minutos;

            // Calculamos la terminacion del Servicio
            this.calculateTerminacionServicio();

            // Esto está hardcodeado para el primer caso
            // Calculamos el ocio del personal
            this.ocioDelPersonal.hora = 0;
            this.ocioDelPersonal.minutos = 0;

        // Si no estamos tratando con el primer evento
        } else {
            // Calculamos el tiempo de llegada
            this.calculateTiempoLlegada(index);

            // Calculamos la iniciación del servicio
            // Si la terminacion del Servicio pasado es después de la llegada de éste evento, el servicio empieza cuando termina el pasado
            if (time1GreaterThanOrEqualTime2(eventos[index - 1].terminacionDelServicio, this.tiempoDeLlegada)) {
                this.iniciacionDelServicio = { ...eventos[index - 1].terminacionDelServicio };
            } else { // sino empieza cuando llega
                this.iniciacionDelServicio = { ...this.tiempoDeLlegada };
            }

            // Calculamos en qué horario comen y recorremos las horas
            if (yaComieron < 0) {
                // Primero checamos si el servicio pasado terminó >= de las 3:00 AM
                const threeAM = { hora: 15, minutos: 0 };
                if (time1GreaterThanOrEqualTime2(eventos[index - 1].terminacionDelServicio, threeAM)) {
                    // Si sí terminó >= 3:00 AM, este servicio empieza media hora después porque van a comer
                    yaComieron = index;
                    const mins = 30 + this.iniciacionDelServicio.minutos;
                    if (mins >= 60) this.iniciacionDelServicio.hora += 1;
                    this.iniciacionDelServicio.minutos = mins % 60;

                // Si no, checamos si éste servicio llegó >= 3:00 AM
                } else if (time1GreaterThanOrEqualTime2(this.tiempoDeLlegada, threeAM)) {
                    // Si sí, el servicio se va a esperar media hora en lo que comen
                    yaComieron = index;
                    // Si no hay tiempo suficiente para comer entre las 3 y el siguiente servicio, se recorren las horas
                    // Si sí hay tiempo suficiente para comer, no se cambian los horarios
                    // TODO: este pedo está mal
                    let minsLibres = (this.tiempoDeLlegada.hora - threeAM.hora) * 60;
                    minsLibres += (this.tiempoDeLlegada.minutos - threeAM.minutos);

                    if (minsLibres < 30) {
                        const mins = (30 - minsLibres) + this.iniciacionDelServicio.minutos;
                        if (mins >= 60) this.iniciacionDelServicio.hora += 1;
                        this.iniciacionDelServicio.minutos = mins % 60;
                    }
                }
            }

            // Calculamos la terminación del servicio de éste evento
            this.calculateTerminacionServicio();

            // Calculamos el ocio del personal
            // Si el tiempo de llegada es después de que terminaron el serivicio pasado, hay tiempo de ocio
            if (time1GreaterThanOrEqualTime2(this.tiempoDeLlegada, eventos[index - 1].terminacionDelServicio)) {
                this.ocioDelPersonal.hora = this.tiempoDeLlegada.hora - eventos[index - 1].terminacionDelServicio.hora;
                this.ocioDelPersonal.minutos = this.tiempoDeLlegada.minutos - eventos[index - 1].terminacionDelServicio.minutos;
                if (this.ocioDelPersonal.minutos < 0) {
                    this.ocioDelPersonal.hora -= 1;
                    this.ocioDelPersonal.minutos += 60;
                }
            } else {
                this.ocioDelPersonal.hora = 0;
                this.ocioDelPersonal.minutos = 0;
            }

            // Calculamos el tiempo de espera del camion
            // La diferencia entre cuando se inicia el servicio y cuando llegó el camión
            if (time1GreaterThanOrEqualTime2(this.iniciacionDelServicio, this.tiempoDeLlegada)) {
                this.tiempoEsperaDelCamion.hora = this.iniciacionDelServicio.hora - this.tiempoDeLlegada.hora;
                this.tiempoEsperaDelCamion.minutos = this.iniciacionDelServicio.minutos - this.tiempoDeLlegada.minutos;
                if (this.tiempoEsperaDelCamion.minutos < 0) {
                    this.tiempoEsperaDelCamion.hora -= 1;
                    this.tiempoEsperaDelCamion.minutos += 60;
                }
            }
        }
    }

    calculateLongitudCola(index) {
        this.longitudCola = 0;
        for (let i = index + 1; i < numAleatorioLlegada.length; i += 1) {
            if (time1GreaterThanOrEqualTime2(this.terminacionDelServicio, eventos[i].tiempoDeLlegada)) this.longitudCola += 1;
        }
    }

    print(index) {
        let minutos;
        // Formamos el string con el tiempo de llegada
        if (this.tiempoDeLlegada.minutos < 10) minutos = `0${this.tiempoDeLlegada.minutos}`; // Le agregamos el '0' que falta para darle mejor formato
        else minutos = this.tiempoDeLlegada.minutos; // eslint-disable-line
        const tiempoLlegadaString = `${this.tiempoDeLlegada.hora % 12}:${minutos}`;

        // Formamos el string con el tiempo de iniciación del servicio
        if (this.iniciacionDelServicio.minutos < 10) minutos = `0${this.iniciacionDelServicio.minutos}`; // Le agregamos el '0' que falta para darle mejor formato
        else minutos = this.iniciacionDelServicio.minutos; // eslint-disable-line
        if (yaComieron === index) minutos += '*';
        const iniciacionDelServicioString = `${this.iniciacionDelServicio.hora % 12}:${minutos}`;

        // Formamos el string con el tiempo de terminación del servicio
        if (this.terminacionDelServicio.minutos < 10) minutos = `0${this.terminacionDelServicio.minutos}`; // Le agregamos el '0' que falta para darle mejor formato
        else minutos = this.terminacionDelServicio.minutos; // eslint-disable-line
        const terminacionDelServicioString = `${this.terminacionDelServicio.hora % 12}:${minutos}`;

        // Formamos el string con el tiempo de ocio del personal
        if (this.ocioDelPersonal.minutos < 10) minutos = `0${this.ocioDelPersonal.minutos}`; // Le agregamos el '0' que falta para darle mejor formato
        else minutos = this.ocioDelPersonal.minutos; // eslint-disable-line
        const ocioDelPersonalString = `${this.ocioDelPersonal.hora % 12}:${minutos}`;

        // Formamos el string con el tiempo de espera del camion
        if (this.tiempoEsperaDelCamion.minutos < 10) minutos = `0${this.tiempoEsperaDelCamion.minutos}`; // Le agregamos el '0' que falta para darle mejor formato
        else minutos = this.tiempoEsperaDelCamion.minutos; // eslint-disable-line
        const tiempoEsperaDelCamionString = `${this.tiempoEsperaDelCamion.hora}:${minutos}`;

        const string = `${index}\t|\t${tiempoLlegadaString}\t|\t${iniciacionDelServicioString}\t|\t ${this.tiempoDuracionServicio} \t|\t${terminacionDelServicioString}\t\t|\t${ocioDelPersonalString}\t|\t${tiempoEsperaDelCamionString}\t|\t${this.longitudCola}\t|`;
        console.log(string); // eslint-disable-line
    }
}

console.log('\nPara el siguiente ejemplo, se utilizaron los número aleatorios de la tabla de 3 trabajadores para todos los casos.');

for (let numTrabajadores = 3; numTrabajadores <= 6; numTrabajadores += 1) {
    // Reiniciamos valores
    eventos = [];
    yaComieron = -1;

    // Generamos los eventos con los números aleatorios
    for (let i = 0; i < numAleatorioLlegada.length; i += 1) {
        eventos[i] = new Evento(numAleatorioLlegada[i], numAleatorioDuracionServicio[i], numTrabajadores);
    }

    // Calculamos la información
    for (let i = 0; i < numAleatorioLlegada.length; i += 1) {
        eventos[i].calculateData(i);
    }

    // Calculamos la longitud de la cola para cada evento
    for (let i = 0; i < numAleatorioLlegada.length; i += 1) {
        eventos[i].calculateLongitudCola(i);
    }

    // Calculamos cuántas horas extras se trabajaron
    // Checamos a qué hora termina el último servicio y vemos la diferencia de eso con la hora en la que deberían de terminar
    let minutosExtras = 0;
    const SevenThirtyAM = { hora: 19, minutos: 30 };
    const ultimoServicio = eventos[numAleatorioLlegada.length - 1].terminacionDelServicio;
    if (time1GreaterThanOrEqualTime2(ultimoServicio, SevenThirtyAM)) {
        minutosExtras += (ultimoServicio.hora - SevenThirtyAM.hora) * 60;
        minutosExtras += (ultimoServicio.minutos - SevenThirtyAM.minutos);
    }

    // Imprimimos la información
    console.log(`\n${numTrabajadores} Trabajadores`);
    const string = '\nIndex\t|Llegada\t|Inicia Servicio|Duración Servicio|Terminación Servicio\t|Ocio Personal\t|Espera Camión\t|Longitud Cola\t|';
    console.log(string);
    for (let i = 0; i < numAleatorioLlegada.length; i += 1) {
        eventos[i].print(i);
    }

    const precioHoraExtraTrabajador = 37.50;
    console.log('\nSueldo por hora Extra por Trabajador: $', precioHoraExtraTrabajador);
    console.log('Minutos Extras por Trabajador: ', minutosExtras);
    const pagoTotalExtraTrabajadores = minutosExtras * numTrabajadores * (precioHoraExtraTrabajador / 60);
    console.log('-> Paga Total de Horas Extras: $', pagoTotalExtraTrabajadores);

    const precioHoraTrabajador = 25;
    console.log('\nSueldo por hora: $', precioHoraTrabajador);
    const pagoTotalTrabajadores = precioHoraTrabajador * numTrabajadores * 8;
    console.log('-> Paga Total por 8 horas de trabajo: $', pagoTotalTrabajadores);

    const costoAlmacenHora = 500;
    const minutosAlmacenAbierto = (8 * 60) + minutosExtras;
    console.log('\nCosto de operación del almacén por hora: $', costoAlmacenHora);
    const pagoTotalAlmacen = minutosAlmacenAbierto * (costoAlmacenHora / 60);
    console.log('-> Paga Total por operación del almacén: $', pagoTotalAlmacen);

    const esperaTotalCamiones = eventos.reduce((acc, cur) => acc + (cur.tiempoEsperaDelCamion.hora * 60) + cur.tiempoEsperaDelCamion.minutos, 0);
    console.log('\nMinutos total de camiones en espera: ', esperaTotalCamiones);
    const pagoTotalEsperaCamiones = esperaTotalCamiones * (100 / 60);
    console.log('-> Paga Total por espera de camiones: $', pagoTotalEsperaCamiones);

    const tempIndex = numTrabajadores - 3;
    gastosTotales[tempIndex] = pagoTotalExtraTrabajadores + pagoTotalTrabajadores + pagoTotalAlmacen + pagoTotalEsperaCamiones;
    console.log('\n-> Gastos Totales: $', gastosTotales[tempIndex]);

    console.log('\n------------------------------------------------------------------------------------------------------------------------------------');
}

console.log('\nResumen de Gastos Totales:');
let lowestIndex = 0;
let lowestValue = gastosTotales[0];
for (let i = 0; i < 4; i += 1) { // 3, 4, 5, 6
    console.log(`${3 + i} Trabajadores: $ ${gastosTotales[i]}`);
    if (gastosTotales[i] < lowestValue) {
        lowestIndex = i;
        lowestValue = gastosTotales[i];
    }
}

console.log(`\nOpción óptima: ${3 + lowestIndex} Trabajadores -> $ ${lowestValue}\n`);
