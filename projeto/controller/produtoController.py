from projeto.model.produto import Produto
from projeto.extension.extensoes import db
from flask import current_app, session
import os
import cloudinary.uploader
from werkzeug.utils import secure_filename

class ProdutoController:
   
   
        
    @staticmethod
    def autenticacao(nome, senha):
        if nome.lower() == 'desen' and senha.lower() == 'desen':
            session['logado'] = True
            session['adm'] = True
            return True
        else:
            return False
    @staticmethod
    def cadastrar_produto(sabor, categoria, preco, peso, foto):
        preco_ajustado = preco.replace(",",".")
        novo_produto = Produto( sabor = sabor, categoria = categoria, preco = float(preco_ajustado), peso = int(peso) , foto = '')
        db.session.add(novo_produto)
        db.session.commit()
        
        extensao = os.path.splitext(foto.filename)[1]
        nome_arquivo = secure_filename(sabor.lower().replace(" ", "_"))
        nome_arquivo = f"{nome_arquivo}-{novo_produto.id_produto}{extensao}"
        result = cloudinary.uploader.upload(foto, public_id=nome_arquivo)
        
        

        novo_produto.foto = result['secure_url']
        db.session.commit()
        return True
    
    @staticmethod
    def listar_todos():
        produtos = Produto.query.all()
        return produtos
    
    @staticmethod
    def excluir_produto(id):
        produto = Produto.query.filter_by(id_produto = id).first()
        if produto:
            db.session.delete(produto)
            db.session.commit()
            return True
        else: 
            return "erro ao excluir o produto", 404
    
    @staticmethod
    def buscar_produto(id):
        produto = Produto.query.filter_by(id_produto = id).first()
        if produto:
            return produto
        else:
            return "erro ao tentar encontrar o produto", 404
        
    @staticmethod
    def editar_produto(id, sabor, categoria, preco, peso, foto):
        produto = Produto.query.filter_by(id_produto = id).first()
        if produto:
             produto.sabor = sabor
             produto.categoria = categoria
             produto.preco = preco
             produto.peso = peso
             if foto.filename == '':
               db.session.commit()

             else:
               extensao = os.path.splitext(foto.filename)[1]
               nome = secure_filename(sabor.lower().replace(" ", "_"))
               nome_arquivo = f"{nome}-{produto.id_produto}{extensao}"
               result = cloudinary.uploader.upload(foto, public_id=nome_arquivo)
               produto.foto = result['secure_url']
               db.session.commit()

             return True
        else:
            return "produto nao encontrado", 404
                
            



