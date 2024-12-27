from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "Bem-vindo ao flask!"

@app.route("/about")
def about():
    return "Pagina about-me"

@app.route("/page/<nome>")
def page(nome):
    return render_template("index.html", nome=nome)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        nome = request.form.get("nome")
        return f"Olá, {nome}!"
    return '''
    <form method="post">
        Nome: <input type="text" name="nome">
        <input type="submit">
    </form>
    '''
    
@app.route("/api/tarefas")
def api_tarefas():
    tarefas = [{"id": 1, "descricao": "Estudar Flask"}]
    return jsonify(tarefas)    


connexion = sqlite3.connect("tarefas.db")
cursor = connexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, descricao TEXT)")
connexion.commit()
connexion.close()


if __name__ == "__main__":
    app.run(debug=True)