from numpy.random import poisson
from random import randint
from math import ceil,floor

for team in range(4,7):
	if team == 4:
		initialTime =15
	elif team == 5:
		initialTime = 10
	elif team == 6:
		initialTime = 5

	workMins = 0
	wait = 0
	trucks = 0


	while workMins < 480 or trucks > 0:
		trucks += poisson(2)
		nextHour = workMins + 60
		for i in range(trucks):
			trucks -= 1
			time = randint(initialTime, initialTime + 10)
			wait += time * trucks
			workMins += time
			if workMins >= nextHour:
				break
		if workMins <= nextHour:
			workMins = nextHour
		else:
			wait += trucks * (workMins - nextHour)
	workSalary = team * ((workMins/60.0) * 25)
	waitCost = (wait/60.0) * 50
	print("∞"*20)
	print("Number of workers:",team)
	print("Final cost: $", "{0:.2f}".format(workSalary+waitCost))
	print("Hours worked:", "{0:.2f}".format(workMins/60.0))
	print("\tSalary: $", "{0:.2f}".format(workSalary))
	print("Truck waiting time:", "{0:.2f}".format(wait/60))
	print("\tTruck cost: $", "{0:.2f}".format(waitCost))
