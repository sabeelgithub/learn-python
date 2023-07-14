########################### ENCAPSILATION ####################################
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # protected attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


# Creating an instance of BankAccount
account = BankAccount("1234567890", 1000)

# Accessing protected attribute (conventionally considered protected)
print("Account Number:", account.get_account_number())

# Accessing private attribute (name mangling is applied)
# This will result in an AttributeError
# print("Balance:", account.__balance)

# Depositing and withdrawing money
account.deposit(500)
account.withdraw(200)

# Accessing balance through a getter method
print("Balance:", account.get_balance())


########################### END ENCAPSILATION ####################################