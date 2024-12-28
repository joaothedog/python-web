from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#modelagem de tarefa usando classe
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)

#renderiza todas as tarefas
@app.route("/")
def index():
    tarefas = Tarefa.query.all() #semelhante ao fetchall
    return render_template("index.html", tarefas=tarefas)

#adicionar tarefas
@app.route("/add", methods=["POST"])
def add():
    descricao = request.form["descricao"]
    nova_tarefa = Tarefa(descricao=descricao)
    db.session.add(nova_tarefa) # semelhante ao insert do sql
    db.session.commit() # submente a transacao no bd
    return redirect(url_for("index"))

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    tarefa = Tarefa.query.get(id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all() #cria tabelas caso nao existam
    app.run(debug=True)