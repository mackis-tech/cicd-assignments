import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.calculator import add, subtract, multiply, divide

def test_add(): 
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(1000000, 2000000) == 3000000

def test_subtract():    
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(1000000, 2000000) == -1000000
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
    assert multiply(-1, -1) == 1
    assert multiply(1000000, 2000000) == 2000000000000

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(0, 5) == 0
    assert divide(-1, -1) == 1
    assert divide(1000000, 2000000) == 0.5
    with pytest.raises(ValueError):
        divide(5, 0)