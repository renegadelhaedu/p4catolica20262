import requests

for i in range(1000):
    resposta = requests.get('http://172.16.17.76:5000/')
    print(resposta.headers)
