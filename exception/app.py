import MySQLdb
class PDBC:
    def __init__(self):
        try:
            con = MySQLdb.connect(host='localhost', user='root', password='Manikanta@556')
            sql = "CREATE DATABASE pdbc_102"

            cursor = con.cursor()
            cursor.execute(sql)
            con.close()
                
        except MySQLdb.Error as e:
            print(f"Error creating database: {e}")
        