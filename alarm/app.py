from datetime import datetime, timedelta
import os

from gtts import gTTS
today_date_time = datetime.now()
print(today_date_time)
print("-----------------")
today_date = today_date_time.date()
print(today_date)
print()
print(today_date.year)
print()
print(today_date.month)
print()
print(today_date.day)
print("=================")

current_time = today_date_time.time()
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


'''
%H == 24-hour format
%M == Minute
%S == Second
%I == 12-hour format
%B == Month name
%Y == Year
%d == day
%p == AM/PM
'''

'''
from datetime import datetime
d = datetime.now().date()

after_5 = d + timedelta(days=5)
print(after_5)
'''


'''
from datetime import datetime, timedelta

t = datetime.now()
a = t + timedelta(hours = 3)
time12 = a.strftime("%I:%M:%S %p")
print(time12)
'''

'''
from datetime import datetime, timedelta

n = "11:00 AM"

t = datetime.strptime(n, "%I:%M %p").strftime("%H:%M")
print(t)
'''

''' 
from datetime import datetime, timedelta

n = "18:00"

t = datetime.strptime(n, "%H:%M").strftime("%I:%M %p")
print(t)
'''


"Alarm"

from datetime import datetime
from gtts import gTTS
import os

Alarm_time = "12:15"

T = datetime.strptime(Alarm_time, "%H:%M").time()
print("Alarm Time =", T)
while True:
    current_time = datetime.now().time()
    if T==current_time:
        n = "hey babuu levvuu melluko legichi nilabadu lekapothee boss tokkestaduu"
        s = gTTS(text=n)
        s.save("Alarm.mp3")
        for x in range(5):
            os.startfile("Alarm.mp3")
        break