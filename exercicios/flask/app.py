from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True)