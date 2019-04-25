# Crie um algoritmo que leia os nomes e preços dos produtos de uma loja e que escreva o

# nome do produto mais caro. Considere que o final da lista é marcado pelo produto 'XXX'

# e que não existem preços repetidos.



entra_dados = 'sim'  # 'sim' para entrar no while

nome = 0

preço = 0

produto_preço = {nome: preço}  # isso é um dicionario {key: valor}



while entra_dados == 'sim':

    nome = input('Digite o nome do produto:')

    preço = float(input('Digite o preço do(a) {}:'.format(nome)))

    produto_preço[nome] = preço  # Isso adiciona a key(nome) e um valor(preço) para ela

    entra_dados = input('Quer adicionar mais produtos?\nResponda sim ou 
