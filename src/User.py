class User:
    def __init__(self, name: str, last_name: str, username: str, password: str, id: str):
        self.name = name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.id = id

    def edit_data(self):
        user_data = {self.id:{"Name": self.name,
                             "Last name": self.last_name,
                             "Username": self.username,
                             "Password": self.password,
                             "ID": self.id,
                             }}
        return user_data