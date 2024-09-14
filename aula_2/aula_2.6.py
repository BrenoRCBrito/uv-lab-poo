# 6.	Classe Funcionario:
#
# Atributos: nome, cargo, salario, departamento
# Métodos: receber_aumento, mudar_departamento, exibir_dados
#
# •	receber_aumento(percentual): Aplica um aumento de percentual ao salario.
# •	mudar_departamento(novo_departamento): Altera o departamento para o novo_departamento.
# •	exibir_dados(): Exibe os dados do funcionário, incluindo nome, cargo, salário e departamento.


class Funcionario:
    def __init__(
        self,
        nome: str = "Nome",
        cargo: str = "Cargo",
        salario: int = 1000,
        departamento: str = "Departamento",
    ):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.departamento: departamento

    def receber_aumento(self, percentual: int):
        if percentual > 0:
            self.salario += self.salario * (percentual / 100)
        else:
            print("Percentual inválido")

    def mudar_departamento(self, novo_departamento: str):
        self.departamento = novo_departamento

    def exibir_dados(self):
        return f"nome={self.nome};cargo={self.cargo};salario={self.salario};departamento={self.departamento}"

    def get_nome(self):
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo: str):
        self.cargo = cargo

    def get_salario(self):
        return self.salario

    def set_salario(self, salario: str):
        self.salario = salario

    def get_departamento(self):
        return self.departamento

    def set_departamento(self, departamento: str):
        self.departamento = departamento


funcionario = Funcionario()
funcionario.set_salario(1000)
funcionario.receber_aumento(10)
print(funcionario.get_salario())
funcionario.set_departamento("TI")
print(funcionario.get_departamento())
funcionario.mudar_departamento("RH")
print(funcionario.get_departamento())
funcionario.set_nome("Ana")
funcionario.set_cargo("Analista")
funcionario.exibir_dados()
