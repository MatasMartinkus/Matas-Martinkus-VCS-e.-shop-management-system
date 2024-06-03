class Warehouse:
    def __init__(self, id: str, location: str, products: list, max_volume: int, fee: float, primary_category: str, secondary_category: str):
        self.id = id
        self.location = location
        self.products = products
        self.max_volume = max_volume
        self.fee = fee
        self.primary_category = primary_category
        self.secondary_category = secondary_category
    
    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
        else:
            return f"Product already in warehouse"
        
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            return f"Product not in warehouse"
    
    def edit_product_stock(self, product, quantity):
        if product in self.products:
            product.stock += quantity
        else:
            return f"Product not in warehouse"
    
    def calculate_fee(self, product):
        if product.category == self.primary_category:
            self.fee = 0.5
        elif product.category == self.secondary_category:
            self.fee = 1
        else:
            self.fee = 2.5

    def check_if_enough_storage(self, product):
        volume = 0
        for product in self.products:
            volume += product.calculate_volume()
        return volume
    
    def get_data(self):
        warehouse_data = {self.id:{"Location": self.location,
                                   "Products": self.products,
                                   "Maximum Volume": self.max_volume,
                                   "Shipping Fee": self.fee,
                                   "Primary Category": self.primary_category,
                                   "Secondary Category": self.secondary_category}}
        return warehouse_data


