#!/usr/bin/env python3
"""
Database Setup Script for Bank Management System
"""
import mysql.connector
from mysql.connector import Error


def create_database():
    """Create the database and user if they don't exist"""
    try:
        # Connect to MySQL without specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user="username",  # Replace with your MySQL username
            password="Yourpassword",  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS bank_management_system")
            print("Database created or already exists")

            # Create user if it doesn't exist
            try:
                cursor.execute("CREATE USER IF NOT EXISTS 'bank_user'@'localhost' IDENTIFIED BY 'bank_password'")
                print("User created or already exists")
            except Error as e:
                print(f"Note: {e}")

            # Grant privileges
            cursor.execute("GRANT ALL PRIVILEGES ON bank_management_system.* TO 'bank_user'@'localhost'")
            print("Privileges granted")

            # Flush privileges
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