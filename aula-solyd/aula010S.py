'''
Aula para aprender a manipular arquivos.
'''
open('arquivo.txt', 'w')  # serve para abrir arquivos, w - write -escrever, r - read - ler
# Colocando o 'r' da errado se existir arquivo, já o w cria um novo arquivo
# Se eu coloco o 'w' de novo ele vai sobrescrever o arquivo.
# O método 'r+' é para ler e escrever. Ele não cria um novo arquivo.
# O método 'a' é um método de escrita também mais diferente do w ele não sobrescreve o
# arquivo e sim adiciona coisas. Ele também cria um arquivo se este não existir.
# Para abrir um arquivo que não seja de texto devemos usar o modo 'b'.
arquivo = open('arquivo.txt', 'w')
arquivo.write('E ai pessoal, blz?')
a2 = open('a2.txt', 'w')
for i in range(0, 11):
    a2.write(str(i)+'\n')  # Se não colocar o barra n ele vai escrever tudo numa linha só.
a2 = open('a2.txt', 'r')
print(a2.read())
#  Para ler uma linha de cada vez devemos fazer como está abaixo.
#  For linha in arquivo:
#   print(linha)
#  Para ler uma imagem devemos escrever o 'b' junto com o 'r'
