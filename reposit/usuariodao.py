from configdb import db
from modelos.usuario import Usuario

#objeto que contém os métodos de CRUD para acesso ao banco de dados
class UsuarioDAO:
    #definir métodos estáticos para serem acessados
    #nas rotas do servidor
    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()

    @staticmethod
    def listar_todos():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_id(id_usuario):
        return db.session.get(Usuario, id_usuario)

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def atualizar_nome(id_usuario, novo_nome):
        usuario = db.session.get(Usuario, id_usuario)
        if usuario:
            usuario.nome = novo_nome
            db.session.commit()
        return usuario

    @staticmethod
    def remover(usuario):
        db.session.delete(usuario)
        db.session.commit()
