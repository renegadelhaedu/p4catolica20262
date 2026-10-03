from configdb import db
from modelos.avaliacao import Avaliacao

#objeto que contém os métodos de CRUD para acesso ao banco de dados
class AvaliacaoDAO:
    #definir métodos estáticos para serem acessados
    #nas rotas do servidor
    @staticmethod
    def salvar(id,texto):
        #falta fazer o tratamento de erro
        db.session.add(Avaliacao(
            usuario_id=id,
            texto=texto,
        ))

        db.session.commit()#salvando e gravando ele no BD
        #este método precisa restornar true ou false

    @staticmethod
    def listar_todos():
        return Avaliacao.query.order_by(Avaliacao.criada_em.desc()).all()


    @staticmethod
    def remover(avaliacao):
        db.session.delete(avaliacao)
        db.session.commit()