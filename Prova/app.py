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

@app.route("/itens/<int:id>")
def detalhes(id):
    i = buscar_por_id(id)
    return render_template("detalhes.html", item=i)

if __name__ == "__main__":
    app.run(debug=True)