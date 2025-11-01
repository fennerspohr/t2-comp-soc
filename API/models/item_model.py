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


def criar_item(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    foto_bytes = base64.b64decode(data["foto_bem"])  # decodifica a imagem Base64

    cursor.execute("""
        INSERT INTO item (
            nome, descr, categoria, valor, data_aquisicao, foto_bem, qrcode,
            observacao, estado_fisico, condicao_uso, conservacao, funcionalidade,
            id_unidade, id_departamento, id_sala
        )
        VALUES (%s, %s, %s, %s, NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data["nome"], data["descr"], data["categoria"], data["valor"], foto_bytes, data["qrcode"],
        data.get("observacao"), data.get("estado_fisico"), data.get("condicao_uso"),
        data.get("conservacao"), data.get("funcionalidade"),
        data["id_unidade"], data["id_departamento"], data["id_sala"]
    ))

    conn.commit()
    cursor.close()
    conn.close()


def listar_itens():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT i.id, i.nome, i.categoria, i.valor, i.qrcode,
               s.nome AS sala, d.nome AS departamento, u.nome AS unidade
        FROM item i
        JOIN sala s ON i.id_sala = s.id
        JOIN departamento d ON i.id_departamento = d.id
        JOIN unidade u ON i.id_unidade = u.id
    """)
    itens = cursor.fetchall()
    cursor.close()
    conn.close()
    return itens


def buscar_item_por_id(item_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT * FROM item WHERE id = %s
    """, (item_id,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()
    if item and item.get("foto_bem"):
        item["foto_bem"] = base64.b64encode(item["foto_bem"]).decode("utf-8")
    return item
