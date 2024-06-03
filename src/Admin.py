import User

class Admin(User.User):
    def __init__(self, name: str, last_name: str, username: str, password: str, id: str, role: str):
        super().__init__(name, last_name, username, password, id)
        self.role = role
    