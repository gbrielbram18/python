

def exibir_menu():
    print("\n=== MENU ===")
    print("1 - Cadastrar cliente ")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Produtos")
    print("4 - Listar produtos")
    print("0 - Sair do Sistema")

def main():

    while True:
        exibir_menu()
        opc=input("Escolha uma opção: ")
        
        if opc == "1":
            nome==input("Nome do Cliente: ")
            email=input("E-mail: ")
            idade=int(input("idade: "))
    
    #salvariamos no banco de dados
        elif opc =="2":
    #listar do banco de dados os clientes
            print("listar")
        
        elif opc=="3":
            nome= input("Nome do Produto: ")
            preco =float(input("preço: "))

        elif opc == "4":
    #listar do banco de dados os produtos
            print("listar")
            break
        else:
            print("Opção invalida. Tente Novamente.")
 