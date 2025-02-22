from ..models.listarprodutos import Produto
from ..database.database import BancoFake

class produtoController:
    def __init__(self):
        self.db = BancoFake()
    
    def criar_produto(self, nome, preco):
        novo_produto = Produto(nome, preco)
        dict_produto = {
            "nome": novo_produto.nome,
            "preco": novo_produto.preco
        }
        self.db.adicionar_produto(dict_produto)
        print("Produto cadastrado com sucesso!")
    
    def listar_produtos(self):
        return self.db.listar_produtos()