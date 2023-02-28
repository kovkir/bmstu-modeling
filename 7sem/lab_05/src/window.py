from tkinter import Tk, Label, Entry, Button, messagebox, DISABLED, END

from distribution import EvenDistribution
from generator import Generator
from processor import Processor
from eventModel import EventModel
from color import *


class Window():
    window: Tk

    windowWidth: int
    windowHeight: int

    countClientsEntry: Entry
    intervalEntry: Entry
    intervalRangeEntry: Entry

    operator1Entry: Entry
    operator1RangeEntry: Entry
    operator2Entry: Entry
    operator2RangeEntry: Entry
    operator3Entry: Entry
    operator3RangeEntry: Entry

    computer1Entry: Entry
    computer2Entry: Entry

    processedEntry: Entry
    refusedEntry: Entry
    refusedPercentageEntry: Entry

    
    def __init__(self, windowWidth: int, windowHeight: int):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.window = self.createWindow(windowWidth, windowHeight)
        self.createInterface()


    def createWindow(self, windowWidth: int, windowHeight: int):
        window = Tk()
        window.title("Лабораторная работа №5 (Ковалец Кирилл ИУ7-73Б)")
        window.geometry("{0}x{1}".format(windowWidth, windowHeight))
        window.resizable(False, False)
        window["bg"] = PURPLE_LIGHT

        return window


    def createInterface(self):
        Label(text = "ПАРАМЕТРЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 10)

        Label(text = "Количество заявок", font = ("Arial", 16), bg = "#e0e0eb",
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


        Label(text = "ОПЕРАТОРЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 130)


        Label(text = "Оператор 1", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 170)

        self.operator1Entry = Entry(font = ("Arial", 17))
        self.operator1Entry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.5, y = 170)

        Label(text = "+/-", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.05, height = 30, x = self.windowWidth * 0.6, y = 170)

        self.operator1RangeEntry = Entry(font = ("Arial", 17))
        self.operator1RangeEntry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.65, y = 170)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 170)

        
        Label(text = "Оператор 2", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 210)

        self.operator2Entry = Entry(font = ("Arial", 17))
        self.operator2Entry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.5, y = 210)

        Label(text = "+/-", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.05, height = 30, x = self.windowWidth * 0.6, y = 210)

        self.operator2RangeEntry = Entry(font = ("Arial", 17))
        self.operator2RangeEntry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.65, y = 210)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 210)

        
        Label(text = "Оператор 3", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 250)

        self.operator3Entry = Entry(font = ("Arial", 17))
        self.operator3Entry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.5, y = 250)

        Label(text = "+/-", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.05, height = 30, x = self.windowWidth * 0.6, y = 250)

        self.operator3RangeEntry = Entry(font = ("Arial", 17))
        self.operator3RangeEntry.place(width = self.windowWidth * 0.1, height = 30, x = self.windowWidth * 0.65, y = 250)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 250)


        Label(text = "КОМПЬЮТЕРЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 290)


        Label(text = "Компьютер 1", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 330)

        self.computer1Entry = Entry(font = ("Arial", 17))
        self.computer1Entry.place(width = self.windowWidth * 0.25, height = 30, x = self.windowWidth * 0.5, y = 330)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 330)


        Label(text = "Компьютер 2", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 370)

        self.computer2Entry = Entry(font = ("Arial", 17))
        self.computer2Entry.place(width = self.windowWidth * 0.25, height = 30, x = self.windowWidth * 0.5, y = 370)

        Label(text = "минут(ы)", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.15, height = 30, x = self.windowWidth * 0.75, y = 370)


        Label(text = "РЕЗУЛЬТАТ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 430)

        Label(text = "Обработано                 Отказано              Процент отказа", 
            font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d")\
                .place(width = self.windowWidth, height = 20, x = 0, y = 470)
            
        self.processedEntry = Entry(font = ("Arial", 17))
        self.processedEntry.place(width = self.windowWidth * 0.267, height = 30, x = self.windowWidth * 0.1, y = 500)

        self.refusedEntry = Entry(font = ("Arial", 17))
        self.refusedEntry.place(width = self.windowWidth * 0.267, height = 30, x = self.windowWidth * 0.367, y = 500)

        self.refusedPercentageEntry = Entry(font = ("Arial", 17))
        self.refusedPercentageEntry.place(width = self.windowWidth * 0.266, height = 30, x = self.windowWidth * 0.634, y = 500)


        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = self.windowWidth * 0.8, height = 40, x = self.windowWidth * 0.1, y = 540)

        solveButton = Button(
            text = "Решить", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.solve())
        solveButton.place(width = self.windowWidth * 0.8 - 4, height = 36, x = self.windowWidth * 0.1 + 2, y = 542)


        Label(text = "О ПРОГРАММЕ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = self.windowHeight - 90)

        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = self.windowWidth * 0.8, height = 40, x = self.windowWidth * 0.1, y = self.windowHeight - 50)

        solveButton = Button(
            text = "Информация о программе", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.aboutProgram())
        solveButton.place(width = self.windowWidth * 0.8 - 4, height = 36, x = self.windowWidth * 0.1 + 2, y = self.windowHeight - 48)


    def aboutProgram(self):
        messagebox.showinfo("О программе",
            "В информационный центр приходят клиенты через интервалы времени 10+/-2 минуты. Если все три имеющихся оператора заняты, клиенту отказывают в обслуживании. Операторы имеют разную производительность и могут обеспечивать обслуживание среднее запросы за 20+/-5, 40+/-10, 40+/-20 минут. Клиенты стремятся занять свободного оператора с максимальной производительностью. Полученные запросы сдаются в приемные накопители, откуда они выбираются для обработки. На первый компьютер - запросы от первого и второго операторов, на второй компьютер — от третьего оператора. Время обработки на первом и втором компьютере равны соответственно 15 и 30 минутам. Смоделировать процесс обработки 300 запросов. Определить вероятность отказа."
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

        if countClients <= 0 or interval <= 0 or intervalRange >= interval:
            messagebox.showwarning("Ошибка", 
                "Недопустимые значения параметров.")
            return

        return Generator(
                EvenDistribution(interval - intervalRange, interval + intervalRange),
                countClients
            )

    
    def getOperator(self, operatorEntry: Entry, operatorRangeEntry: Entry):
        try:
            operator = int(operatorEntry.get())
            operatorRange = int(operatorRangeEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы значения операторов!\n"
                "Ожидался ввод целых чисел.")
            return

        if operator <= 0 or operatorRange >= operator:
            messagebox.showwarning("Ошибка", 
                "Недопустимые значения операторов.")
            return

        return Processor(
                EvenDistribution(operator - operatorRange, operator + operatorRange),
                maxQueue = 1
            )


    def getOperators(self):
        return [self.getOperator(self.operator1Entry, self.operator1RangeEntry),
                self.getOperator(self.operator2Entry, self.operator2RangeEntry),
                self.getOperator(self.operator3Entry, self.operator3RangeEntry)]

    
    def getComputer(self, computerEntry: Entry):
        try:
            computer = int(computerEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы значения компьютеров!\n"
                "Ожидался ввод целых чисел.")
            return

        if computer <= 0:
            messagebox.showwarning("Ошибка", 
                "Недопустимые значения компьютеров.")
            return

        return Processor(
                EvenDistribution(computer, computer),
                maxQueue = -1
            )


    def getComputers(self):
        return [self.getComputer(self.computer1Entry),
                self.getComputer(self.computer2Entry)]


    def writeToEntry(self, numb: float, entry: Entry):
        entry.delete(0, END)
        entry.insert(0, numb)


    def solve(self):
        generator = self.getGenerator()
        operators = self.getOperators()
        computers = self.getComputers()

        model = EventModel(generator, operators, computers)
        result = model.run()

        self.writeToEntry(result[0], self.processedEntry)
        self.writeToEntry(result[1] - 1, self.refusedEntry)
        self.writeToEntry(round(result[2], 2), self.refusedPercentageEntry)


    def run(self):
        self.countClientsEntry.insert(0, 300)
        self.intervalEntry.insert(0, 10)
        self.intervalRangeEntry.insert(0, 2)

        self.operator1Entry.insert(0, 20)
        self.operator1RangeEntry.insert(0, 5)
        self.operator2Entry.insert(0, 40)
        self.operator2RangeEntry.insert(0, 10)
        self.operator3Entry.insert(0, 40)
        self.operator3RangeEntry.insert(0, 20)

        self.computer1Entry.insert(0, 15)
        self.computer2Entry.insert(0, 30)

        self.window.mainloop()
