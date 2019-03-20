from veiculo import Veiculo  # Essa é uma classe que herda as caracteristicas de outra


class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)

    def abastecer(self, litro):
        if self.tanque + litro > 50:
            print('Erro: Tanque cheio')
        else:
            self.tanque += litro

