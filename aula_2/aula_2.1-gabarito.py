# Classe ContaBancaria:
#
# Atributos: titular, numero_conta, saldo
# Métodos: depositar, sacar
# •	depositar(valor): adiciona o valor ao saldo da conta.
# •	sacar(valor): subtrai o valor do saldo da conta, se houver saldo suficiente.


class ContaBancaria:

    def __init__(self):
        self.titular = ""
        self.numero_conta = 0
        self.saldo = 0.0

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_numero_conta(self):
        return self.numero_conta

    def set_numero_conta(self, numero_conta):
        self.numero_conta = numero_conta

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
        else:
            print("Saldo insuficiente")


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
