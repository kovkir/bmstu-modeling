from generator import Generator

class Processor(Generator):
    def __init__(self, distribution):
        self.distribution = distribution
        self.maxQueueSize = 0
        self.currentQueueSize  = 0
        self.processedRequests = 0
        self.receivedRequests  = 0
        self.next = 0
        self.receivers = []

    # Обработка запроса при его наличии
    def processRequest(self):
        if self.currentQueueSize > 0:
            self.processedRequests += 1
            self.currentQueueSize  -= 1

        if len(self.receivers) != 0:
            receiverMin = self.receivers[0]

            for receiver in self.receivers:
                if receiver.currentQueueSize < receiverMin.currentQueueSize: 
                    receiverMin = receiver

            receiverMin.receiveRequest()
            receiverMin.next = self.next + receiverMin.nextTime()
    
    # Добавление реквеста в очередь
    def receiveRequest(self):
        self.currentQueueSize += 1
        self.receivedRequests += 1

        if self.maxQueueSize < self.currentQueueSize:
            self.maxQueueSize = self.currentQueueSize

    def nextTime(self):
        return self.distribution.generate()

    def setReceivers(self, receivers):
        self.receivers = receivers
