n = [10, -5, 20, 8, -2, 15, 3, -9, 12]
positive = 0
negative = 0
for x in n:
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1

print("Positive numbers count:", positive)
print("Negative numbers count:", negative)