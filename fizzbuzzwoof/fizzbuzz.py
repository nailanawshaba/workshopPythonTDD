class FizzBuzz(object):
    def __init__(self):
        self.rules = {3: 'fizz', 5: 'buzz', 7: 'woof'}

    def generate(self, number):
        output = ''
        for key, value in self.rules.iteritems():
            if number % key == 0:
                output += value

        if output:
            return output
        else:
            return number

    def setter(self, rules):
        self.rules = rules
