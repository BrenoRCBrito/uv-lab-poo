# 5.	Classe Produto:
#
# Atributos: nome, preco, quantidade_estoque, categoria
# Métodos: adicionar_estoque, remover_estoque, aplicar_desconto
# •	adicionar_estoque(quantidade): Adiciona quantidade ao quantidade_estoque.
# •	remover_estoque(quantidade): Remove quantidade do quantidade_estoque, se houver quantidade suficiente.
# •	aplicar_desconto(percentual): Aplica um desconto de percentual ao preco do produto.


class Produto:
    def __init__(
        self,
        nome: str = "Nome",
        preco: int = 100,
        quantidade_estoque: int = 100,
        categoria: str = "Categoria",
    ):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.categoria = categoria

    def adicionar_estoque(self, quantidade: int):
        if quantidade < 0:
            print("Quantidade inválida")
        else:
            self.quantidade_estoque += quantidade

    def remover_estoque(self, quantidade: int):
        if quantidade < 0:
            print("Quantidade inválida")
        else:
            if self.quantidade_estoque >= quantidade:
                self.quantidade_estoque -= quantidade
            else:
                print("Estoque insuficiente")

    def aplicar_desconto(self, percentual: float):
        if 0 < percentual <= 100:
            self.preco -= self.preco * (percentual / 100)
        else:
            print("Percentual inválido")

    def get_nome(self):
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_preco(self):
        return self.preco

    def set_preco(self, preco: int):
        self.preco = preco

    def get_quantidade_estoque(self):
        return self.quantidade_estoque

    def set_quantidade_estoque(self, quantidade_estoque: str):
        self.quantidade_estoque = quantidade_estoque

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria: str):
        self.categoria = categoria


produto = Produto()
produto.set_quantidade_estoque(100)
produto.adicionar_estoque(1)
print(produto.get_quantidade_estoque())
produto.remover_estoque(50)
print(produto.get_quantidade_estoque())
produto.set_preco(1000)
produto.aplicar_desconto(10)
print(produto.get_preco())
