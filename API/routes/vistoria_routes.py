from flask import Blueprint
from controllers.vistoria_controller import (
    get_vistorias,
    get_vistoria,
    post_vistoria
)

vistoria_bp = Blueprint("vistoria_bp", __name__)

@vistoria_bp.route("/vistorias", methods=["GET"])
def listar():
    return get_vistorias()

@vistoria_bp.route("/vistorias/<int:vistoria_id>", methods=["GET"])
def buscar(vistoria_id):
    return get_vistoria(vistoria_id)

@vistoria_bp.route("/vistorias", methods=["POST"])
def criar():
    return post_vistoria()
