# Implementar uma classe de Banco com contas de diferentes tipos (Conta Corrente e Conta Poupança) que herdam de uma classe base (Conta).
class Conta:
    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")


class ContaCorrente(Conta):
    def __init__(self, numero_conta, saldo, limite):
        super().__init__(numero_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")


class ContaPoupanca(Conta):
    def render_juros(self, taxa):
        self.saldo += self.saldo * taxa


conta_corrente = ContaCorrente(1, 1000, 500)
conta_poupanca = ContaPoupanca(2, 2000)

conta_corrente.sacar(1500)
print(conta_corrente.saldo)  # Saída: -500 (saldo + limite)

conta_poupanca.render_juros(0.05)
print(conta_poupanca.saldo)  # Saída: 2100 (2000 + 5% de juros)
