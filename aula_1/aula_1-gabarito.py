# Classe Carro:
#
# Atributos: marca, modelo, ano, velocidade_atual, ligado
# Métodos: acelerar, frear, ligar, desligar
# •	acelerar(quantidade): aumenta a velocidade atual do carro pela quantidade especificada.
# •	frear(quantidade): diminui a velocidade atual do carro pela quantidade especificada, sem deixar que a velocidade fique negativa.
# •	ligar(): altera o estado do carro para ligado.
# •	desligar(): altera o estado do carro para desligado e zera a velocidade atual.


class Carro:

    def _init_(self):
        self.marca = ""
        self.modelo = ""
        self.ano = 0
        self.velocidade_atual = 0.0
        self.ligado = False

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_ano(self):
        return self.ano

    def set_ano(self, ano):
        self.ano = ano

    def get_velocidade_atual(self):
        return self.velocidade_atual

    def set_velocidade_atual(self, velocidade_atual):
        self.velocidade_atual = velocidade_atual

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False
        self.set_velocidade_atual(0.0)

    def acelerar(self, quantidade):
        if self.ligado:
            self.velocidade_atual = self.velocidade_atual + quantidade

    def frear(self, quantidade):
        if self.ligado:
            self.velocidade_atual = self.velocidade_atual - quantidade
            if self.velocidade_atual < 0:
                self.set_velocidade_atual(0.0)


carro = Carro()
carro.set_marca("Jeep")
print(carro.get_marca())
carro.ligar()
carro.acelerar(50)
print(carro.get_velocidade_atual())
carro.frear(30)
print(carro.get_velocidade_atual())
carro.desligar()
carro.acelerar(30)
carro.frear(20)
print(carro.get_velocidade_atual())
