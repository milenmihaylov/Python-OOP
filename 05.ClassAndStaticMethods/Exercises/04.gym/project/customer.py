class Customer:
    __cust_id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    @classmethod
    def get_next_id(cls):
        cls.__cust_id += 1
        return cls.__cust_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
