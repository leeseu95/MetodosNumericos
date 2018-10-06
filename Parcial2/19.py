# Alonso Iturbe Sotomayor
# A01021621

# Problema de Tarea II #19 - Ventas durante partidos de americano
# Solución escrita en Python 3

# Librerías utilizadas: random
# Librerías utilizadas: math
# Librerías utilizadas: statistics

# python3 19.py

import random
import numpy
import math
import statistics

# A. Simule las ventas de programas en 10 partidos de fútbol

historicoVentas = []

for partido in range(10):
    
    # Obtener número aleatorio entre 0 y 1
    probVentas = random.uniform(0, 1)

    # Asumimos que empezamos con 27
    programasVendidos = 2700
    if probVentas < 0.82:
        programasVendidos = 2600
        if probVentas < 0.61:
            programasVendidos = 2500
            if probVentas < 0.37:
                programasVendidos = 2400
                if probVentas < 0.15:
                    programasVendidos = 2300
    
    # programasVendidos ahora tiene el resultado real de programas vendidos

    # agregar al histórico
    historicoVentas.append(programasVendidos)

print("A. Simule las ventas de programas en 10 partidos de fútbol")
print("Las ventas de los últimos 10 partidos fueron:")
for partido in range(10):
    print("#", partido, ":", historicoVentas[partido])
print("----------")
print("AVG :", statistics.mean(historicoVentas), "programas por partido")

# ----------------------------------------------------------------------------------------
# B. Si la universidad decide imprimir 2,500 programas para los 10 partidos del inciso A...

programasComprados = 2500
costoPorPrograma = 0.8
ingresoPorProgramaVendido = 2.00

utilidadesHistorico = []

for partido in range(10):
    
    demandaProgramas = historicoVentas[partido]

    if (demandaProgramas > programasComprados): # faltaron programas
        
        costos = programasComprados * costoPorPrograma # igual para ambos casos
        ingresos = programasComprados * ingresoPorProgramaVendido # no se puede vender más de lo que se compró!

        utilidadesHistorico.append(ingresos-costos)

    elif (demandaProgramas <= programasComprados): # hubo menos o igual demanda de lo que se produjo

        costos = programasComprados * costoPorPrograma # igual para ambos casos
        ingresos = demandaProgramas * ingresoPorProgramaVendido # se vendió únicamente lo que se demandó

        utilidadesHistorico.append(ingresos-costos)

print("----------------------------------------------------------------------------------------")
print("B. Si la universidad decide imprimir 2,500 programas para los 10 partidos del inciso A...")
#for partido in range(10):
#    print("Utilidades del partido #", partido, ": ", utilidadesHistorico[partido])
print("El promedio de utilidades de los 10 partidos fue de $", statistics.mean(utilidadesHistorico), "USD por partido")

# ----------------------------------------------------------------------------------------
# C. Si la universidad decide imprimir 2,600 programas para los 10 partidos del inciso A...

programasComprados = 2600
costoPorPrograma = 0.8
ingresoPorProgramaVendido = 2.00

utilidadesHistorico2 = []

for partido in range(10):
    
    demandaProgramas = historicoVentas[partido]

    if (demandaProgramas > programasComprados): # faltaron programas
        
        costos = programasComprados * costoPorPrograma # igual para ambos casos
        ingresos = programasComprados * ingresoPorProgramaVendido # no se puede vender más de lo que se compró!

        utilidadesHistorico2.append(ingresos-costos)

    elif (demandaProgramas <= programasComprados): # hubo menos o igual demanda de lo que se produjo

        costos = programasComprados * costoPorPrograma # igual para ambos casos
        ingresos = demandaProgramas * ingresoPorProgramaVendido # se vendió únicamente lo que se demandó

        utilidadesHistorico2.append(ingresos-costos)

print("----------------------------------------------------------------------------------------")
print("C. Si la universidad decide imprimir 2,600 programas para los 10 partidos del inciso A...")
#for partido in range(10):
#    print("Utilidades del partido #", partido, ": ", utilidadesHistorico2[partido])
print("El promedio de utilidades de los 10 partidos fue de $", statistics.mean(utilidadesHistorico2), "USD por partido")