class User:
    def __init__(self, email = "", password = "", firstName = "", lastName = ""):
        self.firstname = firstName
        self.surname = lastName
        self.email = email
        self.password = password
        self.limit = 50000

    def set_firstname(self, firstname: str):
        self.firstname = firstname
    
    def set_surname(self, surname: str):
        self.surname = surname

    def set_email(self, email: str):
        self.email = email

    def set_password(self, password: str):
        self.password = password

    def set_limit(self, limit: int):
        self.limit = limit

    def get_firstname(self) -> str:
        return self.firstname

    def get_surname(self) -> str:
        return self.surname

    def get_email(self) -> str:
        return self.email

    def get_password(self) -> str:
        return self.password

    def get_limit(self) -> int:
        return self.limit

