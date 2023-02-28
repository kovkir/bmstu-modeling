from math import exp, factorial

class Distribution:
    def uniformDistribution(self, a: float, b: float, x: float):
        if x < a:
            return 0
        elif x > b:
            return 1
        else:
            return (x - a) / (b - a)

    def uniformDistributionDensity(self, a: float, b: float, x: float):
        if a <= x <= b:
            return 1 / (b - a)
        else:
            return 0

    def erlangDistribution(self, k: int, l: float, x: float):
        return 1 - exp((-1) * l * x) * sum([pow(l * x, i) / factorial(i) for i in range(k)])

    def erlangDistributionDensity(self, k: int, l: float, x: float):
        return exp((-1) * l * x) * l * pow(l * x, k - 1) / factorial(k - 1)
