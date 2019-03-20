frase = 'Oi, tudo bem?'
lista_nomes = ['João', 'Camila', 'Maria', 'Joana']
print(lista_nomes[2])  # o colchete nessa situação serve para escreverparte da lista.
print(frase[0:10])  # com o dois pontos eu posso determinar de onde até a aonde ele
#  vai escrever quando eu executar.
print(frase[1:11:2])  # o segundo colchete diz ao pc de quantas em quantas casas ele
#  vai escrever.
print(lista_nomes[-2])  # se eu escrever os números negativos o programa vai escrever
#  de trá para a frente.
print(lista_nomes[-1:-3:-1])
print(frase[::-1])
lista_nomes.append('Paloma')  # o append serve para adicionar algo a lista.
print(lista_nomes)
lista_nomes.insert(1, 'Joana')
lista_nomes[0] = 'Cachaça'
contador_joana = lista_nomes.count('Joana')
print(lista_nomes)
print(contador_joana)
print(len(lista_nomes))  # a função len serve para contar os integrantes da lista.
print(len(frase))
