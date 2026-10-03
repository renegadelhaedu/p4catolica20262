from functools import wraps

from flask import Blueprint, abort, redirect, render_template, url_for, flash, request
from flask_login import current_user, login_required, login_user

from configdb import db
from reposit.avaliacaodao import AvaliacaoDAO
from modelos.avaliacao import Avaliacao
from modelos.usuario import Usuario
from reposit.usuariodao import UsuarioDAO

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

#aqui a gente cria um wrapper para colocar nas rotas e exigir estar logado como admin
def admin_required(view):
    @wraps(view)
    @login_required
    def wrapped(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return view(*args, **kwargs)
    return wrapped


@admin_bp.route('/login', methods=['GET', 'POST'])
def login_admin():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin.painel'))
        return render_template('admin_login.html', mensagem='Esta área é restrita a administradores.'), 403

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '')
        usuario = UsuarioDAO.buscar_por_email(email)
        if usuario and usuario.is_admin and usuario.senha == senha:
            login_user(usuario)
            return redirect(url_for('admin.painel'))

        return render_template(
            'admin_login.html', mensagem='Credenciais inválidas ou conta sem perfil administrativo.'
        ), 401

    return render_template('admin_login.html')


@admin_bp.route('/')
@admin_required
def painel():
    return render_template('admin_painel.html')


@admin_bp.route('/usuarios')
@admin_required
def listar_usuarios():
    usuarios = Usuario.query.order_by(Usuario.nome).all()
    return render_template('admin_usuarios.html', usuarios=usuarios)


@admin_bp.route('/usuarios/<int:id_usuario>/remover', methods=['POST'])
@admin_required
def remover_usuario(id_usuario):
    usuario = db.session.get(Usuario, id_usuario)
    if usuario is None:
        abort(404)
    if usuario.id == current_user.id:
        flash('Você não pode remover sua própria conta.', 'erro')
        return redirect(url_for('admin.listar_usuarios'))

    Avaliacao.query.filter_by(usuario_id=usuario.id).delete()
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuário removido.', 'sucesso')
    return redirect(url_for('admin.listar_usuarios'))


@admin_bp.route('/avaliacoes')
@admin_required
def listar_avaliacoes():
    avaliacoes = AvaliacaoDAO.listar_todos()
    return render_template('admin_avaliacoes.html', avaliacoes=avaliacoes)
