n = 12385868
count = 0

while n:
    d = n % 10
    if d == 8:
        count += 1
    n //= 10
print(count)