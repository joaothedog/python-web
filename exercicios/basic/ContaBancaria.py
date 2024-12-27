class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo #torna o atributo privado
        
    def depositar(self, valor_deposito):
        self.__saldo += valor_deposito
    
    def sacar(self, valor_saque):
        if valor_saque <= self.__saldo:
            self.__saldo -= valor_saque
        else:
            print("Saldo insuficiente")
    
    def show_saldo(self):
        print(f"Saldo: R${self.__saldo:.2f}")

conta1 = ContaBancaria("Maria", 1000)
conta1.show_saldo()
conta1.sacar(200)
conta1.show_saldo()
conta1.sacar(900)
conta1.show_saldo()
conta1.depositar(1900)
conta1.show_saldo()
    
    