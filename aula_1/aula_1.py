class Carro:
    def __init__(
        self,
        marca: str = "KIA",
        modelo: str = "Cerato",
        ano: int = 2014,
        velocidade_atual: int = 0,
        estado: bool = False,
    ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_atual = velocidade_atual
        self.estado = estado

    def acelerar(self, velocidade: int) -> None:
        if self.estado:
            print(f"Acelerando! ({velocidade})")
            self.velocidade_atual += velocidade

    def frear(self, velocidade: int) -> None:
        if self.estado:
            if velocidade > 0:
                print(f"Freando! ({velocidade})")
                self.velocidade_atual -= velocidade
            else:
                self.velocidade_atual = 0

    def ligar(self) -> None:
        if not self.estado:
            print("Ligando!")
            self.estado = True

    def desligar(self) -> None:
        if self.estado:
            print("Desligando!")
            self.estado = False
            self.velocidade_atual = 0

    def get_marca(self) -> str:
        return self.marca

    def set_marca(self, marca: str):
        self.marca = marca

    def get_modelo(self) -> str:
        return self.modelo

    def set_modelo(self, modelo: str):
        self.modelo = modelo

    def get_ano(self) -> int:
        return self.ano

    def set_ano(self, ano: int):
        self.ano = ano

    def get_velocidade_atual(self) -> int:
        return self.velocidade_atual

    def set_velocidade_atual(self, velocidade_atual: int):
        self.velocidade_atual = velocidade_atual

    def get_estado(self) -> bool:
        return self.estado

    def set_estado(self, estado: bool):
        self.estado = estado


def print_carro(carro: Carro):
    print(
        f"marca={carro.get_marca()};modelo={carro.get_modelo()};ano={carro.get_ano()};velocidade_atual={carro.get_velocidade_atual()};estado={carro.get_estado()}"
    )


carro1 = Carro()

print_carro(carro1)

carro1.acelerar(20)

print_carro(carro1)

carro1.ligar()
carro1.acelerar(20)

print_carro(carro1)

carro1.frear(10)

print_carro(carro1)

carro1.desligar()

print_carro(carro1)

carro1.ligar()
carro1.acelerar(30)
carro1.frear(100)

print_carro(carro1)

carro1.acelerar(60)

print_carro(carro1)

carro1.desligar()

print_carro(carro1)
