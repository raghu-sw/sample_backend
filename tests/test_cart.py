import unittest
from src.cart import Cart
import pytest

def add1(x):
    return x + 1

def test_add1():
    assert 3 != 4
    assert 5 == 5
   
@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_add_expression_with_params(test_input, expected):
    assert eval(test_input) == expected

class TestAdd1(unittest.TestCase):
    def test_add1(self):
        self.assertNotEqual(4,5)
        self.assertNotEqual(add1(2),4)

class CartTest(unittest.TestCase):

    def test_empty(self):
        c = Cart()
        assert c.cost() == 0.0

