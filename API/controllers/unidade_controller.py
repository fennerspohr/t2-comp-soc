from flask import request, jsonify
from models.unidade_model import listar_unidades, buscar_unidade, criar_unidade

def listar_unidades_controller():
    unidades = listar_unidades()
    return jsonify(unidades)

def buscar_unidade_controller(unidade_id):
    unidade = buscar_unidade(unidade_id)
    if unidade:
        return jsonify(unidade)
    else:
        return jsonify({"erro": "Unidade não encontrada"}), 404

def criar_unidade_controller():
    data = request.json
    criar_unidade(data)
    return jsonify({"status": "Unidade criada com sucesso"}), 201
