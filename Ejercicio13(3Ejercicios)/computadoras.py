#Seung Hoon Lee
#A01021720
#Ejercicio 13 Markov

import random
import numpy as np
import math

#Variables a definir
matValues = np.zeros(shape=(3,3))
vecValues = [0, 0 ,0]
yearsTaken = 0
iterations = 5000
totalComps = 0
stabilize = .000000001

mat = np.zeros(shape=(3,3))
vecP = np.zeros(shape=(1,3))
# print(mat)
for iters in range (0, 1):
    #Creamos una matriz y la llenamos de vectores cuya suma es igual a 1 aleatorio
    vector = ([.80, .10, .10]) #Northside se queda con el 80%
    mat[0] = vector
    vector = ([.05, .90, .05]) #West End se queda con el 70%
    mat[1] = vector
    vector = ([.20, .10, .70]) #Suburban se qeuda con su 60%
    mat[2] = vector

    vecP[0] = ([200000, 200000, 200000])


    # print(vecP)
    #Empezamos a ciclar para estabilizar el vector
    years = 0
    differenceStabilize = 1
    differenceStabilize2 = 1
    differenceStabilize3 = 1
    
    while(differenceStabilize > stabilize or differenceStabilize2 > stabilize or differenceStabilize3 > stabilize):
        years +=1
        tempVec = vecP

        vecP = np.matmul(vecP, mat)
        differenceStabilize = abs(tempVec[0][0] - vecP[0][0])
        differenceStabilize2 = abs(tempVec[0][1] - vecP[0][1])
        differenceStabilize3 = abs(tempVec[0][2] - vecP[0][2])

        index = 0
        for col in range(0,3):
            vecValues[index] += vecP[0][col]
            index += 1

    #Le agregamos los anos a yearsTaken
    yearsTaken += years

for amount in range(0, 3):
    totalComps += vecValues[amount]

# myList[:] = [x / myInt for x in myList]
# matValues[:] = [x / iterations for x in matValues]
# vecValues[:] = [x / iterations for x in vecValues]
# yearsTaken /= iterations



print("\nMatriz al final ")
print(mat)
print("\nVector Promedio al final")
print(vecP)
print("\nAnos Promedio para estabilizar ")
print(yearsTaken)
print("\nComputadoras compradas por Doorway ")
print(vecValues[0])
print("\nComputadoras compradas por Bell ")
print(vecValues[1])
print("\nComputadoras compradas por Kumpaq ")
print(vecValues[2])
print("\n")