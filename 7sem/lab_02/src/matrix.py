from tkinter import Entry, Label
from random import random

from color import *


class Matrix():
    canvasWidth: int
    canvasHeight: int

    matrixWidth: int
    matrixHeight: int 

    matrixEntries: list
    matrix: list
    matrixSize: int

    matrixElemWidth: int
    matrixElemHeight: int

    matrixXBegin: int
    matrixYBegin: int

    xLabel: int
    yLabel: int

    labelWidth: int
    labelHeight: int


    def __init__(self, canvasWidth: int, canvasHeight: int, matrixSize: int):
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        self.matrixWidth = int(self.canvasWidth * 0.9)
        self.matrixHeight = int(self.canvasHeight * 0.6)

        self.initParameters(matrixSize)
        self.matrixEntries = self.createMatrixEntries()
        self.matrix = self.createMatrix()
        self.generateIntensity()

    
    def initParameters(self, matrixSize: int):
        self.matrixSize = matrixSize

        self.matrixElemWidth = self.matrixWidth // matrixSize
        self.matrixElemHeight = self.matrixHeight // matrixSize

        self.matrixXBegin = (self.canvasWidth - self.matrixWidth) // 2
        self.matrixYBegin = (self.canvasHeight - self.matrixHeight) * 0.9

        self.xLabel = 0
        self.yLabel = self.matrixYBegin - self.canvasHeight * 0.1

        self.labelWidth = self.canvasWidth
        self.labelHeight = self.canvasHeight * 0.1


    def createMatrixEntries(self):
        Label(text = "Матрица интенсивностей переходов состояний", 
              font = ("Arial", 26, "bold"), bg = "white", fg = PURPLE_DARK)\
                .place(
                    width = self.labelWidth, 
                    height = self.labelHeight, 
                    x = self.xLabel, y = self.yLabel)

        matrixEntries = [
            [
                Entry(font = ("Arial", 19), justify = "center", bg = PURPLE_DARK, fg = "white")
                for _ in range(self.matrixSize)
            ]
            for _ in range(self.matrixSize)
        ]

        for i in range(self.matrixSize):
            for j in range(self.matrixSize):
                matrixEntries[i][j].place(
                    x = self.matrixXBegin + self.matrixElemWidth * j,
                    y = self.matrixYBegin + self.matrixElemHeight * i,
                    width = self.matrixElemWidth,
                    height = self.matrixElemHeight)
                
        return matrixEntries 

    
    def createMatrix(self):
        return [[] for _ in range(self.matrixSize)]


    def generateIntensity(self):
        for i in range(self.matrixSize):
            for j in range(self.matrixSize):
                self.matrix[i].append(round(random(), 2))
            
            self.normalize(self.matrix[i])

            for j in range(self.matrixSize):
                self.matrixEntries[i][j].insert(0, round(self.matrix[i][j], 2))


    def normalize(self, probs):
        s = sum(probs)
        for i in range(len(probs)):
            probs[i] /= s


    def getUpdateMatrix(self):
        self.matrix = [
            [
                float(self.matrixEntries[i][j].get())
                for j in range(self.matrixSize)
            ]
            for i in range(self.matrixSize)
        ]
        
        return self.matrix

