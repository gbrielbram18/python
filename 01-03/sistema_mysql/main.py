from src.controller import produto_controller

def exibir_menu():
    
     print("\nMAREA TOCA TUDO LTDA!")
     print("\n=== =menu ====")
     print("1 - Cadastrar Produto")
     print("2 - Listar produto")
     print("3 - Atualizar produto")
     print("4 - deletar Produto") 
     print("5 - Cadastrar Usuario")
     print("0 - Sair")
     
def listar_produto():
    print("\n --- Lista de produtos ---")
    produtos = produto_controller.listar_produtos()
    if produtos: 
        for produto in produtos:
            print(f"ID: {produto['id']} , nome: {produto['nome']}, preco {produto['preco']}")
        else:
            print("nao existe produto")
            

def cadastrar_produto():
    print("\n ---Cadastrar produtos---")
    nome = input("digite o nome:")  
    preco = input("digite o preco:")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"produto cadastrado com sucesso com novo ID{novo_id}.")
    
def opcao_atualizar():
    print("\n atualizando produto")
    produto_id = input("digite o ID do produto")
    nome = input("digite o nome do produto ")
    preco = input ("digite o preço do produto")
    
    linhas = produto_controller.atualizar_produto( produto_id, nome, preco)
    if linhas> 0: #quantidade de linhas modificadas
        print("produto atualizado com sucesso!")
    else:
        print("nenhum produto foi atualizado")
        
        
def cadastrar_user():
    print("\n ---Cadastrar usuario---")
    nome = input("digite o nome: ")
    email = input("digite o email: ")
    idade = input("digite sua idade: ")
    
    novo_id = cadastrar_user(nome, email,idade)
    print(f"usuario cadastrado com sucesso com novo ID.")
    
     
    
    #main -> inicializa o projeto
def main():
    #while true para repetir o mesmo que a opção digitada esteja errada
    while True:
        
        exibir_menu()
        opc= input("escolha uma opção: ")
        
        if opc == "1":
            cadastrar_produto()
            
        elif opc =="2":
            listar_produto() 
            
        elif opc == "3":
            opcao_atualizar()
            
            """ 
        elif opc == "4":
            deletar_prooduto()
            """
            
        elif opc == "5":
            cadastrar_user()  
            
        elif opc == "0":
            print("saindo do sistema...")
            #sys.exit(0)
        else:
            print("opção invalida, tente novamente...")
            
if __name__ == '__main__':
    main()