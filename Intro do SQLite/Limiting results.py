import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()


# Execute Query
c.execute(
    'SELECT rowid, * FROM customers LIMIT 2'
)

items = c.fetchall()

for item in items:
    print(item)

# Close our connection
conn.close()
