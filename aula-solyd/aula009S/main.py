from veiculo import Veiculo
from carro import Carro

carro_rosa = Veiculo('rosa', 4, 'ford', 10)  # Carro rosa é o objeto que foi criado
# apartir da classe Veiculo

print(carro_rosa)
print(type(carro_rosa))
#  Agora o programa reconhece o objeto do mesmo jeito que uma stg por exemplo
print('Cor: ', carro_rosa.cor)
print('Quantidade de rodas: ',  carro_rosa.rodas)
print('Marca: ', carro_rosa.marca)
print('Tamanho do tanque: ', carro_rosa.tanque)
carro_rosa.abastecer(35)
print('Novo tamanho do tanque: ', carro_rosa.tanque)
print('')

carro_azul = Carro('azul', 'BMW', 30)
print('Cor: ', carro_azul.cor)
print('Quantidade de rodas: ',  carro_azul.rodas)
print('Marca: ', carro_azul.marca)
print('Tamanho do tanque: ', carro_azul.tanque)
carro_azul.abastecer(3)
print('Novo tamanho do tanque: ', carro_azul.tanque)
carro_azul.abastecer(300)
print('Tamanho do tanque: ', carro_azul.tanque)
