from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


# conectar no bd
def get_db_cnc():
    cnnc = sqlite3.connect("produtos.db")
    cnnc.row_factory = sqlite3.Row
    return cnnc


@app.before_request
def setup_database():
    cnnc = get_db_cnc()
    cnnc.execute(
        """CREATE TABLE IF NOT EXISTS produtos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        preco REAL NOT NULL,
                        descricao TEXT
                    )"""
    )
    cnnc.close()


@app.route("/")
def index():
    cnnc = get_db_cnc()
    produtos = cnnc.execute("SELECT * FROM produtos").fetchall()
    cnnc.close()
    return render_template("index.html", produtos=produtos)


# criar novo produto
@app.route("/add", methods=["POST"])
def adicionar():
    nome = request.form["nome"]
    preco = request.form["preco"]
    descricao = request.form.get("descricao", "")

    if not nome or not preco:
        return "Nome e preco sao obrigatorios!", 400

    cnnc = get_db_cnc()
    cnnc.execute(
        "INSERT INTO produtos (nome, preco, descricao) VALUES (?, ?, ?)",
        (nome, float(preco), descricao),
    )
    cnnc.commit()  # submeter a transacao dentro do bd
    cnnc.close()
    return redirect(
        url_for("index")
    )  # apos a adicao de um produto no bd ele redireciona para a index que renderiza os produtos


# deletar um produto
@app.route("/deletar/<int:id>", methods=["POST"])
def deletar(id):
    cnnc = get_db_cnc()
    cnnc.execute("DELETE FROM produtos WHERE id = ?", (id,))
    cnnc.commit()
    cnnc.close()
    return redirect(url_for("index"))


# rota para renderizar o formulario de edicao
@app.route("/editar/<int:id>")
def editar(id):
    cnnc = get_db_cnc()
    produto = cnnc.execute("SELECT * FROM produtos WHERE id = ?", (id,)).fetchone()
    cnnc.close()
    return render_template("editar.html", produto=produto)


@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    nome = request.form["nome"]
    preco = request.form["preco"]
    descricao = request.form.get("descricao", "")

    if not nome or not preco:
        return "Nome e preco sao obrigatorios", 400

    cnnc = get_db_cnc()
    cnnc.execute(
        "UPDATE produtos SET nome = ?, preco = ?, descricao = ? WHERE id = ?",
        (nome, float(preco), descricao, id),
    )
    cnnc.commit()
    cnnc.close()
    
    return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(debug=True)
