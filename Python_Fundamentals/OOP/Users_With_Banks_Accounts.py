class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance=0): 
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
        self.balance = (self.balance - amount)
        return self

    def display_account_info(self):
        return(f"Balance: ${self.balance}, Interest Rate: {self.int_rate * 100}%")

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
            "checking" : BankAccount(0.02, 100),
            "savings" : BankAccount(0.05, 500)
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Account Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Account Balance: {self.account['savings'].display_account_info()}")
        return self

    def make_deposit(self,amount,account_name):
        self.account[f"{account_name}"].deposit(amount)
        return self

    def make_withdrawal(self,amount,account_name):
        self.account[f"{account_name}"].withdraw(amount)
        return self

    #I set the default for money transfer to be checking to checking account, but we can do savings if we add the parameter.
    def transfer_money(self,amount,other_user,account_1="checking",account_2="checking"):
        self.account[f"{account_1}"].withdraw(amount)
        other_user.account[f"{account_2}"].deposit(amount)
        return self

user1 = User("Matthew")
user2 = User("Abby")

user1.transfer_money(50,user2,"savings","savings")

user1.display_user_balance()
user2.display_user_balance()