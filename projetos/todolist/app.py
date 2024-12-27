from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# conexao com o banco de dados
def get_db_cnnc():
    cnnc = sqlite3.connect("tarefas.db")
    cnnc.row_factory = sqlite3.Row
    return cnnc

@app.route("/")
def index():
    cnnc = get_db_cnnc()
    tarefas = cnnc.execute("SELECT * FROM tarefas").fetchall()
    cnnc.close()
    return render_template("index.html", tarefas=tarefas)

@app.route("/add", methods=["POST"])
def add():
    descricao = request.form["descricao"]
    cnnc = get_db_cnnc()
    cnnc.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    cnnc.commit()
    cnnc.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    #CRIA A TABELA CASO NAO EXSITA NO BD
    cnnc = get_db_cnnc()
    cnnc.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, descricao TEXT)")
    cnnc.close()
    app.run(debug=True)