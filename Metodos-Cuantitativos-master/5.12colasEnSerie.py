import random
import numpy as np





def simColasEnSerie():
    iterations = 5000
    workHours = 8
    clients = 0
    clientWaitingMean = []
    clientsWaitingFirstStation = []
    clientsWaitingSecondStation = []
    # firstStationTime = 0
    # secondStationTime = 0
    for i in range(iterations):
        firstStationServiceTime = 0
        clientsFirstStation = 0
        clientsSecondStation = 0
        for j in range(workHours):

            #clientsSecondStation = secondStationWaitingLine
            happyClient = 0
            clientsFirstStation += random.randint(10, 30)
            firstStationServiceTime = random.randint(1,3)
            secondStationServicetime = random.choice([1,2])
            for k in range(60):
                #atendiendo en la primera estacion
                if(clientsFirstStation > 0):
                    if(firstStationServiceTime > 0):
                        firstStationServiceTime -= 1
                    else:
                        firstStationServiceTime = random.randint(1,3)
                        clientsFirstStation -= 1
                        clientsSecondStation += 1

                if(clientsSecondStation > 0):
                    if(secondStationServicetime > 0):
                        secondStationServicetime -= 1
                    else:
                        secondStationServicetime = random.choice([1,2])
                        clientsSecondStation -= 1
                        happyClient += 1
                clientsWaitingFirstStation.append(clientsFirstStation)
                clientsWaitingSecondStation.append(clientsSecondStation)
            #print("Hora:", j, "\n", clientsFirstStation, "clientes en la primera estacion\n", clientsSecondStation, "clientes en la segunda estacion\n")
            # print("Promedio de tiempo de espera por cliente en hora", j, 60/happyClient))

            clientWaitingMean.append(60/happyClient)

    print("Promedio de tiempo de espera por cliente:", np.mean(clientWaitingMean))
    print("Promedio de clientes en fila de primera estacion:", np.mean(clientsFirstStation))
    print("Promedio de clientes en fila de segunda estacion:", np.mean(clientsSecondStation))
    if(np.mean(clientsFirstStation) >np.mean(clientsSecondStation)):
        print("En promedio la primera cola es de mayor tamaño")
    else:
        print("En promedio la segunda cola es de mayor tamaño")











if __name__ == '__main__':
    print("Tarea 1 ejercicio 5.12")
    simColasEnSerie()
