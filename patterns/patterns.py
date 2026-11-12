# import re

# def Registration():
#     global user_name
#     user_name = input('Enter user name:')
#     email = input('Enter email:')
    
#     c = re.fullmatch(r"[A-Za-z0-9_.]+@gmail.com",email)
    
#     if c:
#         password = input('Enter Password:')
#         n = re.fullmatch(r"^[A-Z][a-z]{6}\d$",password)
#         if n:
#             print('-----Registartion successful---')

#         else:
#             print('-----invalid password ^[A-Z][a-z]{6}\d$')
            
#     else:
#         print('----invalid email-----')
            
    
    
# def login():
#     l_username = input('Enter username:')
#     l_password = input('Enter password:')    
    


# def call(a):
#     a()
    
    
# call(Registration)

# def login():
#     l_username = input('Enter username:')
#     l_password = input('Enter password:')
#     if user_name == l_username and l_password == password:
#         print('Login successful')
#     else:
#         print('Invalid username or password')

# def call(a):
#     a()

# call(Registration)
# call(login)




def prime(func):
    def check(a, b):
        print("Prime numbers:")
        for i in range(a, b):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    print(i)
        print("-----------------------------------------")
        func(a, b)
    return check

@prime
def even(func):
    def display(a, b):
        print("Even numbers:")
        for i in range(a, b):
            if i % 2 == 0:
                print(i)


even(10, 20)