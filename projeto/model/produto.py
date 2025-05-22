from projeto.extension.extensoes import db

class Produto(db.Model):
    id_produto = db.Column(db.Integer, primary_key = True,  autoincrement = True)
    sabor = db.Column(db.String(100), nullable = False)
    categoria = db.Column(db.String(100), nullable = False)
    preco = db.Column(db.Float, nullable = False)
    peso = db.Column(db.Integer, nullable = False)
    foto = db.Column(db.String(100), nullable = False)