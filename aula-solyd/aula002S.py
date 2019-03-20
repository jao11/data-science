print('olá mundo!\tsegundo print')
nome = 'João'
idade = 27
tipo_nome = type(nome)
tipo_idade = type(idade)
print(nome)
print(idade)
print(tipo_nome, tipo_idade)
n = input('Escreva seu nome:')
print(n,' é o seu nome.')
'''
 Exercícios: Faça um formulário que pergunte o nome, o cpf, o endereço,
 a idade, a altura e o telefone e imprima isso em um relatorio organizado.
'''
n1 = input('Por favor digite o seu nome:')
c1 = input('Seu cpf:')
e1 = input('Seu endereço:')
i1 = input('Sua idade:')
h1 = input('Sua altura:')
t1 = input('E por ultimo seu telefone:')
print('Por favor, verifique se está tudo correto:'
      '\nnome:{}\ncpf:{}\nendereço:{}\nidade:{}\naltura:{}'
      '\ntelefone:{}.'.format(n1, c1, e1, i1, h1, t1))
