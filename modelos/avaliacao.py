from datetime import datetime

from configdb import db


class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    criada_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    usuario = db.relationship('Usuario', backref=db.backref('avaliacoes', lazy=True))

    #converte o objeto para dicionario (JSON-friendly)
    def to_dict(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'texto': self.texto,
            'criada_em': self.criada_em.isoformat(),
            'nome_usuario': self.usuario.nome if self.usuario else None
        }
