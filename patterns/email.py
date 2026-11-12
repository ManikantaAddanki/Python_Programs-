import re
s = "Regular expression manikanta@gmail.com expression is a sequence 123ine of charchter123 that forms a venkat08@gmail.com pattern123. viswaraj_232@gmail.com it praveen27@gmail.in is an sruthi05_@gmail.com, bhargavi2288@gmail.in harini2924@gmail.com"

res = re.findall(r"\w+@gmail\.com|\w+@gmail\.in", s)
print(res)