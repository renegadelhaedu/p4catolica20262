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

#executando o servidor
app.run()