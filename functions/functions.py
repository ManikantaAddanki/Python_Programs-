#Arguments
'''
def student_details(name, age, id, *skills, location="Hyderabad", **marks):
    print(f"Name: {name}, Age: {age}, ID: {id}, Location: {location}")
student_details("Manikanta",22, 102, "Python", "Java", "SQL", Python=90, Java=85, SQL=88)
'''

#even odd
def even_odd(m):
    if m % 2 == 0:
        return "Even"
    else:
        return "Odd"

res = even_odd(18)
print(res)

