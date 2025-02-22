
class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar( self, valor):
        self.saldo += valor
        #self.saldo + valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
        
    def get_saldo(self):
        return self.saldo
    
contaGabriel = ContaBancaria(1000)

contaGabriel.sacar(700)
contaGabriel.depositar(1200)

print(contaGabriel.get_saldo())


 