from decimal import Decimal


class Cart:
    """A shopping cart. Prices are Decimal so totals never lose cents."""

    def __init__(self):
        self.lines = []

    def add(self, name: str, price: str, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError("quantity must be at least 1")
        self.lines.append((name, Decimal(price), qty))

    def subtotal(self) -> Decimal:
        return sum((price * qty for _, price, qty in self.lines), Decimal("0"))

    def total(self) -> Decimal:
        return self.subtotal()
