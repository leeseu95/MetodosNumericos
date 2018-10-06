#Seung Hoon Lee - A01021720
#Ejercicio RanVal

import math
import random
import time
import numpy
start_time = time.time()

def generador():
    n = 1000
    i = 0
    validas = []
    iN = []
    deeplus = []
    deenegative = []
    deeMax = []
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
        iN.append(i/n) #i/n
        if len(validas) == n: #Generando mil numeros
        	loop = 1
    validas.sort()
    # print(validas)
    # print(iN)
    for iters in range (0, 1000):
        temp = ((iters/n) - int(validas[iters])/ div)
        deeplus.append(temp)
    
    for iters in range (0, 1000):
        temp = (int(validas[iters])/ div - (iters-1/n))
        deenegative.append(temp)

    for iters in range (0, 1000):
        if (deeplus[iters] > deenegative[iters]):
            deeMax.append(deeplus[iters])
        elif (deeplus[iters] < deenegative[iters]):
            deeMax.append(deenegative[iters])
        else:
            deeMax.append(deeplus[iters])
            
    maxNum = max(deeMax)
    # print(deeplus)
    # print(deenegative)
    # print(deeMax)
    y = 1.36 / math.sqrt(n)
    print("Max Number: " , maxNum)
    if(maxNum < y):
        print("Numero a comparar: " , y)
        print("Generador Valido")
generador()