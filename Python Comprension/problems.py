# l = [1, 2, 3, 4, 5]
# print(l)


#with out using list comprehension
# n = [0,2,4,6,8,10]
# temp = []
# for x in range(10):
#     if x % 2 == 0:
#         temp.append(x)
# print(temp)


# #using list comprehension
# n = [x for x in range(10) if x % 2 == 0]
# print(n)


# #without using list comprehension
# n = 10  #[1,2,5]
# temp = []
# for x in range(1,n):
#     if n % x == 0:
#         temp.append(x)
# print(temp)


# # with using list comprehension
# n = 17
# res =[x for x in range(1,n) if n % x == 0]
# if len(res) == 1:
#     print("prime number")
# else:
#     print("not prime number")
# print(res)


#without using list comprehension
#[(1,1),(2,4),(3,9),(4,16),]
# n = 5
# temp = []
# for x in range(1,n):
#     temp.append((x,x**2))
# print(temp)

# #with using list comprehension
# res = [(x,x**2) for x in range(1,n)]
# print(res)


# n = [10,2.3,"python",2+3j,18]   #[10,18]
# n = [10,2.3,"python",2+3j,18]
# temp = []
# for x in n:
#     if type(x) == int:
#         temp.append(x)
# print(temp)


# #with using list comprehension
# res = [x for x in n if type(x) == int]
# print(res)


#without using list comprehension
n = ["apple","banana","kiwi","mango"]
temp = []
for x in n:
    if len(x) > 4:
        temp.append(x)
print(temp)


#with using list comprehension
res = [x for x in n if len(x) > 4]
print(res)


