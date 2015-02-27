import unittest
from primefactorization.prime import PrimeFactorizer

class TestPrimeFactorizer(unittest.TestCase):
    def setUp(self):
        pass

    def test_3_for_3(self):
        result = PrimeFactorizer().generate(3)
        self.assertEqual(result, [3])

    def test_2_7_for_14(self):
        result = PrimeFactorizer().generate(14)
        self.assertEqual(result, [2, 7])

    def test_3_3_3607_3803_for_123456789(self):
        result = PrimeFactorizer().generate(123456789)
        self.assertEqual(result, [3, 3, 3607, 3803])


if __name__ == '__main__':
    unittest.main()
