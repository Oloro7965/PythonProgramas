class conta:
    contador=0
    def __init__(self,titular,saldo,limite):
        self.__numero=conta.contador+1
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite
        conta.contador+=1
    def extrato(self):
        return f'cliente {self.__numero}: saldo de {self.__saldo:.2f} reais'.replace('.',',')
    def depositar(self,valor):
        self.__saldo+=valor
        return f'saldo de {self.__saldo} reais'
    def retirar(self,valor):
        self.__saldo-=valor
        return f'saldo de {self.__saldo} reais'
    def get_numero(self):
        return self.__numero
    def set_numero(self,numero):
        self.__numero=numero
    def get_titular(self):
        return self.__titular
    def set_titular(self,titular):
        self.__titular=titular
    def get_saldo(self):
        return self.__saldo
    def transferir(self,destino,valor):
        destino.__saldo+=valor
        self.__saldo-=valor
        return f'saldo da conta de {self.__titular}:{self.__saldo}\nsaldo da conta de {destino.get_titular()}:{destino.get_saldo()}'
    def get_limite(self):
        return self.__limite
    def set_limite(self,valor):
        self.__limite+=valor
        return f'limite da conta alterado para {self.__limite} reais'
conta1=conta('Pedro',50000,2500)
conta2=conta('André',50350,4000)
#soma=conta.get_saldo(conta1)+conta.get_saldo(conta2)
soma=conta1.get_saldo()+conta2.get_saldo()
print(soma)
print(conta1.extrato())
print(conta2.extrato())
print(conta.contador)
print(conta.transferir(conta1,conta2,500))
#print(f'saldo da conta de {conta1.get_titular()}:{conta1.get_saldo()}')
#print(f'saldo da conta de {conta2.get_titular()}:{conta2.get_saldo()}')
print(conta.set_limite(conta1,500))
print(conta1.set_limite(500000))
print(conta('joão',6000,2200).set_limite(3000))
print(conta.get_titular(conta1))


