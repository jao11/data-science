'''
c
'''
import requests
import json

req = None
try:
    req = requests.get('http://www.omdbapi.com/?t=Interstellar')
except:
    print('Erro na conexão.')
    exit()

print(req.text)
dicionario = json.loads(req.text)
print(dicionario)