from tkinter import Tk, Label, Entry, Button, messagebox, DISABLED, VERTICAL, NO, END, CENTER
from tkinter import ttk

from myRandom import MyRandom
from test import TestWindow
from color import *


COUNT_ROWS = 15
ROW_HEIGHT = 30

TABLE_FILE = "../docs/digits.txt"
COUNT_NUMBERS = 10000


class Window():
    window: Tk

    windowWidth: int
    windowHeight: int

    xTable: int
    yTable: int

    tabTable: ttk.Treeview
    algTable: ttk.Treeview

    oneAlgEntry: Entry
    twoAlgEntry: Entry
    threeAlgEntry: Entry

    oneTableEntry: Entry
    twoTableEntry: Entry
    threeTableEntry: Entry


    def __init__(self, windowWidth: int, windowHeight: int):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.xTable = (windowWidth // 2 - 400) // 2
        self.yTable = 70

        self.window = self.createWindow(windowWidth, windowHeight)
        self.tabTable = self.createTable(self.xTable, self.yTable)
        self.algTable = self.createTable(self.xTable + self.windowWidth // 2, self.yTable)
        self.createInterface()


    def createWindow(self, windowWidth: int, windowHeight: int):
        window = Tk()
        window.title("Лабораторная работа №3")
        window.geometry("{0}x{1}".format(windowWidth, windowHeight))
        window.resizable(False, False)
        window["bg"] = PURPLE_LIGHT

        return window

    
    def createTable(self, xTable, yTable):
        s = ttk.Style()
        s.configure('Treeview', rowheight=ROW_HEIGHT)

        # определяем столбцы
        columns = ("number", "one_digit", "two_digits", "three_digits")

        tree = ttk.Treeview(columns=columns, height=COUNT_ROWS, show="headings")
        tree.place(x=xTable, y=yTable)

        # определяем заголовки
        tree.heading("number", text="№")
        tree.heading("one_digit", text="1 разряд")
        tree.heading("two_digits", text="2 разряда")
        tree.heading("three_digits", text="3 разряда")
        
        # настраиваем столбцы
        tree.column("#1", stretch=NO, width=100, anchor=CENTER)
        tree.column("#2", stretch=NO, width=100, anchor=CENTER)
        tree.column("#3", stretch=NO, width=100, anchor=CENTER)
        tree.column("#4", stretch=NO, width=100, anchor=CENTER)

        # задаем размер шрифта элементов таблицы
        tree.tag_configure("item", font=("Arial", 16))

        # добавляем вертикальную прокрутку
        scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
        scrollbar.place(height=ROW_HEIGHT * COUNT_ROWS + 20, x=xTable + 400, y=yTable)
        tree.configure(yscroll=scrollbar.set)

        return tree


    def createInterface(self):
        Label(text="ТАБЛИЧНЫЙ МЕТОД", font=("Arial", 16, "bold"), bg=PURPLE_DARK,
            fg="white").place(width=self.windowWidth // 2, height=30, x=0, y=20)

        Label(text="АЛГОРИТМИЧЕСКИЙ МЕТОД", font=("Arial", 16, "bold"), bg=PURPLE_DARK,
            fg="white").place(width=self.windowWidth // 2, height=30, x=self.windowWidth // 2, y=20)


        Label(text = "Коэф.", font = ("Arial", 16, "bold"), bg = PURPLE_LIGHT, fg = PURPLE_DARK).\
            place(width = 100, height = 30, x = self.xTable, y = self.yTable + ROW_HEIGHT * COUNT_ROWS + 40)

        self.oneAlgEntry = Entry(font = ("Arial", 17))
        self.oneAlgEntry.place(width = 100, height = 30, 
            x = self.xTable + 100, y = self.yTable + ROW_HEIGHT * COUNT_ROWS + 40)

        self.twoAlgEntry = Entry(font = ("Arial", 17))
        self.twoAlgEntry.place(width = 100, height = 30, 
            x = self.xTable + 200, y = self.yTable + ROW_HEIGHT * COUNT_ROWS + 40)

        self.threeAlgEntry = Entry(font = ("Arial", 17))
        self.threeAlgEntry.place(width = 100, height = 30, 
            x = self.xTable + 300, y = self.yTable + ROW_HEIGHT * COUNT_ROWS + 40)


        Label(text = "Коэф.", font = ("Arial", 16, "bold"), bg = PURPLE_LIGHT, fg = PURPLE_DARK).\
            place(width = 100, height = 30, x = self.xTable + self.windowWidth // 2, 
                y = self.yTable + ROW_HEIGHT * COUNT_ROWS + 40)

        self.oneTableEntry = Entry(font = ("Arial", 17))
        self.oneTableEntry.place(width = 100, height=30, 
            x = self.xTable + self.windowWidth // 2 + 100, y = self.yTable + ROW_HEIGHT * COUNT_ROWS + 40)

        self.twoTableEntry = Entry(font = ("Arial", 17))
        self.twoTableEntry.place(width = 100, height=30, 
            x = self.xTable + self.windowWidth // 2 + 200, y = self.yTable + ROW_HEIGHT * COUNT_ROWS + 40)

        self.threeTableEntry = Entry(font = ("Arial", 17))
        self.threeTableEntry.place(width = 100, height=30,
            x = self.xTable + self.windowWidth // 2 + 300, y = self.yTable + ROW_HEIGHT * COUNT_ROWS + 40)



        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = self.windowWidth - 2 * self.xTable, height = 30,  
                x = self.xTable, y = self.windowHeight - 100)

        solveButton = Button(
            text = "Сгенерировать случайные числа и расчитать критерий оценки случайности", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.solve())
        solveButton.place(width = self.windowWidth - 2 * self.xTable - 4, height = 26,  
            x = self.xTable + 2, y = self.windowHeight - 98)

       

        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = 400, height = 30, 
                x = self.xTable, y = self.windowHeight - 50)

        testButton = Button(
            text = "Ручное тестирование", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.test())
        testButton.place(width = 396, height = 26, 
            x = self.xTable + 2, y = self.windowHeight - 48)



        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = 400, height = 30, 
                x = self.windowWidth // 2 + self.xTable, y = self.windowHeight - 50)

        infoButton = Button(
            text = "Информация о программе", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.aboutProgram())
        infoButton.place(width = 396, height = 26, 
            x = self.windowWidth // 2 + self.xTable + 2, y = self.windowHeight - 48)


    def aboutProgram(self):
        messagebox.showinfo("О программе",
            "Необходимо разработать графический интерфейс, который позволяет сгенерировать последовательность псевдослучайных чисел алгоритмическим и табличным методами, а также рассчитать коэффициенты их случайности. Необходимо предусмотреть возможность ввода чесел."
            "\n\nКовалец Кирилл ИУ7-73Б")


    def fillEntry(self, entry: Entry, number: float):
        entry.delete(0, END)
        entry.insert(0, round(number, 2))


    def getNumbers(self, count: int, file: str):
        numbers = set()

        with open(file) as file: 
            rows = file.readlines()

        for row in rows:
            numbers.update(set(row.split()[1:]))
            if len(numbers) >= count + 1:
                break

        numbers = list(numbers)[:count]

        return numbers


    def tabularSolve(self):
        numbers = self.getNumbers(3 * COUNT_NUMBERS, TABLE_FILE)

        oneDigit    = [int(i) % 10        for i in numbers[: COUNT_NUMBERS]]
        twoDigits   = [int(i) % 90 + 10   for i in numbers[COUNT_NUMBERS : 2 * COUNT_NUMBERS]]
        threeDigits = [int(i) % 900 + 100 for i in numbers[2 * COUNT_NUMBERS : 3 * COUNT_NUMBERS]]

        return oneDigit, twoDigits, threeDigits


    def algorithmicSolve(self):
        random = MyRandom()

        oneDigit    = [random.getNumber(0, 10)     for _ in range(COUNT_NUMBERS)]
        twoDigits   = [random.getNumber(10, 100)   for _ in range(COUNT_NUMBERS)]
        threeDigits = [random.getNumber(100, 1000) for _ in range(COUNT_NUMBERS)]

        return oneDigit, twoDigits, threeDigits


    def solveForTable(self, funcSolve, table: ttk.Treeview, oneEntry: Entry, twoEntry: Entry, threeEntry: Entry):
        random = MyRandom()

        oneDigit, twoDigits, threeDigits = funcSolve()
        data = [(i + 1, oneDigit[i],  twoDigits[i], threeDigits[i]) for i in range(COUNT_NUMBERS)]

        # добавляем данные
        for row in data:
            table.insert("", END, values=row, tag='item')

        # вычисление коэффициентов случайности
        self.fillEntry(oneEntry, random.getCoeff(oneDigit))
        self.fillEntry(twoEntry, random.getCoeff(twoDigits))
        self.fillEntry(threeEntry, random.getCoeff(threeDigits))


    def clearTreeview(self, table: ttk.Treeview):
        for i in table.get_children(): 
            table.delete(i) 


    def solve(self):
        # отчистить таблицы
        self.clearTreeview(self.algTable)
        self.clearTreeview(self.tabTable)

        self.solveForTable(self.algorithmicSolve, self.algTable, 
            self.oneAlgEntry, self.twoAlgEntry, self.threeAlgEntry)

        self.solveForTable(self.tabularSolve, self.tabTable, 
            self.oneTableEntry, self.twoTableEntry, self.threeTableEntry)


    def test(self):
        testWindow = TestWindow(400, 600)
        testWindow.run()


    def run(self):
        self.window.mainloop()

