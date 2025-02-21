import csv
import sqlite3
import streamlit
from datetime import datetime

balance = 12000 # Starting balance

# Create a connection to a SQLite database
conn = sqlite3.connect("personalfinance.db")
cursor = conn.cursor()


# Import transactions from a csv file that has 7 columns. Only import columns 0, 1, 3, 5, 6
transactions = []
with open("chasetransactions.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the first row

    for row in reader:
        # Format the date in column 0 to YYYY-MM-DD
        date = datetime.strptime(row[0], "%m/%d/%Y").strftime("%Y-%m-%d")
        transaction = (date, row[2], row[3], row[5])
        transactions.append(transaction)
        cursor.execute('''
        INSERT INTO chasetransactions (date, description, category, amount)
        VALUES (?, ?, ?, ?)
        ''', transaction)


# Fetch all transactions ordered by date
cursor.execute("SELECT id, date, amount FROM chasetransactions ORDER BY id desc;")
transactions = cursor.fetchall()

# Update each transaction with the running balance
for balances in transactions:
    id, date, amount = balances
    
        # Debug: Print balance and id
    print(f"Updating balance for id {id}: {balance}")

    cursor.execute("UPDATE chasetransactions SET balance = ? WHERE id = ?", (balance, id))
    balance += amount

# Commit the changes to the database
conn.commit()

# Fetch the transactions from the database
cursor.execute('SELECT * FROM chasetransactions')
fetched_transactions = cursor.fetchall()

# Close the connection to the database
conn.close()

