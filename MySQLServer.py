import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (without specifying a database)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ganjafarma@1'  
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Try creating the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error:
            print("Error while creating database:", e)
        finally:
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

except Error as e:
    print("Failed to connect to MySQL server:", e)
