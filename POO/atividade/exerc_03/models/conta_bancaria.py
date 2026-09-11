class ContaBancaria:
    contas = []

    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

        ContaBancaria.contas.append(self)

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}"


    @classmethod
    def listar_contas(cls):
        for conta in cls.contas:
            print( f"\nTitular: {conta.titular} \n| Saldo: R$ {conta.saldo:.2f}" "\n\n---------------------------------------------------")

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print(f"Saldo insuficiente para realizar o saque de R$ {valor:.2f}")

    @property
    def saldo(self):
        return self._saldo