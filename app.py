from flask import Flask, render_template, request, redirect
from database import conectar

app = Flask(__name__,
            template_folder = 'front',
            static_folder = 'css',
            static_url_path = '/estilo'
            )

# LISTAR PRODUTOS (Entrega a página única do sistema)
@app.route('/')
def index():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("select * from produtos")
    produtos = cursor.fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

# FORMULÁRIO DE NOVO PRODUTO
@app.route('/novo')
def novo_produto():
    return render_template('novo_produto.html')

# INSERIR NO BANCO
@app.route('/salvar', methods=['post'])
def salva():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    preco = request.form['preco']
    
    conn = conectar()
    cursor = conn.cursor()
    sql = "insert into produtos(nome,quantidade,preco)values (%s, %s, %s)"
    valores = (nome, quantidade, preco)
    
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
