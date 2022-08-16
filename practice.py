class BankAccount:
    def __init__(self, balance,name,number):
        self.name = name
        self.balance = balance
        self.number = number
    def withdraw(self):
        pass
    def deposit(self):
        pass
class SavingAccount:
    def __init__(self,name,number,interest_rate,balance=10500):
        super().__init__(balance,name,number)
        self.interest_rate = interest_rate
    def add_interest(self):
        pass
class CheckingAccount:
    def __init__(self,name,number,withdraw_charge,balance=1890000):
        super().__init__(balance,name,number)
        self.withdraw_charge = withdraw_charge
    def withdraw(self):
        pass
        
