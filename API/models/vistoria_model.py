from mysql.connector import connect
from dotenv import load_dotenv
import os
import base64

load_dotenv()

config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def get_db_connection():
    return connect(**config)


def criar_vistoria(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    foto_ini = base64.b64decode(data["foto_ini"]) if data.get("foto_ini") else None
    foto_fim = base64.b64decode(data["foto_fim"]) if data.get("foto_fim") else None

    cursor.execute("""
        INSERT INTO vistoria (
            data_hora_ini, data_hora_fim, foto_ini, foto_fim, id_inventariante, id_sala
        ) VALUES (NOW(), %s, %s, %s, %s, %s)
    """, (
        data.get("data_hora_fim"),
        foto_ini,
        foto_fim,
        data["id_inventariante"],
        data["id_sala"]
    ))

    conn.commit()
    cursor.close()
    conn.close()


def listar_vistorias():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT v.id, v.data_hora_ini, v.data_hora_fim,
               i.nome AS inventariante, s.nome AS sala
        FROM vistoria v
        JOIN inventariante i ON v.id_inventariante = i.id
        JOIN sala s ON v.id_sala = s.id
        ORDER BY v.data_hora_ini DESC
    """)
    vistorias = cursor.fetchall()
    cursor.close()
    conn.close()
    return vistorias


def buscar_vistoria_por_id(vistoria_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT * FROM vistoria WHERE id = %s
    """, (vistoria_id,))
    vistoria = cursor.fetchone()
    cursor.close()
    conn.close()

    if vistoria:
        if vistoria.get("foto_ini"):
            vistoria["foto_ini"] = base64.b64encode(vistoria["foto_ini"]).decode("utf-8")
        if vistoria.get("foto_fim"):
            vistoria["foto_fim"] = base64.b64encode(vistoria["foto_fim"]).decode("utf-8")
    return vistoria
