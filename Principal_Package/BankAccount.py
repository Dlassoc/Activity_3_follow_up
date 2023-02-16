class Bank:
    def __init__(self, number_account: str, propietary: str, balance: float):
        self.number_account: str = number_account
        self.propietary = propietary
        self.balance: float = balance

    def deposit(self, cant: float):
        self.balance += cant