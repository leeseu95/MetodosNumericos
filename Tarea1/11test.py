# Alonso Iturbe Sotomayor
# A01021621

# Problema de tarea #10 - Demanda diaria sacando (q) y (R)
# Solución escrita en Python 3

# Librerías utilizadas: random
# Librerías utilizadas: math
# Librerías utilizadas: statistics

# python3 10.py

# Resultado ejemplo
'''
Progress: 100.0 %
✓q: 77
✓r: 13
✓c: 1,737.7
'''

import random
import numpy
import math
import statistics

n = 260 #número de días en un año

# Costos
costoPorDia = 0.2
costoDeOrdenar = 100

# Variables para los inventarios
inventario = 15
costo = 0
pedidoTimeout = 0

# Ordenar hasta... (q)
ordenarRange = list(range(1, 101)) # (inclusivo, exclusivo)

# ...cuando el nivel del inventario sea <= .... (r)
nivelDeInventarioRange = list(range(1, 101)) # (inclusivo, exclusivo)

# Variables para guardar el resultado óptimo
bestR = 0
bestQ = 0
bestCost = 999999999999999

# Auxiliar para output
counter = 1

# Política: Ordenar hasta q artículos cuando el nivel del inventario es <= r
for q in ordenarRange:
    print("Progress:", round(counter/len(ordenarRange)*100, 2), "%", end='\r')
    counter += 1
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
                demanda = 0

            # 2. Actualizar inventario por demanda
            if(inventario > demanda):
                inventario -= demanda
            else:
                demanda -= inventario
                inventario = 0
                if (clienteTimeout < pedidoTimeout):
                    costo += 50 * demanda
                else
                    costo += 20 * demanda

            if(inventario == 0 ):
                costo += costo
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