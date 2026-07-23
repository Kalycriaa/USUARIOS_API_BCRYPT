from extensions import Flask, db, bcrypt
from usuarios.routes.usuarios_routes import usuario_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bcrypt.init_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    app.run(debug = True)



