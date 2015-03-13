class BowlingGame(object):
    def __init__(self):
        self.pins_toppled = 0
        self.rolls = []

    def roll(self, pins_toppled):
        self.pins_toppled += pins_toppled
        self.rolls.append(pins_toppled)

    def score(self):
        roll = 0
        score = 0
        for frame in range(0, 10):
            if self.is_strike(roll):
                score += 10 + self.rolls[roll + 1] + self.rolls[roll + 2]
                roll += 1
            elif self.is_spare(roll):
                score += 10 + self.rolls[roll + 2]
                roll += 2
            else:
                score += self.rolls[roll] + self.rolls[roll + 1]
                roll += 2
        return score

    def is_spare(self, roll):
        return self.rolls[roll] + self.rolls[roll + 1] == 10

    def is_strike(self, roll):
        return self.rolls[roll] == 10
