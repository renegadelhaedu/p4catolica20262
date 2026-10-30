from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from services.auth_serv import checar_login

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    dados = request.get_json()

    email = dados.get('email', '').strip()
    senha = dados.get('senha', '')

    #chamada ao service
    usuario = checar_login(email, senha)

    if usuario:
        #cria a sessao do usuario no flask-login
        login_user(usuario)
        return jsonify({
            'mensagem': 'Login realizado com sucesso',
            'usuario': usuario.to_dict()
        }), 200

    return jsonify({'erro': 'Credenciais inválidas'}), 401


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'mensagem': 'Logout realizado com sucesso'}), 200
