//Seung Hoon Lee - A01021720
//Examen Parcial 2
//Elecciones

//Iteraciones
var iters = 5000;

//Cantidad de votos que se pueden acarrear
var cantidadVotosAcarreados = 0;

//Cantida de electores
var electoresTotal = 87838148; //87 millones de electores en total, 68% si votaran
var electoresMillennial = 12000000; //12Millones de electores millenials

//Votos de los millenials
/*https://www.forbes.com.mx/el-voto-millennial-definira-las-elecciones-del-1-de-julio/
26% AMLO
21% Anaya
16% Meade
10% Zavala
7% otros
20% No van a votar*/

//https://www.reforma.com/aplicacioneslibre/articulo/default.aspx?id=1247635&md5=2237e4fdfb27311731eee6f486804598&ta=0dfdbac11765226904c16cb9ad1b2efe
//Referencias electores duros: http://anapaulaordorica.com/asi-se-ve-el-voto-duro-de-los-partidos/
var electoresPRI = 8400000; //8millones400mil para el PRI 
var electoresPAN = 6500000; //6millones500mil para el PAN
var electoresPRD = 2600000; //2Millones600mil para el PRD
var electoresSinVoto = 28108208; //El 68% votara, y el 32% (28millones) no votara
var electoresCambiarVoto = 28000000;
var electoresFueraPais = 500000 //500mil electores fuera del pais

//Electores elegibles (electores de cambiarVoto + electores Fuera Pais + restantes)
var electoresElegibles = (electoresTotal - electoresPRI - electoresPAN - electoresPRD - electoresSinVoto - electoresMillennial);

//Votos totales
var votosTotalAMLO = 0; //Morena 
var votosTotalMeade = 0; //PRI
var votosTotalAnaya = 0; //PAN y PRD
var votosTotalZavala = 0;
var votosTotalOtro = 0;
var votosTotalQueNoFueron = 0;

// console.log(electoresElegibles);
// cantidadVotosAcarreados = electoresTotal - electoresPRI - electoresPAN - electoresPRD - electoresSinVoto-electoresCambiarVoto-electoresFueraPais;

// console.log(cantidadVotosAcarreados);
// console.log(electoresElegibles);

//------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------
//------------------------------------Problema #2-------------------------------------------
console.log("Problema #2 Simulacion de Elecciones:");
for(let i = 0; i < iters; i++) {
    //Votos totales
    //Votos de Meade
    votosTotalMeade += electoresPRI;
    
    //Anaya hizo alianza con PAN Y PRD
    votosTotalAnaya += electoresPAN;
    votosTotalAnaya += electoresPRD;

    let votosAMLO = 0;
    let votosMeade = 0;
    let votosAnaya = 0;
    let votosZavala = 0;
    let votosOtro = 0;
    let votosNulos = 0;

    //Votos de los elegibles
    for(let i = 0; i < (electoresElegibles/10000); i++){ //Redundancia (multiplicamos por 10,000 al final de los votos)
        votosRan = Math.random();
        if(votosRan <= 0.41) votosAMLO ++
        else if(votosRan <= 0.69) votosAnaya ++
        else if(votosRan <= 0.90) votosMeade ++
        else if(votosRan <= 0.96) votosZavala ++
        else votosOtro ++
    }

    //Votos de los millenials
    for(let i = 0; i < (electoresMillennial/10000); i++){ //Redundancia (multiplicamos por 10,000 al final de los votos)
        votosRan = Math.random();
        if(votosRan <= 0.27) votosAMLO ++
        else if(votosRan <= 0.48) votosAnaya ++
        else if(votosRan <= 0.64) votosMeade ++
        else if(votosRan <= 0.74) votosZavala ++
        else if(votosRan <= 0.80) votosOtro ++
        else votosNulos ++
    }
    
    votosAMLO *= 10000;
    votosMeade *= 10000;
    votosAnaya *= 10000;
    votosZavala *= 10000;
    votosOtro *= 10000;
    votosNulos *= 10000;

    votosTotalAMLO += votosAMLO;
    votosTotalMeade += votosMeade;
    votosTotalAnaya += votosAnaya;
    votosTotalZavala += votosZavala;
    votosTotalOtro += votosOtro;
    votosTotalQueNoFueron += electoresSinVoto + votosNulos;
}

console.log(`\nVotos Total de AMLO de 5,000 iteraciones: ${votosTotalAMLO}`);
console.log(`Votos Total de Anaya de 5,000 iteraciones: ${votosTotalAnaya}`);
console.log(`Votos Total de Meade de 5,000 iteraciones: ${votosTotalMeade}`);
console.log(`Votos Total de Zavala de 5,000 iteraciones: ${votosTotalZavala}`);
console.log(`Votos Total de Otros de 5,000 iteraciones: ${votosTotalOtro}`);
console.log(`Votos Totales sin emitir de 5,000 iteraciones: ${votosTotalQueNoFueron}`);

console.log("\n\nVotos promedio:")
console.log(`Votos Total de AMLO : ${votosTotalAMLO/iters}`);
console.log(`Votos Total de Anaya : ${votosTotalAnaya/iters}`);
console.log(`Votos Total de Meade : ${votosTotalMeade/iters}`);
console.log(`Votos Total de Zavala : ${votosTotalZavala/iters}`);
console.log(`Votos Total de Otros : ${votosTotalOtro/iters}`);
console.log(`Votos Total sin emitir : ${votosTotalQueNoFueron/iters}`);

console.log(`\n\nPorcentaje de votos:`)
console.log(`Votos Porcentaje de AMLO : ${votosTotalAMLO*100/(iters*electoresTotal)}%`);
console.log(`Votos Porcentaje de Anaya : ${votosTotalAnaya*100/(iters*electoresTotal)}%`);
console.log(`Votos Porcentaje de Meade : ${votosTotalMeade*100/(iters*electoresTotal)}%`);
console.log(`Votos Porcentaje de Zavala : ${votosTotalZavala*100/(iters*electoresTotal)}%`);
console.log(`Votos Porcentaje de Otros : ${votosTotalOtro*100/(iters*electoresTotal)}%`);
console.log(`Votos Porcentaje sin emitir : ${votosTotalQueNoFueron*100/(iters*electoresTotal)}%`);

console.log("\n\nGanador de la presidencia: Ricardo Anaya (PAN Y PRD)");