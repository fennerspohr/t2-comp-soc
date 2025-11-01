from flask import Blueprint
from controllers.unidade_controller import (
    listar_unidades_controller,
    buscar_unidade_controller,
    criar_unidade_controller
)

unidade_bp = Blueprint("unidade_bp", __name__)

# Rotas
unidade_bp.route("/unidades", methods=["GET"])(listar_unidades_controller)
unidade_bp.route("/unidades/<int:unidade_id>", methods=["GET"])(buscar_unidade_controller)
unidade_bp.route("/unidades", methods=["POST"])(criar_unidade_controller)

