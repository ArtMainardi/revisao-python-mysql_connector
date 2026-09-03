import mysql.connector

def iniciar():
    conexao = None
    try:
        conexao = mysql.connector.connect()
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXIST Cliente(
                id_cliente INT PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(50) NOT NULL,
                email VARCHAR(255) UNIQUE,
                telefone CHAR(14) UNIQUE
            );
        ''')
    except Exception as error:
        print(f"ERRO: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()