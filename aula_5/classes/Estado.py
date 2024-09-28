class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais
