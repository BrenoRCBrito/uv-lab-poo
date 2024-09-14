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

    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.ano_publicacao = 0
        self.numero_paginas = 0
        self.genero = ""
        self.aberto = False
        self.pagina_atual = 0

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor

    def getAnoPublicacao(self):
        return self.ano_publicacao

    def setAnoPublicacao(self, ano_publicacao):
        self.ano_publicacao = ano_publicacao

    def getNumeroPaginas(self):
        return self.numero_paginas

    def setNumeroPaginas(self, numero_paginas):
        self.numero_paginas = numero_paginas

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getPaginaAtual(self):
        return self.pagina_atual

    def setPaginaAtual(self, pagina_atual):
        self.pagina_atual = pagina_atual

    def abrir(self):
        if not self.aberto:
            self.aberto = True
            print("Livro aberto")

    def fechar(self):
        if self.aberto:
            self.aberto = False
            print("Livro fechado")

    def marcar_pagina(self, pagina):
        if not self.aberto:
            print("Pagina nao pode ser marcada em livro fechado")
        else:
            if pagina < 1 or pagina > self.numero_paginas:
                print("Pagina invalida")
            else:
                self.pagina_atual = pagina

    def avancar_pagina(self):
        if self.aberto:
            if self.pagina_atual >= self.numero_paginas:
                print("Nao é possivel avancar pagina")
            else:
                self.pagina_atual += 1

    def retroceder_pagina(self):
        if self.aberto:
            if self.pagina_atual <= 1:
                print("Nao é possivel retroceder pagina")
            else:
                self.pagina_atual -= 1


livro = Livro()
livro.abrir()
livro.setNumeroPaginas(50)
livro.marcar_pagina(2)
livro.retroceder_pagina()
livro.fechar()
