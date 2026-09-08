import mysql.connector
from config import DB_CONFIG

def conectar():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cardapio (
              id int PRIMARY KEY AUTO_INCREMENT,
              nome varchar(100) NOT NULL,
              preco decimal(10,2) NOT NULL,
              tipo varchar(30) DEFAULT NULL,
              disponivel boolean DEFAULT TRUE
            );
        ''')

        return conexao
    except Exception as error:
        print("ERRO: " + error)
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

conectar()