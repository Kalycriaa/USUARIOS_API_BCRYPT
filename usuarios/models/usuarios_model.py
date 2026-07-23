from extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    senha = db.Column(db.String(255), nullable = False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }