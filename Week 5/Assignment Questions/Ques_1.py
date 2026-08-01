class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(self.name + ": Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        print(self.name, "-", self.account_number, "- NPR", self.balance)


accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000)
]

customers = []

for name, account_number, balance in accounts:
    customers.append(BankAccount(name, account_number, balance))

customers[1].deposit(3000)
customers[2].withdraw(15000)
customers[0].withdraw(2000)

print("\nFinal Account Balances")

for customer in customers:
    customer.get_balance()