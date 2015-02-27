import unittest
from fizzbuzzwoof.fizzbuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_returns_1_for_1(self):
        self.assertEqual(self.fb(1), 1)

    def test_returns_2_for_2(self):
        self.assertEqual(self.fb(2), 2)

    def test_returns_fizz_for_3(self):
        self.assertEqual(self.fb(3), 'fizz')

    def test_returns_buzz_for_5(self):
        self.assertEqual(self.fb(5), 'buzz')

    def test_returns_fizz_for_6(self):
        self.assertEqual(self.fb(6), 'fizz')

    def test_returns_woof_for_7(self):
        self.assertEqual(self.fb(7), 'woof')

    def test_returns_fizz_for_9(self):
        self.assertEqual(self.fb(9), 'fizz')

    def test_returns_buzz_for_10(self):
        self.assertEqual(self.fb(10), 'buzz')

    def test_returns_woof_for_14(self):
        self.assertEqual(self.fb(14), 'woof')

    def test_returns_fizzbuzz_for_15(self):
        self.assertEqual(self.fb(15), 'fizzbuzz')

    def test_returns_fizzbuzzwoof_for_105(self):
        self.assertEqual(self.fb(105), 'fizzbuzzwoof')

    def test_it_takes_in_rules(self):
        set_rules = {3: 'ass',
                     5: 'hole'}
        fb = FizzBuzz()
        fb.setter(set_rules)
        self.assertEqual(fb.generate(3), 'ass')
        self.assertEqual(fb.generate(5), 'hole')

    def fb(self, number):
        result = FizzBuzz().generate(number)
        return result


if __name__ == '__main__':
    unittest.main()
