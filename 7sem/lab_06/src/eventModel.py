from processor import Processor

class EventModel:
    def __init__(self, generator, terminals, windows):
        self.generator = generator
        self.terminals = terminals
        self.windows = windows

    def run(self):
        generator = self.generator
        generator.next = generator.nextTime()
        self.terminals[0].next = self.terminals[0].nextTime()

        blocks = [generator] + self.windows + self.terminals 

        numbRequests = generator.numbRequests
        count = 0
        while count < numbRequests:
            # Находим наименьшее время
            currentTime = generator.next
            for block in blocks:
                if 0 < block.next < currentTime:
                    currentTime = block.next

            for block in blocks:
                # Событие наступило для этого блока
                if currentTime == block.next:
                    if not isinstance(block, Processor): # для генератора 
                        # Проверяем, может ли оператор обработать
                        nextGenerator = generator.generateRequest()
                        if nextGenerator is not None:
                            nextGenerator.next = currentTime + nextGenerator.nextTime()

                        generator.next = currentTime + generator.nextTime()
                    else:
                        block.processRequest()
                        if block.currentQueueSize == 0:
                            block.next = 0
                        else:
                            block.next = currentTime + block.nextTime()

            count = 0 
            for computer in self.windows: 
                count += computer.processedRequests

        data = []
        for i in range(len(self.terminals)): 
            data.append(["Терминал " + str(i + 1), 
                self.terminals[i].maxQueueSize, 
                self.terminals[i].processedRequests])

        for i in range(len(self.windows)): 
            data.append(["Окно обслуживания " + str(i + 1), 
                self.windows[i].maxQueueSize, 
                self.windows[i].processedRequests])

        return currentTime, data
