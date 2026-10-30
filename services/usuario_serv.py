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


def atualizar_nome_usuario(id_usuario, novo_nome, id_usuario_logado):
    """Atualiza o nome de um usuario.
    Verifica se o usuario logado tem permissao (apenas o proprio usuario).
    Retorna uma tupla (usuario, mensagem_erro)."""
    if id_usuario != id_usuario_logado:
        return None, 'Acesso não autorizado: você só pode alterar seu próprio nome'

    if not novo_nome or not novo_nome.strip():
        return None, 'O novo nome não pode ser vazio'

    usuario = UsuarioDAO.buscar_por_id(id_usuario)
    if not usuario:
        return None, 'Usuário não encontrado'

    usuario_atualizado = UsuarioDAO.atualizar_nome(id_usuario, novo_nome.strip())
    return usuario_atualizado, None


def remover_usuario(id_usuario):
    """Remove um usuario pelo id.
    Retorna uma tupla (sucesso, mensagem_erro)."""
    usuario = UsuarioDAO.buscar_por_id(id_usuario)
    if not usuario:
        return False, 'Usuário não encontrado'

    UsuarioDAO.remover(usuario)
    return True, None
