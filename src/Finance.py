import Admin

class Finance(Admin.Admin):
    def __init__(self, name: str, last_name: str, username: str, password: str, id: str, role: str, orders_completed: list):
        super().__init__(name, last_name, username, password, id, role)
        self.orders_completed = orders_completed
    
## NEEDS ORDERS_COMPLETED TO CREATE GET DATA FUNCTION