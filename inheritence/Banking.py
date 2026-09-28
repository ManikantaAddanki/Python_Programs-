import regex
import random


class bank:

    Holder_details = []

    def create_Account(self):

        new_user = {}

        new_user['Holder_name'] = input('Enter Holder name: ')

        Mobile = input('Enter Mobile number: ')

        c = regex.fullmatch("[6-9]{1}[0-9]{9}", Mobile)

        if c:

            new_user['Mobile'] = Mobile

            new_user['Aadhar_num'] = input('Enter Aadhar Number: ')

            new_user['IFSC'] = 'SBI0123'

            new_user['Account_num'] = random.randint(
                1000000000, 9999999999
            )

            n = input(
                'Select type of Account (saving/zero): '
            ).lower()

            while True:

                if n == 'saving':

                    Amount = int(input(
                        'Your account is Saving. Deposit 1000 or more: '
                    ))

                    if Amount >= 1000:

                        new_user['Balance'] = Amount

                        break

                    else:

                        print('---- Deposit 1000 or more ----')

                elif n == 'zero':

                    A = int(input(
                        'Your account is Zero Deposit. Deposit 500 or more: '
                    ))

                    if A >= 500:

                        new_user['Balance'] = A

                        break

                    else:

                        print('---- Deposit 500 or more ----')

                else:

                    print('---- Invalid Account Type ----')

                    n = input(
                        'Select type of Account (saving/zero): '
                    ).lower()

            bank.Holder_details.append(new_user)

            print("\nAccount Created Successfully")
            print("Account Number:", new_user['Account_num'])
            print("IFSC:", new_user['IFSC'])
            print("Balance:", new_user['Balance'])

        else:

            print("---- Invalid Mobile Number ------")

    def deposit(self):

        acc = int(input("Enter Account Number: "))

        for user in bank.Holder_details:

            if user['Account_num'] == acc:

                amount = int(input("Enter Deposit Amount: "))

                if amount > 0:

                    user['Balance'] += amount

                    print("\nAmount Deposited Successfully")
                    print("Deposited Amount:", amount)
                    print("Updated Balance:", user['Balance'])

                else:

                    print("---- Enter Valid Amount ----")

                break

        else:

            print("---- Account Not Found ----")


    def withdraw(self):

        acc = int(input("Enter Account Number: "))

        for user in bank.Holder_details:

            if user['Account_num'] == acc:

                amount = int(input("Enter Withdrawal Amount: "))

                if amount <= 0:

                    print("---- Enter Valid Amount ----")

                elif amount <= user['Balance']:

                    user['Balance'] -= amount

                    print("\nAmount Withdrawn Successfully")
                    print("Withdrawn Amount:", amount)
                    print("Updated Balance:", user['Balance'])

                else:

                    print("---- Insufficient Balance ----")

                break

        else:

            print("---- Account Not Found ----")


obj = bank()


while True:

    print('''
    
          1) Create Account
          2) Deposit
          3) Withdraw
          
          ''')

    k = int(input('Select one option: '))

    if k == 1:

        obj.create_Account()

    elif k == 2:

        obj.deposit()

    elif k == 3:

        obj.withdraw()

    elif k == 4:

        print("Thank You")
        break

    else:

        print("---- Invalid Option ----")