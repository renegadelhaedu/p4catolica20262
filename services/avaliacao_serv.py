from reposit.avaliacaodao import AvaliacaoDAO


def listar_avaliacoes():
    """Retorna todas as avaliacoes cadastradas."""
    return AvaliacaoDAO.listar_todos()


def criar_avaliacao(usuario_id, texto):
    """Cria uma nova avaliacao.
    Retorna uma tupla (sucesso, mensagem_erro)."""
    if not texto or not texto.strip():
        return False, 'O texto da avaliação é obrigatório'

    AvaliacaoDAO.salvar(usuario_id, texto.strip())
    return True, None


def remover_avaliacao(id_avaliacao):
    """Remove uma avaliacao pelo id.
    Retorna uma tupla (sucesso, mensagem_erro)."""
    avaliacao = AvaliacaoDAO.buscar_por_id(id_avaliacao)
    if not avaliacao:
        return False, 'Avaliação não encontrada'

    AvaliacaoDAO.remover(avaliacao)
    return True, None
