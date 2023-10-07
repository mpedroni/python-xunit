import xunit
from xunit import TestSuite, TestCase


class Calculator:
    def sum(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


class TestCalculator(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def testSum(self):
        assert self.calculator.sum(2, 3) == 5

    def testMultiplication(self):
        assert self.calculator.multiply(2, 3) == 6

    def testDivision(self):
        assert self.calculator.divide(6, 3) == 2

    def testWrongSum(self):
        assert self.calculator.sum(1, 1) == 3  # false assertion


if __name__ == "__main__":
    suite = TestSuite()

    suite.add(TestCalculator("testSum"))
    suite.add(TestCalculator("testMultiplication"))
    suite.add(TestCalculator("testDivision"))
    suite.add(TestCalculator("testWrongSum"))

    xunit.run(suite)  # output: `4 run, 1 failed`
