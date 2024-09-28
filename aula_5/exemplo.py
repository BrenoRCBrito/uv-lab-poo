class Escolaridade:
    def __init__(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


class Funcionario:
    def __init__(self, escolaridade):
        self.setEscolaridade(escolaridade)
        self.escolaridade = escolaridade

    def getEscolaridade(self):
        return self.escolaridade

    def setEscolaridade(self, escolaridade):
        if escolaridade == None:
            print("Funcionario deve ter uma escolaridade")
            exit()
        self.escolaridade = escolaridade

    def getNomeEscolaridade(self):
        return self.escolaridade.getNome()


class Grupo:
    def __init__(self):
        self.presidente = None

    def getPresidente(self):
        return self.presidente

    def setPresidente(self, presidente):
        self.presidente = presidente

    def getNomeEscolaridadePresidente(self):
        if self.presidente == None:
            print("Grupo sem presidente no momento")
        else:
            return self.presidente.getNomeEscolaridade()


grupo = Grupo()
escolaridade = Escolaridade()
escolaridade.setNome("Doutorado")
presidente = Funcionario(escolaridade)
grupo.setPresidente(presidente)
print(grupo.getNomeEscolaridadePresidente())


class Pais:
    def __init__(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


class Escolaridade:
    def __init__(self):
        self.nome = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


class Funcionario:
    def __init__(self, escolaridade):
        self.setEscolaridade(escolaridade)
        self.escolaridade = escolaridade
        self.departamento = None

    def getEscolaridade(self):
        return self.escolaridade

    def setEscolaridade(self, escolaridade):
        if escolaridade == None:
            print("Funcionario deve ter uma escolaridade")
            exit()
        self.escolaridade = escolaridade

    def getNomeEscolaridade(self):
        return self.escolaridade.getNome()

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getNomePais(self):
        if self.departamento == None:
            print("Funcionario nao esta alocado a departamento no momento")
        else:
            return self.departamento.getNomePais()


class Grupo:
    def __init__(self, pais):
        self.presidente = None
        self.setPais(pais)

    def getPresidente(self):
        return self.presidente

    def setPresidente(self, presidente):
        self.presidente = presidente

    def getPais(self):
        return self.pais

    def setPais(self, pais):
        if pais == None:
            print("Pais nao pode ser vazio")
            exit()
        self.pais = pais

    def getNomeEscolaridadePresidente(self):
        if self.presidente == None:
            print("Grupo sem presidente no momento")
        else:
            return self.presidente.getNomeEscolaridade()

    def getNomePais(self):
        return self.pais.getNome()


class Empresa:
    def __init__(self):
        self.grupo = None

    def getGrupo(self):
        return self.grupo

    def setGrupo(self, grupo):
        self.grupo = grupo

    def getNomePais(self):
        if self.grupo == None:
            print("Empresa sem grupo")
        else:
            return self.grupo.getNomePais()


class Departamento:
    def __init__(self):
        self.empresa = None

    def getEmpresa(self):
        return self.empresa

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getNomePais(self):
        if self.empresa == None:
            print("Departamento sem empresa")
        else:
            return self.empresa.getNomePais()


pais = Pais()
pais.setNome("Brasil")
grupo = Grupo(pais)
escolaridade = Escolaridade()
escolaridade.setNome("Doutorado")
presidente = Funcionario(escolaridade)
grupo.setPresidente(presidente)
print(grupo.getNomeEscolaridadePresidente())
grupo.setPais(pais)
empresa = Empresa()
empresa.setGrupo(grupo)
departamento = Departamento()
departamento.setEmpresa(empresa)
funcionario = Funcionario(escolaridade)
funcionario.setDepartamento(departamento)
print(funcionario.getNomePais())
