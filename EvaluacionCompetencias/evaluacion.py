#Seung Lee - A01021720
#Evaluacion de Competencias

import random
import numpy as np
import math

ranLlegadas = [.37, .77, .13, .10, .02, .18, .31, .19, .32, .85, .31, .94, .81, .43, .31, .58, .33, .51]
ranDescargas = [.69, .84, .12, .94, .51, .36, .17, .02, .15, .29, .16, .52, .56, .43, .26, .22, .08, .62]

llegadas = []
descargas = []

allUnloaded = False

days = 0
faltantes = 0
llegaron = 0
descargadas = 0
faltan = 0

for i in range(0,18):
    if ranLlegadas[i] <= .13:
        llegadas.append(0)
    elif ranLlegadas[i] > .13 and ranLlegadas[i] <= .30:
        llegadas.append(1)
    elif ranLlegadas[i] > .30 and ranLlegadas[i] <= .45:
        llegadas.append(2)
    elif ranLlegadas[i] > .45 and ranLlegadas[i] <= .70:
        llegadas.append(3)
    elif ranLlegadas[i] > .70 and ranLlegadas[i] <= .90:
        llegadas.append(4)
    elif ranLlegadas[i] > .90 and ranLlegadas[i] <= 1:
        llegadas.append(5)
    
    if ranDescargas[i] <= .05:
        descargas.append(1)
    elif ranDescargas[i] > .05 and ranDescargas[i] <= .20:
        descargas.append(2)
    elif ranDescargas[i] > .20 and ranDescargas[i] <= .70:
        descargas.append(3)
    elif ranDescargas[i] > .70 and ranDescargas[i] <= .90:
        descargas.append(4)
    elif ranDescargas[i] > .90 and ranDescargas[i] <= 1:
        descargas.append(5)

missingDays = 0

for days in range(0, 15):
    #Para KPI al final
    llegaron += llegadas[days]
    descargadas += descargas[days]

    #Valores que vamos a utilizar
    dailyUnload = descargas[days]
    dailyBoats = llegadas[days]

    print("Descargadas este dia: ", dailyUnload)
    print("Llegadas este dia: ", dailyBoats)
    print("Faltantes este dia: ", faltan)

    #Checar si hay faltantes del dia pasado
    #Si las que se van a descargar ese dia son mayores a las que faltan de descargar
    if (faltan > 0 and dailyUnload >= faltan):
        dailyUnload -= faltan
        faltan = 0
    elif (faltan > 0 and dailyUnload < faltan): #Si las que faltan son mayores a las que vamos a unload 
        faltan -= dailyUnload #Quitamos las que faltan de las que vamos a descargar ese dia
        faltan += dailyBoats #Agregamos los que llegaron ese dia a "Faltan"
        faltantes += faltan #variable para KPI
        missingDays += 1
        continue

    if dailyBoats > dailyUnload: #Si las que llegaron ese dia son mayores a las que vamos a descargar
        dailyBoats -= dailyUnload #Quitamos las que se descargaron a las que llegaron
        faltan += dailyBoats
        faltantes += faltan #Variable para KPI
        missingDays += 1
    else:
        dailyBoats = 0
    
print("\nNumero promedio de retrasos de barcazas al siguiente dia: " , round((faltantes/missingDays),3))
print("Numero promedio de barcazas llegadas en la noche: " , round((llegaron/15),3))
print("Numero promedio de barcazas descargas: ", round((descargadas/15), 3))
