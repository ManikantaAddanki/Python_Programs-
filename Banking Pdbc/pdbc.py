import MySQLdb
import random


class PDBC:

    def connection(self):

        return MySQLdb.connect(
            host='localhost',
            user='root',
            password='manikanta@556',
            database='bank_db'
        )

    def create_database(self):

        con = MySQLdb.connect(
            host='localhost',
            user='root',
            password='manikanta@556'
        )

        cur = con.cursor()

        cur.execute("CREATE DATABASE IF NOT EXISTS bank_db")

        con.close()

    def create_table(self):

        con = self.connection()
        cur = con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS bank_accounts(
            id INT AUTO_INCREMENT PRIMARY KEY,
            holder_name VARCHAR(100),
            mobile VARCHAR(10),
            aadhar_num VARCHAR(20),
            ifsc VARCHAR(20),
            account_num BIGINT UNIQUE,
            account_type VARCHAR(20),
            balance DECIMAL(12,2)
        )
        """

        cur.execute(sql)

        con.close()

    def insert_account(self):

        holder_name = input("Enter Holder Name: ")
        mobile = input("Enter Mobile Number: ")
        aadhar = input("Enter Aadhar Number: ")

        account_type = input(
            "Enter Account Type (saving/zero): "
        ).lower()

        if account_type == "saving":

            balance = int(
                input("Enter Initial Deposit (minimum 1000): ")
            )

            while balance < 1000:

                print("Minimum deposit is 1000")

                balance = int(
                    input("Enter Initial Deposit: ")
                )

        elif account_type == "zero":

            balance = int(
                input("Enter Initial Deposit (minimum 500): ")
            )

            while balance < 500:

                print("Minimum deposit is 500")

                balance = int(
                    input("Enter Initial Deposit: ")
                )

        else:

            print("Invalid Account Type")
            return

        account_num = random.randint(
            1000000000,
            9999999999
        )

        con = self.connection()
        cur = con.cursor()

        sql = """
        INSERT INTO bank_accounts
        (holder_name, mobile, aadhar_num, ifsc,
        account_num, account_type, balance)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        cur.execute(
            sql,
            (
                holder_name,
                mobile,
                aadhar,
                "SBI0123",
                account_num,
                account_type,
                balance
            )
        )

        con.commit()
        con.close()

        print("\nAccount Created Successfully")
        print("Account Number:", account_num)
        print("Initial Balance:", balance)

    def deposit(self):

        account_num = int(
            input("Enter Account Number: ")
        )

        con = self.connection()
        cur = con.cursor()

        cur.execute(
            "SELECT balance FROM bank_accounts WHERE account_num=%s",
            (account_num,)
        )

        data = cur.fetchone()

        if data:

            amount = int(
                input("Enter Deposit Amount: ")
            )

            if amount > 0:

                new_balance = data[0] + amount

                cur.execute(
                    """
                    UPDATE bank_accounts
                    SET balance=%s
                    WHERE account_num=%s
                    """,
                    (new_balance, account_num)
                )

                con.commit()

                print("\nDeposit Successful")
                print("Deposited Amount:", amount)
                print("New Balance:", new_balance)

            else:

                print("Amount must be greater than zero")

        else:

            print("Invalid Account Number")

        con.close()

    def withdraw(self):

        account_num = int(
            input("Enter Account Number: ")
        )

        con = self.connection()
        cur = con.cursor()

        cur.execute(
            "SELECT balance FROM bank_accounts WHERE account_num=%s",
            (account_num,)
        )

        data = cur.fetchone()

        if data:

            amount = int(
                input("Enter Withdrawal Amount: ")
            )

            if amount <= 0:

                print("Amount must be greater than zero")

            elif data[0] >= amount:

                new_balance = data[0] - amount

                cur.execute(
                    """
                    UPDATE bank_accounts
                    SET balance=%s
                    WHERE account_num=%s
                    """,
                    (new_balance, account_num)
                )

                con.commit()

                print("\nWithdrawal Successful")
                print("Withdrawn Amount:", amount)
                print("New Balance:", new_balance)

            else:

                print("Insufficient Balance")

        else:

            print("Invalid Account Number")

        con.close()

    def check_balance(self):

        account_num = int(
            input("Enter Account Number: ")
        )

        con = self.connection()
        cur = con.cursor()

        cur.execute(
            """
            SELECT holder_name, balance
            FROM bank_accounts
            WHERE account_num=%s
            """,
            (account_num,)
        )

        data = cur.fetchone()

        if data:

            print("\nHolder Name:", data[0])
            print("Account Balance:", data[1])

        else:

            print("Invalid Account Number")

        con.close()

    def details(self):

        account_num = int(
            input("Enter Account Number: ")
        )

        con = self.connection()
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM bank_accounts WHERE account_num=%s",
            (account_num,)
        )

        data = cur.fetchone()

        if data:

            print("\n----------- ACCOUNT DETAILS -----------")
            print("ID           :", data[0])
            print("Holder Name  :", data[1])
            print("Mobile       :", data[2])
            print("Aadhar       :", data[3])
            print("IFSC         :", data[4])
            print("Account No   :", data[5])
            print("Account Type :", data[6])
            print("Balance      :", data[7])
            print("---------------------------------------")

        else:

            print("Invalid Account Number")

        con.close()

    def display_accounts(self):

        con = self.connection()
        cur = con.cursor()

        cur.execute("SELECT * FROM bank_accounts")

        data = cur.fetchall()

        print("\n----------- ALL ACCOUNTS -----------")

        for i in data:

            print("ID           :", i[0])
            print("Holder Name  :", i[1])
            print("Mobile       :", i[2])
            print("Aadhar       :", i[3])
            print("IFSC         :", i[4])
            print("Account No   :", i[5])
            print("Account Type :", i[6])
            print("Balance      :", i[7])
            print("-----------------------------------")

        con.close()


obj = PDBC()

obj.create_database()
obj.create_table()

while True:

    print("""
    ========== BANK MENU ==========

    1. Create Account
    2. Deposit
    3. Withdraw
    4. Check Balance
    5. Account Details
    6. Display All Accounts
    7. Exit

    ===============================
    """)

    choice = int(input("Enter your choice: "))

    if choice == 1:

        obj.insert_account()

    elif choice == 2:

        obj.deposit()

    elif choice == 3:

        obj.withdraw()

    elif choice == 4:

        obj.check_balance()

    elif choice == 5:

        obj.details()

    elif choice == 6:

        obj.display_accounts()

    elif choice == 7:

        print("Thank You")
        break

    else:

        print("Invalid Choice")