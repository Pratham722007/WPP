class BankAccount:
    def __init__(self, acc_num, balance=0):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def display(self):
        print(f"Account {self.acc_num}: Balance {self.balance}")

acc = BankAccount(12345, 1000)
acc.deposit(500)
acc.withdraw(200)
acc.display()
