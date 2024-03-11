# Modificadores de Acesso
class ContaBancaria:
    def __init__(self, saldo_inicial) -> None:
        self.__saldo = saldo_inicial # Atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            
    def ver_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(100)
conta.depositar(50)
print(conta.ver_saldo())  # 150
