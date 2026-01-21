import mysql.connector

class SQLManager:

    
    @classmethod
    def get_records(cls, conn: mysql.connector.connection.MySQLConnection):
        try:
            with conn:
                with conn.cursor(dictionary=True) as cur:
                    query = "SELECT * FROM weather_db"
                    cur.execute(query)
                    data = cur.fetchall()
                    return data
        except mysql.connector.Error as e:
            raise e


    @classmethod
    def get_count_records_by_area(cls, conn: mysql.connector.connection.MySQLConnection):
        try:
            with conn:
                with conn.cursor(dictionary=True) as cur:
                    query = '''SELECT location_name, COUNT(area) 
                              FROM weather_db
                              GROUP BY location_name'''
                    cur.execute(query)
                    data = cur.fetchall()
                    return data
        except mysql.connector.Error as e:
            raise e

    @classmethod
    def get_avg_temperature_by_area(cls, conn: mysql.connector.connection.MySQLConnection):
        try:
            with conn:
                with conn.cursor(dictionary=True) as cur:
                    query = '''SELECT location_name, AVG(temperature)
                                FROM weather_db
                                GROUP BY location_name'''
                    cur.execute(query)
                    data = cur.fetchall()
                    return data
        except mysql.connector.Error as e:
            raise e

    @classmethod
    def get_max_wind_by_area(cls, conn: mysql.connector.connection.MySQLConnection):
        try:
            with conn:
                with conn.cursor(dictionary=True) as cur:
                    query = '''SELECT location_name, MAX(wind)
                                FROM weather_db
                                GROUP BY location_name'''
                    cur.execute(query)
                    data = cur.fetchall()
                    return data
        except mysql.connector.Error as e:
            raise e

    @classmethod
    def get_extreme_locations(cls, conn: mysql.connector.connection.MySQLConnection):
        try:
            with conn:
                with conn.cursor(dictionary=True) as cur:
                    query = '''SELECT *
                                FROM weather_db
                                WHERE temperature_category = %s AND wind_status = %s OR 
                                 temperature_category = %s AND wind_status = %s
                                ''', ('cold', 'calm', 'hot', 'windy')
                    cur.execute(query)
                    data = cur.fetchall()
                    return data
        except mysql.connector.Error as e:
            raise e