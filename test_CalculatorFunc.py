"""
Unit tests for the calculator library
"""
# Import the main Scientific Calculator File
import CalculatorFunc as SciCalc

class TestCalculator:

    def test_sqrt(self):
        assert 14.0 == SciCalc.square_root(196)
        assert 0.0 == SciCalc.square_root(0)
        assert -9.0 == SciCalc.square_root(-9)
        assert  1 == SciCalc.square_root(1)
        assert 1.7320508075688772 == SciCalc.square_root(3)
        
    def test_factorial(self):
        assert 5040 == SciCalc.factorial(7)
        assert 120 == SciCalc.factorial(5)
        assert 1 == SciCalc.factorial(0)
        assert 1 == SciCalc.factorial(1)
        assert 0.0 == SciCalc.factorial(-5)
        assert 0.0 == SciCalc.factorial(-5.5)
        assert 6 == SciCalc.factorial(5.5)
        
    def test_log(self):
    	assert 0 == SciCalc.log(0)
    	assert 0 == SciCalc.log(-1)
    	assert 0 == SciCalc.log(-10)
    	assert 1.0 == SciCalc.log(2.718281828459045)
    	assert 2.995732273553991 == SciCalc.log(20)
    	
    def test_power(self):
    	assert 512 == SciCalc.power(2,9)
    	assert 0 == SciCalc.power(0, 12)
    	assert 1 == SciCalc.power(20, 0)
    	assert 20.0 == SciCalc.power(20, 1)
    	assert 8.0 == SciCalc.power(2, 3)
    	assert -8.0 == SciCalc.power(-2,3)
    	assert 0.125 == SciCalc.power(2,-3)
    	assert -0.125 == SciCalc.power(-2, -3)
    	assert 16.0 == SciCalc.power(-2, 4)
    	assert 1.0 == SciCalc.power(1, 23)
