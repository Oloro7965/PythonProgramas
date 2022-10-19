class pessoa:
    def __init__(self,codigo,nome,idade):
        self.__codigo=codigo
        self.__nome=nome
        self.__idade=idade
        print('Construtor padrão')
    def exibe(self,n=0):
        if n==1:
            print(f'Nome-{self.__nome}\nCódigo-{self.__codigo}\nIdade-{self.__idade}')
        else:
            print(f'Nome-{self.__nome}\nCódigo-{self.__codigo}')
class testapessoa(pessoa):
    pessoa2 = pessoa(28,'joão',29)
    pessoa2.exibe()
    def __init__(self,codigo=193,nome='jon',idade=21):
        super().__init__(codigo,nome,idade)
        self.__codigo=codigo
        self.__nome=nome
        self.__idade=idade
    def instanciar(self):
        self.__nome=input('digite o nome ')
        self.__idade=int(input('digite a idade '))
        self.__codigo=int(input('digite o código '))
        return self.__nome,self.__idade,self.__codigo
    def exibir(self):
        print(f'{self.__nome} {self.__idade} {self.__codigo}')
pessoa1=pessoa(193,'pedro',24)
pessoa1.exibe(1)
pessoa3 = testapessoa()
print(pessoa3.instanciar())
pessoa3.exibir()






