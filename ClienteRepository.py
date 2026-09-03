import mysql.connector
from config import DB_CONFIG
from models.Cliente import Cliente
from banco import iniciar

def cadastrar_cliente(cliente):
    iniciar()
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()

        cursor.execute('''
            INSERT INTO Cliente(nome, email, telefone) VALUES (%s, %s, %s)
        ''', (cliente.converter_tupla()))

        conexao.commit()
        print("Cliente cadastrado com sucesso!")
    except Exception as error:
        print(f"Erro: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def listar_clientes():
    iniciar()
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT * FROM Cliente
        ''')
        listaDB = cursor.fetchall()
        lista = []

        if len(listaDB) != 0:
            print("\n== Lista de Clientes ==")
            for c in listaDB:
                lista.append(Cliente.reverter_tupla(c))
                print(Cliente.reverter_tupla(c).exibir())
            return lista
        else:
            print("Nenhum cliente cadastrado encontrado!")
    except Exception as error:
        print(f"Erro: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_por_id(id):
    iniciar()
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT * FROM Cliente WHERE id_cliente = %s
        ''', (id,))
        cliente = cursor.fetchone()

        if cliente:
            print(cliente)
            return Cliente.reverter_tupla(cliente)
        return None
    except Exception as error:
        print(f"ERRO: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()