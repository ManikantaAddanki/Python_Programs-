s = "aaabbc"
temp = {}
for x in s:
    if x in temp:
        temp[x] += 1
    else:
        temp[x] = 1
print(temp)     


n = 1233