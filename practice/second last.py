n = 12345
temp = n
count = 0

while temp >= 10:
    temp //= 10
    count += 1

second = (n // (10 ** (count - 1))) % 10
second_last = (n // 10) % 10

print(second + second_last)