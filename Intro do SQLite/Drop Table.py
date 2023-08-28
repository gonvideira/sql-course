import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Drop table
c.execute('DROP TABLE customers')
conn.commit()

# Execute Query
c.execute(
    'SELECT rowid, * FROM customers'
)

items = c.fetchall()

for item in items:
    print(item)

# Close our connection
conn.close()
