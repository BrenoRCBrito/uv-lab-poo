# Classe ContaBancaria:
#
# Atributos: titular, numero_conta, saldo
# Métodos: depositar, sacar
# •	depositar(valor): adiciona o valor ao saldo da conta.
# •	sacar(valor): subtrai o valor do saldo da conta, se houver saldo suficiente.


class ContaBancaria:
    def __init__(
        self, titular: str = "Titular", numero_conta: str = "9999", saldo: float = 0.0
    ):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float):
        if self.saldo > 0 and self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def get_titular(self):
        return self.titular

    def set_titular(self, titular: str):
        self.titular = titular

    def get_numero_conta(self):
        return self.numero_conta

    def set_numero_conta(self, numero_conta: str):
        self.numero_conta = numero_conta

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo: float):
        self.saldo = saldo


conta = ContaBancaria()
print(conta.get_saldo())
conta.depositar(100)
print(conta.get_saldo())
conta.depositar(50)
print(conta.get_saldo())
conta.sacar(20)
print(conta.get_saldo())
conta.sacar(150)
print(conta.get_saldo())
