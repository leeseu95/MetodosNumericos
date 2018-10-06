//Seung Hoon Lee - A01021720
//Examen Parcial 2
//Elecciones

var size = 16;
//Cantidad de votos que se pueden acarrear
var cantidadVotosAcarreados = 0;

//Cantida de electores
var electoresTotal = 87838148; //87 millones de electores en total, 68% si votaran
var electoresMillennial = 12000000; //12Millones de electores millenials
electoresTotal += electoresMillennial;

//Referencias electores duros: https://www.reforma.com/aplicacioneslibre/articulo/default.aspx?id=1247635&md5=2237e4fdfb27311731eee6f486804598&ta=0dfdbac11765226904c16cb9ad1b2efe
var electoresPRI = 8400000; //8millones400mil para el PRI 
var electoresPAN = 6500000; //6millones500mil para el PAN
var electoresPRD = 2600000; //2Millones600mil para el PRD
var electoresSinVoto = 28108208; //El 68% votara, y el 32% (28millones) no votara
var electoresCambiarVoto = 28000000;
var electoresFueraPais = 500000 //500mil electores fuera del pais

cantidadVotosAcarreados = electoresTotal - electoresPRI - electoresPAN - electoresPRD - electoresSinVoto-electoresCambiarVoto-electoresFueraPais;

// console.log(cantidadVotosAcarreados);

//Tarjetas de banco
var banamexCantidad = 0;
var bancomerCantidad = 0;
var sorianaCantidad = 0;
var walmartCantidad = 0;

//Tarjetas validas de cada tipo de tarjeta
const listInvalidCardsBanamex = [];
const listInvalidCardsBancomer = [];
const listInvalidCardsSoriana = [];
const listInvalidCardsWalmart = [];

//Tarjetas validas total
const listValidCards = [];
const temps = [];

var moneyDesviado = 0;

function printCards(arrayCards) {
    for(let i = 0; i < 10; i++) {
        console.log(arrayCards[i]);
    }
}

//------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------
//-----------------------------------------Problema #1--------------------------------------
console.log("Problema #1 Tarjetas:")
while(listValidCards.length < 100000) {
    let card = [];
    let temp = 0;

    for(let i = 1; i <= size; i++) {
        card.push(Math.floor(Math.random() * 10));
    }
    
    // console.log(card);
    for (let i = 1; i <= size; i++) {
        if (i % 2 == 1) {
            card[i-1] *= 2;
            if(card[i-1] > 9) {
                card[i-1] = 1 +(card[i-1] % 10);
            }
        }
    }

    for (let i = 1; i <= size; i++) {
        temp += card[i-1];
    }
    
    if(!listValidCards.includes(card) && temp % 10 == 0) {
        listValidCards.push(card);
        temps.push(temp);
    }
    // // console.log(card);

} 

for(let i = 0; i < listValidCards.length; i ++) {
    let money = 100;
    let moneyRan = Math.random();
    
    if(moneyRan <= 0.05) money = 1000;
    else if(moneyRan <= 0.15) money = 500;
    else if(moneyRan <= 0.50) money = 250;

    //Patron de Banamex
    if (temps[i] % 11 == 0){
        if(!listInvalidCardsBanamex.includes(listValidCards[i])){
            banamexCantidad ++;
            listInvalidCardsBanamex.push(listValidCards[i]);
            moneyDesviado += money;
        }
    }

    //Patron de Bancomer
    if (temps[i] * 2 >= 220) {
        if(!listInvalidCardsBancomer.includes(listValidCards[i])) {
            bancomerCantidad ++;
            listInvalidCardsBancomer.push(listValidCards[i]);
            moneyDesviado += money;
        }
    }

    //Patron de Soriana
    if (temps[i] >= 100) {
        if(!listInvalidCardsSoriana.includes(listValidCards[i])) {
            sorianaCantidad++;
            listInvalidCardsSoriana.push(listValidCards[i]);
            moneyDesviado += money;
        }
    }

    //Patron de Walmart
    if (temps[i] % 3 == 0) {
        if(!listInvalidCardsWalmart.includes(listValidCards[i])) {
            walmartCantidad++;
            listInvalidCardsWalmart.push(listValidCards[i]);
            moneyDesviado += money;
        }
    }
}

console.log("\n");
console.log("Patron encontrado para Banamex: Sumatoria de todos los numeros de la tarjeta modulo 11, sea igual a 0");
console.log("10 Tarjetas invalidas de Banamex de " + banamexCantidad + " encontradas : ");
printCards(listInvalidCardsBanamex);
console.log("\n");

console.log("\nPatron encontrado para Bancomer: Sumatoria de todos los numeros de la tarjeta * 2, sea mayor o igual a 220");
console.log("10 Tarjetas invalidas de Bancomer de " + bancomerCantidad + " encontradas : ");
printCards(listInvalidCardsBancomer);
console.log("\n");

console.log("Patron encontrado para Soriana: Sumatoria de todos los numeros de la tarjeta sea mayor a 100");
console.log("10 Tarjetas invalidas de Soriana de " + sorianaCantidad + " encontradas : ");
printCards(listInvalidCardsSoriana);
console.log("\n");

console.log("Patron encontrado para Walmart: Sumatoria de todos los numeros de la tarjeta modulo 3, sea igual a 0");
console.log("10 Tarjetas invalidas de Walmart de " + walmartCantidad + " encontradas : ");
printCards(listInvalidCardsWalmart);
console.log("\n");

//Multiplicamos el dinero desviado por redundancia (100,000 * 1,800) = 18,000,000 votos acarreados
console.log("\nTotal de dinero desviado con alrededor de 100,000 tarjetas investigadas: \n" + moneyDesviado + " pesos");