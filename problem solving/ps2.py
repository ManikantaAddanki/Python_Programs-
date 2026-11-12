# list = [1,2,3,4,5,6]
# dict = {1:'odd', 2:'even', 3:'odd', 4:'even', 5:'odd', 6:'even'}

l = [1,2,3,4,5,6]
dict = {}
for i in l:
    if i % 2 == 0:
        dict[i] = 'even'
    else:
        dict[i] = 'odd'
print(dict)


#list = [2,4,6,4,7,1,5,2]
#target = 8

l = [2,4,6,4,7,1,5,2]
target = 8
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] + l[j] == target:
            print((l[i], l[j]))


#list = [23,14,18,2,13,9,5,4]
#even index num sum = 23+18+13+5 =

list = [23,14,18,2,13,9,5,4]
temp = 0
for x in range(len(list)):
    if x % 2 == 0:
        temp += list[x]
print(temp)


#n = 234556
#first digit and last digit sum

n = 23456
m = n%10
while n >=10:
    n=n//10
r = n
sum = m + r
print(sum)