# Alonso Iturbe Sotomayor
# A01021621

# Problema de Tarea II #18 - Barcazas 2.0
# Solución escrita en Python 3

# Librerías utilizadas: random
# Librerías utilizadas: math
# Librerías utilizadas: statistics

# python3 barcazas.py

# Resultado ejemplo

import random
import math
import statistics

# Vectores de datos hardcodeados
vectorLlegadas = [37,77,13,10,2,18,31,19,32,85,31,94,81,43,31,58,33,51]
vectorDescargas = [69,84,12,94,51,36,17,2,15,29,16,52,56,43,26,22,8,62]

# Vectores históricos
historicoAcarreados = []
historicoLlegadas = []
historicoDescargados = []

n = 15 # número de iteraciones
iteracion = 0 # contador

barcazasAcarreadas = 0 #barcazas que se llevan acarreadas desde el día anterior

for experiment in range(n): # 15 días de experimentos

    print("---------------------------")
    print("Día #", experiment)

    # BARCAZAS QUE LLEGAN
    barcazasProb = vectorLlegadas[iteracion] #obtener probabilidad de barzacas

    barcazasNoche = 5 #asumimos que atracan 5 barcazas
    if barcazasProb < 90:
        barcazasNoche = 4
        if barcazasProb < 70:
            barcazasNoche = 3
            if barcazasProb < 45:
                barcazasNoche = 2
                if barcazasProb < 30:
                    barcazasNoche = 1
                    if barcazasProb < 13:
                        barcazasNoche = 0
    
    # agregar al histórico
    historicoLlegadas.append(barcazasNoche)

    # BARCAZAS QUE SE DESCARGAN
    llegadasProb = vectorDescargas[iteracion] #obtener probabilidad de descarga de barzacas

    capacidadDescarga = 6 # asumimos que descargan 6 barcazas
    if llegadasProb < 95:
        capacidadDescarga = 5
        if llegadasProb < 83:
            capacidadDescarga = 4
            if llegadasProb < 55:
                capacidadDescarga = 3
                if llegadasProb < 15:
                    capacidadDescarga = 2
                    if llegadasProb < 3:
                        capacidadDescarga = 1

    # sacar el total de barcazas a descargar
    totalBarcazasADescargar = barcazasNoche + barcazasAcarreadas

    # resetear el acarreado
    barcazasAcarreadas = 0

    # sacar diferencia de números
    if capacidadDescarga < totalBarcazasADescargar: # falta de capacidad
        
        # patear el sobrante siguiente día
        barcazasAcarreadas = totalBarcazasADescargar - capacidadDescarga

        # agregar el histórico
        historicoAcarreados.append(barcazasAcarreadas)

        # agregar al histórico checando que no agreguemos un cero
        if capacidadDescarga > 0:
            historicoDescargados.append(capacidadDescarga)
    
    else: # capacidad suficiente

        # agregar al histórico
        minimum = min([totalBarcazasADescargar, capacidadDescarga])
        if minimum > 0:
            historicoDescargados.append(minimum)

        # agregar al histórico
        #historicoAcarreados.append(0)

    # incrementar iterador
    iteracion += 1

    print("Llegaron:", barcazasNoche, "barcazas")
    print("Barcazas totales a descargar:", totalBarcazasADescargar)
    print("Capacidad de descarga:", capacidadDescarga, "barcazas")
    print("Se descargaron", min([totalBarcazasADescargar, capacidadDescarga]), "barcazas")
    
print("---------------------------")
print("---------------------------")
print("Número promedio de retrasos de barcazas al siguiente día:", statistics.mean(historicoAcarreados))
print("Número promedio de llegadas nocturnas:", statistics.mean(historicoLlegadas))
print("Número promedio de barcazas descargadas por día:", statistics.mean(historicoDescargados))