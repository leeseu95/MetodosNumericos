import random

iters = 260 #260 dias que se trabajan

#costos
costoOrden = 100 
costoInventario = 52
costoFaltanteEspera = 20
costoFaltanteSinEspera = 50

restock = 100
stock = 100

cost = 0
lowestCost = 0

reorder = 0
bestReorder = 0

ordenarRange = list(range(1, 101))
inventoryRange = list(range(1,101))

for i in ordenarRange:
    reorder += 1
    for j in range(iters):
        if(stock <= 10):
            stock += reorder

        #Probabilidad de cantidad en demanda
        probDemanda = random.uniform(0, 1)

        demanda = 34
        if probDemanda < 0.98:
            demanda = 33
            if probDemanda < 0.93:
                demanda = 32
                if probDemanda < 0.83:
                    demanda = 31
                    if probDemanda < 0.68:
                        demanda = 30
                        if probDemanda < 0.44:
                            demanda = 29
                            if probDemanda < 0.24:
                                demanda = 28
                                if probDemanda < 0.12:
                                    demanda = 27
                                    if probDemanda < 0.06:
                                        demanda = 26
                                        if probDemanda < 0.02:
                                            demanda = 25

        #Probabilidad de tiempo de espera del pedido
        probPedido = random.uniform(0, 1)

        pedidoTimeout = 4
        if probPedido < 0.75:
            pedidoTimeout = 3
            if probPedido < 0.50:
                pedidoTimeout = 2
                if probPedido < 0.20:
                    pedidoTimeout = 1

            #Probabilidad de tiempo de espera del cliente
        probCliente = random.uniform(0, 1)

        clienteTimeout = 4
        if probCliente < 0.90:
            clienteTimeout = 3
            if probCliente < 0.75:
                clienteTimeout = 2
                if probCliente < 0.60:
                    clienteTimeout = 1
                    if probCliente < 0.40:
                        clienteTimeout = 0


        if(clienteTimeout < pedidoTimeout):
            dailyDemand = 0

        cost += 100


        if(stock > demanda):
            stock-= demanda
        else:
            demanda -= stock
            stock = 0
            if(clienteTimeout < pedidoTimeout):
                cost += 50* demanda
            else:
                cost += 20* demanda

        if(stock  == 0):
            cost+= costoInventario * restock

        if(i == 259):
            cost += 52 * stock

    # print("Costos totales al usar 100 unidades de stock inicial y", reorder, "de restock cuando se encontraban 10 o menos unidades en inventario: $", cost, "\n")
    if(i == 1):
        lowestCost = cost
        bestReorder = reorder
    else:
        if(lowestCost > cost):
            lowestCost = cost
            bestReorder = reorder
    cost = 0

print("La canidad optima es:", )
print("La cantidad de reorden optima es:", bestReorder)
print("Costo:", lowestCost)