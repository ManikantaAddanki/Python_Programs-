n = 123
res=""
while n>0:
    d=n%10
    res=str(d**2)+res
    n=n//10
print(int(res))