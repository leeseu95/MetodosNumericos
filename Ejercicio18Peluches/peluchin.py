#Seung Hoon Lee
#A01021720
#Ejercicio 18 Peluchin

import random
import numpy as np
import math
import statistics

iters = 500
histogramaPeluches = []
preciosPeluches = []
revenue = 0
cost = 0
media = 0
peluchesSoldAverage = 0


counter = 215
for i in range(0, 110):
    histogramaPeluches.append(0) #Inicializacion de arreglos (precios y peluches vendidos)
    preciosPeluches.append(counter)
    counter += 1

for i in range(0, iters):
    
    distN = math.floor(np.random.normal(2500, 75)) #distribucion Normal al dia

    peluchesSoldAverage += distN #peluches vendidos por dia
    
    for peluches in range(0, distN):
        price = random.randint(215,324) #El precio es entre de 215 y 324
        revenue += price + 95 #El revenue es el precio + 95
        cost += price
        position = price - 215
        histogramaPeluches[position] += 1

cantidadMedia = 0 #Calculo de la media
for i in range(0, 110):
    media += histogramaPeluches[i] * preciosPeluches[i]
    cantidadMedia += histogramaPeluches[i]

varianzaSuma = 0
for i in range(0, 110):
    varianzaSuma += math.pow((preciosPeluches[i] - int(media/cantidadMedia)),2)
varianzaSuma /= 110

print("\nHistograma de Peluches\n")
print(histogramaPeluches)
print("\nTotal Cost to produce peluches: $", format(cost, ',d'))
print("\nTotal Revenue accumulated: $" , format(revenue, ',d'))
print("\nTotal Winnings: $", format(revenue - cost, ',d'))
print("\nPeluches Vendidos en Promedio por dia:", format(int(peluchesSoldAverage/iters), ',d') , "peluches")
print("\nMedia de precios:", format(int(media/cantidadMedia), ',d'), "pesos")
print("\nVarianza de precios:", format(int(varianzaSuma), ',d'), "pesos")
# print("\nVarianza:", format(int(statistics.variance(histogramaPeluches)), ',d'), "peluches vendidos")