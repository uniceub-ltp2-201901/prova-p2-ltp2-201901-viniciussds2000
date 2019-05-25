from flask import *
from random import *
from flaskext.mysql import MySQL
from BD import *

app = Flask(__name__)

mysql= MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD']= 'root'
app.config['MYSQL_DATABASE_DB']= 'prova2'

@app.route('/')
def pagina_inicial():
    randnum = (randint(10000, 99999))
    cursor = mysql.get_db().cursor()

    return render_template('home.html',rand=randnum,dados=get_dados(cursor))

@app.route('/<rand>', methods=['GET','POST'])
def encurtar(rand):
    if request.method == 'POST':
        projname = request.form.get('nomep')
        projdata = request.form.get('datap')
        descrição = request.form.get('desc')
        url = request.form.get('url')
        ct = 0
        contador = ct+1

    # Obtendo o cursor para acessar o BD
    conn = mysql.connect()
    cursor = conn.cursor()

    cadastrando(cursor, conn,projname,projdata,descrição,url,contador)

    # Fechar o cursor
    cursor.close()
    # Fechar a conexao
    conn.close()


    # retornando a lista de contatos
    return render_template('encurtado.html')







'''
    
    
    
    

@app.route('/<url>', methods=['GET','POST'])
def encurtar(url):
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')
        url = request.form.get('url')

        conn = mysql.connect()
        cursor = conn.cursor()

        cadastrando(cursor,conn,login,senha,url)


        cursor.close()
        conn.close()

        return render_template('encurtado.html')
    else:
        return render_template('home.html')
'''



if __name__ == '__main__':
    app.run(debug=True)