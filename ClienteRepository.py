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