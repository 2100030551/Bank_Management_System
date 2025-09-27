#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user="username",
            password="Yourpassword",
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute("CREATE DATABASE IF NOT EXISTS bank_management_system")
            print("Database created or already exists")

            cursor.execute("SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'bank_user' AND host = 'localhost')")
            user_exists = cursor.fetchone()[0]
            if not user_exists:
                cursor.execute("CREATE USER 'bank_user'@'localhost' IDENTIFIED BY 'bank_password'")
                print("User 'bank_user' created")
            else:
                print("User 'bank_user' already exists")

            cursor.execute("GRANT ALL PRIVILEGES ON bank_management_system.* TO 'bank_user'@'localhost'")
            print("Privileges granted")

            cursor.execute("FLUSH PRIVILEGES")
            print("Privileges flushed")

    except Error as e:
        print(f"Error while setting up database: {e}")
        print("Please make sure MySQL is running and accessible")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")


if __name__ == "__main__":
    print("Setting up MySQL database for Bank Management System...")
    create_database()
    print("Database setup completed!")
