class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawl(self, amount):
        self.balance -= amount
    def display_user_balance(self):
        print(self.balance)


class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
    def display_account_info(self):
        print("Balance: $", self.balance)
    def yield_interest(self):
        if self.balance >= 0:
            self.balance += int(self.balance * self.int_rate)

acct1 = BankAccount(.05, 100)
acct2 = BankAccount(.03, 100)

exampleUser1 = User("Sam", "sam@gmail.com")