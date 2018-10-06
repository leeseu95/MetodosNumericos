import random


# Para este problema se simulo para una maquina con un tecnico en ella dado que no tenia las probablidades del tiempo de servicio para mas de un tecnico.
repairTime = 0
machineOffTime = 0
disasterTime = 0
hours = 1500
totalRepairTime = 0
totalDisasterTime = 0

for hour in range(0,hours):

    if repairTime == 0 and disasterTime == 0:
        disasterTime = random.random()
        if disasterTime <= 0.1:
            disasterTime = random.randint(6,8)
        elif disasterTime > 0.1 and disasterTime <= 0.25:
            disasterTime = random.randint(8,10)
        elif disasterTime > 0.25 and disasterTime <= 0.49:
            disasterTime = random.randint(10,12)
        elif disasterTime > 0.49 and disasterTime <= 0.75:
            disasterTime = random.randint(12,14)
        elif disasterTime > 0.75 and disasterTime <= 0.93:
            disasterTime = random.randint(14,16)
        else:
            disasterTime = random.randint(16,18)

        totalDisasterTime += disasterTime
        disasterTime -= 1

        repairTime = random.random()
        if repairTime <= 0.15:
            repairTime = random.randint(2,4)
        elif repairTime > 0.15 and repairTime <= 0.4:
            repairTime = random.randint(4,6)
        elif repairTime > 0.4 and repairTime <= 0.7:
            repairTime = random.randint(6,8)
        elif repairTime > 0.7 and repairTime <= 0.9:
            repairTime = random.randint(8,10)
        else:
            repairTime = random.randint(10,12)

        totalRepairTime += repairTime

    elif disasterTime != 0:
        disasterTime -= 1
    elif disasterTime == 0 and repairTime != 0:
        repairTime -= 1
    else:
        break

workerSalary = totalRepairTime * 50
avgRepair = repairTime / 1500
avgDisaster = totalDisasterTime / 1500

print("-"*20)
print("The worker salary for", hours,"hours is", workerSalary)
print("Repair time", totalRepairTime)
print("The averga time the machines lasted without failure was", avgDisaster)
print("-"*20)
