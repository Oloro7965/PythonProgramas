class Programa:
    def __init__(self,nome,ano):
        self.__nome=nome.title()
        self.__ano=ano
        self.__likes=0
    @property
    def nome(self):
        return self.__nome
    @property
    def ano(self):
        return self.__ano
    def dar_like(self):
        self.__likes+=1
class filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.__duracao=duracao
    @property
    def duracao(self):
        return self.__duracao
    @property
    def likes(self):
        return self.__likes
class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.__temporadas=temporadas
    @property
    def temporadas(self):
        return self.__temporadas
vingadores=filme("vingadores",2019,100)
Atlanta=Serie("Atlanta",2015,2)
Filmes_e_Series=[Atlanta,vingadores]
for programa in Filmes_e_Series:
    detalhes=programa.temporadas if hasattr(programa,'temporadas') else programa.duracao
    print(f'{programa.nome}-{detalhes}-{programa.ano}')