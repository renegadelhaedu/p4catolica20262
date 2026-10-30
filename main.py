from flask import Flask, jsonify

from blueprints.auth import auth_bp
from blueprints.admin import admin_bp
from blueprints.avaliacoes import avaliacoes_bp
from blueprints.usuarios import usuarios_bp
from configdb import db
from flask_login import LoginManager
from modelos.usuario import Usuario

#instanciando o servidor flask
app = Flask(__name__)
app.secret_key = 'EGUyfgA786#'  # Coloque este valor em uma variável de ambiente.
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:12345@localhost:5432/p4catolicaweb'
)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

#configurar o flask-login
login_manager = LoginManager()
login_manager.init_app(app)


#quando o usuario nao esta logado e tenta acessar rota protegida,
#retorna JSON 401 em vez de redirecionar para uma pagina HTML
@login_manager.unauthorized_handler
def acesso_nao_autorizado():
    return jsonify({'erro': 'Login necessário para acessar este recurso'}), 401


#carrega o usuario da sessao a cada requisicao
@login_manager.user_loader
def carregar_usuario(id_usuario):
    try:
        #puxei o model objeto de usuário
        return db.session.get(Usuario, int(id_usuario))
    except (TypeError, ValueError):
        return None


#registrar as blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(avaliacoes_bp)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
