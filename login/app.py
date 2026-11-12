
import re

class login:
    def __init__(self):
        try:
            user_name = input("Enter your username: ")
            c = re.fullmatch(user_name,"manikanta29") 
            if c:
                password = input("Enter your password: ")
                d = re.fullmatch(password,"Manikanta@556") 
                if d:
                    print("Login successful")
                else:
                    print("Invalid password")

            else:
                print("Invalid username")
        except Exception as e:
            print("e[]")

obj = login()