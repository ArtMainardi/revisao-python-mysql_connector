from flask import *

app = Flask(__name__)

@app.route("/")
def sobre():
    return render_template("sobre.html")

@app.route("/clientes")
def listar_clientes():
    return "Lista de clientes aqui"

@app.route("/cliente/<int:id>")
def buscar_cliente(id):
    return f"Mostrando cliente com o ID {id}"

if __name__ == "__main__":
    app.run(debug=True)