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


def criar_sala(nome, id_departamento):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sala (nome, id_departamento) VALUES (%s, %s)",
        (nome, id_departamento)
    )
    conn.commit()
    cursor.close()
    conn.close()


def listar_salas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.id, s.nome, d.nome AS departamento
        FROM sala s
        JOIN departamento d ON s.id_departamento = d.id
    """)
    salas = cursor.fetchall()
    cursor.close()
    conn.close()
    return salas


def buscar_sala_por_id(sala_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.id, s.nome, d.nome AS departamento
        FROM sala s
        JOIN departamento d ON s.id_departamento = d.id
        WHERE s.id = %s
    """, (sala_id,))
    sala = cursor.fetchone()
    cursor.close()
    conn.close()
    return sala
