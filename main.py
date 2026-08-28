#instalar:
#pip install flask
#importar o flask
from flask import *

#instanciar o servidor flask
app = Flask(__name__)

#decorator do flask para declarar rotas/endpoints da web app
@app.route('/')
def pagina_principal():
    return render_template('principal.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cadastrarusuario', methods=['POST', 'GET'])
def cadastrarusuario():
    if request.method == 'GET':
        return render_template('cadastrarusuario.html')

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

    return render_template('principal.html')


#executando o servidor
app.run(host='0.0.0.0')