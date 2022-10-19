class conta:
    codigo_banco='001'
    def __init__(self,Numero=0,titular="",saldo=1000,limite=2000):
        self.__Numero=Numero
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite
        #self.__codigo_banco="001"
    #@staticmethod
    #def GetCodigo_banco():
    #    return "001"
    @classmethod
    def GetCodigoBanco(cls):
        return cls.codigo_banco
    @property
    def Numero(self):
        return self.__Numero
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self,TitularNovo):
        self.__titular=TitularNovo
    @property
    def saldo(self):
        return self.__saldo
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self,LimiteNovo):
        self.__limite=LimiteNovo
    def depositar(self,valor):
        self.__saldo+=valor
    def sacar(self,valor):
        if (self.__pode_sacar(valor)):
            self.__saldo-=valor
        else:
            print("Você não possui saldo suficiente para realizar este saque")
    def __pode_sacar(self,valor):
        return (self.saldo+self.limite)>=valor
    def transferir(self,ContaDestino,valor):
        if (self.saldo>=valor):
            self.sacar(valor)
            ContaDestino.depositar(valor)
        else:
            print("A sua conta não possui saldo suficiente para realizar essa transferência")
Pedro=conta(232,"Pedro",4000,10000)
print(Pedro.saldo)
Joao=conta(459,"Joao",2000,5000)
Pedro.transferir(Joao,1000)
print(Pedro.saldo)
print(Joao.saldo)
print(Joao.limite)
Joao.limite=6000
print(Joao.limite)
Pedro.sacar(15000)
print(conta.GetCodigoBanco())