"""
    ☐ 1 oz is not the same as 1 g
    ☐ 200 g + 300 g = 500 g
    ☐ 200 g + 1 oz, reduced to grams, using a conversion rate
    ☐ (200 g + 1 oz) × 2
    ☐ defining __eq__ without __hash__ makes instances unhashable
"""

# test_kitchen.py
from kitchen import Quantity

def test_multiplication():
    flour = Quantity(200, "g")
    assert flour.times(3).amount == 600
    
def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200, "g")
    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400
    
def test_equality():
    flour = Quantity(200, "g")
    assert flour.times(3) == Quantity(600, "g")

def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")