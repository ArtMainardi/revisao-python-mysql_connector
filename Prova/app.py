from flask import *
from Prova.cardapio import *
lista = listar_itens()
app = Flask(__name__)

@app.route("/")
def tela_inicial():
    return render_template("tela_inicial.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/itens")
def listar_itens():
    return render_template("lista_itens.html", itens=lista)

@app.route("/cliente/<int:id>")
def buscar_cliente(id):
    return f"Mostrando cliente com o ID {id}"

if __name__ == "__main__":
    app.run(debug=True)