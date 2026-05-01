class bank:
    def __init__(self,balance):
        self.balance=balance
       

    def deposit(self,amount):
        return self.balance+amount
    

    def withdraw(self,amount):
        return self.balance-amount
    
b = bank(10000)

print(b.deposit(500))

print(b.withdraw(500))


