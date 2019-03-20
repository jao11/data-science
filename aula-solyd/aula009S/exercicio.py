'''
Exercício:
Crie um software de gerenciamento bancário;
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo.
'''
print('                   Informações do Cliente                     ')

from cliente import Cliente

usuario = Cliente('João', 14285740770, 24)
print('Nome do cliente:', usuario.nome)
print('cpf:', usuario.cpf)
print('Idade do cliente:', usuario.idade)

print('                 Informações da conta do Cliente 2                 ')


from conta import Conta

cc = Conta('Camila', 14085950670, 22, 100000.00, 1000.00)
print('Nome do cliente:', cc.nome)
print('cpf:', cc.cpf)
print('Idade do cliente:', cc.idade)
print('Saldo da CC:R${:.2f}'.format(cc.saldo))
print('limite do cheque especial:R${:.2f}'.format(cc.limite))

retirada = input('Qual o valor da retirada.\nDigite aqui: R$')

cc.sacar(retirada)
print('Seu novo saldo é R${:.2f}'.format(cc.saldo))

deposit = input('Qual o valor que você deseja depositar?\nDigite aqui:R$')

cc.deposito(deposit)
print('Seu novo saldo é R${:.2f}'.format(cc.saldo))
