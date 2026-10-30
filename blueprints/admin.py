from functools import wraps

from flask import Blueprint, jsonify, abort
from flask_login import login_required, current_user
from services.usuario_serv import listar_usuarios, remover_usuario
from services.avaliacao_serv import listar_avaliacoes, remover_avaliacao

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')


#decorator que exige que o usuario logado seja admin
def admin_required(view):
    @wraps(view)
    @login_required
    def wrapped(*args, **kwargs):
        if not current_user.is_admin:
            return jsonify({'erro': 'Acesso restrito a administradores'}), 403
        return view(*args, **kwargs)
    return wrapped


@admin_bp.route('/usuarios', methods=['GET'])
@admin_required
def listar_usuarios_admin():
    usuarios = listar_usuarios()
    return jsonify([u.to_dict() for u in usuarios]), 200


@admin_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
@admin_required
def remover_usuario_admin(id_usuario):
    sucesso, erro = remover_usuario(id_usuario)

    if not sucesso:
        return jsonify({'erro': erro}), 404

    return jsonify({'mensagem': 'Usuário removido com sucesso'}), 200


@admin_bp.route('/avaliacoes', methods=['GET'])
@admin_required
def listar_avaliacoes_admin():
    avaliacoes = listar_avaliacoes()
    return jsonify([a.to_dict() for a in avaliacoes]), 200


@admin_bp.route('/avaliacoes/<int:id_avaliacao>', methods=['DELETE'])
@admin_required
def remover_avaliacao_admin(id_avaliacao):
    sucesso, erro = remover_avaliacao(id_avaliacao)

    if not sucesso:
        return jsonify({'erro': erro}), 404

    return jsonify({'mensagem': 'Avaliação removida com sucesso'}), 200
