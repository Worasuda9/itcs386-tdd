"""
    ☐ 200 g + 300 g = 500 g
    ☐ 200 g + 1 oz, reduced to grams, using a conversion rate
    ☐ (200 g + 1 oz) × 2
    ☐ defining __eq__ without __hash__ makes instances unhashable
"""

# test_kitchen.py
from kitchen import Quantity, grams, ounces, Converter

def test_multiplication():
    flour = grams(200)
    assert flour.times(3).amount == 600
    
def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400
    
def test_equality():
    flour = grams(200)
    assert flour.times(3) == grams(600)

def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)
    
def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)
    
def test_reduce_same_unit_needs_no_rate():
    converter = Converter()
    assert converter.reduce(grams(500), "g") == grams(500)
    
def test_mixed_addition():
    converter = Converter()
    converter.add_rate("oz", "g", 28)
    total = grams(200).plus(ounces(1))
    assert converter.reduce(total, "g") == grams(228)