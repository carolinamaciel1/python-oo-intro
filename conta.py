class Conta:

    def __init__(self, conta, titular, saldo, limite):
        print("{} seu número de conta é {} seu saldo é {} de um limite de {} ".format(titular, conta, saldo, limite))
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("{} seu saldo é {}".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor
        print("Você está depositando {} na conta de {}".format(valor, self.titular))

    def saca(self, valor):
        self.saldo -= valor
        print("{} você está retindo {} de sua conta.".format(self.titular, valor))
