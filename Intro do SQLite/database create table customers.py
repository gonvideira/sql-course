import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute(
    """CREATE TABLE customers (
    first_name text,
    last_name text, 
    email_address text
    )
"""
)

# Commit our command to the database
conn.commit()

# Close our connection
conn.close()

# Datatypes: 
# NULL
# INTEGER
# REAL
# TEXT
# BLOB
