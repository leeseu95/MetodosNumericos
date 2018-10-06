# Alonso Iturbe Sotomayor
# A01021621

# Problema de tarea #6 - Fallas de equipo
# Solución escrita en Python 3

# Librerías utilizadas: random
# Librerías utilizadas: math
# Librerías utilizadas: statistics

# python3 6.py
# Resultado ejemplo
'''
La política 1 (cambiar cada uno) costó: $ 38,700
La política 2 (cambiar todos) costó: $ 39,000
La política más económica es la 1
'''

import random
import numpy
import math
import statistics

n = 20000 #número de iteraciones

# Variables de costo
costoDeComponente = 200
costoPorHora = 100 
costoPolitica1 = 0
costoPolitica2 = 0

# Variable de timeout
timeout = 0

# Se inicializan las variables de TTL (horas) para cada uno de los componentes
TTL1 = int(numpy.random.normal(600, 100))
TTL2 = int(numpy.random.normal(600, 100))
TTL3 = int(numpy.random.normal(600, 100))
TTL4 = int(numpy.random.normal(600, 100))

# Política 1: reemplazar cada componente conforme falla
for experiment in range(n): # se corre el experimento por 20,000 horas

    #print("D #", experiment)

    # 0. Checar si estamos en un timeout por reparación
    if timeout > 0:
        costoPolitica1 += costoPorHora #sumar costo de estar sin operación
        timeout -= 1 # restar hora de timeout
        continue # saltarnos el resto de la iteración

    # 2. Restar horas de uso
    TTL1 -= 1
    TTL2 -= 1
    TTL3 -= 1
    TTL4 -= 1
    
    # 2. Checar si algún componente ha fallado. If so, repararlo. Se considera que sólo se tarda una hora aún si se reparan más de uno

    # Componente 1
    if TTL1 == 0:
        timeout = 1 # desconectar equipo por una hora
        costoPolitica1 += costoDeComponente # sumar costo del componente
        TTL1 = int(numpy.random.normal(600, 100)) # Darle un nuevo TTL

    # Componente 2
    if TTL2 == 0:
        timeout = 1 # desconectar equipo por una hora
        costoPolitica1 += costoDeComponente # sumar costo del componente
        TTL2 = int(numpy.random.normal(600, 100)) # Darle un nuevo TTL

    # Componente 3
    if TTL3 == 0:
        timeout = 1 # desconectar equipo por una hora
        costoPolitica1 += costoDeComponente # sumar costo del componente
        TTL3 = int(numpy.random.normal(600, 100)) # Darle un nuevo TTL

    # Componente 4
    if TTL4 == 0:
        timeout = 1 # desconectar equipo por una hora
        costoPolitica1 += costoDeComponente # sumar costo del componente
        TTL4 = int(numpy.random.normal(600, 100)) # Darle un nuevo TTL

    #print(experiment, "1:", TTL1, "2:", TTL2, "3:", TTL3, "4:", TTL4)

#################################################

# Variable de timeout
timeout = 0

# Se inicializan las variables de TTL (horas) para cada uno de los componentes
TTL1 = int(numpy.random.normal(600, 100))
TTL2 = int(numpy.random.normal(600, 100))
TTL3 = int(numpy.random.normal(600, 100))
TTL4 = int(numpy.random.normal(600, 100))

# Política 2: reemplazar todos los componentes cuando falle uno
for experiment in range(n): # se corre el experimento por 20,000 horas

    #print("D #", experiment)

    # 0. Checar si estamos en un timeout por reparación
    if timeout > 0:
        costoPolitica2 += costoPorHora #sumar costo de estar sin operación
        timeout -= 1 # restar hora de timeout
        continue # saltarnos el resto de la iteración

    # 2. Restar horas de uso
    TTL1 -= 1
    TTL2 -= 1
    TTL3 -= 1
    TTL4 -= 1

    # 2. Checar si algún componente ha fallado. If so, cambiar todos

    if TTL1 == 0 or TTL2 == 0 or TTL3 == 0 or TTL4 == 0:
        
        # desconectar equipo por dos horas
        timeout = 2 
        
        # sumar costo de cambiar todos los componentes
        costoPolitica2 += (costoDeComponente * 4)
        
        # Nuevos TTLs
        TTL1 = int(numpy.random.normal(600, 100))
        TTL2 = int(numpy.random.normal(600, 100))
        TTL3 = int(numpy.random.normal(600, 100))
        TTL4 = int(numpy.random.normal(600, 100))

    #print(experiment, "1:", TTL1, "2:", TTL2, "3:", TTL3, "4:", TTL4)

print("La política 1 (cambiar cada uno) costó: $", "{:,}".format(costoPolitica1))
print("La política 2 (cambiar todos) costó: $", "{:,}".format(costoPolitica2))
print("La política más económica es la", 1 if costoPolitica1 < costoPolitica2 else 2)
