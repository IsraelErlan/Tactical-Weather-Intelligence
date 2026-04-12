import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

def init_database():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD")
    )
    cursor = conn.cursor()
    
    base_path = os.path.dirname(__file__) 
    sql_path = os.path.join(base_path, "init.sql")
    
    if not os.path.exists(sql_path):
        raise FileNotFoundError(f"file {sql_path} not found")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql_commands = f.read().split(";")

    for command in sql_commands:
        cmd = command.strip()
        if cmd:
            cursor.execute(cmd)

    conn.commit()
    cursor.close()
    conn.close()