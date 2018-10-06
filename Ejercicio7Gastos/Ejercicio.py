#Seung Lee - A01021720
#Problema Cuenta de Gastos

import random

iters = 5000

savings = 0
foodExpense = 0
transportationExpense = 0
remnants = 0

randomCost = 0

for i in range(0, iters):
    savings += 3000

    randomCost = random.randint(1, 6)

    #Si el costo es menos de 3000 se puede quitar de lo mensual
    if randomCost == 1:
        savings -= 1300
        transportationExpense += 1300
        savings -= 1700 * 0.4
        foodExpense += 1700 * 0.4
        remnants += 3000 - 1300 - (1700*.4)
    elif randomCost == 2:
        savings -= 1800
        transportationExpense += 1800
        savings -= (1200 * 0.4)
        foodExpense += 1200 * 0.4
        remnants += 3000 - 1800 - (1200 * 0.4)
    elif randomCost == 3:
        savings -= 2300
        transportationExpense += 2300
        savings -= 700 * 0.4
        foodExpense += 700 * 0.4
        remnants += 3000 - 2300 - (700*.4)
    elif randomCost == 4:
        savings -= 2800
        transportationExpense += 2800
        savings -= 200
        foodExpense += 200
        remnants += 3000 - 2800 - 200
    elif randomCost == 5:
        savings -= 3300
        transportationExpense += 3300
        savings -= 200
        foodExpense += 200
        remnants += 3000 - 3300 - 200
    else:
        savings -= 3800
        transportationExpense += 3800
        savings -= 200
        foodExpense += 200
        remnants += 3000 - 3800 - 200


print("Savings left: ", savings)
print("Transport cost average: ", transportationExpense/iters)
print("Food cost average: ", foodExpense/iters)
print("You should use at most ", remnants/iters, " per day on fun")
