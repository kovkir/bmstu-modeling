from tkinter import Tk, Canvas,Label, Entry, Button, messagebox, DISABLED

from matrix import Matrix
from markovChains import MarkovChains
from resultProgram import ResultProgram
from color import *


MATRIX_MIN_SIZE = 2
MATRIX_MAX_SIZE = 10


class Window():
    window: Tk

    canvasWidth: int
    canvasHeight: int
    
    matrixIntensity: Matrix
    resultProgram: ResultProgram

    stepEntry: Entry
    countEntry: Entry


    def __init__(self, windowWidth: int, windowHeight: int):
        self.canvasWidth = windowWidth - 300
        self.canvasHeight = windowHeight

        self.window = self.createWindow(windowWidth, windowHeight)
        self.createInterface()
        self.createCanvas()


    def createWindow(self, windowWidth: int, windowHeight: int):
        window = Tk()
        window.title("Лабораторная работа №2")
        window.geometry("{0}x{1}".format(windowWidth, windowHeight))
        window.resizable(False, False)
        window["bg"] = PURPLE_LIGHT

        return window


    def createCanvas(self):
        canvas = Canvas(self.window, width = self.canvasWidth, height = self.canvasHeight, bg = "white")
        canvas.place(x = 0, y = 0)


    def createInterface(self):
        Label(text = "КОЛ-ВО СОСТОЯНИЙ", font = ("Arial", 16, "bold"), bg = PURPLE_DARK,
            fg = "white").place(width = 300, height = 30, x = self.canvasWidth , y = 20)

        self.countEntry = Entry(font = ("Arial", 17))
        self.countEntry.place(width = 250, height = 40, x = self.canvasWidth + 30, y = 80)
        self.countEntry.insert(0, 10)


        Label(text = "ШАГ НА ГРАФИКЕ", font = ("Arial", 16, "bold"), bg = PURPLE_DARK,
            fg = "white").place(width = 300, height = 30, x = self.canvasWidth , y = 140)

        self.stepEntry = Entry(font = ("Arial", 17))
        self.stepEntry.place(width = 250, height = 40, x = self.canvasWidth + 30, y = 190)
        self.stepEntry.insert(0, 0.01)


        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = 250, height = 40,  x = self.canvasWidth + 30, y = 440)

        intensityButton = Button(
            text = "Сгенерировать интенсивность", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.buildMatrixIntensity())
        intensityButton.place(width = 246, height = 36,  x = self.canvasWidth + 32, y = 442)


        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = 250, height = 40,  x = self.canvasWidth + 30, y = 500)

        solveButton = Button(
            text = "Решить", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.solve())
        solveButton.place(width = 246, height = 36,  x = self.canvasWidth + 32, y = 502)


        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = 250, height = 40,  x = self.canvasWidth + 30, y = 560)

        solveButton = Button(
            text = "Построить график", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.solve(buildGraph=True))
        solveButton.place(width = 246, height = 36,  x = self.canvasWidth + 32, y = 562)


        Label(text = "О ПРОГРАММЕ", font = ("Arial", 16, "bold"), bg = PURPLE_DARK,
            fg = "white").place(width = 300, height = 30, x = self.canvasWidth , y = 620)

        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = 250, height = 30,  x = self.canvasWidth + 30, y = 670)

        infoButton = Button(
            text = "Информация о программе", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.aboutProgram())
        infoButton.place(width = 246, height = 26,  x = self.canvasWidth + 32, y = 672)


    def aboutProgram(self):
        messagebox.showinfo("О программе",
            "Разработать графический интерфейс, который позволяет по заданной матрице интенсивностей перехода состояний определить время пребывания системы в каждом состоянии в установившемся режиме работы системы. Для каждого состояния также требуется рассчитать предельную вероятность. Количество состояний не более десяти."
            "\n\nКовалец Кирилл ИУ7-73Б")


    def getMatrixSize(self):
        try:
            matrixSize = int(self.countEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно задано кол-во состояний!\n"
                "Ожидался ввод целого числа.")
            return None

        if matrixSize < MATRIX_MIN_SIZE or matrixSize > MATRIX_MAX_SIZE:
            messagebox.showwarning("Ошибка", 
                "Неверно задано кол-во состояний!\n"
                "Ожидался ввод целого числа от 2 до 10.")
            return None

        return matrixSize

    
    def getStep(self):
        try:
            step = float(self.stepEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно задано значение шага!\n"
                "Ожидался ввод действительного числа.")
            return None

        if step <= 0:
            messagebox.showwarning("Ошибка", 
                "Неверно задано значение шага!\n"
                "Ожидался ввод действительного числа > 0.")
            return None

        return step


    def buildMatrixIntensity(self):
        sizeMatrix = self.getMatrixSize()
        if sizeMatrix is None:
            return None

        self.createCanvas()

        self.matrixIntensity = Matrix(
            self.canvasWidth, self.canvasHeight, sizeMatrix)

        self.resultProgram = ResultProgram(
            self.canvasWidth, self.canvasHeight, sizeMatrix)

    
    def solve(self, buildGraph=False):
        dt = self.getStep()
        if dt is None:
            return None

        markovChains = MarkovChains(
            self.matrixIntensity.getUpdateMatrix(), self.matrixIntensity.matrixSize, dt)
        
        res = markovChains.solve(buildGraph)
        self.resultProgram.fillValues(res)


    def run(self):
        self.buildMatrixIntensity()
        self.window.mainloop()

