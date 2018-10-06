//Seung Lee - A01021720
//Validacion Random

const size = 1000;
var arrayOrder = [];

for(let i = 0; i < 1; i++) {
    let temp = 0;

    for(let i = 1; i <= size; i++) {
        arrayOrder.push(Math.floor(Math.random() * 10000));
    }

    // console.log(card);
    // for (let i = 1; i <= size; i++) {
    //     if (i % 2 == 1) {
    //         arrayOrder[i-1] *= 2;
    //         if(arrayOrder[i-1] > 999) {
    //             for(let i = 0; i < 4; i++){
    //                 arrayOrder[i-1] += (arrayOrder[i-1] % 10);
    //             }
    //         }
    //     }
    // }

    arrayOrder.sort();
}
console.log(arrayOrder);