from reposit.usuariodao import UsuarioDAO


def checar_login(email):
    if '@' in email:
        #chama ao repository
        return UsuarioDAO.buscar_por_email(email)
    else:
        return None