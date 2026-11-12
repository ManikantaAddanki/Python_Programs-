#longest substring without repeating characters
s = "abcabcbb"
long = ""

for i in range(len(s)):
    sub = ""
    for j in range(i, len(s)):
        if s[j] in sub:
            sub = s[j]
            break
        sub += s[j]
        if len(sub) > len(long):
            long = sub
print(long)
    
        
#common char b/w two strings

s1 = "programming"
s2 = "python"

res = ""
for char in s1:

    if char in s2 and char not in res:
        res += char
print(res)


#longest palindrome substring

s = "babad"
res = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        if sub == sub[::-1] and len(sub) > len(res):
            res = sub
print(res)


#string is rotation of another string

s1 = "abcd"
s2 = "cdab"

if len(s1) == len(s2) and s2 in s1+s1:
    print("True")
else:
    print("False")