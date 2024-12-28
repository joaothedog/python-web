from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'pass'
db = SQLAlchemy(app)

#modelagem de usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)

#modelagem de tarefa usando classe
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        usuario = Usuario.query.filter_by(nome=nome).first()
        if usuario and check_password_hash(usuario.senha, senha):
            session["usuario_id"] = usuario.id
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("index"))
        else:
            flash("Usuario ou senha incorreta", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario_id", None)
    flash("Logout realizado com sucesso!", "info")
    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nome = request.form["nome"]
        senha = generate_password_hash(request.form["senha"])
        novo_usuario = Usuario(nome=nome, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        flash("Usuário registrado com sucesso!", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

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