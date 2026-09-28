n = [18, 10, 29, 18, 17, 333]
odd_count = 0
even_count = 0
for x in n:
    if x%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)