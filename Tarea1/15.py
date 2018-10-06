# Alonso Iturbe Sotomayor
# A01021621

# Problema de tarea 15 - Depósito de almacenamiento
# Solución escrita en Python 3

# Librerías utilizadas: random
# Librerías utilizadas: math
# Librerías utilizadas: statistics

# python3 15.py

# Resultado ejemplo
'''
1 Camiones: $ 1,578,920.0
2 Camiones: $ 1,569,900.0
3 Camiones: $ 1,537,660.0
4 Camiones: $ 1,521,490.0
5 Camiones: $ 1,489,410.0
6 Camiones: $ 1,489,390.0
7 Camiones: $ 1,475,040.0
8 Camiones: $ 1,446,000.0
9 Camiones: $ 1,399,010.0
10 Camiones: $ 1,407,580.0
11 Camiones: $ 1,393,240.0
12 Camiones: $ 1,382,720.0
13 Camiones: $ 1,386,670.0
14 Camiones: $ 1,441,850.0
15 Camiones: $ 1,514,370.0
16 Camiones: $ 1,606,640.0
17 Camiones: $ 1,700,890.0
18 Camiones: $ 1,800,000
19 Camiones: $ 1,900,000
20 Camiones: $ 2,000,000
El número óptimo de camiones para adquirir es: 12 camiones
'''

import random
import math
import statistics

n = 250 #días que se trabajan en el año
camionesRange = list(range(1, 21)) # (inclusivo, exclusivo)

# Costos
costoAnualPorCamion = 100000
costoPorToneladaExcedente = 100

# Array para guardar costos de cada trial
costosAnuales = []

# Correr la simulación una vez por cada cantidad de camiones deseada
for camiones in camionesRange:
    
    #print("Intentando con", camiones, "camiones...")
    
    # Sumar costo de camiones
    costoAnual = 100000*camiones
    
    for experiment in range(n): # se corre el experimento por un año

        # Sacar cuánto se va a producir en el día
        probProduccionDiaria = random.uniform(0, 1)

        toneladas = random.randint(80, 85)
        if probProduccionDiaria < 0.98:
            toneladas = random.randint(75, 80)
            if probProduccionDiaria < 0.9:
                toneladas = random.randint(65, 70)
                if probProduccionDiaria < 0.55:
                    toneladas = random.randint(60, 65)
                    if probProduccionDiaria < 0.25:
                        toneladas = random.randint(55, 60)
                        if probProduccionDiaria < 0.1:
                            toneladas = random.randint(50, 55)
        
        #print("Se necesitan transportar", round(toneladas, 2), "tn.")

        # Sacar cuanta capacidad de transporte vamos a tener
        capacidadTotal = 0
        for camion in range(camiones):
            # Sacar cuánto puede transportar el camión
            probCapacidad = random.uniform(0, 1)

            capacidad = random.randint(55, 60)/10
            if probCapacidad < 0.9:
                capacidad = random.randint(50, 55)/10
                if probCapacidad < 0.7:
                    capacidad = random.randint(45, 50)/10
                    if probCapacidad < 0.3:
                        capacidad = random.randint(40, 45)/10
            
            # Sumar a la capacidad total
            capacidadTotal += capacidad
        
        #print("Se pueden transportar", round(capacidadTotal, 2), "tn.")

        # Sacar costos por capacidad faltante
        if capacidadTotal > toneladas: #Sobra capacidad, no hay problema
            costoDiario = 0
        else:
            costoDiario = (toneladas-capacidadTotal)*costoPorToneladaExcedente
            #print("Costo del día", experiment, ":", costoDiario)
        
        # Agregar al array histórico
        costoAnual += costoDiario

    # Agregar el valor final al array de costos
    costosAnuales.append(costoAnual)
    print(camiones, "Camiones: $", "{:,}".format(round(costoAnual, 2)))
    
print("El número óptimo de camiones para adquirir es:", camionesRange[costosAnuales.index(min(costosAnuales))], "camiones")