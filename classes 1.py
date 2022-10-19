class pessoa:
    def __init__(self,nome,idade,altura):
        self.__nome=nome
        self.__idade =idade
        self.__altura=altura
        # self.__nome = input('digite o nome ')
        # self.__idade = input('digite a idade ')
        # self.__altura = input('digite a altura ')
    def dados(self):
        return f'{self.__nome} com {self.__idade} anos e {self.__altura:.2f} de altura'
class cliente(pessoa):
    def __init__(self,nome,idade,altura,cpf):
        super().__init__(nome,idade,altura)
        self.__cpf=cpf
class funcionario(pessoa):
    def __init__(self,nome,idade,altura,matricula):
        super().__init__(nome,idade,altura)
        self.__matricula=matricula
    def dados(self):
        return f'funcionário {self.__matricula}-Nome:{self._pessoa__nome}'
user=pessoa('pedro',23,1.90)
#print(cliente.dados(user))
print(user.__dict__)
user1=funcionario('joão',29,1.89,99999)
print(funcionario.dados(user1))