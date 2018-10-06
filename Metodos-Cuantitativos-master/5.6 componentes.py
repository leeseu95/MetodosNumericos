import numpy as np

simulationTime = 20000

comp1Time = np.random.normal(600,100)
comp2Time = np.random.normal(600,100)
comp3Time = np.random.normal(600,100)
comp4Time = np.random.normal(600,100)
compFee = 0

def pol1(simulationTime, comp1Time, comp2Time, comp3Time, comp4Time, compFee):
    for i in range(0,simulationTime):
        if comp1Time < 1:
            # quitar hora de trabajo y cobrar
            simulationTime -= 1
            compFee += 200 + 100
            comp1Time = np.random.normal(600,100)

        if comp2Time < 1:
            simulationTime -= 1
            compFee += 200 + 100
            comp2Time = np.random.normal(600,100)

        if comp3Time < 1:
            simulationTime -= 1
            compFee += 200 + 100
            comp3Time = np.random.normal(600,100)

        if comp4Time < 1:
            simulationTime -= 1
            compFee += 200 + 100
            comp4Time = np.random.normal(600,100)

        if comp1Time != 0 and comp2Time != 0 and comp3Time != 0 and comp4Time != 0:
            comp1Time -= 1
            comp2Time -= 1
            comp3Time -= 1
            comp4Time -= 1

    print("-"*20)
    print("In the current policy the componente Fee is of $",compFee)
    print("The machines worked for",simulationTime,"hours")


def pol2(simulationTime, comp1Time, comp2Time, comp3Time, comp4Time, compFee):
    for i in range(0,simulationTime):
        if comp1Time < 1 or comp2Time < 1 or comp3Time < 1 or comp4Time < 1:
            simulationTime -= 2
            compFee += 800 + 200
            comp1Time = np.random.normal(600,100)
            comp2Time = np.random.normal(600,100)
            comp3Time = np.random.normal(600,100)
            comp4Time = np.random.normal(600,100)

        else:
            comp1Time -= 1
            comp2Time -= 1
            comp3Time -= 1
            comp4Time -= 1

    print("*"*15)
    print("In the new policy the componente Fee is of $",compFee)
    print("The machines worked for",simulationTime,"hours")
    print("-"*20)

pol1(simulationTime, comp1Time, comp2Time, comp3Time, comp4Time, compFee)
pol2(simulationTime, comp1Time, comp2Time, comp3Time, comp4Time, compFee)
