class MyRandom:
    def __init__(self):
        self.current = 1
        self.a = 36261
        self.c = 66037
        self.m = 312500

    def getNumber(self, minNumb, maxNumb):
        '''
        Линейный конгруэнтный метод 
        '''
        self.current = (self.a * self.current + self.c) % self.m
        return int(minNumb + self.current % (maxNumb - minNumb))

    def getCoeff(self, numbers: list):
        '''
        Отношение средних арифметических четных и нечетных элементов друг к другу.
        Чем ближе коэффициент к 1, тем последовательность более случайна.
        '''
        evenNumbers = list()
        oddNumbers = list()

        for numb in numbers:
            if numb & 1:
                oddNumbers.append(numb)
            else:
                evenNumbers.append(numb)

        if len(evenNumbers) == 0 or len(oddNumbers) == 0:
            return 0

        avgEvenNumbers = sum(evenNumbers) / len(evenNumbers)
        avgOddNumbers  = sum(oddNumbers)  / len(oddNumbers)
        avgArr = [avgEvenNumbers, avgOddNumbers]

        return min(avgArr) / max(avgArr)

