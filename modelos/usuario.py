#importar o teu objeto de conexao com o BD
from configdb import db

#(BD-4)galera, voces precisam herdar a classe model para que ele consiga mapear os objetos
class Usuario(db.Model):
    #coloque o nome sempre sem espaço e com letras minusc
    __tablename__ = 'usuarios'

    #agora a gente precisa mapear as colunas do BD no objeto
    #atributos da tabela do banco de dados
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    data_nascimento = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

