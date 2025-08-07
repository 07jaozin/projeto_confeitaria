from projeto.model.produto import Produto
from projeto.model.pedido import Pedido, PedidoItem
from projeto.extension.extensoes import db
from flask import session

class CarrinhoController:

    @staticmethod
    def init_session():
        if 'carrinho' not in session:
            session['carrinho'] = []
        if 'total' not in session:
            session['total'] = 0

    @staticmethod
    def adicionar_carrinho(carrinho):
        CarrinhoController.init_session()
        for item in carrinho:
            encontrado = False
            for iten in session['carrinho']:
                if int(iten['id']) == int(item['id']):
                    iten['quantidade'] += item['quantidade']
                    session.modified = True
                    encontrado = True
                    break

            if not encontrado:
                produto = Produto.query.filter_by(id_produto=item['id']).first()
                novo_item = {
                    'id': item['id'],
                    'nome': produto.sabor,
                    'categoria': produto.categoria,
                    'preco': float(produto.preco),
                    'peso': produto.peso,
                    'foto': produto.foto,
                    'quantidade': item['quantidade']
                }
                session['carrinho'].append(novo_item)
                session.modified = True
        return True

    @staticmethod
    def lista_carrinho():
        CarrinhoController.init_session()
        return session['carrinho']

    @staticmethod
    def total_pagar():
        CarrinhoController.init_session()
        return session['total']

    @staticmethod
    def atualiza(carrinho):
        CarrinhoController.init_session()
        for item in session['carrinho']:
            for item_carrinho in carrinho:
                if int(item['id']) == int(item_carrinho['id']):
                    item['quantidade'] = item_carrinho['quantidade']
                    session.modified = True
        return True

    @staticmethod
    def total():
        CarrinhoController.init_session()
        total = 0
        for item in session['carrinho']:
            valor = round(float(item['preco']) * int(item['quantidade']), 2)
            total += valor
        session['total'] = total
        session.modified = True
        return total

    @staticmethod
    def finalizar_pedido(nome, telefone):
        CarrinhoController.init_session()
        itens = session['carrinho']
        total = session['total']

        novo_pedido = Pedido(nome=nome, telefone=telefone, total_pagar=float(total))
        db.session.add(novo_pedido)
        db.session.commit()

        for item in itens:
            novo_item = PedidoItem(
                id_pedido=novo_pedido.id,
                nome_produto=item['nome'],
                categoria=item['categoria'],
                preco_produto=float(item['preco']),
                quantidade=item['quantidade'],
                nome_usuario=nome
            )
            db.session.add(novo_item)

        db.session.commit()
        session['carrinho'] = []
        session['total'] = 0
        session.modified = True
        return True

    @staticmethod
    def exclui_pedido(id):
        CarrinhoController.init_session()
        session['carrinho'] = [item for item in session['carrinho'] if int(item['id']) != int(id)]
        session.modified = True
        return True
