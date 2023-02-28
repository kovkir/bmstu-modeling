from tkinter import Tk, Label, Entry, Button, messagebox, DISABLED, VERTICAL, NO, END, CENTER
from tkinter import ttk

from distribution import EvenDistribution
from generator import Generator
from processor import Processor
from eventModel import EventModel
from color import *


COUNT_ROWS = 5
ROW_HEIGHT = 30


class Window():
    window: Tk

    windowWidth: int
    windowHeight: int

    countClientsEntry: Entry
    intervalEntry: Entry
    intervalRangeEntry: Entry

    terminal1Entry: Entry
    terminal1RangeEntry: Entry
    terminal2Entry: Entry
    terminal2RangeEntry: Entry
    terminal3Entry: Entry
    terminal3RangeEntry: Entry

    window1Entry: Entry
    window1RangeEntry: Entry
    window2Entry: Entry
    window2RangeEntry: Entry

    operatingTimeEntry: Entry
    table: ttk.Treeview

    
    def __init__(self, windowWidth: int, windowHeight: int):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.window = self.createWindow(windowWidth, windowHeight)
        self.createInterface()


    def createWindow(self, windowWidth: int, windowHeight: int):
        window = Tk()
        window.title("Лабораторная работа №6 (Ковалец Кирилл ИУ7-73Б)")
        window.geometry("{0}x{1}".format(windowWidth, windowHeight))
        window.resizable(False, False)
        window["bg"] = PURPLE_LIGHT

        return window


    def createInterface(self):
        Label(text = "ПАРАМЕТРЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 10)

        Label(text = "Количество клиентов", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 50)

        self.countClientsEntry = Entry(font = ("Arial", 17))
        self.countClientsEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.5, y = 50)

        Label(text = "Интервал прихода клиента", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 90)

        self.intervalEntry = Entry(font = ("Arial", 17))
        self.intervalEntry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.5, y = 90)

        Label(text = "+/-", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.05, height = 30, x = self.windowWidth * 0.6, y = 90)

        self.intervalRangeEntry = Entry(font = ("Arial", 17))
        self.intervalRangeEntry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.65, y = 90)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 90)


        Label(text = "ТЕРМИНАЛЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 130)


        Label(text = "Терминал 1", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 170)

        self.terminal1Entry = Entry(font = ("Arial", 17))
        self.terminal1Entry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.5, y = 170)

        Label(text = "+/-", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.05, height = 30, x = self.windowWidth * 0.6, y = 170)

        self.terminal1RangeEntry = Entry(font = ("Arial", 17))
        self.terminal1RangeEntry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.65, y = 170)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 170)

        
        Label(text = "Терминал 2", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 210)

        self.terminal2Entry = Entry(font = ("Arial", 17))
        self.terminal2Entry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.5, y = 210)

        Label(text = "+/-", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.05, height = 30, x = self.windowWidth * 0.6, y = 210)

        self.terminal2RangeEntry = Entry(font = ("Arial", 17))
        self.terminal2RangeEntry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.65, y = 210)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 210)

        
        Label(text = "Терминал 3", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 250)

        self.terminal3Entry = Entry(font = ("Arial", 17))
        self.terminal3Entry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.5, y = 250)

        Label(text = "+/-", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.05, height = 30, x = self.windowWidth * 0.6, y = 250)

        self.terminal3RangeEntry = Entry(font = ("Arial", 17))
        self.terminal3RangeEntry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.65, y = 250)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 250)


        Label(text = "ОКНА ОБСЛУЖИВАНИЯ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 290)


        Label(text = "Окно обслуживания 1", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 330)

        self.window1Entry = Entry(font = ("Arial", 17))
        self.window1Entry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.5, y = 330)

        Label(text = "+/-", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.05, height = 30, x = self.windowWidth * 0.6, y = 330)

        self.window1RangeEntry = Entry(font = ("Arial", 17))
        self.window1RangeEntry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.65, y = 330)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 330)


        Label(text = "Окно обслуживания 2", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 370)

        self.window2Entry = Entry(font = ("Arial", 17))
        self.window2Entry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.5, y = 370)

        Label(text = "+/-", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.05, height = 30, x = self.windowWidth * 0.6, y = 370)

        self.window2RangeEntry = Entry(font = ("Arial", 17))
        self.window2RangeEntry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.65, y = 370)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 370)


        Label(text = "РЕЗУЛЬТАТ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 410)

        Label(text = "Время работы системы", 
            font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d")\
                .place(width = self.windowWidth * 0.4, height = 20, x = self.windowWidth * 0.1, y = 450)
            
        self.operatingTimeEntry = Entry(font = ("Arial", 17))
        self.operatingTimeEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.5, y = 450)


        self.table = self.createTable(int(self.windowWidth * 0.1), 490)


        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = self.windowWidth * 0.8, height = 40, x = self.windowWidth * 0.1, y = 670)

        solveButton = Button(
            text = "Решить", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.solve())
        solveButton.place(width = self.windowWidth * 0.8 - 4, height = 36, x = self.windowWidth * 0.1 + 2, y = 672)


        Label(text = "О ПРОГРАММЕ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = self.windowHeight - 90)

        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = self.windowWidth * 0.8, height = 40, x = self.windowWidth * 0.1, y = self.windowHeight - 50)

        solveButton = Button(
            text = "Информация о программе", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.aboutProgram())
        solveButton.place(width = self.windowWidth * 0.8 - 4, height = 36, x = self.windowWidth * 0.1 + 2, y = self.windowHeight - 48)


    def createTable(self, xTable, yTable):
        s = ttk.Style()
        s.configure('Treeview', rowheight=ROW_HEIGHT)

        # определяем столбцы
        columns = ("elements", "maxQueue", "processed")

        tree = ttk.Treeview(columns=columns, height=COUNT_ROWS, show="headings")
        tree.place(x=xTable, y=yTable)

        # определяем заголовки
        tree.heading("elements", text="Элементы")
        tree.heading("maxQueue", text="Максимальная очередь")
        tree.heading("processed", text="Обработано")
        
        # настраиваем столбцы
        tree.column("#1", stretch=NO, width=int(self.windowWidth * 0.3), anchor=CENTER)
        tree.column("#2", stretch=NO, width=int(self.windowWidth * 0.25), anchor=CENTER)
        tree.column("#3", stretch=NO, width=int(self.windowWidth * 0.25), anchor=CENTER)

        # задаем размер шрифта элементов таблицы
        tree.tag_configure("item", font=("Arial", 16))

        return tree

    def aboutProgram(self):
        messagebox.showinfo("О программе",
            "В данной лабораторной работе моделируется следующая система. В пункт получения документов приходят клиенты с заданным интервалом времени, которые сначала подходят к терминалу выдачи талонов. У каждого терминала формируется своя очередь. Клиент выбирает очередь с минимальной длиной. Терминалы обслуживают клиентов за заданный интервал времени. Далее клиент отправляется к окну, в котором его обслужат. У каждого окна формируется своя очередь. Клиента отправляют к окну с минимальной очередью. В окне клиента обслуживают за заданный интервал времени. Количество клиентов задается."
            "\n\nКовалец Кирилл ИУ7-73Б")


    def getGenerator(self):
        try:
            countClients = int(self.countClientsEntry.get())
            interval = int(self.intervalEntry.get())
            intervalRange = int(self.intervalRangeEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы параметры!\n"
                "Ожидался ввод целых чисел.")
            return

        if countClients <= 0 or interval <= 0 or intervalRange > interval:
            messagebox.showwarning("Ошибка", 
                "Недопустимые значения параметров.")
            return

        return Generator(
                EvenDistribution(interval - intervalRange, interval + intervalRange),
                countClients
            )

    
    def getTerminal(self, terminalEntry: Entry, terminalRangeEntry: Entry):
        try:
            terminal = int(terminalEntry.get())
            terminalRange = int(terminalRangeEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы значения терминалов!\n"
                "Ожидался ввод целых чисел.")
            return

        if terminal <= 0 or terminalRange > terminal:
            messagebox.showwarning("Ошибка", 
                "Недопустимые значения терминалов.")
            return

        return Processor(
                EvenDistribution(terminal - terminalRange, terminal + terminalRange)
            )


    def getTerminals(self):
        return [self.getTerminal(self.terminal1Entry, self.terminal1RangeEntry),
                self.getTerminal(self.terminal2Entry, self.terminal2RangeEntry),
                self.getTerminal(self.terminal3Entry, self.terminal3RangeEntry)]

    
    def getWindow(self, windowEntry: Entry, windowRangeEntry: Entry):
        try:
            window = int(windowEntry.get())
            windowRange = int(windowRangeEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы значения для окон обслуживания!\n"
                "Ожидался ввод целых чисел.")
            return

        if window <= 0 or windowRange > window:
            messagebox.showwarning("Ошибка", 
                "Недопустимые значения для окон обслуживания.")
            return

        return Processor(
                EvenDistribution(window, window)
            )


    def getWindows(self):
        return [self.getWindow(self.window1Entry, self.window1RangeEntry),
                self.getWindow(self.window2Entry, self.window2RangeEntry)]


    def writeToEntry(self, numb: float, entry: Entry):
        entry.delete(0, END)
        entry.insert(0, numb)

    
    def clearTreeview(self, table: ttk.Treeview):
        for i in table.get_children(): 
            table.delete(i) 

    
    def fillTable(self, data):
        self.clearTreeview(self.table)
        # добавляем данные
        for row in data:
            self.table.insert("", END, values=row, tag='item')


    def solve(self):
        generator = self.getGenerator()
        terminals = self.getTerminals()
        windows = self.getWindows()

        generator.setReceivers(terminals.copy())

        for terminal in terminals:
            terminal.setReceivers(windows.copy())

        model = EventModel(generator, terminals, windows)
        currentTime, data = model.run()
        self.writeToEntry(round(currentTime, 2), self.operatingTimeEntry)
        self.fillTable(data)

     
    def run(self):
        self.countClientsEntry.insert(0, 100)
        self.intervalEntry.insert(0, 1)
        self.intervalRangeEntry.insert(0, 1)

        self.terminal1Entry.insert(0, 3)
        self.terminal1RangeEntry.insert(0, 1)
        self.terminal2Entry.insert(0, 3)
        self.terminal2RangeEntry.insert(0, 1)
        self.terminal3Entry.insert(0, 3)
        self.terminal3RangeEntry.insert(0, 1)

        self.window1Entry.insert(0, 4)
        self.window1RangeEntry.insert(0, 2)
        self.window2Entry.insert(0, 4)
        self.window2RangeEntry.insert(0, 2)

        self.window.mainloop()
