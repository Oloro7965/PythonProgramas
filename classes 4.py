class pessoa:
    contador=0
    def __init__(self,nome,sobrenome):
        self.__nome=nome
        self.__sobrenome=sobrenome
        pessoa.contador += 1
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
class funcionario(pessoa):
    def __init__(self,nome,sobrenome,matricula):
        super().__init__(nome,sobrenome)
        self.__matricula=matricula
    @property
    def nome(self):
        return self._pessoa__nome
    @property
    def sobrenome(self):
        return self._pessoa__sobrenome
    @property
    def matricula(self):
        return self.__matricula
    def dados(self):
        return f'{self.nome} {self.sobrenome} - matrícula {self.matricula}'
class estudante(funcionario):
    def __init__(self,nome,sobrenome,matricula,nota):
        super().__init__(nome,sobrenome,matricula)
        self.__nota=nota
pessoa1=pessoa('Pedro','Rômulo')
print(pessoa1.nome_completo())
pessoa2=funcionario('João','Vitor',144151096)
#print(pessoa2.nome)
#print(pessoa2.dados())
print(pessoa2.matricula)
print(pessoa2.nome)
print(pessoa2.dados())


