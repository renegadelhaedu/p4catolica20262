#instalar:
#pip install flask
#importar o flask
from flask import *
from modelos.usuario import Usuario

us1 = Usuario('diego', 'd@d', '1', '123')
us2 = Usuario('alan', 'a@d', '2', '123')
us3 = Usuario('maria', 'm@d', '3', '123')
usuarios = [us1, us2, us3]

#instanciar o servidor flask
app = Flask(__name__)

#decorator do flask para declarar rotas/endpoints da web app
@app.route('/')
def pagina_principal():
    return render_template('index.html')



#1-verificar que o usuário está querendo exibir a página de cadastro, retornando a pag html
#2-via post, possa receber as informaçoes do formulário para que seja cadastrado no BD o usuário
@app.route('/cadastrarusuario', methods=['POST', 'GET'])
def cadastrarusuario():
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
    #usuarios = ['miro','diego','eduarda','alisson','gabriel']
    #puxei do banco de dados

    return render_template('listarusuarios.html', usuarios=usuarios)

@app.route('/detalharusuario/<idusuario>')
def detalharusuario(idusuario):
    print('ID:', idusuario)
    #forma provisória de buscar o objeto dado o interesse do usuário
    for u in usuarios:
        if u.id == idusuario:
            return render_template('detalharusuario.html', usuario=u)

    #busco no banco de dados o objeto pelo ID
    #retornar uma pagina com as informaçoes do objeto
    us2 = Usuario('alan', 'a@d', '2', '123')
    return render_template('detalharusuario.html')



#executando o servidor
app.run(host='0.0.0.0')