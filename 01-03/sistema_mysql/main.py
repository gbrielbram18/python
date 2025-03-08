from src.controller import produto_controller

def exibir_menu():
    
     print("\nMAREA TOCA TUDO LTDA!")
     print("\n=== =menu ====")
     print("1 - Cadastrar Produto")
     print("2 - Listar produto")
     print("3 - Atualizar produto")
     print("4 - deletar Produto")
     print("0 - Sair")
     
def listar_produto():
    print("\n --- Lista de produtos ---")
    produtos= produto_controller.listar_produtos()
    if produtos: 
        for produtos in produtos:
            print(f"ID: {produtos['id']} , nome: {produtos['nome']}, preco {produtos['preco']}")
        else:
            print("nao existe produto")
            

def cadastrar_produto():
    print("\n --- Cadastrar produtos---")
    nome = input("digite o nome:")
    preco = input("digite o preco:")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"produto cadastrado com sucesso com novo ID{novo_id}.")
    