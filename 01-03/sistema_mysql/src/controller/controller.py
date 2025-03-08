from model.produto_model import ProdutoModel

def listar_produtos():
    """retorna a lista de todos os produtos (dict)"""
    
    model = ProdutoModel()
    produtos= model.get_all_procucts()
    model.close_connection()
    return produtos

def cadastrar_produto(nome, preco):
    """cadastrar um produto no banco"""
    model = ProdutoModel()
    novo_id= model.insert_product(nome, preco)
    model.close_connection()
    return novo_id


def atualizar_produto(produto_id, nome , preco):
    model = ProdutoModel()
    linhas_afetadas=model.update_product_by_id(produto_id, nome, preco)
    model.close_connection()
    return linhas_afetadas 


def obert_produto(produto_id):
    model =ProdutoModel()
    produto= model.get_product_by_id(produto_id)
    model.close_connection()
    return produto  
    