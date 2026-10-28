from decimal import Decimal

from shop.cart import Cart


def test_subtotal_adds_lines():
    cart = Cart()
    cart.add("mug", "12.50", 2)
    cart.add("tea", "4.00")
    assert cart.subtotal() == Decimal("29.00")


def test_rejects_zero_quantity():
    cart = Cart()
    try:
        cart.add("mug", "12.50", 0)
    except ValueError:
        return
    raise AssertionError("expected ValueError")
