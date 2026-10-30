from modelos.usuario import Usuario
from reposit.usuariodao import UsuarioDAO


def listar_usuarios():
    """Retorna todos os usuarios cadastrados."""
    return UsuarioDAO.listar_todos()


def buscar_usuario(id_usuario):
    """Busca um usuario pelo id."""
    return UsuarioDAO.buscar_por_id(id_usuario)


def cadastrar_usuario(nome, email, data_nascimento, senha):
    """Cadastra um novo usuario.
    Retorna uma tupla (usuario, mensagem_erro).
    Se sucesso, mensagem_erro sera None."""
    if not nome or not email or not data_nascimento or not senha:
        return None, 'Todos os campos são obrigatórios'

    #verificar se o email ja esta cadastrado
    existente = UsuarioDAO.buscar_por_email(email)
    if existente:
        return None, 'Email já cadastrado'

    usuario = Usuario(
        nome=nome,
        email=email,
        data_nascimento=data_nascimento,
        senha=senha
    )
    UsuarioDAO.salvar(usuario)
    return usuario, None


def remover_usuario(id_usuario):
    """Remove um usuario pelo id.
    Retorna uma tupla (sucesso, mensagem_erro)."""
    usuario = UsuarioDAO.buscar_por_id(id_usuario)
    if not usuario:
        return False, 'Usuário não encontrado'

    UsuarioDAO.remover(usuario)
    return True, None
