#Seung Lee - A01021720
#Problema 10 Cita

import random

iters = 5000

numberMet = 0 #Inicializamos nuestras variables, y la cantidad de veces que se vieron en 0
timeArrivalRosy = 0
timeArrivalAfro = 0

for i in range(0, iters): #Iteramos un for desde 0 hasta iters
    timeArrivalRosy = random.randint(0, 59) #Inicializamos sus tiempos desde 0 a 60 de Rosy y Afro
    timeArrivalAfro = random.randint(0, 59)

    if (abs(timeArrivalRosy - timeArrivalAfro)) <= 15: #Si el tiempo de llegada de valor absoluto de  Rosy - Afro es menor a 15
        numberMet += 1
        print("Rosy: ", timeArrivalRosy, "Afro: ", timeArrivalAfro)
        continue #Si el if jala, nos salimos de esta iteracion
    
    if (abs(timeArrivalAfro - timeArrivalRosy)) <= 20: #Misma logica que el de arriba
        numberMet += 1
        print("Afro: ", timeArrivalAfro, "Rosy: ", timeArrivalRosy)
        continue #Si el if jala, nos salimos de esta iteracion
    
print("Amount of dates that succeeded: ", numberMet)
print("Probability: ", round((numberMet/iters * 100), 2), "%")