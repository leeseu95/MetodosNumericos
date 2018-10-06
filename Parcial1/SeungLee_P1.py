# Seung Hoon Lee Kim - A01021720

# Examen - Parcial 1
# Pregunta 1 Manejo de inventario
# Solución escrita en Python 3

# Librerías utilizadas: random
# Librerías utilizadas: math
# Librerías utilizadas: statistics

import random
import numpy
import math
import statistics

inventory = 0
limite = 5
order = 0
costOrder = 50
costInventory = 26/200 #Costo de unidad de inventario al ano
costMissing = 25

missing = 0
totalMissing = 0
stock = 0

for day in range(0,200):
    probDemanda = random.uniform(0, 1)

    demanda = 8
    if probDemanda < 0.99:
        demanda = 7
        if probDemanda < 0.96:
            demanda = 6
            if probDemanda < 0.88:
                demanda = 5
                if probDemanda < 0.7:
                    demanda = 4
                    if probDemanda < 0.4:
                        demanda = 3
                        if probDemanda < 0.2:
                            demanda = 2
                            if probDemanda < 0.1:
                                demanda = 1
                                if probDemanda < 0.04:
                                    demanda = 0
    # print("Todays demand", demanda)

    if inventory < demanda: #Si el inventario es menor a la demanda
        # print("Demanda", demanda, "inventory", inventory)
        demanda = demanda - inventory #La demanda le restamos lo que tenemos
        inventory = 0 #el inventari ose vuelve 0
        missing += demanda #Le agregamos lo que nos falta de la demanda
        totalMissing += demanda #se lo agregamos a los costos al final

    elif inventory > demanda: #si el inventario es mayor
        inventory -= demanda #le quitamos al inventario lo que nos hacia falta
        stock += inventory #y al stock le agregamos el costo de inventario 
    
    if inventory <= limite: #Si nuestro inventario cae de 5 o menos
        inventory += 15 # Ordenados 15 al inventario otra vez despues de cada dia
        order += 1
        # print("Reordenando 15 mas")

print("\nReordenando cuando el inventario es :", limite, " o menos" )

print("\nCostos en faltantes: $", totalMissing*costMissing)
print("Costos de ordenes: $", order*costOrder)
print("Costos de inventario: $",stock*costInventory)

print("\nCosto total al ano de 200 dias: $", (totalMissing*costMissing + order*costOrder + stock*costInventory))
