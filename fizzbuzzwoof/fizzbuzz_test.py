import unittest
from fizzbuzzwoof.fizzbuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fb = FizzBuzz()

    def test_returns_1_for_1(self):
        self.assertEqual(self.fb.generate(1), 1)

    def test_returns_2_for_2(self):
        self.assertEqual(self.fb.generate(2), 2)

    def test_returns_fizz_for_3(self):
        self.assertEqual(self.fb.generate(3), 'fizz')

    def test_returns_buzz_for_5(self):
        self.assertEqual(self.fb.generate(5), 'buzz')

    def test_returns_fizz_for_6(self):
        self.assertEqual(self.fb.generate(6), 'fizz')

    def test_returns_woof_for_7(self):
        self.assertEqual(self.fb.generate(7), 'woof')

    def test_returns_fizz_for_9(self):
        self.assertEqual(self.fb.generate(9), 'fizz')

    def test_returns_buzz_for_10(self):
        self.assertEqual(self.fb.generate(10), 'buzz')

    def test_returns_woof_for_14(self):
        self.assertEqual(self.fb.generate(14), 'woof')

    def test_returns_fizzbuzz_for_15(self):
        self.assertEqual(self.fb.generate(15), 'fizzbuzz')

    def test_returns_fizzbuzzwoof_for_105(self):
        self.assertEqual(self.fb.generate(105), 'fizzbuzzwoof')

    def test_it_takes_in_rules(self):
        # ass hole, because all of the sudden the tester throws a curve ball
        set_rules = {3: 'ass',
                     5: 'hole'}
        self.fb.set_rules(set_rules)
        self.assertEqual(self.fb.generate(3), 'ass')
        self.assertEqual(self.fb.generate(5), 'hole')


if __name__ == '__main__':
    unittest.main()
