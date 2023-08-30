import sqlite3
import json

class CarDatabase():
    """Class to hold functions for the car database"""
    
    db_connection = sqlite3.connect('car.db')
    db_cursor = db_connection.cursor()

    def create_table_cars(self):
        """Create the cars table"""
        query_string = (
            """
                CREATE TABLE cars (
                car_id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
                car_make TEXT,
                car_model TEXT,
                car_version TEXT,
                car_transmission TEXT,
                car_fuel TEXT,
                car_engine_power INTEGER,
                car_engine_capacity INTEGER,
                UNIQUE (car_make,car_model,car_version,car_transmission)
                )
            """
        )
        self.db_cursor.execute(query_string)
        self.db_connection.commit()
        print('Database table CARS created successfully!')

    def create_table_ads(self):
        """Create the ads table"""
        query_string = (
            """
                CREATE TABLE ads (
                car_id INT, 
                car_ad_id INT PRIMARY KEY,
                car_ad_title TEXT,
                car_ad_created TEXT,
                car_ad_modified TEXT,
                car_ad_days INT,
                car_ad_shortDescription TEXT,
                car_ad_url BLOB,
                car_ad_badges BLOB,
                car_ad_loc_region TEXT,
                car_ad_loc_city TEXT,
                car_ad_price_value INT,
                car_ad_price_currency TEXT,
                car_ad_year INT,
                car_ad_month INT,
                car_ad_age REAL,
                car_ad_mileage INT,
                car_ad_warranty INT,
                car_ad_origin TEXT
                )
            """
        )
        self.db_cursor.execute(query_string)
        self.db_connection.commit()
        print('Database table ADS created successfully!')

    def create_table_prices(self):
        """Create the prices table"""
        query_string = (
            """
                CREATE TABLE prices (
                car_ad_id INT,
                car_modified TEXT,
                car_price_value INT,
                )
            """
        )
        self.db_cursor.execute(query_string)
        self.db_connection.commit()
        print('Database table PRICES created successfully!')

    def add_cars(self,json_file):
        """Function that ads records to key tables from json file"""
        with open(json_file, 'r', encoding='utf-8') as file:
            json_string = json.load(file)
            for record in json_string:
                if 'car_version' not in record:
                    record['car_version'] = 'not available'
                if 'car_transmission' not in record:
                    record['car_transmission'] = 'not available'
                if 'car_engine_capacity' not in record:
                    record['car_engine_capacity'] = 'not available'
                self.db_cursor.execute(
                    'INSERT OR IGNORE INTO cars (car_make, car_version, car_model, car_fuel, car_engine_power, car_engine_capacity, car_transmission) '
                    'VALUES (:car_make, :car_version, :car_model, :car_fuel, :car_engine_power, :car_engine_capacity, :car_transmission)',
                    record
                )
        print('Records added to Database!')
        self.db_connection.commit()

    def show_all(self):
        """Show all records"""
        query_string = ('SELECT * FROM cars')
        self.db_cursor.execute(query_string)
        records = self.db_cursor.fetchall()
        for record in records:
            print(record)


    def close_connection(self):
        """Needed to invoke close connection"""
        self.db_connection.close()
        print('Connection to database closed!')
