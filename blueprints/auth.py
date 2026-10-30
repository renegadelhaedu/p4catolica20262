from flask import Blueprint, request, jsonify
from services.auth_serv import checar_login

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    #recebe o arquivo json e converte para uma estrutura python
    dados = request.get_json()
    print(dados)
    email = dados.get('email', '').strip()
    senha = dados.get('senha', '')

    #chamada ao service
    usuario = checar_login(email, senha)

    if usuario:
        #retornar json: via jsonify
        return jsonify({
            'mensagem': 'Login realizado com sucesso',
            'usuario': usuario.to_dict()
        }), 200

    return jsonify({'erro': 'Credenciais inválidas'}), 401
