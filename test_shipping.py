import pytest

from shipping import shipping_fee


# Rule 1 is broken because a weight of 0 kg is accepted.
@pytest.mark.parametrize("weight_kg", [0, -0.1])
def test_rule_1_nonpositive_weight_is_rejected(weight_kg):
    with pytest.raises(ValueError):
        shipping_fee(weight_kg)


# Rule 2 is broken because exactly 1 kg costs 60 baht instead of 40.
@pytest.mark.parametrize(
    ("weight_kg", "expected_fee"),
    [(0.01, 40), (0.99, 40), (1, 40)],
)
def test_rule_2_shipping_fee(weight_kg, expected_fee):
    assert shipping_fee(weight_kg) == expected_fee


# Rule 3 is covered at both edges: just above 1 kg and exactly 5 kg.
@pytest.mark.parametrize(
    ("weight_kg", "expected_fee"),
    [(1.01, 60), (4.99, 60), (5, 60)],
)
def test_rule_3_shipping_fee(weight_kg, expected_fee):
    assert shipping_fee(weight_kg) == expected_fee


# Rule 4 is broken because the code truncates started kilograms instead of rounding them up.
@pytest.mark.parametrize(
    ("weight_kg", "expected_fee"),
    [(5.2, 70), (6, 70), (6.01, 80)],
)
def test_rule_4_shipping_fee(weight_kg, expected_fee):
    assert shipping_fee(weight_kg) == expected_fee