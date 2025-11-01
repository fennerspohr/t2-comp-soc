import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sql_path = os.path.join(BASE_DIR, "createBD.sql")

with open(sql_path, "r") as f:
    sql_script = f.read()

# Configuração da conexão
config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# Conecta e executa
try:
    conn = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"]
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS {0};".format(config["database"]))
    cursor.close()
    conn.close()

    # Reabre conexão no banco inventario
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    # Divide o script em comandos individuais
    for stmt in sql_script.split(";"):
        stmt = stmt.strip()
        if stmt:
            cursor.execute(stmt + ";")

    conn.commit()
    print("Banco inicializado com sucesso!")
except mysql.connector.Error as e:
    print("Erro:", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
