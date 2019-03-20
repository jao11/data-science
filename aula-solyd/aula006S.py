minha_lista = ['Jo', 'Pe']  # LISTA (list) essa lista é mutável
minha_tupla = ('Jo', 'Pe')  # TUPLA (tuple) essa lista não é mutável
meu_dicionario = {'nome': 'Jo', 'idade': 24}  # DICIONÁRIO (dict) marca: valor
meu_conjunto = {'Jo','Pe'}  # CONJUNTO (set) igual a lista mas sem elementos repetidos
                            # e não tem ordem.
if 'Jo' in meu_dicionario.values():
    print('Jo está no dicionário.')
for valores in meu_dicionario.keys():
    print(valores)
for valores in meu_dicionario.values():
    print(valores)
meu_dicionario['telefone'] = 979848975  # isso adiciona coisas no dicionário.
print(meu_dicionario)
meu_conjunto.add('Maria')

lista = []
tupla = ()
dicionario = {}
