class Filial:
    def __init__(self, nome, cidade, empresa):
        self.nome = nome
        self.cidade = cidade
        self.empresa = empresa

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cidade(self):
        return self.cidade

    def set_cidade(self, cidade):
        self.cidade = cidade

    def get_empresa(self):
        return self.empresa

    def set_empresa(self, empresa):
        self.empresa = empresa
