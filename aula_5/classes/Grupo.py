class Grupo:
    def __init__(self, nome, sede, presidente):
        self.nome = nome
        self.sede = sede
        self.presidente = presidente

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_sede(self):
        return self.sede

    def set_sede(self, sede):
        self.sede = sede

    def get_presidente(self):
        return self.presidente

    def set_presidente(self, presidente):
        self.presidente = presidente
