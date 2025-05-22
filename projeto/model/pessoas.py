from projeto.extension.extensoes import db

class Pessoas(db.Model):
   id = db.Column(db.Integer, primary_key = True, autoincrement = True)
   nome = db.Column(db.String(100), nullable = False)
   telefone = db.Column(db.String(15), unique = True, nullable = False)