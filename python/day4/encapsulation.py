class bank:
    def __init__(self,balance):
        self.__balance=balance

    


    def add(self,amount):
        return self.__balance+amount
    

    def rem(self,amount):

        if self.__balance<amount:
            return f"insuffiefcnt"
        else:
            return self.__balance-amount
        

obj1 = bank(5000)
print(obj1.rem(300))
print(obj1.rem(7000))
print(obj1.add(1000))
