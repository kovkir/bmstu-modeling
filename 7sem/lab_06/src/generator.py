class Generator:
    def __init__(self, distribution, countClients):
        self.distribution = distribution
        self.receivers = []
        self.numbRequests = countClients
        self.next = 0 

    def nextTime(self):
        return self.distribution.generate()

    def generateRequest(self):
        self.numbRequests -= 1
        receiverMin = self.receivers[0]

        for receiver in self.receivers:
            if receiver.currentQueueSize < receiverMin.currentQueueSize: 
                receiverMin = receiver

        receiverMin.receiveRequest()
        return receiverMin

    def setReceivers(self, receivers):
        self.receivers = receivers
