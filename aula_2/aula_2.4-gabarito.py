# 4.	Classe Pessoa:
#
# Atributos: nome, idade, altura, peso
# Métodos: envelhecer, crescer, ganhar_peso, perder_peso
# •	envelhecer(): Aumenta a idade da pessoa em um ano.
# •	Crescer(centímetros): Aumenta a altura da pessoa em centímetros, se a pessoa tiver menos de 21 anos.
# •	Ganhar_peso(quilos): Aumenta o peso da pessoa em quilos.
# •	Perder_peso(quilos): Diminui o peso da pessoa em quilos.


class Pessoa:

    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.altura = 0.0
        self.peso = 0.0

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        if idade < 0:
            print("Idade invalida")
        else:
            self.idade = idade

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        if peso < 0:
            print("Peso invalido")
        else:
            self.peso = peso

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        if altura < 0:
            print("Altura invalida")
        else:
            self.altura = altura

    def envelhecer(self):
        self.idade += 1

    def crescer(self, centimetros):
        if self.idade >= 21:
            print("Maior ou igual a 21 anos")
        else:
            if centimetros < 0:
                print("Centimetros invalidos")
            else:
                self.altura += centimetros

    def ganharPeso(self, quilos):
        if quilos < 0:
            print("Quantidade de quilos invalida")
        else:
            self.peso += quilos

    def perderPeso(self, quilos):
        if quilos < 0:
            print("Quantidade de quilos invalida")
        else:
            if quilos > self.peso:
                print("Nao pode perder mais quilos do que o peso atual")
            else:
                self.peso -= quilos


pessoa = Pessoa()
pessoa.setIdade(10)
pessoa.envelhecer()
print(pessoa.getIdade())
pessoa.setAltura(100)
pessoa.crescer(1)
print(pessoa.getAltura())
pessoa.setPeso(80)
pessoa.ganharPeso(5)
print(pessoa.getPeso())
pessoa.perderPeso(10)
print(pessoa.getPeso())
