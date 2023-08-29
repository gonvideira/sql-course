from car_database import CarDatabase

db_connection = CarDatabase()

db_connection.create_table_cars()

db_connection.add_cars('cars.json')
