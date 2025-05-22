from projeto.model.carrinho import Carrinho
from projeto.controller.carrinhoController import CarrinhoController
from projeto.model.pedido import Pedido, PedidoItem
from projeto.app import db
from flask import current_app, session
import os

carrinhoControler = CarrinhoController()

class PedidoController:

    @staticmethod
    def finalizar_pedido(nome, telefone):
        item = carrinhoControler.lista_carrinho
        print(item)
        

        #total = carrinho.total_pagar
        #novo_pedido = Pedido(nome = nome, telefone = telefone, total_pagar = total)
        #db.session.add(novo_pedido)
        #db.session.commit()
#
        #pedido = carrinho.lista_carrinho
        #print(pedido)
        #for item in pedido:
        #    novo_item = PedidoItem(id_pedido = novo_pedido.id, nome_produto = item['nome'], categoria = item['categoria'], preco_produto = item['preco'], quantidade = item['quantidade'], nome_usuario = nome)
        #    db.session.add(novo_item)
        #    db.session.commit()
#
        #return True
    @staticmethod
    def listar_pedidosItem():
        pedidos = PedidoItem.query.all()
        print(pedidos)
        return pedidos
    @staticmethod
    def listar_pedidos():
        pedidos = Pedido.query.all()
        print(pedidos)
        return pedidos
       

    