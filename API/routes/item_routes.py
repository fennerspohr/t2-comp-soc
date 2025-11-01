from flask import Blueprint
from controllers.item_controller import (
    get_itens,
    get_item,
    post_item
)

item_bp = Blueprint("item_bp", __name__)

@item_bp.route("/itens", methods=["GET"])
def listar():
    return get_itens()

@item_bp.route("/itens/<int:item_id>", methods=["GET"])
def buscar(item_id):
    return get_item(item_id)

@item_bp.route("/itens", methods=["POST"])
def criar():
    return post_item()
