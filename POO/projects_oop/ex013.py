#  Implementar uma classe para representar uma Conta Bancária com métodos de depósito, saque e transferência.
class ContaBancaria:
    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def transferir(self, outra_conta, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            outra_conta.depositar(valor)
        else:
            print("Saldo insuficiente!")


conta1 = ContaBancaria(1, 1000)
conta2 = ContaBancaria(2, 500)
conta1.transferir(conta2, 300)
print(conta1.saldo)
print(conta2.saldo)
