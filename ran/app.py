#import random
#print(random.randint(188, 1818))

'''
import random
for i in range(5):
    s = random.randint(18888, 28999)
    print(s)
'''


'''
import random
for i in range(5):
    phone = random.randint(6000000000, 9000000000)
    print(phone)
'''


'''
import random
while True:
    n = int(input("Enter the number:"))
    guess_a_number = random.randint(1,5)

    if n == guess_a_number:
        print("You guessed the number")
        break
'''


''''
import random
p1_score = 0
p2_score = 0
while True:
    n = (input("Enter player one 0:"))
    print()
    if n == '0':
       s = random.randint(10, 18)
       p1_score += s
       print("player 1 score =", p1_score)
       print()
       print("----------------")
       if p1_score >= 20:
           print("player 1 wins")
           break

       p2 = input("Enter player two 0:")
       if p2 == '0':
          s2 = random.randint(10, 18)
          p2_score += s2
          print("player 2 score =", p2_score)
          print()
          print("----------------")
          if p2_score >= 20:
              print("player 2 wins")
              break
'''


'''
import random

n = random.randint(10, 20)
print(n)
'''

'''
pyttsx3 ==> pip install pyttsx3
'''

''''
import pyttsx3
temp = pyttsx3.init()
voices = temp.getProperty('voices')
temp.setProperty('voice', voices[1].id)
temp.setProperty('rate', 120)
text ="my name is kurramayya my favorite player also peddi sir"
temp.say(text)
temp.runAndWait()
'''


'''
import time
import pyttsx3

tem=pyttsx3.init()
tem.setProperty('rate', 120)

voices=tem.getProperty('voices')
tem.setProperty('voice',voices[1].id)

std=['mani','mahesh', 'kohli', 'sachin']

for i in std:
    tem.say(i)
    tem.runAndWait()
    time.sleep(5)
'''


import time
import pyttsx3

std=['mani','mahesh', 'kohli', 'sachin']
tem=pyttsx3.init()
voices=tem.getProperty('voices')
tem.setProperty('voice',voices[1].id)
tem.setProperty('rate',100)
d={}
for i in std:
    tem.say(i)
    time.sleep(2)
    tem.runAndWait()
    n=input("enter attendence:")
    if n=='present':
        d[i]=n
    else:
        d[i]='absent'
print(d)
