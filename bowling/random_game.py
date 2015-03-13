from random import randrange
from BowlingGame import BowlingGame


if __name__ == '__main__':
    bg = BowlingGame()

    # letting a random game play itself, just cause :)
    for frame in range(10):
        roll1 = randrange(0, 11)
        bg.roll(roll1)
        print 'Frame #{}: {}'.format(frame + 1, roll1)
        if roll1 == 10:  # strike
            if frame == 9:  # the 10th frame
                roll2 = randrange(0, 11)
                bg.roll(roll2)
                print 'Frame #{}: {}'.format(frame + 1, roll2)
                if roll2 == 10:  # another strike so roll 3 has 10 pins up
                    roll3 = randrange(0, 11)
                else:
                    roll3 = randrange(0, 10 - roll2)
                bg.roll(roll3)
                print 'Frame #{}: {}'.format(frame + 1, roll3)
            else:
                continue
        else:
            roll2 = randrange(0, 10 - roll1)
            print 'Frame #{}: {}'.format(frame + 1, roll2)
            bg.roll(roll2)
    print 'Final Score: {}'.format(bg.score())