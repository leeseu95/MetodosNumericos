//Seung Lee - A01021720

const size = 16;
const max = 99999999999999999;

const list = [];
const ranList = [];

for (let i = 0; i < max; i ++) {
    list.push((new Array(size + 1). join('0') + i).slice(-size));
}

for (let i = 0; i < max; i++) {
    let randomNum = Math.floor((Math.random() * list.length));
    ranList.push(list[randomNum]);
    // console.log(list[randomNum]);
    list.splice(randomNum, 1);
}

console.log(ranList);