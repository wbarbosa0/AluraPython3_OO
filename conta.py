class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular.title()
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo da conta {} de {} é de {}".format(self.__numero, self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            return True
        else:
            print("{} não pode ser sacado.".format(valor))
            return False

    def transfere(self, valor, destino):
        if(self.saca(valor)):
            destino.deposita(valor)
        else:
            print("Nao foi possivel transferir {}".format(valor))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite=limite

    def __pode_sacar(self, valor):
        return(valor <= self.__saldo+self.__limite)

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB":"001","CEF":"104","Bradesco":"237"}