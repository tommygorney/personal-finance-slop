import sqlite3
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st. set_page_config(layout="wide")

# Create a connection to a SQLite database
conn = sqlite3.connect("personalfinance.db")
cursor = conn.cursor()

# Select all transactions from the database and display them in a table
cursor.execute("select strftime('%Y-%m', date) AS 'Date', sum(CASE WHEN amount < 0 THEN Amount ELSE 0 END) AS 'Spending', sum(CASE WHEN amount > 0 THEN Amount ELSE 0 END) AS 'Income', ROUND(sum(Amount), 2) as 'Balance' from sftransactions group by strftime('%Y-%m', date);")
transactions = cursor.fetchall()
df = pd.DataFrame(transactions, columns=["Date", "Spending", "Income", "Balance"])
# st.dataframe(df.style.highlight_max(axis=0))
st.write(df)


# Display a line with the balance over time
# cursor.execute("SELECT date, balance FROM sftransactions where Date > '2024-1-1'")
# transactions = cursor.fetchall()
# chart_data = pd.DataFrame(transactions, columns=["Date", "Balance"])
# st.line_chart(chart_data.set_index("Date"))

cursor.execute("select strftime('%Y-%m', date) AS 'Date', ROUND(sum(Amount), 2) as 'Spending' from sftransactions group by strftime('%Y-%m', date);")
transactions = cursor.fetchall()
# Create DataFrame
df = pd.DataFrame(transactions, columns=["Date", "Spending"])
# Create Plotly bar chart
fig = px.bar(df, x='Date', y='Spending', color='Spending', color_continuous_scale=['red', 'green'], color_continuous_midpoint=0)
# Display the chart in Streamlit
st.plotly_chart(fig)



# Close the connection to the database
conn.close()

