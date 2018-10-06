#Seung Lee - A01021720
#Problema 9 Arte

import random

iters = 5000

profit1Day = 0 #inicializar variables de los profits que pudo haber en cada alternativa
profit2Day = 0
profit3Day = 0

randomWait1Day = 0 #Inicializar randoms para los dias
randomWait2Day = 0

for i in range(0, iters): #Iteramos un for desde 0 hasta iters
    randomWait1Day = random.random()
    randomWait2Day = random.random()
    randomWait3Day = random.random()
    if(randomWait1Day < 0.60 and randomWait2Day < 0.60 and randomWait3Day < 0.60):
        profit3Day += 240000
    if(randomWait1Day < 0.60 and randomWait2Day < 0.60):
        profit2Day += 200000
    if(randomWait1Day < 0.60):
        profit1Day += 100000

day = ""
if(profit1Day >= profit2Day and profit1Day >= profit3Day):
    day = "Day 1, Price 400,000"
elif (profit2Day >= profit1Day and profit2Day >= profit3Day):
    day = "Day 2, Price 300,000"
else:
    day = "Day 3, Price 260,000"

print("Profits if you didn't wait and bought at 400,000: ", "{:,}".format(profit1Day))
print("Profits if you waited 1 day and bought at 300,000: ", "{:,}".format(profit2Day))
print("Profits if you waited 2 day wait and bought at 260,000: ", "{:,}".format(profit3Day))
profits = [profit1Day, profit2Day, profit3Day]
highestProfit = max(profits)

print("\nHighest profit to buy at: ", day)