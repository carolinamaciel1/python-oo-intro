class Conta:

    def __init__(self, conta, titular, saldo, limite):
        print("{} seu número de conta é {} seu saldo é {} de um limite de {} ".format(titular, conta, saldo, limite))
        self.conta = conta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
