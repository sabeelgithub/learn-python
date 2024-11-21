########################### ENCAPSILATION ####################################

class BankAccount:
    def __init__(self,name,account_number,balance):
        self.name = name
        self._account_number = account_number
        self.__balance = balance

    
    def __balance_info_offical(self):
        return print(f"balance of {self.name}: {self.__balance}")

    def add_money(self,amount):
        self.__balance += amount
        return print(f"Hi {self.name}, Amount {amount} Credited To Your Bank Account {self._account_number}")
    
    def money_withdraw(self,amount):
        if self.__balance < amount:
            return print("Insufficient Balance")
        else:
            self.__balance -= amount
            return print(f"Hi {self.name}, Amount {amount} Is Debited From Your Bank Account {self._account_number}")

    def bank_balance(self):
        return print(f"Balance is : {self.__balance}")


ac1 = BankAccount("Sabeel",999,2000)
print(ac1.name,ac1._account_number)
ac1.bank_balance()
ac1.add_money(1000)
ac1.bank_balance()
ac1.money_withdraw(500)
ac1.bank_balance()

########################### END ENCAPSILATION ####################################