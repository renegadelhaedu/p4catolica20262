from flask import Flask, redirect, request, url_for

from blueprints.auth import auth_bp
from blueprints.admin import admin_bp
from blueprints.avaliacoes import avaliacoes_bp
from blueprints.usuarios import usuarios_bp
from configdb import db
from extensoes import login_manager
from modelos.usuario import Usuario


app = Flask(__name__)
app.secret_key = 'EGUyfgA786#'  # Coloque este valor em uma variável de ambiente.
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:12345@localhost:5432/p4catolicaweb'
)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
login_manager.init_app(app)

#a gente precisa disso p evitar q outros usuários simulem um perfil q nao é seu ou acesso a endpoints desautoriza..
@login_manager.unauthorized_handler
def acesso_nao_autorizado():
    if request.blueprint == 'admin':
        return redirect(url_for('admin.login_admin'))
    return redirect(url_for('auth.login'))


@login_manager.user_loader
def carregar_usuario(id_usuario):
    try:
        return db.session.get(Usuario, int(id_usuario))
    except (TypeError, ValueError):
        return None


app.register_blueprint(auth_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(avaliacoes_bp)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
