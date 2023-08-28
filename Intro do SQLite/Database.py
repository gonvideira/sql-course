import sqlite3

class CustomerDatabase():
    """Database class"""
    # Connect to a database
    conn = sqlite3.connect('customer.db')
    # Create a cursor
    cursor = conn.cursor()

    def show_all(self):
        """Function to show all"""

        # Query the database
        self.cursor.execute(
            'SELECT rowid, * FROM customers ORDER BY first_name DESC'
        )
        items = self.cursor.fetchall()
        for item in items:
            print(item)


    def add_record(self, first_name, last_name, email_address):
        """Function to add a record to the table"""
        # Insert one record
        self.cursor.execute(
            "INSERT INTO customers VALUES (?, ?,?)",
            (first_name, last_name, email_address)
        )
        items = self.cursor.fetchall()
        for item in items:
            print(item)
        # Commit
        self.conn.commit()

    def delete_record(self, id):
        """Delete one record with id"""
        self.cursor.execute(
            "DELETE from customers WHERE rowid = (?)",
            id
        )

    def add_many(self, record_list):
        """Add many records"""
        self.cursor.executemany(
            """
            INSERT INTO customers VALUES (?, ?,?)
            """,
            (record_list)
        )

    def email_lookup(self, email_address):
        """Playing with WHERE clause"""
        self.cursor.execute(
            "SELECT * from customers WHERE email_address = (?)",
            (email_address,) # need to pass a tupple always; include comma when only one value
        )
        items = self.cursor.fetchall()
        for item in items:
            print(item)

    def close_connection(self):
        """Close connection"""
        self.conn.close()
