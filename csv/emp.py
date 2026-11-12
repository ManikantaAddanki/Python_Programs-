
import csv

n = int(input("Enter how many records: "))

with open("employee.csv", 'w', newline="") as f:
    w = csv.writer(f)
    w.writerow(['id', 'name', 'salary', 'dept'])

    for i in range(n):
        print("Enter employee", i + 1)

        emp_id = int(input("Enter Emp id: "))
        emp_name = input("Enter Emp name: ")
        emp_salary = int(input("Enter Emp salary: "))
        emp_dept = input("Enter Emp dept: ")

        w.writerow([emp_id, emp_name, emp_salary, emp_dept])

print("Employee records stored successfully")


#dict reader is used read the data from csv file in dictionary format
#dict writer is used to write the data in csv file in dictionary format