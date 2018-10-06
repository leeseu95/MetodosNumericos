#A01021730 Edgar Adrina Garcia Villegas

import random

totalCars = 0
totalBudget = 0

Scar = 0
Sbudget = 0
sitem = [0]*5

Mcar = 0
Mbudget = 0
mitem = [0]*5

Lcar = 0
Lbudget = 0
litem = [0]*5

simulation = int(input("¿Cuántas rondas quieres simular? "))

for i in range(0,simulation):
    numberOfCars = random.random()

    smallCars = 0
    smallBudget = 0

    mediumCars = 0
    mediumBudget = 0

    largeCars = 0
    largeBudget = 0

    if numberOfCars <= 0.05:
        numberOfCars = 3
    elif numberOfCars > 0.05 and numberOfCars <= 0.2:
        numberOfCars = 4
    elif numberOfCars > 0.2 and numberOfCars <= 0.5:
        numberOfCars = 5
    elif numberOfCars > 0.5 and numberOfCars <= 0.75:
        numberOfCars = 6
    elif numberOfCars > 0.75 and numberOfCars <= 0.9:
        numberOfCars = 7
    else:
        numberOfCars = 8

    totalCars += numberOfCars

    for cars in range(0,numberOfCars):
        typeOfCar = random.random()
        if typeOfCar <= 0.33:
            smallCars += 1
        elif typeOfCar > 0.33 and typeOfCar <= 0.66:
            mediumCars += 1
        else:
            largeCars += 1

    Scar += smallCars
    Mcar += mediumCars
    Lcar += largeCars

    for small in range(0, smallCars):
        obj = random.random()
        if obj <= 0.45:
            smallBudget += 350
            sitem[0] += 1
        elif obj > 0.45 and obj <= 0.6:
            smallBudget += 1575
            sitem[1] += 1
        elif obj > 0.60 and obj <= 0.8:
            smallBudget += 1925
            sitem[2] += 1
        elif obj > 0.8 and obj <= 0.9:
            smallBudget += 2540
            sitem[3] += 1
        else:
            smallBudget += 700
            sitem[4] += 1

    for medium in range(0, mediumCars):
        obj = random.random()
        if obj <= 0.25:
            mediumBudget += 550
            mitem[0] += 1
        elif obj > 0.25 and obj <= 0.5:
            mediumBudget += 1975
            mitem[1] += 1
        elif obj > 0.5 and obj <= 0.65:
            mediumBudget += 2545
            mitem[2] += 1
        elif obj > 0.65 and obj <= 0.85:
            mediumBudget += 2925
            mitem[3] += 1
        else:
            mediumBudget += 700
            mitem[4] += 1

    for large in range(0, largeCars):
        obj = random.random()
        if obj <= 0.1:
            largeBudget += 750
            litem[0] += 1
        elif obj > 0.1 and obj <= 0.25:
            largeBudget += 2275
            litem[1] += 1
        elif obj > 0.25 and obj <= 0.55:
            largeBudget += 2845
            litem[2] += 1
        elif obj > 0.55 and obj <= 0.95:
            largeBudget += 3415
            litem[3] += 1
        else:
            largeBudget += 700
            litem[4] += 1

    Sbudget += smallBudget
    Mbudget += mediumBudget
    Lbudget += largeBudget

totalBudget += Sbudget + Mbudget + Lbudget

print("Total de dias simulados: ", totalCars)
print("\nTotal de presupuesto $", totalBudget)
#Amount of cash by percentage
print("\t75%: $", totalBudget*0.75/simulation)
print("\t80%: $", totalBudget*0.80/simulation)
print("\t85%: $", totalBudget*0.85/simulation)
print("\t90%: $", totalBudget*0.90/simulation)
print("\t95%: $", totalBudget*0.95/simulation)
#Small Cars
print("\nCarros Pequeno: ", Scar, " - ", "%{0:.4f}".format(Scar/totalCars))
print("\tPresupuestos: $", Sbudget)
print("\tAceite y Filtro: ", sitem[0])
print("\tBalatas: ", sitem[1])
print("\tAceite, filtro y balatas: ", sitem[2])
print("\tAceite, filtro, balatas y bujías: ", sitem[3])
print("\tVerificacion: ", sitem[3])
#Medium Cars
print("\nCarros Medianos: ", Mcar, " - ", "%{0:.4f}".format(Mcar/totalCars))
print("\tPresupuestos: $", Mbudget)
print("\tAceite y Filtro: ", mitem[0])
print("\tBalatas: ", mitem[1])
print("\tAceite, filtro y balatas: ", mitem[2])
print("\tAceite, filtro, balatas y bujías: ", mitem[3])
print("\tVerificacion: ", mitem[3])
#Large cars
print("\nCarros Grandes ", Lcar, " - ", "%{0:.4f}".format(Lcar/totalCars))
print("\tPresupuestos: $", Lbudget)
print("\tAceite y Filtro: ", litem[0])
print("\tBalatas: ", litem[1])
print("\tAceite, filtro y balatas: ", litem[2])
print("\tAceite, filtro, balatas y bujías: ", litem[3])
print("\tVerificacion: ", litem[3])
#Stadar
print("")
