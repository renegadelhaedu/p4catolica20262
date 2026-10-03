from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user

from reposit.usuariodao import UsuarioDAO

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def pagina_principal():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin.painel'))
        return render_template('principal.html')
    return render_template('index.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin.painel'))
        return redirect(url_for('usuarios.pagina_inicial'))

    if request.method == 'GET':
        return render_template('index.html')

    email = request.form.get('email', '').strip()
    senha = request.form.get('senha', '')
    usuario = UsuarioDAO.buscar_por_email(email)

    if usuario and usuario.senha == senha:
        login_user(usuario)
        if usuario.is_admin:
            return redirect(url_for('admin.painel'))
        return redirect(url_for('usuarios.pagina_inicial'))

    return render_template('index.html', mensagem='Erro ao fazer login'), 401


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.pagina_principal'))
