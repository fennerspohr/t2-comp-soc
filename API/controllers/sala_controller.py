from flask import jsonify, request
from models.sala_model import (
    criar_sala,
    listar_salas,
    buscar_sala_por_id
)

def get_salas():
    salas = listar_salas()
    return jsonify(salas)

def get_sala(sala_id):
    sala = buscar_sala_por_id(sala_id)
    if sala:
        return jsonify(sala)
    return jsonify({"erro": "Sala não encontrada"}), 404

def post_sala():
    data = request.json
    nome = data.get("nome")
    id_departamento = data.get("id_departamento")

    if not nome or not id_departamento:
        return jsonify({"erro": "Campos obrigatórios: nome, id_departamento"}), 400

    criar_sala(nome, id_departamento)
    return jsonify({"status": "Sala criada com sucesso"}), 201
