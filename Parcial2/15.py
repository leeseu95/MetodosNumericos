# Alonso Iturbe Sotomayor
# A01021621

# Problema de Tarea II #15 - Car Wash
# Solución escrita en Python 3

# Librerías utilizadas: random
# Librerías utilizadas: math
# Librerías utilizadas: statistics

# python3 15.py

import random
import numpy
import math
import statistics

historicoCoches = []

for hora in range(15): # simular 15 horas
    
    # Obtener número aleatorio entre 0 y 1
    probCantidad = random.uniform(0, 1)

    # Asumimos que empezamos con 8 coches
    coches = 8
    if probCantidad < 0.8:
        coches = 7
        if probCantidad < 0.5:
            coches = 6
            if probCantidad < 0.25:
                coches = 5
                if probCantidad < 0.1:
                    coches = 4

    historicoCoches.append(coches)

    print("-----------------------------")
    print("Hora #", hora, ": llegaron", coches, "coches")

print("*****************************")
print("En promedio, llegan", round(statistics.mean(historicoCoches), 2), "coches por hora")

