'''
Requisições web
'''
#  A função 'pip' serve para baixar novas bibliotecas.

import requests

requisicao = None
try:
    requisicao = requests.get('https://solyd.com.br')  # get = pegar
except Exception as e:
    print('Requisição deu erro:', e)

print(requisicao)
print(type(requisicao))
print(requisicao.status_code)  # pesquisar tabela de status_code!!
print(requisicao.text)  # acessa o código fonte , quando não abrir provavelmente o site
#  tem proteções contra esse tio de requisição
#  Sempre é bom usar o try - except nesse tipo de requisição...
try:
    requisicao = requests.get('https://g1.com.br')  # get = pegar
    print(requisicao.text)
except Exception as e:
    print('Requisição deu erro:', e)
#  Para ter mais informações sobre sites podemos procurar a
# 'biblioteca Beautiful Soup 4' ou BS4

texto = None
cabecalho = {'User-agent': 'Windows 12', 'referer': 'https://google.com'}
meus_cookies = {'Ultima-visita': '10-10-2020'}
dados = {'username': 'gui', 'password': 'gui321'}

try:
    requisicao = requests.get('https://putsreq.com/01buOagCGVcNgBUzFlZr',
                              headers=cabecalho, cookies=meus_cookies, data=dados)
    requisicao = requests.post('https://putsreq.com/01buOagCGVcNgBUzFlZr',
                               headers=cabecalho, cookies=meus_cookies, data=dados)
    texto = requisicao.text
except Exception as e:
    print('Algo deu errado:', e)
print(texto)
