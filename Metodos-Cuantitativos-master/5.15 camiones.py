import random
import math

outsourcing = 0
productOutsourced = 0

for i in range(0,250):
    production = random.random()

    if production <= 0.1:
        production = random.randint(50,55)
    elif production > 0.1 and production <= 0.25:
        production = random.randint(55,60)
    elif production > 0.25 and production <= 0.55:
        production = random.randint(60,65)
    elif production > 0.55 and production <= 0.9:
        production = random.randint(65,70)
    elif production > 0.9 and production <= 0.98:
        production = random.randint(70,75)
    else:
        production = random.randint(75,80)

    truckLoad = random.random()

    if truckLoad <= 0.3:
        truckLoad = random.uniform(4.0,4.5)
    elif truckLoad > 0.3 and truckLoad <= 0.7:
        truckLoad = random.uniform(4.5, 5.0)
    elif truckLoad > 0.7 and truckLoad <= 0.9:
        truckLoad = random.uniform(5.0,5.5)
    else:
        truckLoad = random.uniform(5.5,6.0)

    production -= truckLoad

    if production > 0:
        outsourcing += production * 100
        productOutsourced += production

productOutsourced /= 250

print("\n","-"*20)
print("Outsourcing investment: $","{0:.2f}".format(outsourcing))
print("You can by ", math.ceil(outsourcing/100000),"trucks with the investment of outsourcing")
print("You'll nead a total of",math.ceil(productOutsourced/5),"trucks (5Ton load) to transport", math.ceil(productOutsourced),"Tons")
print(" -"*20,"\n")
