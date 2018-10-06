//Seung Hoon Lee - A01021720
//Ejercicio Javascript 1

function assert(value, text) {
    var li = document.createElement("li");
    li.className = value ? "pass" : "fail";
    li.appendChild(document.createTextNode(text));
    var results = document.getElementById("results");
    if (!results) {
      results = document.createElement("ul");
      results.setAttribute('id','results');
      document.body.appendChild(results);
    }
    results.appendChild(li);
  }
  
  function pass(text) { assert(true, text); }
  function fail(text) { assert(false, text); }
  function report(text) { pass(text); }

  function buscaMayor(arrayNumbers) {
      var count = 1;
      var sequenceSize = 1;
      var initialPos;
      var sequenceRes = [];
      var result = {tam:0, res:0};

      for (i = 0; i < arrayNumbers.length; i++){
          if (arrayNumbers[i+1] >= arrayNumbers[i]){
              count ++;
          } else {
              count = 1;
          }
          if (count > sequenceSize) {
              sequenceSize = count;
              initialPos = i - (sequenceSize-2);
          }
      }
      for (i = initialPos; i < (initialPos + sequenceSize); i++)
      {
          sequenceRes.push(arrayNumbers[i])
      }
      result.res = sequenceRes;
      result.tam = sequenceSize;
      return result;
  }













