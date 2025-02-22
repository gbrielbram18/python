
class Cliente :
    
    def _init_(self, nome, email , idade):
        self.nome = nome
        self.email = email
        self.idade = idade
    
    def __str__(self):
        return f"Cliente(nome={self.nome}, email={self.email}, idade= {self.idade})"

