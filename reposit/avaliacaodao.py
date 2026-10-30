from configdb import db
from modelos.avaliacao import Avaliacao

#objeto que contém os métodos de CRUD para acesso ao banco de dados
class AvaliacaoDAO:
    #definir métodos estáticos para serem acessados
    #nas rotas do servidor
    @staticmethod
    def salvar(usuario_id, texto):
        db.session.add(Avaliacao(
            usuario_id=usuario_id,
            texto=texto,
        ))
        db.session.commit()

    @staticmethod
    def listar_todos():
        return Avaliacao.query.order_by(Avaliacao.criada_em.desc()).all()

    @staticmethod
    def buscar_por_id(id_avaliacao):
        return db.session.get(Avaliacao, id_avaliacao)

    @staticmethod
    def remover(avaliacao):
        db.session.delete(avaliacao)
        db.session.commit()
