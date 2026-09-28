salary = float(input("Enter your salary: "))
if salary < 250000:
    tax = 0
elif salary < 500000:
    tax = (salary - 250000) * 5 / 100
elif salary < 1000000:
    tax = (salary - 250000) * 7 / 100 
else:
    tax = (salary - 250000) * 10 / 100
print("Tax to be paid :", tax)