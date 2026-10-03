from flask import Blueprint, render_template, request
from flask_login import login_required

from modelos.usuario import Usuario
from reposit.usuariodao import UsuarioDAO

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route('/principal')
@login_required
def pagina_inicial():
    return render_template('principal.html')


@usuarios_bp.route('/cadastrarusuario', methods=['GET', 'POST'])
@login_required
def cadastrarusuario():
    if request.method == 'GET':
        return render_template('cadastrarusuario.html')

    nome = request.form.get('nome')
    email = request.form.get('email')
    nascimento = request.form.get('nascimento')
    senha = request.form.get('senha')
    confirma = request.form.get('confirma')

    if senha and senha == confirma:
        UsuarioDAO.salvar(Usuario(
            nome=nome, email=email, data_nascimento=nascimento, senha=senha
        ))
        mensagem = 'Usuário cadastrado com sucesso!'
    else:
        mensagem = 'Erro no cadastro de usuário!'

    return render_template('principal.html', mensagem=mensagem)


@usuarios_bp.route('/listarusuarios')
@login_required
def listarusuarios():
    return render_template('listarusuarios.html', usuarios=UsuarioDAO.listar_todos())


@usuarios_bp.route('/detalharusuario/<int:idusuario>')
@login_required
def detalharusuario(idusuario):
    usuario = Usuario.query.get_or_404(idusuario)
    return render_template('detalharusuario.html', usuario=usuario)
