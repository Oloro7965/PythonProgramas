class a:
    def __init__(self,nome,idade):
        self.__nome=nome
        self.__idade=idade
class b(a):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
    def cumprimentar(self):
        return f'Olá, meu nome é {self._a__nome} e eu sou produção'
class c(a):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
    def cumprimentar(self):
        return f'Olá, meu nome é {self._a__nome} e eu sou civil'
class d(c,b):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
pessoa=d('Pedro',25)
print(pessoa.cumprimentar())
print(pessoa._a__nome)




