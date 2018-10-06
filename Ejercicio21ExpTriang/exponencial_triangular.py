# Seung Lee - A01021720
# Exponencial y triangular

import math
import random
import numpy as np
import matplotlib.pyplot as plt

pruebas = 5
valido = 0
plot = 0
plot2 = 0
exponencial_x = []
triangular = []

def generador(i,l):
    n = 1000
    loop = 0
    mu = 0
    validas = []
    sumatoria = []
    lambda_value = 4
    seed = 9876543456789
    div = 100000000
    temp = 0
    while loop == 0:
        seed = int(seed)
        seed = pow(seed,3)
        seed = seed / (math.sqrt(seed))
        seed = math.floor(seed)
        seed = str(seed)
        if len(seed) % 2 == 0:
        	while len(seed) > 8:
        			seed = seed[1:]
        			seed = seed[:-1]
        else:
        	seed = "0"+seed
        	while len(seed) > 8:
        			seed = seed[1:]
        			seed = seed[:-1]
        validas.append(seed) # Random number
        
        # Funcion exponencial
        temp = (-1 / lambda_value) * (math.log(1-int(seed)/div))
        exponencial_x.append(temp)

        # Triangular
        if int(seed)/div < 0.5:
            triangular.append(math.sqrt(2 * int(seed)/div))
        else:
            triangular.append(2 - math.sqrt(2 - (2 * (int(seed)/div))))

        if len(validas) == n: # 1000 numbers
        	loop = 1

    mu = n / l - i - 1 

    for k in range (n-1):
        pos1 = (i + (k*l)) 
        pos2 = (i + (k+1)*l)
        if(pos1 >= n or pos2 >= n):
            break
        else: 
            res = (int(validas[pos1])/div) * (int(validas[pos2])/div)
            sumatoria.append(res)

    res1 = ((1/(mu-1)) * np.sum(sumatoria)) - 0.25
    res2 = math.sqrt(((13*mu)-7)/(12*(mu+1)))

    zeta = (res1/res2)
    
    if(zeta > -1.96 and zeta < 1.96):
        # Valid generator
        # print("Zeta value:",zeta)
        return True
    else: 
        # Not valid generator
        return False

for i in range(pruebas):
    i = random.randint(1,5)
    l = random.randint(1,5)
    if(generador(i,l)):
        valido += 1

print("Numeros totales", len(exponencial_x))
plot = plt.hist(exponencial_x, bins=20)
plt.title("Histograma de distribucion exponencial")
plt.show(plot)

plot2 = plt.hist(triangular, bins=20)
plt.title("Histograma triangular")
plt.show(plot2)
