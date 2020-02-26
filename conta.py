class Conta:

    def __init__(self, conta, titular, saldo, limite):
        print("{} seu número de conta é {} seu saldo é {} de um limite de {} ".format(titular, conta, saldo, limite))
        # O caractere _ serve para encapsular os atributos de uma classe
        self.__conta = conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("{} seu saldo é {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
        print("Você está depositando {} na conta de {}".format(valor, self.__titular))

    def saca(self, valor):
        self.__saldo -= valor
        print("{} você está retindo {} de sua conta.".format(self.__titular, valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
