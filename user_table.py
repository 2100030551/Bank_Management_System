class UserTable:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    # User login function
    def login(self):
        email = input("Enter your registered email: ")
        self.cursor.execute("SELECT account_no, name FROM users WHERE email = %s", (email,))
        result = self.cursor.fetchone()
        if result:
            print(f"Welcome {result[1]}! Login successful.")
            return result[0]  # Return the account number for further transactions
        else:
            print("Email not found.")
            return None

    # Function to create a new user account
    def create_account(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")

        # Ensure unique email address
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        if self.cursor.fetchone():
            print("Email is already registered. Please use a different email.")
            return None

        balance = float(input("Enter initial balance: "))

        query = "INSERT INTO users (name, email, balance) VALUES (%s, %s, %s)"
        values = (name, email, balance)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"Account created for {name} with initial balance: {balance}")
        return self.login()  # After successful account creation, automatically prompt for login.

    # Function to view balance
    def view_balance(self, account_no):
        self.cursor.execute("SELECT name, balance FROM users WHERE account_no = %s", (account_no,))
        result = self.cursor.fetchone()
        if result:
            print(f"User: {result[0]}, Balance: {result[1]}")
        else:
            print("Account not found.")
