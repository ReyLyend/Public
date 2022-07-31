import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 0.1, 100) == 10

    def test_exception_ZeroDivision_raised(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 5, 0)

    def test_subtraction_correct(self):
        assert self.calc.subtraction(self, 100,1000) == -900

    def test_adding_correct(self):
        assert self.calc.adding(self, 100, 100) == 200