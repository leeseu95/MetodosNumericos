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

mat = np.zeros(shape=(3,3))
vecP = np.zeros(shape=(1,3))
# print(mat)
for iters in range (0, 1):
    mat = np.zeros(shape=(3,3))
    vecP = np.zeros(shape=(1,3))
    #Creamos una matriz y la llenamos de vectores cuya suma es igual a 1 aleatorio
    vector = ([.80, .10, .10]) #Northside se queda con el 80%
    mat[0] = vector
    vector = ([.20, .70, .10]) #West End se queda con el 70%
    mat[1] = vector
    vector = ([.25, .15, .60]) #Suburban se qeuda con su 60%
    mat[2] = vector
    
    #Metemos los valores a un arreglo para regresar el promedio al final
    # for row in range(0,3):
    #     for col in range(0,3):
    #         matValues[row][col] += mat[row][col]

    # print(mat)
    #Creamos un vector random que sera nuestro VectorP
    vecP[0] = ([100, 80 ,60])

    # print(vecP)
    #Empezamos a ciclar para estabilizar el vector
    years = 1
    differenceStabilize = 1
    differenceStabilize2 = 1
    differenceStabilize3 = 1
    
    while(differenceStabilize >= .0001 and differenceStabilize2 >= .0001 and differenceStabilize3 >= .0001):
        years +=1
        tempVec = vecP

        vecP = np.matmul(vecP, mat)
        differenceStabilize = abs(tempVec[0][0]) - abs(vecP[0][0])
        differenceStabilize2 = abs(tempVec[0][1]) - abs(vecP[0][1])
        differenceStabilize3 = abs(tempVec[0][2]) - abs(vecP[0][2])

    #Le agregamos los anos a yearsTaken
    yearsTaken += years

    #Metemos los valores a un arreglo para regresar el vector promedio al final
    # index = 0
    # for col in range(0,3):
    #     vecValues[index] += vecP[0][col]
    #     index += 1

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
print("\n")