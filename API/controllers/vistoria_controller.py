from flask import jsonify, request
from models.vistoria_model import (
    criar_vistoria,
    listar_vistorias,
    buscar_vistoria_por_id
)

def get_vistorias():
    vistorias = listar_vistorias()
    return jsonify(vistorias)

def get_vistoria(vistoria_id):
    vistoria = buscar_vistoria_por_id(vistoria_id)
    if vistoria:
        return jsonify(vistoria)
    return jsonify({"erro": "Vistoria não encontrada"}), 404

def post_vistoria():
    data = request.json

    obrigatorios = ["id_inventariante", "id_sala"]
    for campo in obrigatorios:
        if campo not in data:
            return jsonify({"erro": f"Campo obrigatório ausente: {campo}"}), 400

    criar_vistoria(data)
    return jsonify({"status": "Vistoria criada com sucesso"}), 201
