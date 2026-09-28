a = 18
b = 45
c = input("Enter an operator (+, -, *, %, /): ")

if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '%':
    print(a%b)
elif c == '/':
    print(a/b)
else:
    print("Invalid operator")

