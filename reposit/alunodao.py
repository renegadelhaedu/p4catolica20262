from configdb import db
from modelos.usuario import Usuario

#objeto que contém os métodos de CRUD para acesso ao banco
class UsuarioDAO:
    #definir métodos estáticos para serem acessados
    #nas rotas do servidor
    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()#salvando e gravando ele no BD

    @staticmethod
    def listar_todos():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def remover(usuario):
        db.session.delete(usuario)
        db.session.commit()