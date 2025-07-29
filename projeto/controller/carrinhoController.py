from projeto.model.carrinho import Carrinho
from projeto.controller.produtoController import ProdutoController
from projeto.model.produto import Produto
from projeto.model.pedido import Pedido, PedidoItem
from projeto.extension.extensoes import db
from flask import current_app, session
import os

class CarrinhoController:
    def __init__(self):
        self.__carrinho = []
        self.__total = 0


    def adicionar_carrinho(self, carrinho):
        encontrado = False
        for item in carrinho:
            for iten in self.__carrinho:
                
                if iten['id'] == item['id']:
                    iten['quantidade'] += item['quantidade']
                    encontrado = True

            if not encontrado:  
                produto = Produto.query.filter_by(id_produto = item['id']).first()
                novo_item = {
                    'id': item['id'],
                    'nome': produto.sabor,
                    'categoria': produto.categoria,
                    'preco': float(produto.preco),
                    'peso': produto.peso,
                    'foto': produto.foto,
                    'quantidade': item['quantidade']
                }
                self.__carrinho.append(novo_item)
        print('carrinho ',carrinho)
        return True
    
    @property
    def lista_carrinho(self):
        return self.__carrinho
    @property
    def total_pagar(self):
        return self.__total
    
    def atualiza(self, carrinho):
        itens = self.__carrinho
        for item in itens:
            for item_carrinho in carrinho:
                if item['id'] == item_carrinho['id']:
                    item['quantidade'] = item_carrinho['quantidade']
        return True
    
    def total(self):
        self.__total = 0
        itens = self.__carrinho
        for item in itens:
            numero = round(float(item['preco']) * int(item['quantidade']), 2)
            self.__total += numero
        return self.__total
    
    def finalizar_pedido(self, nome, telefone):
        itens = self.__carrinho
        total = self.__total
        novo_pedido = Pedido(nome = nome, telefone = telefone, total_pagar = float(total))
        db.session.add(novo_pedido)
        db.session.commit()

        
        
        for item in itens:
            novo_item = PedidoItem(id_pedido = novo_pedido.id, nome_produto = item['nome'], categoria = item['categoria'], preco_produto = float(item['preco']), quantidade = item['quantidade'], nome_usuario = nome)
            db.session.add(novo_item)
            db.session.commit()
        self.__carrinho = []
        return True
    
    def exclui_pedido(self, id):
        itens  = self.__carrinho
        for item in itens:
            if item['id'] == id:
                self.__carrinho.remove(item)
        return True
    
    #@staticmethod
    #def adicionar_carrinho(carrinho):
    #    for item in carrinho:
    #        novo_card = Carrinho(id_usuario = session['id'], id_produto = item['id'], quantidade = int(item['quantidade']))
    #        db.session.add(novo_card)
    #        db.session.commit()
    #    return True
    #
    #@staticmethod
    #def listar_carrinho():
    #    id = session['id']
    #    itens = Carrinho.query.filter_by(id_usuario = id).all()
    #    
    #    return itens
    #
    #@staticmethod
    #def excluir_carrinho(id):
    #    itens = Carrinho.query.filter_by(id_usuario = session['id'], id_produto = id).first()
    #    db.session.delete(itens)
    #    db.session.commit()
    #    return True
    #@staticmethod
    #def atualiza_quant(id, quant):
    #    itens = Carrinho.query.all()
    #    for item in itens:
    #        if id == item.id:
    #            item.quantidade = quant
    #            db.session.commit()
#
    #    return True
#

      
            
        

