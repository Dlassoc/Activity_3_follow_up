class Bank:
    def __init__(self, number_account: str, propietary: str, balance: float):
        self.number_account: str = number_account
        self.propietary = propietary
        self.balance: float = balance

    def deposit(self, cant: float):
        self.balance += cant

    def retire(self, cant: float):
        if self.balance >= cant:
            self.balance -= cant

    def cuot(self):
        self.balance = self.balance - (self.balance * 0.02)

    def show_details(self):
        print("Los detalles de la cuenta de numero", self.number_account, "son:")
        print(self.balance)
        print (self.propietary)

