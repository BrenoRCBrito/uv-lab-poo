class Marca:
    def __init__(self, nome: str = "KIA"):
        self.nome = nome

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome


class Modelo:
    def __init__(self, nome: str = "Cerato") -> None:
        self.nome = nome

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome


class Carro:
    def __init__(
        self,
        marca: Marca | None = Marca("KIA"),
        modelo: Modelo | None = Modelo("Cerato"),
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

    def get_marca(self) -> Marca | None:
        return self.marca

    def set_marca(self, marca: Marca | None):
        self.marca = marca

    def get_modelo(self) -> Modelo | None:
        return self.modelo

    def set_modelo(self, modelo: Modelo | None):
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

    def get_nome_marca(self):
        if self.marca is None:
            print("Carro está sem marca")
        else:
            return self.marca.get_nome()

    def get_nome_modelo(self):
        if self.modelo is None:
            print("Carro está sem modelo")
        else:
            return self.modelo.get_nome()


def print_carro(carro: Carro):
    print(
        f"marca={carro.get_marca()};modelo={carro.get_modelo()};ano={carro.get_ano()};velocidade_atual={carro.get_velocidade_atual()};estado={carro.get_estado()}"
    )


marca = Marca()
marca.set_nome("Fiat")
carro = Carro()
carro.set_marca(marca)
carro.set_modelo(Modelo("Marea"))
print(carro.get_nome_marca())
print(carro.get_nome_modelo())
print(carro.get_estado())
