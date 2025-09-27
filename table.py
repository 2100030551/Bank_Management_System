class UserTable:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    # Function to create a new user account
    def create_account(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        balance = float(input("Enter initial balance: "))

        query = "INSERT INTO users (name, email, phone, balance) VALUES (%s, %s, %s, %s)"
        values = (name, email, phone, balance)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"Account created for {name} with initial balance: {balance}")

    # Function to view balance
    def view_balance(self):
        user_id = int(input("Enter your user ID: "))
        query = "SELECT name, balance FROM users WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        if result:
            print(f"User: {result[0]}, Balance: {result[1]}")
        else:
            print("User not found.")
