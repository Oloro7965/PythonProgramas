class conta:
    contador=0
    def __init__(self,titular,saldo,limite):
        self.__numero=conta.contador+1
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite
        conta.contador+=1
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self,nome):
        self.__titular=nome
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self,num):
        self.__numero=num
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,saldo_novo):
        self.__saldo=saldo_novo
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self,valor):
        self.__limite=valor
    def extrato(self):
        return f'cliente {self.__numero}: saldo de {self.__saldo:.2f} reais'.replace('.',',')
    def depositar(self,valor):
        self.__saldo+=valor
        return f'saldo de {self.__saldo} reais'
    def retirar(self,valor):
        self.__saldo-=valor
        return f'saldo de {self.__saldo} reais'
    def transferir(self,valor,destino):
        destino.__saldo+=valor
        self.__saldo-=valor
    @property
    def valor_total(self):
        return self.__saldo+self.__limite
conta1 = conta('Pedro', 50000, 2500)
conta2=conta('André',50350,4000)
soma=conta1.saldo+conta2.saldo
print(soma)
print(conta1.limite)
conta1.limite=70000
print(conta1.limite)
print(conta1.valor_total)
print(conta2.valor_total)
#soma=conta.get_saldo(conta1)+conta.get_saldo(conta2)


