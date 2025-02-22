#definição  da classe pessoa
class pessoa:

    #metodo construtor 
    # e chamado quando criamos um objeto#
    def __init__(self, nome , idade, altura):
        #atribir a entidade
        self.nome = nome
        self.idade = idade
        self.altura = altura

    
    def apresentar (self):
        print(f'Ola, meu nome é :{self.nome} e tenho'  f'{self.idade} anos de idade, e tenho' f'{self.altura} tenho tudo isso de altura')


p1=pessoa("refael", 34, "1.50")
p2=pessoa("guilherme" ,7, "1.35")
p3=pessoa("alberto", 18 ,"1.95")


p1.apresentar()
p2.apresentar()
p3.apresentar()