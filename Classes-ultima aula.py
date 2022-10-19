class Funcionario:
    def __init__(self,Nome,idade,salario):
        self.__Nome=Nome
        self.__idade=idade
        self.__salario=salario
    @property
    def nome(self):
        return self.__Nome
    @property
    def idade(self):
        return self.__idade
    @property
    def salario(self):
        return self.__salario
class Alura(Funcionario):
    def __init__(self,Nome,idade,salario):
        super().__init__(Nome,idade,salario)
class Caelum(Funcionario):
    def __init__(self,Nome,idade,salario):
        super().__init__(Nome,idade,salario)
class Junior(Alura):
    def __init__(self,Nome,idade,salario):
        super().__init__(Nome,idade,salario)
class Senior(Alura,Caelum):
    def __init__(self,Nome,idade,salario):
        super().__init__(Nome,idade,salario)
class Pleno(Alura,Caelum):
    def __init__(self, Nome, idade, salario):
        super().__init__(Nome, idade, salario)
pedro=Funcionario("Pedro",24,3000)
print(pedro.nome)
