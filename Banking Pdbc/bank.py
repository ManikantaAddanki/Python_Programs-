
import re
import random

class bank:
    Holder_details = []
    
    def create_Account(self):
        new_user = {}
        
        new_user['Holder_name'] = input('Enter Holder name:')
        
        Mobile = input('Enter Mobile number:')  #  7845613
        
        c = re.fullmatch("[6-9]{1}[0-9]{9}",Mobile)
        
        if c:
            new_user['Mobile'] = Mobile
            new_user['Aadhar_num']  = input('Enter Aadhar Number:')
            new_user['IFSC']  = 'SBI0123'
            new_user['Account_num'] =  random.randint(1000000000,9999999999)
            
            n = input('select type of Account (saving/zero):').lower()
            
            while True:
                if n=='saving':
                    
                    Amount = int(input('your Account is so saving Deposit 1000/---'))
                    if Amount>=1000:
                        new_user['Balance'] = Amount
                        break
                    else:
                        print('----Deposit 1000 /----')
                elif n=='zero':
                    A = int(input('your Account is so zero Deposit 500/---'))
                    if A>=500:
                        new_user['Balance']=A
                        break
                        
                    else:
                          print('----Deposit 500 /----')
                          
            bank.Holder_details.append(new_user)
            print(bank.Holder_details)
            
        else:
            print("----invalid Mobile number------") 
    def desopit(self):
        Acc_nu=int(input('enter your account number:'))
        for i in bank.Holder_details:
            if i['Account_num']== Acc_nu:
                Amount=int(input('enter amount to despoit:'))
                i['Balance']+=Amount
                print('your new balance is:',i['Balance'])
                print(i)
                break
            else:
                print('invalid account number') 
    def withdraw(self):
        k=int(input('enter your account number:'))
        for i in bank.Holder_details:
            if i['Account_num']==k:
                amount=int(input('enter amount to withdraw:'))
                if i['Balance']>=amount:
                    i['Balance']-=amount
                    print('your new balance is:',i['Balance'])
                else:
                    print('insufficient balance')
            else:
                print('invalid account number')
    def check_balance(self):
        Acc_nu=int(input('enter your account number:'))
        for i in bank.Holder_details:
            if i['Account_num']== Acc_nu:
                print("your account balance:",i['Balance']) 
    def details(self):
        Acc_nu=int(input('enter your account number:'))
        for i in bank.Holder_details:
             if i['Account_num']== Acc_nu:
                 for k,v in i.items():
                     print(k,'==>',v)
             else:
                 print("invaild account number")



                    
  
obj = bank()

while True:
    print('''
          1) Create Account
          2) desopit
          3)withdraw
          4)check balance
          5)details''')
    k = int(input('select one option:'))
    if k==1:
        obj.create_Account()
    elif k==2:
        obj.desopit()
    elif k==3:
        obj.withdraw()
    elif k==4:
        obj.check_balance()
    elif k==5:
        obj.details()                 
    else:
        break