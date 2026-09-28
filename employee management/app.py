def task_logger(func):
    def wrapper(*args, **kwargs):
        print("Task execution started")
       
        result = func(*args, **kwargs)
       
        print("Task execution completed")
        return result
   
    return wrapper




class Employee():
   Company_name="TechSolutions"


   def __init__(self,name,employee_id,salary):
      self.name=name
      self.emp_id=employee_id
      if salary <= 0:
         print("Invalid salary! Salary must be greater than 0.")
         self.salary = 0
      else:
         self.salary = salary


   def display_details(self):
      print('Employee Name: ',self.name)
      print('Employee id: ',self.emp_id )
      print('Employee Salary: ',self.salary)
      print('Company_name: ',Employee.Company_name)
   @classmethod
   def change_company_name(cls):
      cls.Company_name="Cognizant"
      # print('Company_name: ',cls.Company_name)
   @staticmethod
   def validate_salary(Employee):
      if Employee.salary>0:
         return True
      else:
         return False




class developer(Employee):
   Programming_language='Python'
   def write_code(self):
      super().__init__(self.name,self.emp_id,self.salary)
      # print('Developer name:',self.name)
      # print('Programming_language:',developer.Programming_language)
      print(f'{self.name} is writing code using {developer.Programming_language}')


class ProjectManager(Employee):
   team_size=10
   @task_logger
   def assign_task(self, taskname):
      if taskname.strip() == "":
         print("Invalid Task Name")
         return


      self.task = taskname
      print("Assigned Task:", self.task)
      print("Team Size:", ProjectManager.team_size)






project=ProjectManager('Manikanta',11,50000)
project.assign_task('build company website')


print()


obj1=Employee('Manikanta',11,50000)
# obj.validate_salary()
obj1.display_details()
print('validate salary:',Employee.validate_salary(obj1))
print()
obj=developer('Manikanta',11,50000)
obj.write_code()


print()


obj2=Employee("Ganesh",12,25000)
obj2.change_company_name()
obj2.display_details()
print('validate salary:',Employee.validate_salary(obj2))
print()


obj=developer('Ganesh',11,50000)
obj.write_code()




developer1=developer("Manikanta",101,60000)
developer2=developer("Harini",102,55000)


manager=ProjectManager("Sruthi",103,95000)




developer1.display_details()
print()
developer2.display_details()
print()
manager.display_details()


developer1.write_code()
developer2.write_code()
print()
manager.assign_task("Company website")


print()


Employee.change_company_name()
developer1.display_details()
print()
developer2.display_details()


print()
manager.display_details()






print('------step1-------')


emp1=developer('Manikanta',101,-5000)
emp1.display_details()


print('-----step2-------')


emp2=developer('Harini',102,50000)
emp2.display_details()


print('-----step3------')


pm=ProjectManager('Sruthi',103,90000)
pm.assign_task("")


print('------step4------')
emp3=developer("Venkat",105,55000)
emp4=developer('Rushi',106,45000)




developer1=developer("Manikanta",101,60000)
developer2=developer("Harini",102,55000)


developer1.display_details()
print()
developer1.write_code()
print()
pm=ProjectManager('Sruthi',103,80000)
pm.assign_task('Webpage design')
print()
developer2.display_details()
print()
developer2.write_code()
print()
pm=ProjectManager('Bhargavi',10,80000)
pm.assign_task('App design')
print()