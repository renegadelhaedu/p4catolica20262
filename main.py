from flask import Flask

from blueprints.auth import auth_bp
from blueprints.admin import admin_bp
from blueprints.avaliacoes import avaliacoes_bp
from blueprints.usuarios import usuarios_bp
from configdb import db

#instanciando o servidor flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:12345@localhost:5432/p4catolicaweb'
)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

#registrar as blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(avaliacoes_bp)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
