import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    
    assert calculator.fun4 (-1, -1, 100) == 98

def test_fun5():
    # Basic division tests
    assert calculator.fun5(6, 2) == 3.0
    assert calculator.fun5(10, 4) == 2.5
    assert calculator.fun5(-8, 2) == -4.0
    assert calculator.fun5(8, -2) == -4.0
    assert calculator.fun5(-8, -2) == 4.0
    assert calculator.fun5(0, 5) == 0.0
    
    # Test division by zero raises exception
    with pytest.raises(ZeroDivisionError):
        calculator.fun5(5, 0)
    
    # Test invalid input types
    with pytest.raises(ValueError):
        calculator.fun5("5", 2)
    with pytest.raises(ValueError):
        calculator.fun5(5, "2")

def test_fun6():
    # Basic power tests
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 2) == 25
    assert calculator.fun6(3, 0) == 1
    assert calculator.fun6(4, 0.5) == 2.0
    assert calculator.fun6(-2, 3) == -8
    assert calculator.fun6(-2, 2) == 4
    assert calculator.fun6(10, -1) == 0.1
    
    # Test invalid input types
    with pytest.raises(ValueError):
        calculator.fun6("2", 3)
    with pytest.raises(ValueError):
        calculator.fun6(2, "3")

def test_fun7():
    # Basic modulo tests
    assert calculator.fun7(10, 3) == 1
    assert calculator.fun7(15, 4) == 3
    assert calculator.fun7(20, 5) == 0
    assert calculator.fun7(-7, 3) == 2
    assert calculator.fun7(7, -3) == -2
    assert calculator.fun7(-7, -3) == -1
    
    # Test modulo by zero raises exception
    with pytest.raises(ZeroDivisionError):
        calculator.fun7(10, 0)
    
    # Test invalid input types
    with pytest.raises(ValueError):
        calculator.fun7("10", 3)
    with pytest.raises(ValueError):
        calculator.fun7(10, "3")

def test_fun8():
    # Basic absolute value tests
    assert calculator.fun8(5) == 5
    assert calculator.fun8(-5) == 5
    assert calculator.fun8(0) == 0
    assert calculator.fun8(3.14) == 3.14
    assert calculator.fun8(-3.14) == 3.14
    assert calculator.fun8(-100) == 100
    
    # Test invalid input types
    with pytest.raises(ValueError):
        calculator.fun8("5")
    with pytest.raises(ValueError):
        calculator.fun8([5])

def test_fun9():
    # Basic square root tests
    assert calculator.fun9(4) == 2.0
    assert calculator.fun9(9) == 3.0
    assert calculator.fun9(16) == 4.0
    assert calculator.fun9(0) == 0.0
    assert calculator.fun9(1) == 1.0
    assert calculator.fun9(2) == pytest.approx(1.414, abs=1e-3)
    assert calculator.fun9(0.25) == 0.5
    
    # Test negative number raises exception
    with pytest.raises(ValueError):
        calculator.fun9(-4)
    with pytest.raises(ValueError):
        calculator.fun9(-1)
    
    # Test invalid input types
    with pytest.raises(ValueError):
        calculator.fun9("4")
    with pytest.raises(ValueError):
        calculator.fun9([4])
