from flask import Blueprint, flash, redirect, render_template, request, url_for, abort
from flask_login import current_user, login_required
from reposit.avaliacaodao import AvaliacaoDAO
from configdb import db
from modelos.avaliacao import Avaliacao

avaliacoes_bp = Blueprint('avaliacoes', __name__)


@avaliacoes_bp.route('/avaliacoes/nova', methods=['GET', 'POST'])
@login_required
def nova_avaliacao():
    if current_user.is_admin:
        abort(403)

    if request.method == 'POST':
        texto = request.form.get('texto', '').strip()
        if not texto:
            flash('Escreva sua avaliação sobre sua disciplina.', 'erro')
            return render_template('nova_avaliacao.html')

        AvaliacaoDAO.salvar(current_user.id, texto)

        flash('Avaliação enviada.', 'sucesso')
        return redirect(url_for('usuarios.pagina_inicial'))

    return render_template('nova_avaliacao.html')
