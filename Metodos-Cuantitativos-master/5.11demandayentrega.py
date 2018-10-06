
import random




def simulacionPedido():
    iterations = 260
    restockCost = 52
    restockQuantity = 100
    stock = 100
    cost = 0
    lowestCost = 0
    reorder = 10
    bestReorder = 0
    for j in range(5):
        reorder += 5
        print("Simulacion con ", reorder, " de restock")
        for i in range(iterations):

            if(stock <= 10):
                stock += reorder


            dailyDemandRand = random.random()
            if(dailyDemandRand <= 0.02):
                #25
                dailyDemand = 25
            elif(dailyDemandRand > 0.02 and dailyDemandRand <=0.06):
                #26
                dailyDemand = 26
            elif(dailyDemandRand > 0.06 and dailyDemandRand <= 0.12):
                #27
                dailyDemand = 27
            elif(dailyDemandRand > 0.12 and dailyDemandRand <= 0.24):
                #28
                dailyDemand = 28
            elif(dailyDemandRand > 0.24 and dailyDemandRand <= 0.44):
                #29
                dailyDemand = 29
            elif(dailyDemandRand > 0.44 and dailyDemandRand <= 0.68):
                #30
                dailyDemand = 30
            elif(dailyDemandRand > 0.68 and dailyDemandRand <= 0.83):
                #31
                dailyDemand = 31
            elif(dailyDemandRand > 0.83 and dailyDemandRand <= 0.93):
                #32
                dailyDemand = 32
            elif(dailyDemandRand > 0.93 and dailyDemandRand <= 0.98):
                #33
                dailyDemand = 33
            elif(dailyDemandRand > 0.98 and dailyDemandRand <= 1.00):
                #34
                dailyDemand = 34

            deliveryTimeRand = random.random()


            if(deliveryTimeRand <= 0.20):
                #1
                deliveryTime = 1
            elif(deliveryTimeRand > 0.20 and deliveryTimeRand <=0.50):
                #2
                deliveryTime = 2
            elif(deliveryTimeRand > 0.50 and deliveryTimeRand <= 0.75):
                #3
                deliveryTime = 3
            elif(deliveryTimeRand > 0.75 and deliveryTimeRand <= 1.00):
                #4
                deliveryTime = 4

            clientWaitingTimeRand = random.random()

            if(clientWaitingTimeRand <= 0.40):
                #0
                clientWaitingTime = 0
            elif(clientWaitingTimeRand > 0.40 and clientWaitingTimeRand <=0.60):
                #1
                clientWaitingTime = 1
            elif(clientWaitingTimeRand > 0.60 and clientWaitingTimeRand <= 0.75):
                #2
                clientWaitingTime = 2
            elif(clientWaitingTimeRand > 0.75 and clientWaitingTimeRand <= 0.90):
                #3
                clientWaitingTime = 3
            elif(clientWaitingTimeRand > 0.90 and clientWaitingTimeRand <= 1.00):
                #4
                clientWaitingTime = 4

            if(clientWaitingTime < deliveryTime):
                dailyDemand = 0

            cost += 100


            if(stock > dailyDemand):
                stock-= dailyDemand
            else:
                dailyDemand -= stock
                stock = 0
                if(clientWaitingTime < deliveryTime):
                    cost += 50* dailyDemand
                else:
                    cost += 20* dailyDemand

            if(stock  == 0):
                cost+= restockCost * restockQuantity

            if(i == 259):
                print("Al final del año quedaron", stock, " productos")
                cost += 52 * stock

        print("Costos totales al usar 100 unidades de stock inicial y", reorder, "de restock cuando se encontraban 10 o menos unidades en inventario: $", cost, "\n")
        if(j == 0):
            lowestCost = cost
            bestReorder = reorder
        else:
            if(lowestCost > cost):
                lowestCost = cost
                bestReorder = reorder
        cost = 0

    print("La cantidad de reorden optima es:", bestReorder)





if __name__ == '__main__':
    print("Tarea 1 ejercicio 5.11")
    simulacionPedido()
