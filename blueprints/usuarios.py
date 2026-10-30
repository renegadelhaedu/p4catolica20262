from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from services.usuario_serv import (
    listar_usuarios,
    buscar_usuario,
    cadastrar_usuario,
    remover_usuario,
    atualizar_nome_usuario
)

#instanciando uma blueprint para que seja possível utilizar e vincular ao servidor flask
usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/api/usuarios')


@usuarios_bp.route('', methods=['GET'])
@login_required
def listar():
    usuarios = listar_usuarios()
    return jsonify([u.to_dict() for u in usuarios]), 200


@usuarios_bp.route('/<int:id_usuario>', methods=['GET'])
@login_required
def detalhar(id_usuario):
    usuario = buscar_usuario(id_usuario)
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    return jsonify(usuario.to_dict()), 200


@usuarios_bp.route('', methods=['POST'])
def cadastrar():
    dados = request.get_json()

    nome = dados.get('nome')
    email = dados.get('email')
    data_nascimento = dados.get('data_nascimento')
    senha = dados.get('senha')

    #chamada ao service
    usuario, erro = cadastrar_usuario(nome, email, data_nascimento, senha)

    if erro:
        return jsonify({'erro': erro}), 400

    return jsonify({
        'mensagem': 'Usuário cadastrado com sucesso',
        'usuario': usuario.to_dict()
    }), 201


#PUT: substitui o recurso inteiro
#PATCH: atualiza parcialmente o recurso, modificando apenas os campos especificados
@usuarios_bp.route('/<int:id_usuario>', methods=['PUT', 'PATCH'])
@login_required
def atualizar(id_usuario):
    dados = request.get_json() or {}
    novo_nome = dados.get('nome')

    #chamo o service para ver se pode atualizar
    usuario, erro = atualizar_nome_usuario(
        id_usuario=id_usuario,
        novo_nome=novo_nome,
        id_usuario_logado=current_user.id
    )

    if erro:
        if 'Acesso não autorizado' in erro:
            return jsonify({'erro': erro}), 403
        if 'não encontrado' in erro:
            return jsonify({'erro': erro}), 404
        return jsonify({'erro': erro}), 400

    return jsonify({
        'mensagem': 'Nome atualizado com sucesso',
        'usuario': usuario.to_dict()
    }), 200


@usuarios_bp.route('/<int:id_usuario>', methods=['DELETE'])
@login_required
def remover(id_usuario):
    #chamada ao service
    sucesso, erro = remover_usuario(id_usuario)

    if not sucesso:
        return jsonify({'erro': erro}), 404

    return jsonify({'mensagem': 'Usuário removido com sucesso'}), 200
