from abc import ABC, abstractmethod

class sra(ABC):
    @abstractmethod
    def new_employee(self):
        pass

    @abstractmethod
    def details(self):
        pass


class sub(sra):
    pass


class ATM(ABC):
    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class sbi(ATM):
    def deposit(self, Acc_num, Balance):
        print('-----sbi deposit----')
        self.balance = 5000

        if Acc_num == '123':
            self.balance += Balance
        else:
            print('---invalid Account number-----')

    def check_balance(self, Acc_num):
        if Acc_num == '123':
            print(self.balance)

    def method(self):
        print('----instance method----')


obj = sbi()
obj.deposit('123', 2000)
obj.check_balance('123')
obj.method()