class Produto:

    def __init__(self, nome, preco):
        self.nome= nome
        self.preco= preco

    def __str__(self):
        return f"Produtos(nome={self.nome}, preço={self.preco})"
 
