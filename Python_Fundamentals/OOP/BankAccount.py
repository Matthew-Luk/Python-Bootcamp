class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = (self.balance - 5)
        else:
            self.balance = (self.balance - amount)
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

account1 = BankAccount(0.05, 500)
account2 = BankAccount(0.03, 1000)
account1.deposit(50).deposit(70).deposit(30).withdraw(20).yield_interest().display_account_info()
account2.deposit(100).deposit(75).withdraw(10).withdraw(200).withdraw(50).withdraw(25).yield_interest().display_account_info()

BankAccount.print_accounts()