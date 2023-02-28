from tkinter import Tk, Label, Entry, Button, messagebox, DISABLED
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from distribution import Distribution

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 840

CANVAS_WIDTH = WINDOW_WIDTH - 300
CANVAS_HEIGHT = WINDOW_HEIGHT / 2

X_COUNT = 1000
X_MIN_INIT = -10
X_MAX_INIT = 10


class Window():
    window: Tk
    figures: list
    canvases: list
    axes: list


    def __init__(self, windowWidth: int, windowHeight: int):
        self.window = self.createWindow(windowWidth, windowHeight)
        self.figures = self.createFigures()
        self.canvases = self.createCanvas()
        self.axes = self.createAxes()
        self.createInterface()


    def createWindow(self, windowWidth: int, windowHeight: int):
        window = Tk()
        window.title("Лабораторная работа №1")
        window.geometry("{0}x{1}".format(windowWidth, windowHeight))
        window.resizable(False, False)
        window["bg"] = "#e0e0eb"

        return window


    def createFigures(self):
        figures = list()

        for _ in range(2):
            figure = plt.figure()
            figure.set(facecolor = "#b3b3cc")
            figure.subplots_adjust(right = 0.97, left = 0.06, bottom = 0.08 , top = 0.9)
            figures.append(figure)

        return figures


    def createCanvas(self):
        canvases = list()

        for i in range(2):
            canvas = FigureCanvasTkAgg(self.figures[i], master = self.window)
            canvases.append(canvas)

            tk_widget = canvas.get_tk_widget()

            if i == 0:
                tk_widget.place(x = 0, y = 0, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
            else:
                tk_widget.place(x = 0, y = CANVAS_HEIGHT, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

        return canvases


    def createAxes(self):
        axes = list()

        for i in range(2):
            ax = self.figures[i].add_subplot(111)
            ax.set(facecolor = "#f0f0f5")

            ax.spines["bottom"].set_color("#29293d")
            ax.spines["top"].set_color("#29293d")
            ax.spines["left"].set_color("#29293d")
            ax.spines["right"].set_color("#29293d")

            ax.tick_params(axis = "x", colors = "#29293d")
            ax.tick_params(axis = "y", colors = "#29293d")
            ax.grid(color = "#a3a3c2", linestyle = '--')

            axes.append(ax)

        return axes


    def aboutProgram(self):
        messagebox.showinfo("О программе",
            "Программа для построения графиков распределения и плотности распределения для:\n"
            "   1) равномерного распределения;\n"
            "   2) распределения Эрланга."
            "\n\nКовалец Кирилл ИУ7-73Б")


    def createInterface(self):
        Label(text = "ИНТЕРВАЛ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = 300, height = 30, x = CANVAS_WIDTH , y = 20)

        Label(text = "Xmin\t\tXmax", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = 250, height = 20, x = CANVAS_WIDTH + 30, y = 70)

        xMinEntry = Entry(font = ("Arial", 17))
        xMinEntry.place(width = 125, height = 30, x = CANVAS_WIDTH + 30, y = 100)
        xMinEntry.insert(0, X_MIN_INIT)

        xMaxEntry = Entry(font = ("Arial", 17))
        xMaxEntry.place(width = 125, height = 30, x = CANVAS_WIDTH + 155, y = 100)
        xMaxEntry.insert(0, X_MAX_INIT)


        Label(text = "РАВНОМЕРНОЕ РАСПРЕДЕЛЕНИЕ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = 300, height = 30, x = CANVAS_WIDTH , y = 160)

        Label(text = "a\t\tb", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = 250, height = 20, x = CANVAS_WIDTH + 30, y = 210)

        aEntry = Entry(font = ("Arial", 17))
        aEntry.place(width = 125, height = 30, x = CANVAS_WIDTH + 30, y = 240)

        bEntry = Entry(font = ("Arial", 17))
        bEntry.place(width = 125, height = 30, x = CANVAS_WIDTH + 155, y = 240)

        Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
            place(width = 250, height = 30,  x = CANVAS_WIDTH + 30, y = 280)

        uniformDistrButton = Button(
            text = "Построить графики", font = ("Arial", 16), 
            highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
            command = lambda: self.drawUniformDistrGraphs(aEntry, bEntry, xMinEntry, xMaxEntry))
        uniformDistrButton.place(width = 246, height = 26,  x = CANVAS_WIDTH + 32, y = 282)


        Label(text = "РАСПРЕДЕЛЕНИЕ ЭРЛАНГА", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = 300, height = 30, x = CANVAS_WIDTH , y = 340)

        Label(text = "k\t\tλ", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = 250, height = 20, x = CANVAS_WIDTH + 30, y = 390)

        kEntry = Entry(font = ("Arial", 17))
        kEntry.place(width = 125, height = 30, x = CANVAS_WIDTH + 30, y = 420)

        lEntry = Entry(font = ("Arial", 17))
        lEntry.place(width = 125, height = 30, x = CANVAS_WIDTH + 155, y = 420)

        Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
            place(width = 250, height = 30,  x = CANVAS_WIDTH + 30, y = 460)

        erlangDistrButton = Button(
            text = "Построить графики", font = ("Arial", 16), 
            highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
            command = lambda: self.drawErlangDistrGraphs(kEntry, lEntry, xMinEntry, xMaxEntry))
        erlangDistrButton.place(width = 246, height = 26,  x = CANVAS_WIDTH + 32, y = 462)


        Label(text = "О ПРОГРАММЕ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = 300, height = 30, x = CANVAS_WIDTH , y = 740)

        Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
            place(width = 250, height = 30,  x = CANVAS_WIDTH + 30, y = 790)

        infoButton = Button(
            text = "Информация о программе", font = ("Arial", 16), 
            highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
            command = lambda: self.aboutProgram())
        infoButton.place(width = 246, height = 26,  x = CANVAS_WIDTH + 32, y = 792)


    def getXminXmax(self, xMinEntry: Entry, xMaxEntry: Entry, erlangDistr = False):
        try:
            xMin = float(xMinEntry.get())
            xMax = float(xMaxEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы значения интервала.\n"
                "Ожидался ввод действительных чисел!")
            return

        if xMin >= xMax:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы значения интервала.\n"
                "Требуется, чтобы Xmin < Xmax!")
            return

        if erlangDistr and xMin < 0:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы значения интервала для распределения Эрланга.\n"
                "Требуется, чтобы Xmin >= 0!")
            return

        
        return xMin, xMax


    def getAcoefBcoef(self, aEntry: Entry, bEntry: Entry):
        try:
            a = float(aEntry.get())
            b = float(bEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы параметры для равномерного распределения!\n"
                "Ожидался ввод действительных чисел.")
            return

        if a >= b:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы параметры для равномерного распределения.\n"
                "Требуется, чтобы a < b!")
            return

        return a, b


    def getKcoefLcoef(self, kEntry: Entry, lEntry: Entry):
        try:
            k = int(kEntry.get())
            l = float(lEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы параметры для распределения Эрланга!\n"
                "k - натуральное число;\n"
                "λ - действительное число.")
            return

        if k <= 0 or l < 0:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы параметры для распределения Эрланга.\n"
                "Требуется, чтобы λ >= 0, k = 1, 2, ...!")
            return

        return k, l


    def drawUniformDistrGraphs(self, aEntry: Entry, bEntry: Entry, xMinEntry: Entry, xMaxEntry: Entry):
        xMin, xMax = self.getXminXmax(xMinEntry, xMaxEntry)
        if xMin == None:
            return

        a, b = self.getAcoefBcoef(aEntry, bEntry)
        if a == None:
            return

        distribution = Distribution()

        xArr = list()
        uniformDistrArr = list()
        uniformDistrDensityArr = list()

        step = (xMax - xMin) / X_COUNT
        x = xMin

        while x <= xMax:
            uniformDistrArr.append(distribution.uniformDistribution(a, b, x))
            uniformDistrDensityArr.append(distribution.uniformDistributionDensity(a, b, x))
            xArr.append(x)
            x += step

        self.figures[0].clear()
        self.figures[1].clear()
        self.axes = self.createAxes()
        self.axes[0].plot(xArr, uniformDistrArr)
        self.axes[1].plot(xArr, uniformDistrDensityArr)
        self.axes[0].set(title = 'Функция равномерного распределения')
        self.axes[1].set(title = 'Функция плотности равномерного распределения')
        self.canvases[0].draw()
        self.canvases[1].draw()


    def drawErlangDistrGraphs(self, kEntry: Entry, lEntry: Entry, xMinEntry: Entry, xMaxEntry: Entry):
        xMin, xMax = self.getXminXmax(xMinEntry, xMaxEntry, erlangDistr = True)
        if xMin == None:
            return

        k, l = self.getKcoefLcoef(kEntry, lEntry)
        if k == None:
            return

        distribution = Distribution()

        xArr = list()
        erlangDistrArr = list()
        erlangDistrDensityArr = list()

        step = (xMax - xMin) / X_COUNT
        x = xMin

        while x <= xMax:
            erlangDistrArr.append(distribution.erlangDistribution(k, l, x))
            erlangDistrDensityArr.append(distribution.erlangDistributionDensity(k, l, x))
            xArr.append(x)
            x += step

        self.figures[0].clear()
        self.figures[1].clear()
        self.axes = self.createAxes()
        self.axes[0].plot(xArr, erlangDistrArr)
        self.axes[1].plot(xArr, erlangDistrDensityArr)
        self.axes[0].set(title = 'Функция распределения Эрланга')
        self.axes[1].set(title = 'Функция плотности распределения Эрланга')
        self.canvases[0].draw()
        self.canvases[1].draw()


    def run(self):
        self.window.mainloop()


def main(): 
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.run()


if __name__ == "__main__":
    main()
