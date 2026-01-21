import mysql.connector

class SQLManager:

    
    @classmethod
    def get_records(cls, conn: mysql.connector):
        try:
            with conn:
                with conn.cursor(dictionary=True) as cur:
                    query = "SELECT * FROM "
                    cur.execute(query)
                    data = cur.fetchall()
                    return data
        except mysql.connector.Error as e:
            raise e


    @classmethod
    def get_count_records_by_area(cls, conn):
        try:
            with conn:
                with conn.cursor(dictionary=True) as cur:
                    query = '''SELECT location_name, COUNT(area) 
                              FROM 
                              GROUP BY location_name'''
                    cur.execute(query)
                    data = cur.fetchall()
                    return data
        except mysql.connector.Error as e:
            raise e

    @classmethod
    def get_avg_temperature_by_area(cls, conn):
        try:
            with conn:
                with conn.cursor(dictionary=True) as cur:
                    query = '''SELECT location_name, AVG(temperature)
                                FROM 
                                GROUP BY location_name'''
                    cur.execute(query)
                    data = cur.fetchall()
                    return data
        except mysql.connector.Error as e:
            raise e

    @classmethod
    def get_max_wind_by_area(cls, conn):
        try:
            with conn:
                with conn.cursor(dictionary=True) as cur:
                    query = '''SELECT location_name, MAX(wind)
                                FROM 
                                GROUP BY location_name'''
                    cur.execute(query)
                    data = cur.fetchall()
                    return data
        except mysql.connector.Error as e:
            raise e

    @classmethod
    def get_extreme_locations(cls, conn):
        try:
            with conn:
                with conn.cursor(dictionary=True) as cur:
                    query = '''SELECT *
                                FROM 
                                WHERE temperature_category = 'cold' AND wind_status = 'calm' OR 
                                 temperature_category = 'hot' AND wind_status = 'windy'
                                '''
                    cur.execute(query)
                    data = cur.fetchall()
                    return data
        except mysql.connector.Error as e:
            raise e