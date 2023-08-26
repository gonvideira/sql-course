import sqlite3

# Connect to a database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

many_items = [
    ('Christoph', 'Smith', 'chris@gmail.com'),
    ('Robert', 'Simons', 'robert@gmail.com'),
    ('The Giant', 'Rock', 'therock@gmail.com')
]

# Insert one record
c.executemany(
    """
    INSERT INTO customers VALUES (?, ?,?)
    """,
    many_items
)

# Commit our command to the database
conn.commit()

# Close our connection
conn.close()
