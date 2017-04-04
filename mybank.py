class Account :
    def __init__(self, name, balance, min_balance) :
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposite(self, amount) :
        self.balance += amount

    def withdraw(self, amount) :
        if self.balance - amount >= self.min_balance :
            self.balance = self.balance - amount
        else :
            print("Not enough funds in {}'s account".format(self.name))

    def statement(self) :
        print("{}'s {} Account has {} Rs.".format(self.name, self.get_type(), self.balance))

    def get_type(self) :
        return ""

    def __str__(self) :
        return "{}'s {} Account with {} Rs.".format(self.name, self.get_type(), self.balance)
            

class Current_Account(Account) :
    def __init__(self, name, balance) :
        super().__init__(name, balance, -10000)

    def get_type(self) :
        return "Current"

class Saving_Account(Account) :
    def __init__(self, name, balance) :
        super().__init__(name, balance, 0)

    def get_type(self) :
        return "Saving"


hdfc_account = Saving_Account("Nilesh", 100)
print(hdfc_account)

hdfc_account.deposite(200)
print(hdfc_account)

hdfc_account.withdraw(150)
print(hdfc_account)

hdfc_account.withdraw(300)

citi_account = Current_Account("Injulkar", 3000)
print(citi_account)

citi_account.statement()

citi_account.withdraw(400)
print(citi_account)

citi_account.deposite(9400)
print(citi_account)

citi_account.withdraw(15000)
citi_account.statement()

citi_account.withdraw(8000)
print(citi_account)


