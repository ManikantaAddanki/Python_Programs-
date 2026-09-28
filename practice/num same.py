n = 8888
last = n % 10
same = True
while n >= 10:
    n //= 10
    if n % 10 != last:
        same = False
        break
print(same)