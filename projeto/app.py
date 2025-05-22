from flask import Flask, request, redirect, flash, render_template, session, jsonify
from projeto.extension.extensoes import db
from projeto.controller.appController import PessoasController
from projeto.config.config import Config
from projeto.controller.produtoController import ProdutoController
from projeto.controller.carrinhoController import CarrinhoController
from projeto.controller.pedidoControler import PedidoController
from projeto.model.pedido import Pedido, PedidoItem


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

usuarioController = PessoasController()
produtosController = ProdutoController()
carrinhoControler = CarrinhoController()
pedidoControler = PedidoController()

with app.app_context():  
    

    #db.drop_all() #apaga todos os dados
    db.create_all()  
    Pedido.__table__.drop(db.engine)
    
    



@app.route('/')
def principal():
    
    return render_template("principal.html", produto = produtosController.listar_todos())
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
       nome = request.form.get('nome-login')
       telefone_original = request.form.get('telefone-login')
       nomeSemEspacos = nome.strip()
       nome_ajustado = nomeSemEspacos.lower()
       telefone = telefone_original.replace(" ","")

       if carrinhoControler.finalizar_pedido(nome_ajustado, telefone):
           return redirect('/')
       else:
           flash("dados incorretos")
           return redirect('/login')
    else:
        total = carrinhoControler.total()
        return render_template("login.html", total = total)
    
@app.route('/cadastrar', methods = ['POST'])
def cadastrar():
    nome = request.form.get('nome')
    telefone_original = request.form.get('telefone')
    nomeSemEspacos = nome.strip()
    nome_ajustado = nomeSemEspacos.lower()
    telefone = telefone_original.replace(" ","")

    if usuarioController.cadastrar_usuario(nome_ajustado, telefone):
        return redirect('/')
    else:
        return redirect('/login')

@app.route('/carrinho')
def carrinho():
    itens = carrinhoControler.lista_carrinho
    
    return render_template("carrinho.html", itens = itens)
   

@app.route('/gerenciamento', methods = ['GET', 'POST'])
def gerenciamento():
    if 'logado' not in session:
      return redirect('/')
    if request.method == 'POST':
        sabor = request.form.get('sabor')
        categoria = request.form.get('categoria')
        preco = request.form.get('preco')
        peso = request.form.get('peso')
        foto = request.files['foto']
        if produtosController.cadastrar_produto(sabor, categoria, preco, peso, foto):

            return redirect('/')
        else:
            return "erro ao cadastrar o produto", 404
    else:
        return render_template("gerenciamento.html", produto = produtosController.listar_todos(), clientes = usuarioController.listar_todos(), pedido = pedidoControler.listar_pedidos(), pedidoItem = pedidoControler.listar_pedidosItem())

@app.route('/excluir_produto/<int:id>')
def excluir_produto(id):
    if 'logado' not in session:
      return redirect('/')
    produtosController.excluir_produto(id)
    return redirect('/gerenciamento')

@app.route('/editar_produto/<int:id>', methods = ['GET', 'POST'])
def editar_produto(id):
    if 'logado' not in session:
      return redirect('/')
    if request.method == 'POST':
        sabor = request.form.get('sabor-editar')
        categoria = request.form.get('categoria-editar')
        preco = request.form.get('preco-editar')
        peso = request.form.get('peso-editar')
        foto = request.files['foto-editar']
        if produtosController.editar_produto(id, sabor, categoria, preco, peso, foto):
            return redirect('/gerenciamento')
        else:
            return "erro ao editar produto", 404
    else:
        return render_template("editar.html", produto = produtosController.buscar_produto(id))
    

@app.route('/adiciona_carrinho', methods = ['POST'])
def adiciona_carrinho():
    carrinho = request.get_json()
    carrinhoControler.adicionar_carrinho(carrinho)
    print(carrinho)
    return redirect('/')
@app.route('/exclui_carrinho', methods = ['POST'])
def exclui_carrinho():
    item = request.get_json()
    carrinhoControler.exclui_pedido(item)
    print(carrinho)
    return redirect('/')
@app.route('/atualiza_carrinho', methods = ['POST'])
def atualiza_carrinho():
    carrinho = request.get_json()
    carrinhoControler.atualiza(carrinho)
    print(carrinho)
    return "certo"
@app.route('/autenticacao', methods = ['POST', 'GET'])
def autenticacao():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        if produtosController.autenticacao(nome,senha):
            return redirect('/gerenciamento')
        else:
            return redirect('/autenticacao')
    else:
        return render_template("autenticacao.html")


@app.route('/logout')
def logout():
    if 'logado' not in session:
      return redirect('/')
    session.pop('nome', default=None)
    session.pop('logado', default=None)
    session.pop('enviado', default=None)
    session.pop('id', default=None)
    session.pop('adm', default=None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)