# Coding Task:
class Account:
    def __init__(self,acc_num,balance):
        self.acc_num = acc_num
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("Deposited: ",amount)
    def display_balance(self):
        print("Balance: ",self.balance)
class SavingsAccount(Account):
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw: ",amount)
        else:
            print("Insufficient balance")
account = SavingsAccount("SA101",10000)
account.deposit(2000)
account.withdraw(3000)
account.display_balance()

# Assignment:
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def display_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings withdrawal:", amount)
        else:
            print("Insufficient balance")


class CurrentAccount(Account):
    def withdraw(self, amount):
        minimum_balance = 1000

        if self.balance - amount >= minimum_balance:
            self.balance -= amount
            print("Current account withdrawal:", amount)
        else:
            print("Withdrawal denied. Minimum balance of 1000 must be maintained.")


savings = SavingsAccount("SA101", 10000)
current = CurrentAccount("CA101", 10000)

savings.withdraw(9000)
current.withdraw(9500)

savings.display_balance()
current.display_balance()