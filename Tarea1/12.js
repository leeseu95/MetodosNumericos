/*
Se tiene un sistema de colas formado por dos estaciones en serie.
Los clientes atendidos en la primera estación pasan en seguida a
formar cola en la segunda. En la primera estación de servicio, la
razón de llegadas sigue una distribución poisson con media de (20 clientes/hora)
y el tiempo de servicio sigue una distribución exponencial con media
de (2 minutos/persona). En la segunda estación, el tiempo de servicio
está uniformemente distribuido (entre 1 y 2 minutos/persona).
Para esta información, ¿cuál es el tiempo promedio en el sistema?,
¿cuál de las dos colas que se forman es mayor?
*/

const probabilidad = 20 / 60; // 20 clientes por hora
const primeraCola = [];
const segundaCola = [];
let maxLengthPrimeraCola = 0;
let maxLengthSegundaCola = 0;
let peopleCounter = 0;
let minutesCounter = 0;

// Loop de 1 hora (60 minutos)
for (let minutos = 0; minutos < 60; minutos += 1) {
    const rand = Math.random();

    // Si hay alguien siendo atendido en la segunda cola, se resta 1 minuto al tiempo que se atendió
    if (segundaCola.length) {
        if (segundaCola.length > maxLengthSegundaCola) maxLengthSegundaCola = segundaCola.length;
        segundaCola[0] -= 1;

        if (segundaCola[0] === 0) {
            // Si ya se atendió a la persona, sale y se va
            segundaCola.splice(0, 1);
            // console.log('Minuto: ', minutos);
            // console.log('-> alguien salió de la Segunda cola');
        }
    }

    // Si hay alguien siendo atendido en la primera cola, se resta 1 minuto al tiempo que se atendió
    if (primeraCola.length) {
        if (primeraCola.length > maxLengthPrimeraCola) maxLengthPrimeraCola = primeraCola.length;
        primeraCola[0] -= 1;

        if (primeraCola[0] === 0) {
            // Si ya se atendió a la persona, sale de la primera cola y va a la segunda
            primeraCola.splice(0, 1);
            // console.log('Minuto: ', minutos);
            // console.log('* alguien salió de la Primera cola');
            // Es un 50/50 si se tarda 1 ó 2 minutos en la segunda cola
            let time = 0;
            if (rand < 0.5) time = 1;
            else time = 2;
            segundaCola.push(time);
            minutesCounter += time;
        }
    }

    // Si llega un persona a la primera estación
    if (rand < probabilidad) {
        // console.log('Minuto: ', minutos);
        // console.log('<- llegó alguien');
        primeraCola.push(2); // Se van a tardar 2 minutos en atender a esa persona.
        peopleCounter += 1;
        minutesCounter += 2;
    }
}

const avgTime = minutesCounter / peopleCounter;

console.log('Tamaño máximo de la Primera cola: ', maxLengthPrimeraCola);
console.log('Tamaño máximo de la Segunda cola: ', maxLengthSegundaCola);
console.log(`Tiempo promedio del sistema: ${avgTime.toFixed(2)} minutos.`);

