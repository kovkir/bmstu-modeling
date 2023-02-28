from tkinter import Entry, Label, END

from color import *


class ResultProgram():
    matrix: list
    matrixXSize: int
    matrixYSize: int

    matrixElemWidth: int
    matrixElemHeight: int

    matrixXBegin: int
    matrixYBegin: int

    xLabel: int
    yLabel: int

    labelWidth: int
    labelHeight: int
    

    def __init__(self, canvasWidth: int, canvasHeight: int, matrixXSize: int):
        matrixWidth = int(canvasWidth * 0.8)
        matrixHeight = int(canvasHeight * 0.18)

        self.matrixXSize = matrixXSize
        self.matrixYSize = 2

        self.matrixElemWidth = matrixWidth // self.matrixXSize
        self.matrixElemHeight = matrixHeight // self.matrixYSize

        self.matrixXBegin = (canvasWidth - matrixWidth) // 2
        self.matrixYBegin = (canvasHeight - matrixHeight) * 0.1

        self.xLabel = 0
        self.yLabel = self.matrixYBegin - canvasHeight * 0.1

        self.labelWidth = canvasWidth
        self.labelHeight = canvasHeight * 0.1

        self.matrix = self.createMatrix()
        self.fillZeros()


    def createMatrix(self):
        Label(text = "Результат вычисления", 
              font = ("Arial", 26, "bold"), bg = "white", fg = PURPLE_DARK)\
                .place(
                    width = self.labelWidth, 
                    height = self.labelHeight, 
                    x = self.xLabel, y = self.yLabel)

        Label(text = "P", 
              font = ("Arial", 26, "bold"), bg = "white", fg = PURPLE_DARK)\
                .place(
                    width = 50, 
                    height = self.matrixElemHeight, 
                    x = self.matrixXBegin - 50,
                    y = self.matrixYBegin)
        
        Label(text = "T", 
              font = ("Arial", 26, "bold"), bg = "white", fg = PURPLE_DARK)\
                .place(
                    width = 50, 
                    height = self.matrixElemHeight, 
                    x = self.matrixXBegin - 50,
                    y = self.matrixYBegin + self.matrixElemHeight)


        matrix = [ 
            [
                Entry(font = ("Arial", 19), justify = "center", bg = PURPLE_DARK, fg = "white")
                for _ in range(self.matrixXSize)
            ]
            for _ in range(self.matrixYSize)
        ]

        
        for i in range(self.matrixYSize):
            for j in range(self.matrixXSize):
                matrix[i][j].place(
                    x = self.matrixXBegin + self.matrixElemWidth * j,
                    y = self.matrixYBegin + self.matrixElemHeight * i,
                    width = self.matrixElemWidth,
                    height = self.matrixElemHeight)
                
        return matrix 


    def fillZeros(self):
        for i in range(self.matrixYSize):
            for j in range(self.matrixXSize):
                self.matrix[i][j].insert(0, "––")

    
    def fillValues(self, values: list):
        for i in range(self.matrixYSize):
            for j in range(self.matrixXSize):
                self.matrix[i][j].delete(0, END)
                self.matrix[i][j].insert(0, round(values[i][j], 2))

    