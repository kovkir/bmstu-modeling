import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


EPS = 1e-3


class MarkovChains():
    matrix: list
    matrixSize: int

    initProbs: list
    dt: float


    def __init__(self, matrix: int, matrixSize: int, dt: float):
        self.matrix = matrix
        self.matrixSize = matrixSize
        self.initProbs = self.createInitProbabilities(matrixSize)
        self.dt = dt


    def createInitProbabilities(self, arraySize):
        return [1 if i == 0 else 0 for i in range(arraySize)]

    
    def getProbabilities(self):
        freeMembers = [0 for _ in range(self.matrixSize - 1)]
        freeMembers.append(1)

        matrixСoeffs = [
            [
                -sum(self.matrix[i]) + self.matrix[i][j] if j == i else self.matrix[j][i] 
                for j in range(self.matrixSize)
            ]
            for i in range(self.matrixSize - 1)
        ]
        matrixСoeffs.append([1 for _ in range(self.matrixSize)])

        # Стабильное состояние
        probsSteady = np.linalg.solve(matrixСoeffs, freeMembers)

        return probsSteady


    def solveOde(self, initProbs: list, _, matrixСoeffs: list):
        dydt = [0 for _ in range(self.matrixSize)]
        
        for i in range(self.matrixSize):
            dydt[i] = sum(initProbs[j] * matrixСoeffs[i][j] for j in range(self.matrixSize))

        return dydt


    def getTimes(self, probsSteady: list, buildGraph: bool):
        matrixСoeffs = [
            [
                -sum(self.matrix[i]) + self.matrix[i][j] if j == i else self.matrix[j][i] 
                for j in range(self.matrixSize)
            ]
            for i in range(self.matrixSize)
        ]

        times = np.arange(0, 20, self.dt)
    
        resOde = odeint(self.solveOde, self.initProbs, times, args=(matrixСoeffs,))
        resOde = np.transpose(resOde)

        timesSteady = list()

        for i in range(self.matrixSize):
            if buildGraph:
                plt.plot(times, resOde[i], label = "p{}".format(i))

            for j in range(len(resOde[i]) - 1, -1, -1):
                if abs(probsSteady[i] - resOde[i][j]) > EPS:
                    # Времена достижения стабильного состояния
                    timesSteady.append(times[j])
                    break
        
        if buildGraph:
            plt.legend()
            plt.grid()
            plt.show()

        return timesSteady


    def solve(self, buildGraph: bool):
        probsSteady = self.getProbabilities()
        timesSteady = self.getTimes(probsSteady, buildGraph)

        return [probsSteady, timesSteady]

