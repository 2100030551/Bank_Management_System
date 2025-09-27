import mysql.connector
from menu import display_menu
from user_table import UserTable
from transaction_table import TransactionTable

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="username",
        password="Yourpassword",
        database="Your databasename"
    )
    return connection

def main():
    connection = create_connection()
    user_table = UserTable(connection)
    transaction_table = TransactionTable(connection)

    account_no = None
    while True:
        print("Welcome to the Bank Management System!")
        print("1. Login")
        print("2. Register")
        print("0. Exit")

        choice = input("Please choose an option (1, 2, or 0 to exit): ")

        if choice == '1':
            account_no = user_table.login()
            if account_no:
                print("Login successful!")
                break
            else:
                print("Email not found. Please try again or register.")

        elif choice == '2':
            user_table.create_account()
            print("Registration successful! Please log in.")
            account_no = user_table.login()
            if account_no:
                print("Login successful!")
                break

        elif choice == '0':
            print("Exiting the system. Goodbye!")
            connection.close()
            return

        else:
            print("Invalid choice. Please try again.")

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            user_table.create_account()
        elif choice == '2':
            user_table.view_balance(account_no)
        elif choice == '3':
            transaction_table.deposit(account_no)
        elif choice == '4':
            transaction_table.withdraw(account_no)
        elif choice == '5':
            transaction_table.view_transactions(account_no)
        elif choice == '6':
            transaction_table.transfer(account_no)
        elif choice == '7':
            print("Exiting system.")
            connection.close()
            break
        elif choice == '0':
            print("Exiting system.")
            connection.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
