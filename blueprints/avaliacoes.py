from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from services.avaliacao_serv import listar_avaliacoes, criar_avaliacao, remover_avaliacao

avaliacoes_bp = Blueprint('avaliacoes', __name__, url_prefix='/api/avaliacoes')


@avaliacoes_bp.route('', methods=['GET'])
@login_required
def listar():
    avaliacoes = listar_avaliacoes()
    return jsonify([a.to_dict() for a in avaliacoes]), 200


@avaliacoes_bp.route('', methods=['POST'])
@login_required
def criar():
    dados = request.get_json()

    texto = dados.get('texto')

    #usa o id do usuario logado via flask-login (current_user)
    sucesso, erro = criar_avaliacao(current_user.id, texto)

    if not sucesso:
        return jsonify({'erro': erro}), 400

    return jsonify({'mensagem': 'Avaliação criada com sucesso'}), 201


@avaliacoes_bp.route('/<int:id_avaliacao>', methods=['DELETE'])
@login_required
def remover(id_avaliacao):
    #chamada ao service
    sucesso, erro = remover_avaliacao(id_avaliacao)

    if not sucesso:
        return jsonify({'erro': erro}), 404

    return jsonify({'mensagem': 'Avaliação removida com sucesso'}), 200
