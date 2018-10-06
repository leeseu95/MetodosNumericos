var queueLine = 0;
var clientsAttended = 0;
var systemTime = 0;

var cashier1Time = 0;
var cashier2Time = 0;
var cashier3Time = 0;

var cashier1TimeBusy = 0;
var cashier2TimeBusy = 0;
var cashier3TimeBusy = 0;

var cashier1Prob = 0;
var cashier2Prob = 0;
var cashier3Prob = 0;

var cashier1Free = true;
var cashier2Free = true;
var cashier3Free = true;

for (j = 0; j < 500; j++) {
    cashier1Time = 0;
    cashier2Time = 0;
    cashier3Time = 0;

    var cashier1TimeBusy = 0;
    var cashier2TimeBusy = 0;
    var cashier3TimeBusy = 0;
    for (i = 1; i <= 86400; i++) {
        if(i % 90 == 0) { //Cada 1:30 (minuto y medio) llega un nuevo cliente 
            queueLine += 1;
        }
        //Pasa 1 segundo para los 3 cajeros despues de cada iteracion
        cashier1Time += 1;
        cashier2Time += 1;
        cashier3Time += 1;

        //Checamos si alguno de los cajeros esta disponible cada segundo y si hay alguien en la linea del queue
        if(queueLine > 0 && cashier1Free == true){
            cashier1Prob = Math.floor(((Math.random() * 60) + 1));
            // console.log(cashier1TimeBusy);
            cashier1TimeBusy = cashier1Time + cashier1Prob; //El tiempo hasta el que va a estar ocupado este cajero
            queueLine -= 1;
            cashier1Free = false;
            systemTime += cashier1Prob;
            clientsAttended += 1;
        } 
        if(queueLine > 0 && cashier2Free == true) {
            cashier2Prob = Math.floor(((Math.random() * 60) + 1));
            cashier2TimeBusy = cashier2Time + cashier2Prob; //El tiempo hasta el que va a estar ocupado este cajero
            queueLine -= 1;
            cashier2Free = false;
            systemTime += cashier2Prob;
            clientsAttended += 1;
        } 
        if (queueLine > 0 && cashier3Free == true) {
            cashier3Prob = Math.floor(((Math.random() * 60) + 1));
            cashier3TimeBusy = cashier3Time + cashier3Prob; //El tiempo hasta el que va a estar ocupado este cajero
            queueLine -= 1;
            cashier3Free = false;
            systemTime += cashier3Prob;
            clientsAttended += 1;
        }
    
        //Despues de cada segundo tenemos que ver si alguno de los cajeros ya se libero
        if(cashier1TimeBusy <= i) //Si el tiempo que decidimos que el cajero iba a estar ocupado ya paso, entonces deberia de estar libre
            cashier1Free = true;
        if(cashier2TimeBusy <= i)
            cashier2Free = true;
        if (cashier3TimeBusy <= i)
            cashier3Free = true;
    }
}

console.log("\nTotal time in system: ", Math.floor((systemTime/60)), " minutes" );
console.log("Total amount of customers attended: " , clientsAttended, "\n\n");
console.log("System Average Time per day: ", Math.floor((systemTime/60)/500), " minutes ");
console.log("Average customers attended per day: ", clientsAttended/500);
