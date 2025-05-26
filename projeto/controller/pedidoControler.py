from projeto.model.carrinho import Carrinho
from projeto.controller.carrinhoController import CarrinhoController
from projeto.model.pedido import Pedido, PedidoItem
from projeto.app import db
from flask import current_app, session
import os

carrinhoControler = CarrinhoController()

class PedidoController:

   
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
       

    