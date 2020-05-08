"""Classes for melon orders."""
class AbstractMelonOrder():
    def __init__(self, species, qty, shipped, order_type, tax, country_code=None):
        self.species = species
        self.qty = qty
        self.shipped = shipped
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty, country_code=None):
        super().__init__(species, qty, False, 'domestic', 0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code=None):
        super().__init__(species, qty, False, 'international', 0.17, country_code=None)
