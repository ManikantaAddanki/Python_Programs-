" "

'csv'

# with open('emp.csv','w',newline="") as k:
#     pass



# n = open('std.csv','w',newline="")

# writer

import csv

# with open('std.csv','w',newline="") as n:
#     s = csv.writer(n)
#     s.writerow(['c1','c2','c3'])
    
#     s.writerow([10,20,30])
#     s.writerow([100,200,300])



# import csv

# n = open('emp.csv','w',newline="")

# s = csv.writer(n)         #  

# s.writerow(['Employee_id','Employee_name','join_date','department','salary'])

# m = [[101,'kumar','12/2/2023','sales',25000],
#      [102,'mohan','23/10/2025','hr',35000],
#      [103,'hari','20/10/2022','it',45000]]

# s.writerows(m)



" "
# import csv

# with open('emp.csv','w',newline="")as n:
#     s = csv.DictWriter(n,fieldnames=['pin','name'])
#     s.writeheader()
    
#     s.writerow({'pin':101,'name':'kumar'})



" "


# import csv
# import logging


# class employee:
    
#     def __init__(self):
#         logging.basicConfig(filename="employee.log",
#                             filemode='a',
#                             level=logging.INFO,
#                             format="%(asctime)s / %(levelname)s / %(message)s")
    
#     def create_employee(self):
#         with open('emp.csv','a',newline="") as n:
#             s = csv.DictWriter(n,fieldnames=['emp_id','emp_name','salary'])
            
#             s.writeheader()
            
#             h = int(input('Enter no/of employee:'))  # 3
            
#             a = 1
#             while a<=h:
#                 d = {}
#                 d['emp_id'] = int(input('Enter employee id:'))
#                 d['emp_name'] = input('Enter employee name:')
#                 d['salary'] = int(input('Enter employee salary:'))
                
#                 s.writerow(d)
                
#                 logging.info(f"{a} records created successful employee id = {d['emp_id']}")
                
#                 a+=1
                
                
                
# obj = employee()
# obj.create_employee()
                
                
                
"r"

# import csv

# with open('emp.csv','r') as n:
#     d = list(csv.reader(n))   #  [[],[],[]]
    
#     l = []
#     for x in d[1:]:
#         if x[0] == '101':
#             x[1]='saikumar'
#             l.append(x)
#         else:
#             l.append(x)
#     print(l)
    
#     t = open('emp.csv','w',newline="")
    
#     w = csv.writer(t)
#     w.writerow(d[0])
#     w.writerows(l)
   
    
                
            
            
" "


import csv

with open('emp.csv','r') as n:
    d = list(csv.reader(n))   #  [[],[],[]]
    
    l = []
    for x in d[1:]:
        if x[0] == '102':
            continue
        else:
            l.append(x)
    print(l)
    
    t = open('emp.csv','w',newline="")
    
    w = csv.writer(t)
    w.writerow(d[0])
    w.writerows(l)