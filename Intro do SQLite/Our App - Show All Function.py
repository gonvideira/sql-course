from Database import CustomerDatabase

connection = CustomerDatabase()

# connection.add_record("Louis", "Franklin", "louiiii@mail.com")
# connection.delete_record('8')

list_records = [
    ('Brenda', 'Jenkings', 'brenda@smith.com'),
    ('Joshua', 'Raintree', 'josh@rain.com')

]
connection.add_many(list_records)

connection.email_lookup('brenda@smith.com')

# connection.show_all()

connection.close_connection()
