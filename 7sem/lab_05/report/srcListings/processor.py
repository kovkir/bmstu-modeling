from generator import Generator

class Processor(Generator):
    def __init__(self, distribution, maxQueue):
        self.distribution = distribution
        self.maxQueueSize = maxQueue
        self.currentQueueSize  = 0
        self.processedRequests = 0
        self.receivedRequests  = 0
        self.next = 0

    # Обработка запроса при его надичии
    def processRequest(self):
        if self.currentQueueSize > 0:
            self.processedRequests += 1
            self.currentQueueSize  -= 1
    
    # Добавление реквеста в очередь
    def receiveRequest(self):
        if self.maxQueueSize == -1 or self.maxQueueSize > self.currentQueueSize:
            self.currentQueueSize += 1
            self.receivedRequests += 1
            return True
        else:
            return False

    def nextTime(self):
        return self.distribution.generate()
