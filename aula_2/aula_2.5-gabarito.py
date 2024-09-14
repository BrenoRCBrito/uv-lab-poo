# 5.	Classe Produto:
#
# Atributos: nome, preco, quantidade_estoque, categoria
# Métodos: adicionar_estoque, remover_estoque, aplicar_desconto
# •	adicionar_estoque(quantidade): Adiciona quantidade ao quantidade_estoque.
# •	remover_estoque(quantidade): Remove quantidade do quantidade_estoque, se houver quantidade suficiente.
# •	aplicar_desconto(percentual): Aplica um desconto de percentual ao preco do produto.


class Produto:

    def __init__(self):
        self.nome = ""
        self.preco = 0.0
        self.quantidade_estoque = 0.0
        self.categoria = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        if preco < 0:
            print("Preco invalido")
        else:
            self.preco = preco

    def getQuantidadeEstoque(self):
        return self.quantidade_estoque

    def setQuantidadeEstoque(self, quantidade_estoque):
        if quantidade_estoque < 0:
            print("Quantidade em estoque invalida")
        else:
            self.quantidade_estoque = quantidade_estoque

    def getCategoria(self):
        return self.categoria

    def setCategoria(self, categoria):
        self.categoria = categoria

    def adicionarEstoque(self, quantidade):
        if quantidade < 0:
            print("Quantidade invalida")
        else:
            self.quantidade_estoque += quantidade

    def removerEstoque(self, quantidade):
        if quantidade < 0:
            print("Quantidade invalida")
        else:
            if quantidade > self.quantidade_estoque:
                print("Nao pode retirar mais que a quantidade atual")
            else:
                self.quantidade_estoque -= quantidade

    def aplicarDesconto(self, percentual):
        if percentual < 0 or percentual > 100:
            print("Percentual invalido")
        else:
            self.preco = self.preco * (1 - (percentual / 100))


produto = Produto()
produto.setQuantidadeEstoque(100)
produto.adicionarEstoque(1)
print(produto.getQuantidadeEstoque())
produto.removerEstoque(50)
print(produto.getQuantidadeEstoque())
produto.setPreco(1000)
produto.aplicarDesconto(10)
print(produto.getPreco())
