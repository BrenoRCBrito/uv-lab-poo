class Cidade:
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado
