class Product:
    def __init__(self, product_id: str, product_name: str, product_options: dict, price: float, stock: int, dimensions: tuple, category: str, tags: list):
        self.product_id = product_id
        self.product_name = product_name
        self.product_options = product_options
        self.price = price
        self.stock = stock
        self.dimensions = dimensions
        self.category = category
        self.tags = tags
    
    def calculate_volume(self):
        volume = 1
        for dimension in self.dimensions:
            volume *= dimension
        return volume
    
    def get_data(self):
        product_data = {self.id:{"Product Name": self.product_name,
                                 "Product Options": self.product_options,
                                 "Price": self.price,
                                 "Stock": self.stock,
                                 "Dimensions": self.dimensions,
                                 "Category": self.category,
                                 "Tags": self.tags,
                                 "Volume": self.calculate_volume()}}
        return product_data