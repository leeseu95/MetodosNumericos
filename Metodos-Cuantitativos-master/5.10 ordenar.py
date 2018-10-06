from random import random
from math import ceil

inventory = 0
orderTime = 0
order = 0
holding = 0
missing = 0
totMissing = 0
waitingOrder = False
inventory = 15
limite = 5

for day in range(0,260):

    if orderTime == 0 and waitingOrder == True:
        inventory += 15
        order += 1
        waitingOrder = False
        print("Stocked")

    if inventory <= limite and not waitingOrder:
        print("Reordered")
        orderTime = random()
        if orderTime <= 0.25:
            orderTime = 1
        elif orderTime > 0.25 and orderTime <= 0.75:
            orderTime = 2
        elif orderTime > 0.75 and orderTime <= 0.95:
            orderTime = 3
        else:
            orderTime = 4
        waitingOrder = True

    print("D",day,"i" ,inventory, "m",totMissing, "h",holding, "or",orderTime)



    dailyDemand = random()
    if dailyDemand <= 0.04:
        dailyDemand = 0
    elif dailyDemand > 0.04 and dailyDemand <= 0.1:
        dailyDemand = 1
    elif dailyDemand > 0.1 and dailyDemand <= 0.2:
        dailyDemand = 2
    elif dailyDemand > 0.2 and dailyDemand <= 0.4:
        dailyDemand = 3
    elif dailyDemand > 0.4 and dailyDemand <= 0.7:
        dailyDemand = 4
    elif dailyDemand > 0.7 and dailyDemand <= 0.88:
        dailyDemand = 5
    elif dailyDemand > 0.88 and dailyDemand <= 0.96:
        dailyDemand = 6
    elif dailyDemand > 0.96 and dailyDemand <= 0.99:
        dailyDemand = 7
    else:
        dailyDemand = 8
    print("Todays demand", dailyDemand)

    if orderTime > 0:
        orderTime -= 1
        if inventory < dailyDemand:
            dailyDemand = dailyDemand - inventory
            inventory = 0
            #print("Daily deman missing", dailyDemand)
            missing += dailyDemand
            totMissing += dailyDemand
            #print(missing)
        elif inventory > dailyDemand:
            inventory -= dailyDemand
            holding += inventory
    else:
        if inventory > dailyDemand:
            inventory -= dailyDemand
            holding += inventory




print("-"*20)
print("Reordering everytime stock hits:",limite )
print("Lost Fee Cost: $",totMissing*25)
print("Order Fee Cost: $", order*50)
print("Holding Fee Cost: $",holding*26)
print("-"*20)
#print("Total demand:", totalDemand, "that would be",ceil(totalDemand/15),"reorders")
