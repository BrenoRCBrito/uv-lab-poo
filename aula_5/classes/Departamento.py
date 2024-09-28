class Departamento:
    def __init__(self, nome, empresa):
        self.nome = nome
        self.empresa = empresa
        self.chefia = None

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_empresa(self):
        return self.empresa

    def set_empresa(self, empresa):
        self.empresa = empresa

    def get_chefia(self):
        return self.chefia

    def set_chefia(self, chefia):
        self.chefia = chefia
