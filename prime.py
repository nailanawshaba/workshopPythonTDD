class PrimeFactorizer(object):
    def __init__(self):
        pass

    def generate(self, number):
        factors = []
        candidate = 2

        while candidate < number:
            while number % candidate == 0:
                factors.append(candidate)
                number /= candidate
            candidate += 1

        if number > 1:
            factors.append(number)

        return factors
