import sqlite3
import os

# Get the current working directory
project_folder = os.getcwd()
# Define the path where the SQLite database file will be stored
db_path = os.path.join(project_folder, 'tablicakalorija.db')

# SQLite Connection Setup
def create_database():
    try:
        # Connect to SQLite database (it will be created if it doesn't exist)
        conn = sqlite3.connect(db_path)

        cursor = conn.cursor()

        # Create table SQL query (correct data types for SQLite)
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS tablicakalorija (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       namirnica TEXT,
                       proteini REAL,
                       ugljenihidrati REAL,
                       masti REAL
                       )''')
        print("Table 'tablicakalorija' created successfully.")

        # Commit the changes to the database
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

    except sqlite3.Error as err:
        print(f"SQLite error: {err}")
    else:
        print("Database and table setup successful!")

# Call the function
create_database()
