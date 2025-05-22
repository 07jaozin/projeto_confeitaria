from projeto.extension.extensoes import db
from projeto.model.pessoas import Pessoas
from projeto.model.produto import Produto


class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('pessoas.id'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id_produto'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    

    # Relações
    usuario = db.relationship('Pessoas', backref=db.backref('carrinho', lazy=True))
    produto = db.relationship('Produto', backref=db.backref('carrinho', lazy=True))
    

