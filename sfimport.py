import csv
import sqlite3
import streamlit
from datetime import datetime

# Create a connection to a SQLite database
conn = sqlite3.connect("personalfinance.db")
cursor = conn.cursor()

# Import transactions from a csv file that has 7 columns. Only import columns 0, 1, 3, 5, 6
transactions = []
with open("sftransactions.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the first row

    for row in reader:
        # Format the date in column 0 to YYYY-MM-DD
        date = datetime.strptime(row[0], "%m/%d/%Y").strftime("%Y-%m-%d")
        transaction = (date, row[1], row[3], row[5], row[6])
        transactions.append(transaction)
        cursor.execute('''
        INSERT INTO sftransactions (date, description, category, amount, balance)
        VALUES (?, ?, ?, ?, ?)
        ''', transaction)

# Commit the changes to the database
conn.commit()

# Fetch the transactions from the database
cursor.execute('SELECT * FROM sftransactions')
fetched_transactions = cursor.fetchall()

# Close the connection to the database
conn.close()

