#Seung Hoon Lee
#A01021720
#Ejercicio 11 Mundial

import random
import numpy
import math

#Variables a definir
teamNames = ["Germany", "Portugal", "Argentina", "Brazil"]
teamWins = [0, 0, 0, 0]
teamMedians = [48, 53, 50, 48]
teamPenalties = [0.58, 0.40, 0.55, 0.5]

# print(math.floor(numpy.random.exponential(teamMedians[0])))

def juego(index, medians, penalties):
    goals1 = 0
    goals2 = 0
    timeTeam1 = 0
    timeTeam2 = 0
    
    #Empezamos una simulacion del equipo en 90 minutos de partida
    while timeTeam1 < 90:
        timeTeam1 += math.floor(numpy.random.exponential(medians[index[0]]))
        if timeTeam1 < 90:
            goals1 += 1
        else:
            timeTeam1 = 90

    #Repetimos lo mismo para el equipo 2
    while timeTeam2 < 90:
        timeTeam2 += math.floor(numpy.random.exponential(medians[index[1]]))
        if timeTeam2 < 90:
            goals2 += 1
        else:
            timeTeam2 = 90
    
    #Si el equipo 1 tiene mas goles que el equipo 2, regresamos al equipo 1 o vice versa
    if goals1 > goals2:
        return index[0]
    if goals1 < goals2:
        return index[1]

    #Si empataron, nos vamos a medio tiempo
    while timeTeam1 < 120:
        timeTeam1 += math.floor(numpy.random.exponential(medians[0]))
        if timeTeam1 < 120:
            goals1 += 1
        else:
            timeTeam1 = 120

    while timeTeam2 < 120:
        timeTeam2 += math.floor(numpy.random.exponential(medians[1]))
        if timeTeam2 < 120:
            goals2 += 1
        else:
            timeTeam2 = 120
    
    #Si el equipo 1 tiene mas goles que el equipo 2, regresamos al equipo 1 o vice versa
    if goals1 > goals2:
        return index[0]
    if goals1 < goals2:
        return index[1]

    #Si en medio tiempo empataron, nos metemos a penalties
    for penales in range(0, 5):
        penal = random.uniform(0, 1)
        if penalties[index[0]] > penal:
            goals1 += 1
        
        penal = random.uniform(0, 1)
        if penalties[index[1]] > penal:
            goals2+= 1
    
    #Si el equipo 1 tiene mas goles que el equipo 2, regresamos al equipo 1 o vice versa
    if goals1 > goals2:
        return index[0]
    if goals1 < goals2:
        return index[1]

    #50/50 si vuelven a empatar despues de penales
    randWinner = random.uniform(0,1)
    if randWinner >= 0.5:
        return index[0]
    else:
        return index[1]

for iters in range (0,5000):
    finalist1 = juego([0, 1], teamMedians, teamPenalties)
    finalist2 = juego([2, 3], teamMedians, teamPenalties)
    winner = juego([finalist1, finalist2], teamMedians, teamPenalties)

    teamWins[winner] += 1

for prints in range (0, 4):
    print("Numero de ganadas del equipo " , teamNames[prints] , " : " , teamWins[prints] , " / 5000")
    print("Probabilidad de ganar el mundial del equipo " , teamNames[prints] , " : " , round((teamWins[prints]/5000) *100, 2) , " %\n")