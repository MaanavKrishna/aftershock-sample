from decimal import Decimal


class Cart:
    """A shopping cart. Prices are Decimal so totals never lose cents."""

    CODES = {"WELCOME10": Decimal("0.10"), "SPRING20": Decimal("0.20")}

    def __init__(self):
        self.lines = []
        self.discounts = []
        self.applied_codes = set()

    def add(self, name: str, price: str, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError("quantity must be at least 1")
        self.lines.append((name, Decimal(price), qty))

    def subtotal(self) -> Decimal:
        return sum((price * qty for _, price, qty in self.lines), Decimal("0"))

    def apply_discount(self, code: str) -> None:
        key = code.upper()
        rate = self.CODES.get(key)
        if rate is None:
            raise ValueError(f"unknown discount code {code!r}")
        if key in self.applied_codes:
            return  # a code applies once per cart, however often it is submitted
        self.applied_codes.add(key)
        self.discounts.append(rate)

    def total(self) -> Decimal:
        total = self.subtotal()
        for rate in self.discounts:
            total -= (total * rate).quantize(Decimal("0.01"))
        return total
