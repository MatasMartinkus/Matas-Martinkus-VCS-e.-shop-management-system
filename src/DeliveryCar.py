import Warehouse

class DeliveryCar(Warehouse.Warehouse):
    def __init__(self, id: str, location: str, products: list, max_volume: int, warehousing_fee: float, primary_category: str, secondary_category: str) -> None:
        super().__init__(id, location, products, max_volume, warehousing_fee, primary_category, secondary_category)