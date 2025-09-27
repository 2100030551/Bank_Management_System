import mysql.connector


class TransactionTable:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    # Deposit function
    def deposit(self, account_no):
        amount = float(input("Enter deposit amount: "))
        self.cursor.execute("UPDATE users SET balance = balance + %s WHERE account_no = %s", (amount, account_no))
        self.connection.commit()
        print(f"Deposited {amount}. New balance: {self.get_balance(account_no)}")

    # Withdraw function
    def withdraw(self, account_no):
        amount = float(input("Enter withdrawal amount: "))
        balance = self.get_balance(account_no)
        if amount > balance:
            print("Insufficient balance.")
        else:
            self.cursor.execute("UPDATE users SET balance = balance - %s WHERE account_no = %s", (amount, account_no))
            self.connection.commit()
            print(f"Withdrawn {amount}. New balance: {self.get_balance(account_no)}")

    # Function to get balance (helper function for deposit/withdraw)
    def get_balance(self, account_no):
        self.cursor.execute("SELECT balance FROM users WHERE account_no = %s", (account_no,))
        result = self.cursor.fetchone()
        return result[0] if result else 0

    # View transaction history (you need to implement this feature)
    def view_transactions(self, account_no):
        self.cursor.execute("SELECT txn_id, txn_type, amount, txn_date FROM transactions WHERE account_no = %s",
                            (account_no,))
        transactions = self.cursor.fetchall()
        if transactions:
            for txn in transactions:
                print(f"ID: {txn[0]}, Type: {txn[1]}, Amount: {txn[2]}, Date: {txn[3]}")
        else:
            print("No transactions found.")

    # Fund transfer between two accounts
    def transfer(self, account_no):
        to_account = int(input("Enter recipient account number: "))
        amount = float(input("Enter transfer amount: "))

        balance = self.get_balance(account_no)
        if amount > balance:
            print("Insufficient balance.")
            return

        # Deduct from sender's account
        self.cursor.execute("UPDATE users SET balance = balance - %s WHERE account_no = %s", (amount, account_no))
        # Add to recipient's account
        self.cursor.execute("UPDATE users SET balance = balance + %s WHERE account_no = %s", (amount, to_account))

        # Log transaction
        self.cursor.execute("INSERT INTO transactions (account_no, txn_type, amount) VALUES (%s, 'TRANSFER', %s)",
                            (account_no, amount))
        self.cursor.execute("INSERT INTO transactions (account_no, txn_type, amount) VALUES (%s, 'TRANSFER', %s)",
                            (to_account, amount))

        self.connection.commit()

        print(f"Transferred {amount} to account {to_account}. New balance: {self.get_balance(account_no)}")
