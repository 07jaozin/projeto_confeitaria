from projeto.model.pessoas import Pessoas
from projeto.app import db
from flask import session, flash

class PessoasController:
    @staticmethod
    def cadastrar_usuario(nome, telefone):
        
        pessoa = Pessoas.query.filter_by(telefone = telefone).first()
        if pessoa:
            flash("Esse numero de telefone ja esta cadastrado")
            return False
        else:
            novo_usuario = Pessoas( nome = nome, telefone = telefone)
            db.session.add(novo_usuario)
            db.session.commit()
            session['id'] = novo_usuario.id
            session['logado'] = True
            session['nome'] = nome
            print(novo_usuario.id)
            return True
        
    @staticmethod
    def login_usuario(nome, telefone):
        usuario = Pessoas.query.filter_by(nome = nome, telefone = telefone).first()
        if nome == 'ola' and telefone == '(16)99299-2992':
            session['adm'] = True
            return 'adm'
        if usuario:
            session['id'] = usuario.id
            session['logado'] = True
            session['nome'] = nome
            return 'usuario'
        else:
            return None
    
    @staticmethod
    def listar_todos():
        usuario = Pessoas.query.all()
        return usuario
    
    