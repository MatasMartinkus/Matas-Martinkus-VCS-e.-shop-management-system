import Customer

class PremiumCustomer(Customer.Customer):
    def __init__(self, name: str, last_name: str, username: str, password: str, id: str, _registration_address: str, shipping_address: str, products: dict, default_discount = 0.1):
        super().__init__(name, last_name, username, password, id, _registration_address, shipping_address, products)
        self.default_discount = default_discount

    def edit_data(self):
        premium_customer_data = super().edit_data()
        premium_customer_data.update({self.id:{"Default discount": self.default_discount}})
        return premium_customer_data