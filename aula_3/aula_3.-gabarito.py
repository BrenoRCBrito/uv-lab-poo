# Classe Carro:
#
# Atributos: marca, modelo, ano, velocidade_atual, estado
# Métodos: acelerar, frear, ligar, desligar
# •	acelerar(quantidade): aumenta a velocidade atual do
# carro pela quantidade especificada.
# •	frear(quantidade): diminui a velocidade atual do
# carro pela quantidade especificada, sem deixar que a velocidade fique negativa.
# •	ligar(): altera o estado do carro para ligado.
# •	desligar(): altera o estado do carro para desligado e
# zera a velocidade atual.

class Marca:

    def _init_(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

class Carro:
    def _init_(self):
        self.marca = None
        self.modelo = ""
        self.ano = 0
        self.velocidade_atual = 0
        self.estado = "desligado"
    def get_marca(self):
        return self.marca
    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_velocidade_atual(self):
        return self.velocidade_atual

    def set_velocidade_atual(self, velocidade_atual):
        if velocidade_atual < 0:
            print("velocidade invalida")
        else:
            self.velocidade_atual = velocidade_atual
    def ligar(self):
        if self.estado == "desligado":
            self.estado = "ligado"
        else:
            print("carro já ligado")
    def desligar(self):
        if self.estado == "ligado":
            self.estado = "desligado"
            self.velocidade_atual = 0
        else:
            print("carro já desligado")
    def getNomeMarca(self):
        if self.marca == None:
            print("Carro está sem marca")
        else:
            return self.marca.getNome()


marca = Marca()
marca.setNome("Fiat")
carro = Carro()
#carro.set_marca(marca)
carro.set_modelo("Marea")
print(carro.getNomeMarca())
print(carro.get_estado())

# carro2 = Carro()
# carro2.set_marca("Peugeot")
# carro2.set_modelo("206")
# carro2.ligar()
# carro2.ligar()
# print(carro2.get_marca())
# print(carro2.get_estado())
# carro2.set_velocidade_atual(100)
# print(carro2.get_velocidade_atual())
# carro2.desligar()
# carro2.desligar()
# print(carro2.get_estado())
# print(carro2.get_velocidade_atual())