from flask import Blueprint
from controllers.sala_controller import (
    get_salas,
    get_sala,
    post_sala
)

sala_bp = Blueprint("sala_bp", __name__)

@sala_bp.route("/salas", methods=["GET"])
def listar():
    return get_salas()

@sala_bp.route("/salas/<int:sala_id>", methods=["GET"])
def buscar(sala_id):
    return get_sala(sala_id)

@sala_bp.route("/salas", methods=["POST"])
def criar():
    return post_sala()
