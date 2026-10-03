import MySQLdb

# Create Database
connection = MySQLdb.connect(
    user="root",
    host="localhost",
    password="manikanta@556"
)

c = connection.cursor()

sql = "CREATE DATABASE IF NOT EXISTS pdbc_102"
c.execute(sql)

connection.close()


# Create Table
connection = MySQLdb.connect(
    user="root",
    host="localhost",
    database="pdbc_102",
    password="manikanta@556"
)

c = connection.cursor()

sql = """
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    emp_id INT,
    emp_name VARCHAR(30),
    emp_salary FLOAT,
    join_date DATE DEFAULT (CURRENT_DATE)
)
"""

c.execute(sql)

connection.close()



import MySQLdb


class PDBC:
    def __init__(self):
        connection = MySQLdb.connect(user = 'root',
                              host = 'localhost',
                              database = 'pdbc_102',
                              password = 'manikanta@556')
        
        for x in range(4):
            eid = int(input('Enter Employee id:'))
            emp_name = input('Enter Employee name:')
            emp_salary = int(input('Enter salary'))
            j_date = input('Enter Date:')
            
            sql = f"insert into employee values({eid},'{emp_name}',{emp_salary},'{j_date}')"
            
            cursor = connection.cursor()
            
            cursor.execute(sql)
            connection.commit()
            
            
        connection.close()
        
obj = PDBC()