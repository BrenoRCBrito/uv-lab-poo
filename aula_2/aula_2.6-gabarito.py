# 6.	Classe Funcionario:
#
# Atributos: nome, cargo, salario, departamento
# Métodos: receber_aumento, mudar_departamento, exibir_dados
#
# •	receber_aumento(percentual): Aplica um aumento de percentual ao salario.
# •	mudar_departamento(novo_departamento): Altera o departamento para o novo_departamento.
# •	exibir_dados(): Exibe os dados do funcionário, incluindo nome, cargo, salário e departamento.


class Funcionario:

    def _init_(self):
        self.nome = ""
        self.cargo = ""
        self.salario = 0.0
        self.departamento = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCargo(self):
        return self.cargo

    def setCargo(self, cargo):
        self.cargo = cargo

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        if salario < 0:
            print("Salario invalido")
        else:
            self.salario = salario

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def receberAumento(self, percentual):
        if percentual < 0:
            print("Percentual invalido")
        else:
            self.salario = self.salario * (1 + (percentual / 100))

    def mudar_departamento(self, departamento):
        self.setDepartamento(departamento)

    def exibirDados(self):
        print(self.nome, self.departamento, self.salario, self.cargo)


funcionario = Funcionario()
funcionario.setSalario(1000)
funcionario.receberAumento(10)
print(funcionario.getSalario())
funcionario.setDepartamento("TI")
print(funcionario.getDepartamento())
funcionario.mudar_departamento("RH")
print(funcionario.getDepartamento())
funcionario.setNome("Ana")
funcionario.setCargo("Analista")
funcionario.exibirDados()
