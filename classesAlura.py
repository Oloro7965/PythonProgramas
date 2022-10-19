class conta:
    def __init__(self,nome,idade,saldo,titular):
        self.__nome=nome
        self.__idade=idade
        self.__saldo=saldo
        self.__titular=titular
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,NomeNovo):
        self.__nome=NomeNovo
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self,IdadeNova):
        self.__idade=IdadeNova
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self,TitularNovo):
        self.__titular=TitularNovo
    def depositar(self,valor):
        self.__saldo+=valor
    def sacar(self,valor):
        self.__saldo-=valor
    def transfere(self,ContaDestino,valor):
        ContaDestino.depositar(valor)
        self.sacar(valor)
    def __str__(self):
        return f'dados da conta :\nNome:{self.nome}\nIdade:{self.idade}\nSaldo:{self.saldo}\nTitular:{self.titular}'
Pedro=conta("Pedro",23,10000,"PedroRc")
print(Pedro)
Joao=conta("Joao",23,2000,"JoaoP")
print(Pedro.nome)
print(Pedro.titular)
#Pedro.titular="Sandro"
#print(Pedro.titular)
print(Pedro.nome)
print(Pedro.saldo)
print(Joao.saldo)
Pedro.transfere(Joao,5000)
print(Pedro.saldo)
print(Joao.saldo)