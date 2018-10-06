import math
import random
import time
start_time = time.time()

def generador():
    n = 1000
    i = 0
    x = 0
    y = 0
    validas = []
    iN = []
    d_mas = []
    d_menos = []
    seed = 8273647364
    loop = 0
    div = 10000000000000000
    while loop == 0:
        i += 1
        seed = int(seed)
        seed = pow(seed,3)
        seed = seed / (math.sqrt(seed))
        seed = math.floor(seed)
        seed = str(seed)
        if len(seed) % 2 == 0:
        	while len(seed) > 16:
        			seed = seed[1:]
        			seed = seed[:-1]
        else:
        	seed = "0"+seed
        	while len(seed) > 16:
        			seed = seed[1:]
        			seed = seed[:-1]
        validas.append(seed) #rando number
        if len(validas) == n: #Generando mil numeros
        	loop = 1

    validas.sort()
    # print(validas)
    for i in range (n):
        # print(seed)
        iN.append(i/n) #i/n
        x1 = ((1/n) - int(validas[i])/div)
        d_mas.append(x1) #D+
        x2 = (int(validas[i])/div - ((i-1)/n))
        d_menos.append(x2) #D-

    y = 1.36/(math.sqrt(n))
    # print(d_menos)
    if(max(d_menos) > max(d_mas)):
        mayor = max(d_menos)
    else:
        mayor = max(d_mas)
    if(y > mayor):
        print(mayor)
        print(y)
        print("Generador valido")
    else: 
        print("No valido")

generador()