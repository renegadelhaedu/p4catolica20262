from datetime import datetime

from configdb import db


class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    criada_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    usuario = db.relationship('Usuario', backref=db.backref('avaliacoes', lazy=True))
