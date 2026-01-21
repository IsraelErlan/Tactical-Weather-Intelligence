import mysql.connector.pooling
import os
from dotenv import load_dotenv
load_dotenv()
_connection_pool = None


def init_connection_pool():
    global _connection_pool
    if _connection_pool is None:
        _connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="weather_pool",
            pool_size=5,
            host=os.getenv("HOST"),
            port=int(os.getenv("PORT", 3306)),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
            autocommit=True
        )

def get_connection():
    if _connection_pool is None:
        raise RuntimeError("Connection pool not initialized")
    return _connection_pool.get_connection()