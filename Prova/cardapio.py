import mysql.connector
from models import Item
from banco import conectar

def cadastrar_item(item):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''
            INSERT INTO cardapio(nome, preco, tipo, disponivel) VALUES (%s, %s, %s, %s)
        ''', (item.converter_tupla()))

        conexao.commit()
        print("Item cadastrado com sucesso!")
    except Exception as error:
        print(f"Erro: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def listar_itens():
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT * FROM cardapio
        ''')
        listaDB = cursor.fetchall()
        lista = []

        if len(listaDB) != 0:
            print("\n== Lista de Itens ==")
            for c in listaDB:
                lista.append(Item.reverter_tupla(c))
                print(Item.reverter_tupla(c).exibir())
            return lista
        else:
            print("Nenhum item cadastrado encontrado!")
    except Exception as error:
        print(f"Erro: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_por_id(id):
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''
            SELECT * FROM cardapio WHERE id = %s
        ''', (id,))
        item = cursor.fetchone()

        if item:
            i = Cliente.reverter_tupla(cliente)
            print(i.exibir())
            return i
        return None
    except Exception as error:
        print(f"ERRO: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()