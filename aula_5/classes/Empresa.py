class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.grupo = None
        self.diretor = None

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_grupo(self):
        return self.grupo

    def set_grupo(self, grupo):
        self.grupo = grupo

    def get_diretor(self):
        return self.diretor

    def set_diretor(self, diretor):
        self.diretor = diretor
