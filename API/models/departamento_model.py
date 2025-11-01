from mysql.connector import connect
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def get_db_connection():
    return connect(**config)


def criar_departamento(nome, id_unidade):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO departamento (nome, id_unidade) VALUES (%s, %s)",
        (nome, id_unidade)
    )
    conn.commit()
    cursor.close()
    conn.close()


def listar_departamentos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT d.id, d.nome, u.nome AS unidade
        FROM departamento d
        JOIN unidade u ON d.id_unidade = u.id
    """)
    departamentos = cursor.fetchall()
    cursor.close()
    conn.close()
    return departamentos


def buscar_departamento_por_id(dep_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT d.id, d.nome, u.nome AS unidade
        FROM departamento d
        JOIN unidade u ON d.id_unidade = u.id
        WHERE d.id = %s
    """, (dep_id,))
    departamento = cursor.fetchone()
    cursor.close()
    conn.close()
    return departamento
