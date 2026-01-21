from connection_db import get_connection

def save_weather_records(records:list[dict]):
    insert_data_to_db(records)
    return {"status": "ok", "inserted": len(records)}




def insert_data_to_db(records):
    conn = get_connection()  # pool one connection
    cursor = conn.cursor()
    try:
        query = """
            INSERT INTO weather_records (
                timestamp, location_name, country, latitude, longitude,
                temperature, wind_speed, humidity,
                temperature_category, wind_category
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        values = [
            (
                r["timestamp"],
                r["location_name"],
                r["country"],
                r["latitude"],
                r["longitude"],
                r["temperature"],
                r["wind_speed"],
                r["humidity"],
                r["temperature_category"],
                r["wind_category"]
            )
            for r in records
        ]

        cursor.executemany(query,values)
        conn.commit()
    finally:
        cursor.close()
        conn.close()





