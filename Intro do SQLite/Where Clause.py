import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()


# Execute Query
c.execute(
    'SELECT * FROM customers WHERE last_name LIKE "Sm%"'
)

items = c.fetchall()

for item in items:
    print(item)

# Close our connection
conn.close()
