import csv
import sqlite3
import streamlit
from datetime import datetime

# Create a connection to a SQLite database
conn = sqlite3.connect("personalfinance.db")
cursor = conn.cursor()

# Import transactions from a csv file that has 7 columns. Only import columns 0, 1, 3, 5, 6
transactions = []
with open("cititransactions.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the first row

    for row in reader:
        # Format the date in column 0 to YYYY-MM-DD
        date = datetime.strptime(row[1], "%m/%d/%Y").strftime("%Y-%m-%d")
        category = ''
        amount = row[3] if row[3] else row[4]
        transaction = (date, row[2], category, amount)
        transactions.append(transaction)
        cursor.execute('''
        INSERT INTO cititransactions (date, description, category, amount)
        VALUES (?, ?, ?, ?)
        ''', transaction)

# Commit the changes to the database
conn.commit()

# Fetch the transactions from the database
cursor.execute('SELECT * FROM cititransactions')
fetched_transactions = cursor.fetchall()

# Close the connection to the database
conn.close()

