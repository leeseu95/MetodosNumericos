# Alonso Iturbe Sotomayor
# A01021621

# Problema de Tarea II #29 - Pacientes en un hospital
# Solución escrita en Python 3

# Librerías utilizadas: random
# Librerías utilizadas: math
# Librerías utilizadas: statistics

# python3 27.py

import random
import numpy
import math
import statistics

trayectoria = [] # individual, de cada paciente
trayectorias = [] # de todos los pacientes
alta = False
entradasARayosX = 0
dobleEntradaARayosX = 0 # número de pacientes que entraron al departamento de rayos x exactamente 2 veces

# mover paciente de emergencias a otro departamento
def emergencias():
    prob = random.uniform(0, 1)
    depto = "A" # Alta
    if prob < 0.7:
        depto = "V" # obserVación
        if prob < 0.6:
            depto = "O" # Operación
            if prob < 0.45:
                depto = "X" # X-ray
    trayectoria.append(depto) # movernos al siguiente departamento
    return

# mover paciente de rayos X a otro departamento
def rayosX():
    global entradasARayosX
    entradasARayosX += 1
    prob = random.uniform(0, 1)
    depto = "A" # Alta
    if prob < 0.7:
        depto = "V" # obserVación
        if prob < 0.35:
            depto = "P" # Postoperatoria
            if prob < 0.1:
                depto = "O" # Operación
    trayectoria.append(depto) # movernos al siguiente departamento
    return

# mover paciente de operacion a otro departamento
def operacion():
    prob = random.uniform(0, 1)
    depto = "A" # Alta
    if prob < 0.95:
        depto = "V" # obserVación
        if prob < 0.25:
            depto = "P" # Postoperatoria
    trayectoria.append(depto) # movernos al siguiente departamento
    return

# mover paciente de postoperatoria a otro departamento
def postoperatoria():
    prob = random.uniform(0, 1)
    depto = "A" # Alta
    if prob < 0.6:
        depto = "X" # rayosX
        if prob < 0.55:
            depto = "V" # obserVación
    trayectoria.append(depto) # movernos al siguiente departamento
    return

# mover paciente de observación a otro departamento
def observacion():
    prob = random.uniform(0, 1)
    depto = "A" # Alta
    if prob < 0.3:
        depto = "X" # rayosX
        if prob < 0.15:
            depto = "O" # Operación
    trayectoria.append(depto) # movernos al siguiente departamento
    return

for paciente in range(10):
    
    # inicializar variables
    trayectoria = ["E"]
    alta = False
    entradasARayosX = 0

    while alta == False: # mientras no nos hayan dado de alta...
        
        temp = trayectoria.copy() # shallow copy
        latest = temp.pop() # ver cual es la sala en la que estamos

        if latest == "E": # estamos en la sala de emergencia
            emergencias()
        elif latest == "X": # estamos en la sala de rayos X
            rayosX()
        elif latest == "O": # estamos en la sala de operaciones
            operacion()
        elif latest == "P": # estamos en la sala postoperatoria
            postoperatoria()
        elif latest == "V": # estamos en la sala de observación
            observacion()
        elif latest == "A": # ya nos dieron de alta
            alta = True # salir del while

    trayectorias.append(trayectoria)
    if entradasARayosX == 2: # el paciente entró a la sala de rayos X dos veces
        dobleEntradaARayosX += 1

print("Las trayectorias seguidas por los pacientes fueron las siguientes:")
print("E - Emergencias | X - Rayos X | O - Operación | P - Postoperatoria | V - obserVación | A - Alta")
print("---------------------------")
for paciente in range(10):
    print("p", paciente, ": ", end="", sep="")
    print(*trayectorias[paciente], sep='->')

print("---------------------------")
print("En total,", dobleEntradaARayosX, "paciente(s) entraron a la sala de rayos X exactamente dos veces")
print("Ergo, la probabilidad que un paciente entre dos veces a la sala de rayos X es de", (dobleEntradaARayosX/10)*100, "%")

