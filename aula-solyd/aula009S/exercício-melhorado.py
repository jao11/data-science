'''
Exercício:
Crie um software de gerenciamento bancário;
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo.
'''

print('\f\fBem vindo(a) ao seu Banco pessoal\f\f')
r = input('Você é nosso cliente?\nResponda 1 para sim ou 2 para não: ')
if '1' == r:
    n = input('Seu nome:')
    cpf = input('Seu cpf:')
    i = input('Sua idade:')
    from cliente import Cliente

    usuario = Cliente(n, cpf, i)
    print('Por favor confirme as informações para prosseguir.')
    print('Nome do cliente:', usuario.nome)
    print('cpf:', usuario.cpf)
    print('Idade do cliente:', usuario.idade)
    o = input('Suas informações estão corretas?\nDigite 1 para sim e 2 para não\nDigite aqui:')
    if '1' == o:
        print('Sua cc é a conta número 002244-6')
        o1 = input('Confirma?\nDigite 1 para sim e 2 para não\nDigite aqui:')
        if '1' == o1:
            from conta import Conta

            cc = Conta(n, cpf, i, 100.00, 1000.00)
            o2 = input('Olá, se você gostaria de fazer uma consulta do seu saldo digite 1, para '
                       'sacar digite 2 e\n para depositar digite3\nDigite aqui:')
            if '1' == o2:
                print('Seu saldo é R${:.2f}'.format(cc.saldo))
                print('O seu limite do cheque especial é R${:.2f}'.format(cc.limite))
                o3 = input('Se você deseja sacar digite 1, se deseja depositar digite 2,'
                           'se deseja terminar as operações digite 3\nDigite aqui:')
                if '1' == o3:
                    retirada = input('Qual o valor da retirada?\nDigite aqui:R$')

                    cc.sacar(retirada)
                elif '2' == o3:
                    deposit = input('Qual o valor que você deseja depositar?\nDigite aqui:R$')

                    cc.deposito(deposit)
                elif '3' == o3:
                    print('Obrigado por usar nossos serviços, volte sempre.')
            elif '2' == o2:
                retirada = input('Qual o valor da retirada.\nDigite aqui: R$')

                cc.sacar(retirada)
            elif '3' == o2:
                deposit = input('Qual o valor que você deseja depositar?\nDigite aqui:R$')

                cc.deposito(deposit)
        elif '2' == o1:
            print('Você deve ter digitado alguma informação incorreta, tente de novo.')
    elif '2' == o:
        print('Perdão pelo transtorno, tente de novo.')
elif '2' == r:
    print('Por favor, Fale com um atendente humano.')
