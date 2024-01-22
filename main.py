class BankAccount:
    default = 1

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.default
        BankAccount.default = BankAccount.default + 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough money left !")
        else:
            self.balance -= amount

    def show_balance(self):
        return self.balance


if __name__ == "__main__":
    Marian = BankAccount("Marian", 2500)
    print(f"Initial money in account: {Marian.__dict__}")

    Marian.deposit(5000)
    print(f"After deposit: {Marian.__dict__}")

    Marian.withdraw(3000)
    print(f"After withdraw: {Marian.__dict__}")

    Florin = BankAccount("Florin", 1000)

    print(Florin.__dict__)


