n = 25
len = len(str(n))
m = n**2
if n == m % (10 ** len):
    print("The number is an Automorphic number.")
else:
    print("The number is not an Automorphic number.")