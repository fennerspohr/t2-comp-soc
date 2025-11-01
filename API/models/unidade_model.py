import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Configuração do banco
config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def get_db_connection():
    return mysql.connector.connect(**config)

# Listar todas as unidades
def listar_unidades():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, latitude, longitude FROM unidade")
    unidades = cursor.fetchall()
    cursor.close()
    conn.close()
    return unidades

# Buscar unidade por ID
def buscar_unidade(unidade_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, latitude, longitude FROM unidade WHERE id = %s", (unidade_id,))
    unidade = cursor.fetchone()
    cursor.close()
    conn.close()
    return unidade

# Criar nova unidade
def criar_unidade(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO unidade (nome, latitude, longitude)
        VALUES (%s, %s, %s)
    """, (
        data["nome"],
        data.get("latitude"),
        data.get("longitude")
    ))
    conn.commit()
    cursor.close()
    conn.close()
