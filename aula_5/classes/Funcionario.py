class Funcionario:
    def __init__(self, nome, alocacao, escolaridade, coordenacao):
        self.nome = nome
        self.alocacao = alocacao
        self.escolaridade = escolaridade
        self.coordenacao = coordenacao

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_alocacao(self):
        return self.alocacao

    def set_alocacao(self, alocacao):
        self.alocacao = alocacao

    def get_escolaridade(self):
        return self.escolaridade

    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def get_coordenacao(self):
        return self.coordenacao

    def set_coordenacao(self, coordenacao):
        self.coordenacao = coordenacao

    def get_nome_escolaridade(self):
        return self.get_escolaridade().get_nome()

    def get_nome_pais_alocacao(self):
        return self.get_alocacao().get_empresa().get_grupo().get_sede().get_nome()

    def get_estado_coordenacao(self):
        return self.get_coordenacao().get_cidade().get_estado().get_nome()
