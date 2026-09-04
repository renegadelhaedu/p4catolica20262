#instalar:
#pip install flask
#importar o flask
from flask import *
from modelos.usuario import Usuario
from configdb import db
#instanciar o servidor flask
app = Flask(__name__)
app.secret_key = 'EGUyfgA786#' #colocaremos este valor dentro de um arquivo .env

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/p4catolicaweb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)


#decorator do flask para declarar rotas/endpoints da web app
@app.route('/')
def pagina_principal():
    return render_template('index.html')

#mesmo endpoint/rota declarada no formulário da página principal
@app.route('/login', methods=['POST','GET'])
def fazer_login():
    if session.get('login'):
        return render_template('principal.html')

    email = request.form.get('email')
    senha = request.form.get('senha')
    #vamos usar um biblioteca para criptografar esta senha e guardar criptografada no BD

    if email == 'renegadelha@gmail.com' and senha == '123':
        session['login'] = email
        return render_template('principal.html')
    else:
        return render_template('index.html', mensagem= 'Erro ao fazer login')

@app.route('/logout')
def logout():
    session.pop('login', None)
    return render_template('index.html')


#1-verificar que o usuário está querendo exibir a página de cadastro, retornando a pag html
#2-via post, possa receber as informaçoes do formulário para que seja cadastrado no BD o usuário
@app.route('/cadastrarusuario', methods=['POST', 'GET'])
def cadastrarusuario():
    if session.get('login') is None:
        print('voce nao está logado')
        return render_template('index.html')

    if request.method == 'GET':
        return render_template('cadastrarusuario.html')

    #aqui as informações estão vindo do form e são capturadas
    nome = request.form.get('nome')
    email = request.form.get('email')
    nascimento = request.form.get('nascimento')
    senha = request.form.get('senha')
    confirma = request.form.get('confirma')
    print(nome,email,nascimento,senha,confirma)
    if senha == confirma:
        print('cadastrou')
        msg = 'usuário cadastrado com sucesso!'
    else:
        print('NAO cadastrou')
        msg = 'Erro no cadastro de usuário!'
    #futuramente iremos salvar no BD
    return render_template('principal.html', mensagem=msg)

@app.route('/listarusuarios')
def listarusuarios():
    if session.get('login') is None:
        print('voce nao está logado')
        return render_template('index.html')
    #usuarios = ['miro','diego','eduarda','alisson','gabriel']
    #puxei do banco de dados
    return render_template('listarusuarios.html', usuarios=[])

@app.route('/detalharusuario/<idusuario>')
def detalharusuario(idusuario):
    if session.get('login') is None:
        print('voce nao está logado')
        return render_template('index.html')


    #busco no banco de dados o objeto pelo ID
    #retornar uma pagina com as informaçoes do objeto
    us2 = Usuario('alan', 'a@d', '2', '123')
    return render_template('detalharusuario.html')



#executando o servidor
app.run(host='0.0.0.0')