import random

class Pluma:
	def __init__(self):
		self.duration = 100

downtime = 50 # 50$ por hora
repair_cost = 8 # 8$ por reparar una pluma
single_repair_probability = [.05, .2, .35, .55, .75, .9, 1]
multiple_repair_probability = [.15, .4, .75, .95, 1]
failure_probability = .2 # Probabilidad de que una pluma falle en una hora

Plumas = [Pluma(), Pluma(), Pluma(), Pluma()]
total_single = 0
total_multi = 0
i = 0
while(i < 5000):
	for j in range(len(Plumas)):
		Plumas[j].duration -= 1
		if Plumas[j].duration <= 0:
			rand_1 = random.random()
			if rand_1 <= failure_probability:
				Plumas[j].duration = 100
				total_single += repair_cost
				rand_2 = random.random()
				if rand_2 <= single_repair_probability[0]:
					total_single += 10 * downtime
					i += 10
				elif single_repair_probability[0] < rand_2 <= single_repair_probability[1]:
					total_single += 20 * downtime
					i += 20
				elif single_repair_probability[1] < rand_2 <= single_repair_probability[2]:
					total_single += 30 * downtime
					i += 30
				elif single_repair_probability[2] < rand_2 <= single_repair_probability[3]:
					total_single += 40 * downtime
					i += 40
				elif single_repair_probability[3] < rand_2 <= single_repair_probability[4]:
					total_single += 50 * downtime
					i += 50
				elif single_repair_probability[4] < rand_2 <= single_repair_probability[5]:
					total_single += 60 * downtime
					i += 60
				elif single_repair_probability[5] < rand_2 <= single_repair_probability[6]:
					total_single += 70 * downtime
					i += 70
	i += 1

print("Costo de cambiar individualmente cada pluma:", total_single)

i = 0
while i < 5000:
	for j in range(len(Plumas)):
		Plumas[j].duration -= 1
		if Plumas[j].duration <= 0:	
			rand_1 = random.random()
			if rand_1 <= failure_probability:
				Plumas[0].duration = 100
				Plumas[1].duration = 100
				Plumas[2].duration = 100
				Plumas[3].duration = 100
				total_multi += 4 * repair_cost
				rand_2 = random.random()
				if rand_2 <= multiple_repair_probability[0]:
					total_multi += 100 * downtime
					i += 100
				elif multiple_repair_probability[0] < rand_2 <= multiple_repair_probability[1]:
					total_multi += 110 * downtime
					i += 110
				elif multiple_repair_probability[1] < rand_2 <= multiple_repair_probability[2]:
					total_multi += 120 * downtime
					i += 120
				elif multiple_repair_probability[2] < rand_2 <= multiple_repair_probability[3]: 
					total_multi += 130 * downtime
					i += 130
				else:
					total_multi += 140 * downtime
					i += 140
	i += 1

print("Costo de cambiar todas las plumas a la vez:", total_multi)
