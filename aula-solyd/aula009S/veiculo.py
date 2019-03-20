'''
Orientação a objeto.
Esse vai ser um arquivo de referência para o arquivo main.
Criamos a classe dele e nisso especificamos tudo que tem nele.
'''


class Veiculo:

    def __init__(self, cor, rodas, marca, tanque):
        # o init(é o método construtor) self(eu mesmo) está passando ele mesmo
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    # Agora criamos um método
    def abastecer(self, litro):
        self.tanque += litro
