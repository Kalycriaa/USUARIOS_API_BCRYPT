from flask import Blueprint, jsonify, request
from usuarios.services import usuarios_services
usuario_bp = Blueprint("usuarios", __name__, url_prefix = "/usuarios")

@usuario_bp.route("", methods = ['POST'])
def cadastrar_usuario():

    dados = request.get_json()
    if not dados or "nome" not in dados or "email" not in dados or "senha" not in dados:
        return jsonify({"error": "por favor preencher todos os campos obrigatorio"}), 400

    resultado = usuarios_services.cadastrar_usuario(dados)

    return jsonify(resultado), 201

@usuario_bp.route("/login", methods = ['POST'])
def login_usuario():

    dados = request.get_json()
    if not dados or "email" not in dados or "senha" not in dados:
        return jsonify({"error": "por favor preencher todos campos obrigatorio"}), 400

    resultado = usuarios_services.login_usuario(dados)
    if resultado is None:
        return jsonify({"error": "usuario nao existe"}), 404

    if resultado is False:
        return jsonify({"error": "senha incorreta."}), 401

    return jsonify(resultado.to_dict())

