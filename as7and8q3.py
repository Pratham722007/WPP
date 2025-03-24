class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc_number, initial_balance=0):
        self.accounts[acc_number] = initial_balance

    def deposit(self, acc_number, amount):
        if acc_number in self.accounts:
            self.accounts[acc_number] += amount

    def withdraw(self, acc_number, amount):
        if acc_number in self.accounts and self.accounts[acc_number] >= amount:
            self.accounts[acc_number] -= amount

    def display_accounts(self):
        for acc_number, balance in self.accounts.items():
            print(f"Account {acc_number}: Balance {balance}")


bank = Bank()
bank.add_account(101, 500)
bank.deposit(101, 200)
bank.withdraw(101, 100)
bank.display_accounts()
