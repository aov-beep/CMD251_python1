import pyodbc
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Define connection parameters
server = os.getenv('SERVER')
database = os.getenv('DATABASE')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

print("Attempting to connect to the database...")

# Create the connection string
# For Windows Authentication, use: Trusted_Connection=yes;
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Establish connection
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        print("Connection successful!")
        # Execute a query
        cursor.execute("SELECT TOP 10 * FROM Users")

        # Fetch results
        for row in cursor.fetchall():
            print(row)

except Exception as e:
    print(f"Error: {e}")
