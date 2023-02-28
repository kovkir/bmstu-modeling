from processor import Processor

class EventModel:
    def __init__(self, generator, operators, computers):
        self.generator = generator
        self.operators = operators
        self.computers = computers

    def run(self):
        refusals = 0
        processed = 0
        generatedRequests = self.generator.numbRequests
        generator = self.generator

        generator.receivers = self.operators.copy()
        self.operators[0].receivers = [self.computers[0]]
        self.operators[1].receivers = [self.computers[0]]
        self.operators[2].receivers = [self.computers[1]]

        generator.next = generator.nextTime()
        self.operators[0].next = self.operators[0].nextTime()

        blocks = [
            generator, 
            self.operators[0], self.operators[1], self.operators[2],
            self.computers[0], self.computers[1]
        ]

        while generator.numbRequests >= 0:
            # Находим наименьшее время
            currentTime = generator.next
            for block in blocks:
                if 0 < block.next < currentTime:
                    currentTime = block.next

            for block in blocks:
                # Событие наступило для этого блока
                if currentTime == block.next:
                    if not isinstance(block, Processor):
                        # Проверяем, может ли оператор обработать
                        nextGenerator = generator.generateRequest()
                        if nextGenerator is not None:
                            nextGenerator.next = currentTime + nextGenerator.nextTime()
                            processed += 1
                        else:
                            refusals += 1

                        generator.next = currentTime + generator.nextTime()
                    else:
                        block.processRequest()
                        if block.currentQueueSize == 0:
                            block.next = 0
                        else:
                            block.next = currentTime + block.nextTime()

        return [processed, refusals, refusals / generatedRequests * 100]
