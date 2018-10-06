# Seung Hoon Lee Kim
# A01021720
# Hecho en python3

# Librerías utilizadas: random
# Librerías utilizadas: math
# Librerías utilizadas: statistics

# Correr asi: python3 A01021720SeungP1.py

import random
import numpy
import math
import statistics

# timer utilizado para medir los minutos entre llamadas
timeout = 0

enEspera = []
enEsperaHistorico = []

# retorna una duración aleatoria de una llamada
def getDuracion():
    # obtener nueva llamada
    probDuracion = random.uniform(0, 1)

    # Sacamos los minutos de la duracion dependiendo de la tabla
    minutos = 7
    if probDuracion < 0.97:
        minutos = 6
        if probDuracion < 0.87:
            minutos = 5
            if probDuracion < 0.64:
                minutos = 4
                if probDuracion < 0.57:
                    minutos = 3
                    if probDuracion < 0.39:
                        minutos = 2
                        if probDuracion < 0.20:
                            minutos = 1
    
    return minutos

# A. 1 operador asumiendo la distribución actual
# 0. inicializa el arreglo de minutos restantes con ceros, ya que ambos operadores están listos para atender clientes
minutosRestantes = 0

# simular 360 minutos de operación (de 12AM a 6AM son seis horas, 6*60 = 360)
for minuto in range(360):

    # print("----------------")
    # print("M:", minuto)

    # 1. RESTAR/SUMAR TIEMPOS

    # sumar minutos a llamadas en espera
    if len(enEspera) > 0:
        enEspera = [x+1 for x in enEspera]
        #print("oh:", len(enEspera), enEspera)

    # restar minutos del agente en la línea
    if minutosRestantes > 0:
        minutosRestantes -= 1
    # print("mr:", minutosRestantes)
    
    # si estamos en un timeout entre llamadas... restar minuto del timeout entre llamadas entrantes
    if timeout > 0:
        timeout -= 1
    # print("t:", timeout)

    # 2. CHECAR SI HAY ALGUIEN ON HOLD
    if len(enEspera) > 0:
        if minutosRestantes == 0: # el agente está disponible
            
            # para fines de estadística
            enEsperaHistorico.append(enEspera.pop(0))

            # duración de la llamada
            minutosRestantes = getDuracion()

            #print("Se tomó una llamada de", minutosRestantes, "minutos que estaba on hold")
    
    # 3. CHECAR SI TOCA LA ENTRADA DE UNA NUEVA LLAMADA
    if timeout == 0:
        probLlamada = random.uniform(0, 1)
    
        # asumimos que entrará una llamada en 6 minutos
        minutos = 6
        if probLlamada < 0.90:
            minutos = 5
            if probLlamada < 0.74:
                minutos = 4
                if probLlamada < 0.54:
                    minutos = 3
                    if probLlamada < 0.32:
                        minutos = 2
                        if probLlamada < 0.11:
                            minutos = 1

        # set del nuevo timeout
        timeout = minutos

        # checar si podemos atender la llamada que acaba de entrar
        if minutosRestantes == 0: # el agente está disponible
            
            # para fines de estadística
            enEsperaHistorico.append(0)

            # asignar duración de la llamada
            minutosRestantes = getDuracion()

            #print("Se tomó una llamada de", minutosRestantes, "minutos")

        else:
            # no hay, poner en espera
            enEspera.append(0)

print("\n\nResultados con 1 agente bajo condiciones normales:")
onHoldHistoricoSinCeros = [x for x in enEsperaHistorico if x != 0]
if len(onHoldHistoricoSinCeros) > 0:
    print("Tiempo promedio de espera:", round(statistics.mean(onHoldHistoricoSinCeros), 2), "minutos")
else:
    print("No hubo clientes en espera")

onHoldHistoricoSoloCeros = [1 for x in enEsperaHistorico if x == 0]
print("Total de clientes que fueron atendidos sin tener que esperar:", sum(onHoldHistoricoSoloCeros))

# ******************************************************************************************************************

# timer utilizado para medir los minutos entre llamadas
timeout = 0

enEspera = []
enEsperaHistorico = []

# A. 1 operador asumiendo la distribución actual
# 0. inicializa el arreglo de minutos restantes con ceros, ya que ambos operadores están listos para atender clientes
minutosRestantesOp1 = 0
minutosRestantesOp2 = 0

# simular 360 minutos de operación (de 12AM a 6AM son seis horas, 6*60 = 360)
for minuto in range(360):

    # print("----------------")
    # print("M:", minuto)

    # 1. RESTAR/SUMAR TIEMPOS

    # sumar minutos a llamadas en espera
    if len(enEspera) > 0:
        enEspera = [x+1 for x in enEspera]
        #print("oh:", len(enEspera), enEspera)

    # restar minutos de los agentes en la línea
    if minutosRestantesOp1 > 0:
        minutosRestantesOp1 -= 1
    if minutosRestantesOp2 > 0:
        minutosRestantesOp2 -= 1
    # print("mr:", minutosRestantesOp1)
    
    # si estamos en un timeout entre llamadas... restar minuto del timeout entre llamadas entrantes
    if timeout > 0:
        timeout -= 1
    # print("t:", timeout)

    # 2. CHECAR SI HAY ALGUIEN ON HOLD
    if len(enEspera) > 0:
        if minutosRestantesOp1 == 0: # el agente está disponible
            
            # para fines de estadística
            enEsperaHistorico.append(enEspera.pop(0))

            # duración de la llamada
            minutosRestantesOp1 = getDuracion()

            #print("El operador 1 tomó una llamada de", minutosRestantesOp1, "minutos que estaba on hold")
        
        elif minutosRestantesOp2 == 0:
            
            # para fines de estadística
            enEsperaHistorico.append(enEspera.pop(0))

            # duración de la llamada
            minutosRestantesOp1 = getDuracion()

            #print("El operador 2 tomó una llamada de", minutosRestantesOp2, "minutos que estaba on hold")

    
    # 3. CHECAR SI TOCA LA ENTRADA DE UNA NUEVA LLAMADA
    if timeout == 0:
        probLlamada = random.uniform(0, 1)
    
        # asumimos que entrará una llamada en 6 minutos
        minutos = 6
        if probLlamada < 0.93:
            minutos = 5
            if probLlamada < 0.81:
                minutos = 4
                if probLlamada < 0.66:
                    minutos = 3
                    if probLlamada < 0.47:
                        minutos = 2
                        if probLlamada < 0.22:
                            minutos = 1

        # set del nuevo timeout
        timeout = minutos

        # checar si podemos atender la llamada que acaba de entrar
        if minutosRestantesOp1 == 0: # el agente 1 está disponible
            
            # para fines de estadística
            enEsperaHistorico.append(0)

            # asignar duración de la llamada
            minutosRestantesOp1 = getDuracion()

            #print("El operador 1 tomó una llamada de", minutosRestantesOp1, "minutos")
        
        elif minutosRestantesOp2 == 0: # el agente 2 está disponible
            
            # para fines de estadística
            enEsperaHistorico.append(0)

            # asignar duración de la llamada
            minutosRestantesOp2 = getDuracion()

            #print("El operador 2 tomó una llamada de", minutosRestantesOp2, "minutos")

        else:
            # no hay, poner en espera
            enEspera.append(0)


print("\n\n-------------------------------------")
print("Resultados con 2 agentes y asumiendo la campaña publicitaria:")
onHoldHistoricoSinCeros = [x for x in enEsperaHistorico if x != 0]
if len(onHoldHistoricoSinCeros) > 0:
    print("Tiempo promedio de espera:", round(statistics.mean(onHoldHistoricoSinCeros), 2), "minutos")
else:
    print("No hubo clientes en espera")

onHoldHistoricoSoloCeros = [1 for x in enEsperaHistorico if x == 0]
print("Total de clientes que fueron atendidos sin tener que esperar:", sum(onHoldHistoricoSoloCeros))


print("\n\n-------------------------------------------")
print("El modelo es basicamente una simulacion de 360 minutos (6 Horas para simular entre las 12:00 AM y las 6:00 AM). Durante cada ciclo restamos y sumamos los tiempos necesarios. Despues checamos si ya estaba cualquier cliente en espera mientras el operador este ocupado y en ese mismo ciclo tambien checamos si llega algun otro cliente que se conecte y se meta al queue de esepra. Como se puede ver en la primera simulacion el promedio de espera es bastante alto (de 20 minutos). Para poder cortar el tiempo de espera seria mejor si se implementan a varios agentes para atender a los clientes. Esto se puede ver en base a lo que paso en la segunda simulacion con dos agentes, se puede acortar el tiempo y el total de clientes atendidos sin espera es mucho mas alto.")
print("25 Puntos")
print("\n\n-------------------------------------------")
print("Es bastante necesario que se utilize la campaña de publicidad ya que a traves de la simulacion se pudo ver que se atendieron mas de 100 clientes sin espera a comparacion de 1 cliente sin espera. La satisfaccion del cliente seria mucho mas alta y por ende se podrian atraer a muchos mas clientes. Mi recomendacion seria personalmente que si se haga la campana ya que podria ademas atraer a mas clientes.")
print("15 Puntos")