//Seung Lee - A01021720
//Validacion Random

const size = 1000;

while (validCardNum < 1) {
    let arrayOrder = [];
    let temp = 0;

    for(let i = 1; i <= size; i++) {
        arrayOrder.push(Math.floor(Math.random() * 10));
    }
    // console.log(card);
    for (let i = 1; i <= size; i++) {
        if (i % 2 == 1) {
            arrayOrder[i-1] *= 2;
            if(arrayOrder[i-1] > 9) {
                arrayOrder[i-1] = 1 +(arrayOrder[i-1] % 10);
            }
        }
    }

    arrayOrder.sort();


    // console.log(card);
    
    // for (let i = 1; i <= size; i++) {
    //     temp += card[i-1];
    // }

    // if (temp % 10 == 0){
    //     if(!listValidCards.includes(card)){
    //         validCardNum ++;
    //         listValidCards.push(card);
    //     }
    // }
    // counter ++;
}
console.log(arrayOrder);