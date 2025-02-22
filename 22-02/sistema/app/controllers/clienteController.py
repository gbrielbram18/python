from ..models.cliente import Cliente

class clienteController:

    def __init__(self):
        #contexto com o banco
        self.db = ""
    
    def criar_cliente(self, nome,email,idade):
        #cria o objeto cliente e salva no banco
        novo_cliente= Cliente(nome, email, idade)
        #converter para dict (JSON)
        dict_cliente ={
            "nome":novo_cliente.nome,
            "email":novo_cliente.email,
            "idade":novo_cliente.idade
        }
        #salvar no banco 
        print("Cliente cadastrado")
    
    def listar_cliente(self):
        print("listar clientes")