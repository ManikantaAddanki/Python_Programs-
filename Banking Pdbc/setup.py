from pdbc import PDBC

obj = PDBC()

obj.create_database()
obj.create_table()

print("Database and table created successfully")