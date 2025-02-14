class Customer:
    """A sample customer class"""

    discount = 0.95

    def __init__(self, first_name, last_name, purchase):
        self.first = first_name
        self.last = last_name
        self.purchase = purchase

    @property
    def customer_mail(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def customer_fullname(self):
        return f'{self.first} {self.last}'

    def apply_discount(self):
        self.purchase = int(self.purchase * self.discount)

