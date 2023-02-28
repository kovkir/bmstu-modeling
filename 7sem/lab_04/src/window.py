from tkinter import Tk, Label, Entry, Button, messagebox, DISABLED, END

from distribution import EvenDistribution, ErlangDistribution
from eventModel import eventModel
from stepModel import stepModel
from color import *


class Window():
    window: Tk

    windowWidth: int
    windowHeight: int

    aEntry: Entry
    bEntry: Entry

    kEntry: Entry
    lEntry: Entry

    countTasksEntry: Entry
    repeatProbabilityEntry: Entry
    stepEntry: Entry

    
    def __init__(self, windowWidth: int, windowHeight: int):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.window = self.createWindow(windowWidth, windowHeight)
        self.createInterface()


    def createWindow(self, windowWidth: int, windowHeight: int):
        window = Tk()
        window.title("Лабораторная работа №4")
        window.geometry("{0}x{1}".format(windowWidth, windowHeight))
        window.resizable(False, False)
        window["bg"] = PURPLE_LIGHT

        return window


    def createInterface(self):
        Label(text = "ГЕНЕРАТОР", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 10)

        Label(text = "Равномерный закон распределения", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth, height = 20, x = 0, y = 50)

        Label(text = "a\t\t\tb", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth, height = 20, x = 0, y = 80)

        self.aEntry = Entry(font = ("Arial", 17))
        self.aEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 110)

        self.bEntry = Entry(font = ("Arial", 17))
        self.bEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.5, y = 110)


        Label(text = "ОБСЛУЖИВАЮЩИЙ АППАРАТ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 150)

        Label(text = "Закон распределения Эрланга", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth, height = 20, x = 0, y = 190)

        Label(text = "k\t\t\tλ", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth, height = 20, x = 0, y = 220)

        self.kEntry = Entry(font = ("Arial", 17))
        self.kEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 250)

        self.lEntry = Entry(font = ("Arial", 17))
        self.lEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.5, y = 250)


        Label(text = "ПАРАМЕТРЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 290)

        Label(text = "Количество заявок", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 20, x = self.windowWidth * 0.1, y = 330)

        Label(text = "Вероятность возврата заявки", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 20, x = self.windowWidth * 0.1, y = 360)

        Label(text = "Временной шаг", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth * 0.4, height = 20, x = self.windowWidth * 0.1, y = 390)

        self.countTasksEntry = Entry(font = ("Arial", 17))
        self.countTasksEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.5, y = 330)

        self.repeatProbabilityEntry = Entry(font = ("Arial", 17))
        self.repeatProbabilityEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.5, y = 360)

        self.stepEntry = Entry(font = ("Arial", 17))
        self.stepEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.5, y = 390)

        Label(text = "РЕЗУЛЬТАТ", font = ("Arial", 16, "bold"), bg = "#7575a3",
            fg = "white").place(width = self.windowWidth, height = 30, x = 0 , y = 430)

        Label(text = "Максимальная длина очереди", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth, height = 20, x = 0, y = 470)

        Label(text = "Пошаговый подход\tСобытийный подход", font = ("Arial", 16), bg = "#e0e0eb",
            fg = "#29293d").place(width = self.windowWidth, height = 20, x = 0, y = 500)
            

        self.stepApproachEntry = Entry(font = ("Arial", 17))
        self.stepApproachEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.1, y = 530)

        self.eventApproachEntry = Entry(font = ("Arial", 17))
        self.eventApproachEntry.place(width = self.windowWidth * 0.4, height = 30, x = self.windowWidth * 0.5, y = 530)


        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, fg = PURPLE_LIGHT, state = DISABLED).\
            place(width = self.windowWidth * 0.8, height = 40, x = self.windowWidth * 0.1, y = 570)

        solveButton = Button(
            text = "Решить", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = "#33334d",
            command = lambda: self.solve())
        solveButton.place(width = self.windowWidth * 0.8 - 4, height = 36, x = self.windowWidth * 0.1 + 2, y = 572)


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
            "Промоделировать систему, состоящую из генератора, памяти и обслуживающего аппарата. Генератор подает сообщения, распределенные по равномерному закону, они приходят в память и выбираются на обработку по закону из ЛР1 (Эрланга). Количество заявок конечно и задано. Предусмотреть случай, когда обработанная заявка возвращается обратно в очередь. Определить оптимальную длину очереди, при которой не будет потерянных сообщений. Реализовать двумя способами: используя пошаговый и событийный подходы."
            "\n\nКовалец Кирилл ИУ7-73Б")


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

    
    def getParameters(self, countTasksEntry: Entry, repeatProbabilityEntry: Entry, stepEntry: Entry):
        try:
            countTasks = int(countTasksEntry.get())
            repeatProbability = int(repeatProbabilityEntry.get())
            step = float(stepEntry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданы параметры!")
            return

        if countTasks <= 0:
            messagebox.showwarning("Ошибка", 
                "Неверно задано количество заявок!")
            return
        
        if repeatProbability < 0 or repeatProbability > 100:
            messagebox.showwarning("Ошибка", 
                "Неверно задана вероятность возврата заявки!")
            return

        if step <= 0:
            messagebox.showwarning("Ошибка", 
                "Неверно задан временной шаг!")
            return

        return countTasks, repeatProbability, step


    def writeToEntry(self, numb: int, entry: Entry):
        entry.delete(0, END)
        entry.insert(0, numb)


    def solve(self):
        a, b = self.getAcoefBcoef(self.aEntry, self.bEntry)
        if a == None:
            return

        k, l = self.getKcoefLcoef(self.kEntry, self.lEntry)
        if k == None:
            return

        countTasks, repeatProbability, step = \
            self.getParameters(self.countTasksEntry, self.repeatProbabilityEntry, self.stepEntry)
        if countTasks == None:
            return

        generator = EvenDistribution(a, b)
        processor = ErlangDistribution(k, l)

        self.writeToEntry(
            eventModel(generator, processor, countTasks, repeatProbability), 
            self.eventApproachEntry)

        self.writeToEntry(
            stepModel(generator, processor, countTasks, repeatProbability, step), 
            self.stepApproachEntry)


    def run(self):
        self.aEntry.insert(0, -5)
        self.bEntry.insert(0, 5)

        self.kEntry.insert(0, 3)
        self.lEntry.insert(0, 2)

        self.countTasksEntry.insert(0, 1000)
        self.repeatProbabilityEntry.insert(0, 0)
        self.stepEntry.insert(0, 0.01)

        self.window.mainloop()
