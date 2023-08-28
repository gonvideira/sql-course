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
c.execute(
    'SELECT * FROM customers'
)

items = c.fetchall()

print('NAME' + '\t' + 'EMAIL:\n')
for item in items:
    print(item[1] + ', ' + item[0] + '\t' + item[2])

# Close our connection
conn.close()
