import pytest
from app.calculator import Calculator
class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding_succes(self):
        assert self.calculator.adding(self, 1, 1) == 2

    def test_subtraction(self):
        assert self.calculator.subtraction(self, 4, 1) == 3

    def test_division(self):
        assert self.calculator.division(self, 8, 2) == 4

    def test_multiply(self):
        assert self.calculator.multiply(self, 5, 3) == 15


    def teardown(self):
        print('Выполнение метода teardown')
