from reposit.usuariodao import UsuarioDAO


def checar_login(email, senha):
    """Valida as credenciais do usuario.
    Retorna o usuario se as credenciais estiverem corretas, None caso contrario."""
    if not email or '@' not in email:
        return None

    #chamar o repository
    usuario = UsuarioDAO.buscar_por_email(email)

    if usuario and usuario.senha == senha:
        return usuario

    return None
