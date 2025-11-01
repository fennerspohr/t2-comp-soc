from flask import jsonify, request
from models.item_model import (
    criar_item,
    listar_itens,
    buscar_item_por_id
)

def get_itens():
    itens = listar_itens()
    return jsonify(itens)

def get_item(item_id):
    item = buscar_item_por_id(item_id)
    if item:
        return jsonify(item)
    return jsonify({"erro": "Item não encontrado"}), 404

def post_item():
    data = request.json
    obrigatorios = [
        "nome", "descr", "categoria", "valor", "foto_bem", "qrcode",
        "id_unidade", "id_departamento", "id_sala"
    ]
    if not all(campo in data for campo in obrigatorios):
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

    criar_item(data)
    return jsonify({"status": "Item criado com sucesso"}), 201
