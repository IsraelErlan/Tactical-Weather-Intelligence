from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

print("HOST:", os.getenv("HOST"))
print("PORT:", os.getenv("PORT"))
print("USER:", os.getenv("USER"))
print("DB:", os.getenv("DATABASE"))

conn = mysql.connector.connect(
    host=os.getenv("HOST"),
    port=int(os.getenv("PORT")),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE")
)

print("CONNECTED OK")
conn.close()
