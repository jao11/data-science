'''
Tratamentos de erros: erros de execução
'''
try:  # Tente - try : dessa maneira mesmo que aja erro o programa vai rodar.
    a = 12 / 0
except ZeroDivisionError:  # Exceto - except. Escrevendo somente o except ele é lido não
    # importa o erro, mas podemos especificar o tipo de erro que ele vai ler.
    print('Divisão por zero é indermininavel!')
try:
    adoefb()
except Exception as err:  # Exception tb pega qualquer erro
    print('Tem algo errado, que é:', err)
import time


def abre_arquivo():
    try:
        arquivo = open('arquivodoido.txt')
        return True
    except Exception as erro:
        print('Aconteceu algum erro', erro)
        return False


while not abre_arquivo():
    print('Tentando abrir o arquivo')
    time.sleep(5)

print('Consegui abrir o arquivo.')
#  Se nesse meio tempo eu criar esse arquivo o programa vai rodar.
