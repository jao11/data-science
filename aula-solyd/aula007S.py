print('Olá mundo!')


# Vamos definir uma função:
def soma(numero1, numero2):  # def - definir
    resp = numero1 + numero2
    return resp


# com isso criamos uma função e podemos usa-la sem repetir o programa
variavel = soma(75, 1200)
print(variavel)


def im():  # Esse seria um método pois não tem o retorno
    print('OI')


im()


def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False


print(tem_sete_itens('Camila.'))

'''
Exercício:
Escreva uma função que recebe um objeto de coleção e retorna o valor do maior número 
dentro dessa coleção. Faça outra função que retorna o menor número dessa coleção.
'''


def maior(x):
    mi = x[0]
    for it in x:
        if it > mi:
            mi = it
    return mi


print(maior([129, 19, 13, 18, 1, 39, 23]))


def menor(x):
    mi = x[0]
    for it in x:
        if it < mi:
            mi = it
    return mi


print(menor([212,132,345,7,8,23,4,67,4,34,3,7,0]))