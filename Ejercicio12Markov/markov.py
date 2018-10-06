#Seung Hoon Lee
#A01021720
#Ejercicio 12 Markov

import random
import numpy as np
import math

#Variables a definir
matValues = np.zeros(shape=(3,3))
vecValues = [0, 0 ,0]
yearsTaken = 0
iterations = 5000

mat = np.zeros(shape=(3,3))
vecP = np.zeros(shape=(1,3))
# print(mat)
for iters in range (0, 5000):
    mat = np.zeros(shape=(3,3))
    vecP = np.zeros(shape=(1,3))
    #Creamos una matriz y la llenamos de vectores cuya suma es igual a 1 aleatorio
    for llenar in range(0, 3):
        vector = np.random.dirichlet(np.ones(3),size=1)
        mat[llenar] = vector
    
    #Metemos los valores a un arreglo para regresar el promedio al final
    for row in range(0,3):
        for col in range(0,3):
            matValues[row][col] += mat[row][col]

    # print(matValues)
    #Creamos un vector random que sera nuestro VectorP
    vector = np.random.dirichlet(np.ones(3),size=1)
    vecP[0] = vector

    #Empezamos a ciclar para estabilizar el vector
    years = 1
    differenceStabilize = 1
    differenceStabilize2 = 1
    differenceStabilize3 = 1
    
    while(differenceStabilize >= .0001 and differenceStabilize2 >= .0001 and differenceStabilize3 >= .0001):
        years +=1
        tempVec = vecP

        vecP = np.matmul(vecP, mat)
        differenceStabilize = abs(tempVec[0][0] - vecP[0][0])
        differenceStabilize2 = abs(tempVec[0][1] - vecP[0][1])
        differenceStabilize3 = abs(tempVec[0][2] - vecP[0][2])

    #Le agregamos los anos a yearsTaken
    yearsTaken += years

    #Metemos los valores a un arreglo para regresar el vector promedio al final
    index = 0
    for col in range(0,3):
        vecValues[index] += vecP[0][col]
        index += 1

# myList[:] = [x / myInt for x in myList]
matValues[:] = [x / iterations for x in matValues]
vecValues[:] = [x / iterations for x in vecValues]
yearsTaken /= iterations



print("\nMatriz Promedio al final de ", iterations, " iteraciones:")
print(matValues)
print("\nVector Promedio estabilizado al final de ", iterations, " iteraciones:")
print(vecValues)
print("\nAnos Promedio para estabilizar al final de ", iterations, " iteraciones:")
print(round(yearsTaken, 2))
print("\n")