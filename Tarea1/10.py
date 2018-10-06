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

n = 200 #número de días en un año

# Costos
costoPorDia = 0.1
costoDeFaltante = 25
costoDeOrdenar = 50

# Variables para los inventarios
inventario = 0
costo = 0
pedidoTimeout = 0

# Ordenar hasta... (q)
ordenarRange = list(range(1, 15)) # (inclusivo, exclusivo)

# ...cuando el nivel del inventario sea <= .... (r)
nivelDeInventarioRange = list(range(1, 31)) # (inclusivo, exclusivo)

# Variables para guardar el resultado óptimo
bestR = 0
bestQ = 0
bestCost = 999999999999999

# Política: Ordenar hasta q artículos cuando el nivel del inventario es <= r
for q in ordenarRange:
    for r in nivelDeInventarioRange:
        costo = 0
        for experiment in range(n): # se corre el experimento por un año (260 días)

            # 1. Obtener demanda por día
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
            
            # 2. Actualizar inventario por demanda
            inventario -= demanda
            
            # 3. Checar si nos pasamos de lo que había
            if inventario < 0: # sí nos pasamos
                costo += abs(inventario)*costoDeFaltante #sumar penalización
                inventario = 0 #reestablecer

            # 4. Checar si ya nos llegó un pedido previo
            if pedidoTimeout == 1: # Sólo faltaba un día, y ya se cumplió
                pedidoTimeout = 0 # reestablecerlo
                inventario = q # inventario repuesto
            
            elif pedidoTimeout > 1: # día normal
                pedidoTimeout -= 1 # decrementar un día

            # 3. Hacer pedido en caso de ser necesario
            if inventario <= r and pedidoTimeout == 0: # hay menos de r, hay que ordenar AND NO HAY PEDIDOS VIGENTES
                costo += costoDeOrdenar # se hizo una órden
                
                # Sacar cuántos días se tardará nuestro pedido en llegar
                probPedido = random.uniform(0, 1)

                pedidoTimeout = 4
                if probPedido < 0.95:
                    pedidoTimeout = 3
                    if probPedido < 0.75:
                        pedidoTimeout = 2
                        if probPedido < 0.25:
                            pedidoTimeout = 1

            # 4. Sumar costos por tener mantener elementos en el inventario
            costo += inventario * costoPorDia
        
        print("q:", q, "r:", r, " => $", "{:,}".format(round(costo, 2)))
        if costo < bestCost:
            bestCost = costo
            bestQ = q
            bestR = r
        
print()
print("✓q:", bestQ)
print("✓r:", bestR)
print("✓c: $", "{:,}".format(round(bestCost, 2)))