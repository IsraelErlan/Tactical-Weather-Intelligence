import os
import mysql.connector

def init_database():
    conn = mysql.connector.connect(
        host=os.getenv("HOST","localhost"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD")
    )
    cursor = conn.cursor()
    sql_path = os.path.join("sql", "init.sql")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql_commands = f.read().split(";")

    for command in sql_commands:
        cmd = command.strip()
        if cmd:
            cursor.execute(cmd)

    conn.commit()
    cursor.close()
    conn.close()