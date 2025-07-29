from projeto.model.carrinho import Carrinho
from projeto.controller.carrinhoController import CarrinhoController
from projeto.model.pedido import Pedido, PedidoItem
from projeto.extension.extensoes import db
from flask import current_app, session
import os
from datetime import date

carrinhoControler = CarrinhoController()

class PedidoController:

   
   @staticmethod
   def listar_pedidos():
        pedidos = Pedido.query.all()
        return pedidos
   @staticmethod
   def listar_pedidosItem():
        pedidos = PedidoItem.query.all()
        return pedidos
    
   @staticmethod 
   def listar_pedidos_hoje():
        data = date.today()
        produtos = Pedido.query.filter_by(data = data).all()

        return produtos
       

    