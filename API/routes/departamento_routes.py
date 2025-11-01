from flask import Blueprint
from controllers.departamento_controller import (
    get_departamentos,
    get_departamento,
    post_departamento
)

departamento_bp = Blueprint("departamento_bp", __name__)

@departamento_bp.route("/departamentos", methods=["GET"])
def listar():
    return get_departamentos()

@departamento_bp.route("/departamentos/<int:dep_id>", methods=["GET"])
def buscar(dep_id):
    return get_departamento(dep_id)

@departamento_bp.route("/departamentos", methods=["POST"])
def criar():
    return post_departamento()
