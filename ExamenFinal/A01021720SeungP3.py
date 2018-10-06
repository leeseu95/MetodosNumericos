# Seung Hoon Lee Kim
# A01021720
# Hecho en python3

# Librerías utilizadas: random

# Correr asi: python3 A01021720SeungP3.py

import random

class Pluma:
	def __init__(self):
		self.duration = 100

downtime = 50 # 50$ por hora
repairCost = 8 # 8$ por reparar una pluma

#probabilidades si una se tiene que reparar
singleRepairProb = [.05, .20, .35, .55, .75, .90, 1]
#probabilidad para ver si una pluma falla horas
singleReplaced = [.47, .03, .11, .10, .67, .23, .89, .62, .56, .74, .54, .31, .62, .37, .33 , .33, .82, .68, .50, .22]
#counter para 10 fallas de 1 pluma
singleFailureCounter = 0
singleCounter = 0

#probabilidades si todas se van a cambiar
multipleRepairProb = [.15, .40, .75, .95, 1]
#probabilidad para ver si las cuatro fallan (horas)
multipleReplaced = [.99, .29, .27, .75, .89, .78, .68, .64, .62, .30, .17, .12, .74, .45, .11, .52, .59, .22, .03, .03]
#counter para 10 fallas de 4 plumas
multipleFailureCounter = 0
multipleCounter = 0

failureProb = .2 # Probabilidad de que una pluma falle en una hora

Plumas = [Pluma(), Pluma(), Pluma(), Pluma()]
total_single = 0
total_multi = 0

i = 0
while(i < 5000 and singleFailureCounter < 10):
	for j in range(len(Plumas)):
		Plumas[j].duration -= 1
		if Plumas[j].duration <= 0:
			rand_1 = random.random()
			if rand_1 <= failureProb:
				Plumas[j].duration = 100
				singleFailureCounter += 1                
				total_single += repairCost
				rand_2 = singleReplaced[singleFailureCounter-1]
				if rand_2 <= singleRepairProb[0]:
					total_single += 10 * downtime
					i += 10
				elif singleRepairProb[0] < rand_2 <= singleRepairProb[1]:
					total_single += 20 * downtime
					i += 20
				elif singleRepairProb[1] < rand_2 <= singleRepairProb[2]:
					total_single += 30 * downtime
					i += 30
				elif singleRepairProb[2] < rand_2 <= singleRepairProb[3]:
					total_single += 40 * downtime
					i += 40
				elif singleRepairProb[3] < rand_2 <= singleRepairProb[4]:
					total_single += 50 * downtime
					i += 50
				elif singleRepairProb[4] < rand_2 <= singleRepairProb[5]:
					total_single += 60 * downtime
					i += 60
				elif singleRepairProb[5] < rand_2 <= singleRepairProb[6]:
					total_single += 70 * downtime
					i += 70              
	i += 1

print("\nCosto de cambiar individualmente cada pluma: $", total_single, " con las 10 primeras fallas")

i = 0
counter = 0
while (i < 5000 and multipleFailureCounter < 10):
	for j in range(len(Plumas)):
		Plumas[j].duration -= 1
		if Plumas[j].duration <= 0:	
			rand_1 = random.random()
			if rand_1 <= failureProb:
				multipleFailureCounter += 1
				Plumas[0].duration = 100
				Plumas[1].duration = 100
				Plumas[2].duration = 100
				Plumas[3].duration = 100
				total_multi += 4 * repairCost
				rand_2 = multipleReplaced[multipleFailureCounter-1]
				if rand_2 <= multipleRepairProb[0]:
					total_multi += 100 * downtime
					i += 100
				elif multipleRepairProb[0] < rand_2 <= multipleRepairProb[1]:
					total_multi += 110 * downtime
					i += 110
				elif multipleRepairProb[1] < rand_2 <= multipleRepairProb[2]:
					total_multi += 120 * downtime
					i += 120
				elif multipleRepairProb[2] < rand_2 <= multipleRepairProb[3]: 
					total_multi += 130 * downtime
					i += 130
				else:
					total_multi += 140 * downtime
					i += 140
	i += 1

print("Costo de cambiar todas las plumas a la vez: $", total_multi, " con las 10 primeras fallas")

print("\n\nComo se puede ver el costo para cambiar una de las plumas de una vez es mucho menor (costo de 19,080 pesos vs 60,820). Por eso se deberia de cambiar solo una pluma cada vez que ocurra una falla (15 puntos)\n")
print("\n\nOtra forma de resolver este problema podria ser tomando todas las probabilidades que llegase a fallar y hacer un promedio de estas probabilidades y sus horas de falla. Una vez que tenemos las horas de falla promedio podemos hacer un calculo para saber cual seria el costo promedio de reemplazar una o varias plumas.\n")