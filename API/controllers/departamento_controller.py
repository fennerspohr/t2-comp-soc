from flask import jsonify, request
from models.departamento_model import (
    criar_departamento,
    listar_departamentos,
    buscar_departamento_por_id
)

def get_departamentos():
    departamentos = listar_departamentos()
    return jsonify(departamentos)

def get_departamento(dep_id):
    departamento = buscar_departamento_por_id(dep_id)
    if departamento:
        return jsonify(departamento)
    return jsonify({"erro": "Departamento não encontrado"}), 404

def post_departamento():
    data = request.json
    nome = data.get("nome")
    id_unidade = data.get("id_unidade")

    if not nome or not id_unidade:
        return jsonify({"erro": "Campos obrigatórios: nome, id_unidade"}), 400

    criar_departamento(nome, id_unidade)
    return jsonify({"status": "Departamento criado com sucesso"}), 201
