# 3.	Classe Livro:
#
# Atributos: titulo, autor, ano_publicacao, numero_paginas, genero
# Métodos: abrir, fechar, marcar_pagina, avancar_pagina, retroceder_pagina
# •	abrir(): Exibe uma mensagem indicando que o livro foi aberto.
# •	fechar(): Exibe uma mensagem indicando que o livro foi fechado.
# •	marcar_pagina(pagina): Marca a página atual do livro.
# •	avancar_pagina(): Avança uma página, se não estiver na última página.
# •	retroceder_pagina(): Retrocede uma página, se não estiver na primeira página.


class Livro:
    def __init__(
        self,
        aberto: bool = False,
        titulo: str = "Titulo",
        autor: str = "Autor",
        ano_publicacao: int = 2010,
        numero_paginas: int = 120,
        genero: str = "genero",
        pagina_marcada: int = 0,
        pagina_atual: int = 0,
    ):
        self.aberto = aberto
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.genero = genero
        self.pagina_marcada = pagina_marcada
        self.pagina_atual = pagina_atual

    def abrir(self):
        if not self.aberto:
            self.aberto = True
            print(f"Livro {self.titulo} foi aberto.")

    def fechar(self):
        if self.aberto:
            self.aberto = False
            print(f"Livro {self.titulo} foi fechado.")

    def marcar_pagina(self, pagina: int):
        if self.aberto:
            if 0 > pagina > self.numero_paginas:
                print("Página inválida")
            else:
                self.pagina_marcada = pagina
        else:
            print("Não é permitido marcar a página com livro fechado.")

    def avancar_pagina(self):
        if self.aberto:
            if self.pagina_atual >= self.numero_paginas:
                print("Não é possível avançar página.")
            else:
                self.pagina_atual += 1

    def retroceder_pagina(self):
        if self.aberto:
            if self.pagina_atual <= 1:
                print("Não é possível retroceder página.")
            else:
                self.pagina_atual -= 1

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo: str):
        self.titulo = titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor: str):
        self.autor = autor

    def get_ano_publicacao(self):
        return self.ano_publicacao

    def set_ano_publicacao(self, ano_publicacao: int):
        self.ano_publicacao = ano_publicacao

    def get_numero_paginas(self):
        return self.numero_paginas

    def set_numero_paginas(self, numero_paginas: int):
        self.numero_paginas = numero_paginas

    def get_genero(self):
        return self.genero

    def set_genero(self, genero: str):
        self.genero = genero

    def get_pagina_marcada(self):
        return self.pagina_marcada

    def set_pagina_marcada(self, pagina_marcada: int):
        self.pagina_marcada = pagina_marcada

    def get_pagina_atual(self):
        return self.pagina_atual

    def set_pagina_atual(self, pagina_atual: int):
        self.pagina_atual = pagina_atual


livro = Livro()
livro.abrir()
livro.set_numero_paginas(50)
livro.marcar_pagina(2)
livro.retroceder_pagina()
livro.fechar()
