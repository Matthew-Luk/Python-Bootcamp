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
        return(f"{self.balance}")

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(0.02, 1000),
            "savings" : BankAccount(0.05, 5000)
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

matthew = User("Matthew")

matthew.account["savings"].deposit(1000)
matthew.account["checking"].deposit(50)
matthew.display_user_balance()