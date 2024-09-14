# 4.	Classe Pessoa:
#
# Atributos: nome, idade, altura, peso
# Métodos: envelhecer, crescer, ganhar_peso, perder_peso
# •	envelhecer(): Aumenta a idade da pessoa em um ano.
# •	Crescer(centímetros): Aumenta a altura da pessoa em centímetros, se a pessoa tiver menos de 21 anos.
# •	Ganhar_peso(quilos): Aumenta o peso da pessoa em quilos.
# •	Perder_peso(quilos): Diminui o peso da pessoa em quilos.


class Pessoa:
    def __init__(
        self, nome: str = "Nome", idade: int = 40, altura: int = 180, peso: int = 80
    ):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def envelhecer(self):
        self.idade += 1

    def crescer(self, centimetros: int):
        if self.idade >= 21:
            print("Pessoa com idade maior a 21 anos")
        else:
            if centimetros < 0:
                print("Não são aceitos centimetros negativos")
            else:
                self.altura += centimetros

    def ganhar_peso(self, quilos: int):
        if quilos < 0:
            print("Não são aceitos quilos negativos")
        else:
            self.peso += quilos

    def perder_peso(self, quilos: int):
        if quilos < 0:
            print("Não são aceitos quilos negativos")
        else:
            if quilos >= self.peso:
                print("Peso atual é menor que a quantidade de quilos")
            else:
                self.peso -= quilos

    def get_nome(self):
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade: int):
        self.idade = idade

    def get_altura(self):
        return self.altura

    def set_altura(self, altura: int):
        self.altura = altura

    def get_peso(self):
        return self.peso

    def set_peso(self, peso: int):
        self.peso = peso


pessoa = Pessoa()
pessoa.set_idade(10)
pessoa.envelhecer()
print(pessoa.get_idade())
pessoa.set_altura(100)
pessoa.crescer(1)
print(pessoa.get_altura())
pessoa.set_peso(80)
pessoa.ganhar_peso(5)
print(pessoa.get_peso())
pessoa.perder_peso(10)
print(pessoa.get_peso())
