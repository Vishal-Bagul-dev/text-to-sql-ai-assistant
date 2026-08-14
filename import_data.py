import mysql.connector
import csv
from dotenv import load_dotenv
import os

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = connection.cursor()

cursor.execute("DELETE FROM employees")
connection.commit()
print("Old data cleared!")

# CSV file ka path yaha daalo
csv_file_path = r"C:\Hr Attrition Project Power Bi +sql\hr_attrition_full_raw_data.csv"

with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # pehli row (column names) skip karo
    print("Columns found:", header)

    rows = list(csv_reader)
    print(f"Total rows to import: {len(rows)}")

    placeholders = ", ".join(["%s"] * len(header))
    columns = ", ".join(header)
    insert_query = f"INSERT INTO employees ({columns}) VALUES ({placeholders})"

    cursor.executemany(insert_query, rows)
    connection.commit()

    print(f"Successfully imported {cursor.rowcount} rows!")

cursor.close()
connection.close()