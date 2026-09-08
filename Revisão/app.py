from flask import *
from ClienteRepository import *
lista = listar_clientes()

app = Flask(__name__)

@app.route("/")
def sobre():
    return render_template("sobre.html")

@app.route("/clientes")
def listar_clientes():
    return render_template("lista_clientes.html", clientes=lista)

@app.route("/cliente/<int:id>")
def buscar_cliente(id):
    return f"Mostrando cliente com o ID {id}"

if __name__ == "__main__":
    app.run(debug=True)