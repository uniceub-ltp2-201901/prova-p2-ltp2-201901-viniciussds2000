def cadastrando(cursor,conn,login,senha,descrição,url,ct):
    cursor.execute(f'INSERT into prova2.usuarios (login,senha,descrição,url,contador) VALUES ("{login}","{senha}","{descrição}","{url}","{ct}")')
    conn.commit()



def get_dados(cursor):
    cursor.execute(f'SELECT * FROM usuarios')
    dados = cursor.fetchall()

    return dados