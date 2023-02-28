from tkinter import Tk, Label, Entry, Button, messagebox, DISABLED, END

from myRandom import MyRandom
from color import *


COUNT_NUMBERS = 10
ROW_WIDTH  = 100
ROW_HEIGHT = 30


class TestWindow():
    window: Tk

    windowWidth: int
    windowHeight: int

    xTable: int
    yTable: int

    entries: list


    def __init__(self, windowWidth: int, windowHeight: int):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.xTable = windowWidth // 2 - 50
        self.yTable = 100

        self.window = self.createWindow(windowWidth, windowHeight)
        self.entries: list[Entry] = self.createTable()
        self.createInterface()


    def createWindow(self, windowWidth: int, windowHeight: int):
        window = Tk()
        window.title("Лабораторная работа №3")
        window.geometry("{0}x{1}".format(windowWidth, windowHeight))
        window.resizable(False, False)
        window["bg"] = PURPLE_LIGHT

        return window

    
    def createTable(self):
        entries = [
            Entry(self.window, font = ("Arial", 19), justify = "center", bg = "white", fg = "black")
            for _ in range(COUNT_NUMBERS)
        ]

        for i in range(COUNT_NUMBERS):
            entries[i].place(
                x = self.xTable,
                y = self.yTable + ROW_HEIGHT * i,
                width  = ROW_WIDTH,
                height = ROW_HEIGHT)

            Label(self.window, text = i + 1, font = ("Arial", 16, "bold"),bg = PURPLE_LIGHT, fg = PURPLE_DARK).\
                place(width = 50, height = 30, x = self.xTable - 50, y = self.yTable + i * ROW_HEIGHT)
                
        return entries 


    def createInterface(self):
        Label(self.window, text="РУЧНОЕ ТЕСТИРОВАНИЕ", font=("Arial", 16, "bold"), bg=PURPLE_DARK,
            fg="white").place(width=self.windowWidth, height=30, x=0, y=20)


        Label(self.window, text = "1 разряд", font = ("Arial", 16, "bold"), bg = PURPLE_LIGHT, fg = PURPLE_DARK).\
            place(width = 100, height = 30, x = self.xTable, y = self.yTable - 40)

        Label(self.window, text = "Коэф.", font = ("Arial", 16, "bold"), bg = PURPLE_LIGHT, fg = PURPLE_DARK).\
            place(width = 100, height = 30, x = self.xTable - 100, y = self.yTable + ROW_HEIGHT * COUNT_NUMBERS + 40)


        oneEntry = Entry(self.window, font = ("Arial", 17))
        oneEntry.place(width = 100, height=30, 
            x = self.xTable, y = self.yTable + ROW_HEIGHT * COUNT_NUMBERS + 40)


        Button(self.window, highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = self.windowWidth - 80, height = 30, x = 40, y = self.windowHeight - 50)

        solveButton = Button(self.window, 
            text = "Расчитать критерий оценки случайности", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.solve(oneEntry))
        solveButton.place(width = self.windowWidth - 84, height = 26, x = 42, y = self.windowHeight - 48)


    def fillEntry(self, entry: Entry, number: float):
        entry.delete(0, END)
        entry.insert(0, round(number, 2))


    def getNumbers(self):
        numbers = list()

        for i in range(COUNT_NUMBERS):
            try:
                number = int(self.entries[i].get())
                numbers.append(number)
            except:
                messagebox.showwarning("Ошибка", 
                    "Неверно задано значение!\n"
                    "Ожидался ввод целого числа.")
                return None

        return numbers


    def solve(self, entry: Entry):
        numbers = self.getNumbers()
        if numbers is None:
            return None

        random = MyRandom()
        # вычисление коэффициента случайности
        self.fillEntry(entry, random.getCoeff(numbers))
       

    def run(self):
        self.window.mainloop()

