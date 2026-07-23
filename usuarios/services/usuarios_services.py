from extensions import db, bcrypt
from usuarios.models.usuarios_model import Usuario

def cadastrar_usuario(dados):

    senha_hash = bcrypt.generate_password_hash(dados.get("senha")).decode("utf-8")

    novo_usuario = Usuario(
        nome = dados.get("nome"),
        email = dados.get("email"),
        senha = senha_hash
    )

    db.session.add(novo_usuario)
    db.session.commit()

    return novo_usuario.to_dict()

def login_usuario(dados):

    email_digitado = dados.get("email")
    senha_digitado = dados.get("senha")

    usuario = Usuario.query.filter_by(email = email_digitado).first()
    if not usuario:
        return None

    senha_valida = bcrypt.check_password_hash(usuario.senha, senha_digitado)
    if not senha_valida:
        return False

    return usuario