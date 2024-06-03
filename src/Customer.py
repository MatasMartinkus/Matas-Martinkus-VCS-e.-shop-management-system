import User

class Customer(User.User):
    def __init__(self, name: str, last_name: str, username: str, password: str, id: str, _registration_address: str, shipping_address: str, products: dict):
        super().__init__(name, last_name, username, password, id)
        self._registration_address = _registration_address
        self.shipping_address = shipping_address
        self.products = products
    
    def edit_data(self):
        customer_data = super().edit_data()
        customer_data.update({self.id:{"Registration Address": self._registration_address,
                                        "Shipping Address": self.shipping_address,
                                        "Ordered Products": self.products}})
    

        return customer_data