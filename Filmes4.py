class Playlist(list):
    def __init__(self,nome,programas):
        super().__init__(programas)
        self.__nome=nome
        #self.__programas=programas
class Programa:
    def __init__(self,nome,ano):
        self.__nome=nome.title()
        self.__ano=ano
        self.__likes=0
    def __str__(self):
        return f'Nome:{self.nome}\n{self.likes}'
    @property
    def likes(self):
        return self.__likes
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
    def __str__(self):
        return f'Nome:{self.nome}\nDuração:{self.detalhes}\nLikes:{self.likes}'
    @property
    def detalhes(self):
        return self.__duracao
    def imprimir(self):
        print(f'{self.nome}\nano:{self.ano}\nduração:{self.detalhes}')
class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.__temporadas=temporadas
    def __str__(self):
        return f'Nome:{self.nome}\nTemporadas:{self.detalhes}\nLikes:{self.likes}'
    @property
    def temporadas(self):
        return self.__temporadas
    @property
    def detalhes(self):
        return self.__temporadas
    def imprimir(self):
        print(f'{self.nome}\nano:{self.ano}\ntemporadas:{self.detalhes}')
vingadores=filme("vingadores",2019,100)
Atlanta=Serie("Atlanta",2015,2)
tmep=filme("todo mundo em pânico",2015,120)
demolidor=Serie("Demolidor",2004,2)
print(vingadores)
print(Atlanta)

Filmes_e_Series=[Atlanta,vingadores,demolidor,tmep]
Playlist1=Playlist("Playlist1",Filmes_e_Series)
print()
print(f'Tamanho da playlist: {len(Playlist1)}')
for programa in Playlist1:
    #print(f'{programa.nome}-{programa.detalhes}-{programa.ano}')
    #programa.imprimir()
    print(programa)
    print()

print(f'O programa demolidor se encontra na posição {Playlist1.index(demolidor)+1} da lista ')
print(demolidor in Playlist1)