nomes = ['João', 'Ana', 'Camila', 'Joana']
for nome in nomes:  # for - para nome numa lista
    print(nome)
for item in range(len(nomes)):
    print(nomes[item])

lista_n = range(5)
for i in lista_n:
    print(i)
lista_n1 = range(5, 10, 2)  # vai do 5 ao 9 de dois em dois
for i in lista_n1:
    print(i)

i1 = 0
while i1 < 10:  # while - enquanto
    print('i ainda é menor que 10:', i1)
    i1 = i1 + 1
print('Acabou o while, o valor final de i1 é ',i1)
while True:
    print(i1)
    if i1 == 20:
        break  # break - parar
    i1 += 1

'''
Exercício:
Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista 
de convidados.
Após isso irá imprimir todos os nomes numa lista.
'''
n2 = input('Quantas pessoas você pretende convidar? Por favor digite aqui:')
print('Por favor digite os nomes dos convidados.')
l = []
i2 = 1
while i2 <= int(n2):
    nc = input('Convidado '+ str(i2) +':')
    l.append(nc)
    i2 += 1
print('Serão ', n2,' convidados.')
print('\nLISTA DE CONVIDADOS')
for nc in l:
    print(nc)
