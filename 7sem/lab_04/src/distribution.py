from numpy import log as ln
from random import random


class EvenDistribution:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def generate(self):
        return self.a + (self.b - self.a) * random()


class ErlangDistribution:
    def __init__(self, k: int, l: float):
        self.k = k
        self.l = l

    def generate(self):
        return 1 / (self.k * self.l) * \
            sum([ln(1 - random()) for _ in range(self.k)])
