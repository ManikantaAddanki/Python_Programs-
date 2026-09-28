class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance     # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


obj = BankAccount("Manikanta", 10000)

obj.deposit(5000)
obj.withdraw(2000)

print("Balance:", obj.get_balance())