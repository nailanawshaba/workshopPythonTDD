class PrimeFactorizer(object):
    def __init__(self, number):
        self.number = number

    def generate(self):
        factors = []
        candidate = 2

        while candidate < self.number:
            while self.number % candidate == 0:
                factors.append(candidate)
                self.number /= candidate
            candidate += 1

        if self.number > 1:
            factors.append(self.number)

        return factors
