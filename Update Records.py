import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# update
c.execute(
    """
    UPDATE customers SET first_name = "The"
    WHERE rowid = 6
"""
)

conn.commit()

# Execute Query
c.execute(
    'SELECT * FROM customers'
)

items = c.fetchall()

for item in items:
    print(item)

# Close our connection
conn.close()
