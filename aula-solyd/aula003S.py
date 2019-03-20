# Comparações: == igual, != diferente, > maior que, < menor que,
# >= maior ou igual, <= menor ou igual, and - e, or - ou.
var_verdade = True # booleano
var_falso = False
print(type(var_verdade), type(var_falso))
if var_verdade == True:  # if = se
    print('var_verdade é verdadeiro.')

a = 2
b = 12
if a > b:
    print('{} é maior que {}'.format(a,b))
else:   # else = se não
    print('{} não é maior que {}'.format(a,b))

print('Menu:\n 1. picanha\n 2. sushi\n 3. lasanha')
n = input('escolha um dos pratos:')
if n == '1':
    print('Sua picanha chegará daqui a pouco.')
elif n == '2':
    print("Seus sushis chegaram daqui a pouco.")
elif n == '3':
    print('Sua lasanha chegará daqui a pouco.')
else:
    print('Opção invalida.')

idade = 50
if not idade == 50:
    print('Você não tem 50 anos')
else:
    print('Você tem 50 anos')

'''
Exercício:
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e 
decide se ela está apta a ser do exercito.
Para entrar no exercito é preciso ter mais de 18 anos, pesar mais ou 
igual a 60kg e medir mais ou igual 1.70m.
'''
print('Por favor preencha a lista abaixo')
i = input('Idade:')
p = input('Peso:')
h = input('Altura:')
if not (i > '18'):
    print('Você não pode entrar no exercito.')
if not (p >= '60'):
    print('Você não pode entrar no exercito.')
if not (h >= '1.70'):
    print('Você não pode entrar no exercito.')
else:
    print('Você está apto a entrar no exercito.')
