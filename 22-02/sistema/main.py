from app.controllers.controller import clienteController
from app.models.listarprodutos import Produto
from app.controllers.produtoController import produtoController
def exibir_menu():
    print("\n=== MENU ===")
    print("1 - Cadastrar cliente ")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Produtos")
    print("4 - Listar produtos")
    print("0 - Sair do Sistema")

def main():
    cntrlCliente = clienteController()
    
    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")
        
        if opc == "1":
            nome = input("Nome do Cliente: ")
            email = input("E-mail: ")
            try:
                idade = int(input("Idade: "))
            except ValueError:
                print("Idade inválida. Por favor, insira um número.")
                continue
            # salvar no banco de dados
            cntrlCliente.criar_cliente(nome, email, idade)
    
        elif opc == "2":
            # listar do banco de dados os clientes
            for index, cliente in enumerate(cntrlCliente.listar_clientes(), 1):
                # index -> posição atual do cliente listado
                # __str__ -> cliente(nome="", email = "")
                print(f"{index}. {cliente}")
        
        elif opc == "3":
            nome = input("Nome do Produto: ")
            try:
                preco = float(input("Preço: "))
            except ValueError:
                print("Preço inválido. Por favor, insira um número.")
                continue
                cntrlProduto.criar_produto(nome, preco)
            # Implementar lógica para cadastrar produto
            print(f"Produto {nome} com preço {preco} cadastrado.")
            
        
        elif opc == "4":
            # listar do banco de dados os produtos
            print(Produto)
            # Implementar lógica para listar produtos
            for index, produto in enumerate(Produto.listarprodutos(), 1):
                print(f"{index}. {produto}")           
        
        elif opc == "0":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()
    
    
    
    
 