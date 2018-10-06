# Seung Hoon Lee Kim - A01021720

# Examen - Parcial 1
# Pregunta 2 - Teoria de colas
# Solución escrita en Python 3

import random
import numpy
import math

constructionCost = 12000 #si se construye 1 ventana
constructionCost2 = 20000 #si se construyen 2 ventanas en vez de 1
employeeCost = 16000 #costo del personal anual

clientCostperMin = 1 #costo del cliente por minuto

ranInterarrivalTime = [52, 37, 82, 69, 98, 96, 33, 50, 88, 90, 50, 27, 45, 81, 66, 74, 30, 59, 67, 28, 2, 74, 35, 24, 3, 29, 60, 74, 85, 90]
ranServiceTime = [60, 60, 80, 53, 69, 37, 6, 63, 57, 2, 94, 52, 69, 33, 32, 30, 48, 88, 33, 48, 72, 33, 62, 13, 74, 68, 22, 44, 42, 9]

interarrivalTime = []
serviceTime = []

n = 200 #numero de dias al ano
#Funcion para agregar nuestros tiempos de intervalo y servicio de cada cliente que llego
for i in range(0,30):
    if ranInterarrivalTime[i] <= 20:
        interarrivalTime.append(1)
    elif ranInterarrivalTime[i] > 20 and ranInterarrivalTime[i] <=45:
        interarrivalTime.append(2)
    elif ranInterarrivalTime[i] > 45 and ranInterarrivalTime[i] <=75:
        interarrivalTime.append(3)
    elif ranInterarrivalTime[i] > 75 and ranInterarrivalTime[i] <=90:
        interarrivalTime.append(4)
    elif ranInterarrivalTime[i] > 90 and ranInterarrivalTime[i] <=100:
        interarrivalTime.append(5)
    
    if ranServiceTime[i] <= 10:
        serviceTime.append(1)
    elif ranServiceTime[i] > 10 and ranServiceTime[i] <= 25:
        serviceTime.append(2)
    elif ranServiceTime[i] > 25 and ranServiceTime[i] <= 60:
        serviceTime.append(3)
    elif ranServiceTime[i] > 60 and ranServiceTime[i] <= 75:
        serviceTime.append(4)
    elif ranServiceTime[i] > 75 and ranServiceTime[i] <= 90:
        serviceTime.append(5)
    elif ranServiceTime[i] > 90 and ranServiceTime[i] <= 100:
        serviceTime.append(6)

#Inciso A -------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
print( "A) Simulacion de 1 periodo de 1 hora con UNA ventanilla\n")
customerCounter = 0 #Counter para cada cliente que llega

cashierFree = [True] #variables para nuestra ventana
cashierTimeBusy = [0]

clientsAttended = 0

customerTime = 0
queueLine = 0
queue = []
minutesLost = 0 # segundos perdidos de clientes de dinero

customerArrivalTime = interarrivalTime[0]
queue.append(serviceTime[customerCounter])

for minutes in range(0, 60): #simulacion de 1 hora por cada segundo que pasa
    # print("\nCurrent minute: " ,minutes)
    if minutes >= cashierTimeBusy[0]:
        cashierFree[0] = True
    
    # print(customerArrivalTime)

    if minutes >= customerArrivalTime:
        customerCounter += 1
        customerArrivalTime += interarrivalTime[customerCounter]
        queue.append(serviceTime[customerCounter])
    
    # print(cashierTimeBusy[0])
    if cashierFree[0] == True and queue:
        temp = queue[0]
        # print(temp)
        queue.pop(0)
        cashierTimeBusy[0] += temp
        cashierFree[0] = False
        clientsAttended += 1


    minutesLost += len(queue)

    # print("Linea de tiempo binario", customerArrival)
    # print("Queue de linea en cada minuto de clientes con sus tiempos de servicio:", queue)
    # print("Clientes atendidos:" , clientsAttended)
    # print("Minutes lost every minute: ", minutesLost)

print("Clientes atendidos: ", clientsAttended)
print("Minutos perdidos: ", minutesLost)
print("Pesos perdidos: ", minutesLost, "$")
print("Costo de personal: ", (employeeCost) / 1400, "$")
print("Costo de construccion: ", constructionCost / 1400, "$\n")
print("Costo total en perdidas: ", minutesLost + constructionCost/1400 + employeeCost/1400, "$")
print( "-------------------------------------------------------")
print( "-------------------------------------------------------\n\n")
res1Clients = clientsAttended * 7 * 200
res1Minutes = minutesLost * 7 * 200




#Inciso B -------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
print( "B) Simulacion de 1 periodo de 1 hora con DOS ventanilla\n")
customerCounter = 0 #Counter para cada cliente que llega

cashierFree = [True, True] #variables para nuestra ventana
cashierTimeBusy = [0, 0]

clientsAttended = 0

customerTime = 0
queueLine = 0
queue = []
minutesLost = 0 # segundos perdidos de clientes de dinero

customerArrivalTime = interarrivalTime[0]
queue.append(serviceTime[customerCounter])

for minutes in range(0, 60): #simulacion de 1 hora por cada segundo que pasa
    # print("\nCurrent minute: " ,minutes)
    if minutes >= cashierTimeBusy[0]:
        cashierFree[0] = True
    
    if minutes >= cashierTimeBusy[1]:
        cashierFree[1] = True
    
    # print(customerArrivalTime)

    if minutes >= customerArrivalTime:
        customerCounter += 1
        customerArrivalTime += interarrivalTime[customerCounter]
        queue.append(serviceTime[customerCounter])
    
    # print(cashierTimeBusy[0])
    if cashierFree[0] == True and queue:
        temp = queue[0]
        # print(temp)
        queue.pop(0)
        cashierTimeBusy[0] += temp
        cashierFree[0] = False
        clientsAttended += 1

    if cashierFree[1] == True and queue:
        temp = queue[0]
        # print(temp)
        queue.pop(0)
        cashierTimeBusy[1] += temp
        cashierFree[1] = False
        clientsAttended += 1

    minutesLost += len(queue)

    # print("Linea de tiempo binario", customerArrival)
    # print("Queue de linea en cada minuto de clientes con sus tiempos de servicio:", queue)
    # print("Clientes atendidos:" , clientsAttended)
    # print("Minutes lost every minute: ", minutesLost)

print("Clientes atendidos: ", clientsAttended)
print("Minutos perdidos: ", minutesLost)
print("Pesos perdidos: ", minutesLost, "$")
print("Costo de personal: ", (employeeCost * 2) / 1400, "$")
print("Costo de construccion: ", constructionCost2 / 1400, "$\n")
print("Costo total en perdidas: ", minutesLost + constructionCost2/1400 + employeeCost*2/1400, "$")
print( "-------------------------------------------------------")
print( "-------------------------------------------------------\n\n")
res2Clients = clientsAttended * 7 * 200
res2Minutes = minutesLost * 7 * 200



#Inciso C -------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
print( "C) Simulacion de 1 periodo de 200 dias con 7 horas diarias con UNA ventanilla\n")

print("Clientes atendidos: ", res1Clients)
print("Minutos perdidos: ", res1Minutes)
print("Pesos perdidos: ", res1Minutes, "$")
print("Costo de personal: ", employeeCost, "$")
print("Costo de construccion: ", constructionCost, "$\n")
print("Costo/Perdidas totales: ", res1Minutes + employeeCost + constructionCost, "$\n\n")

print( "C) Simulacion de 1 periodo de 200 dias con 7 horas diarias con DOS ventanilla\n")

print("Clientes atendidos: ", res2Clients)
print("Minutos perdidos: ", res2Minutes)
print("Pesos perdidos: ", res2Minutes, "$")
print("Costo de personal: ", employeeCost * 2, "$")
print("Costo de construccion: ", constructionCost2, "$\n")
print("Costo/Perdidas totales: ", res2Minutes + employeeCost * 2 + constructionCost2, "$")

print( "-------------------------------------------------------")
print( "-------------------------------------------------------")


# for day in range (0, n): #iteramos en 200 dias
