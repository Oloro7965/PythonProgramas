class filme:
    def __init__(self,nome,ano,duracao):
        self.__nome=nome.title()
        self.__ano=ano
        self.__duracao=duracao
        self.__likes=0
    def dar_like(self):
        self.__likes+=1
    @property
    def likes(self):
        return self.__likes
class Serie(filme):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano,duracao)
        self.__temporadas=temporadas
Serie=Serie("efed",2019)
#portão principal(próximo ao bompreço) laudos e exames solicitados, o RG e a carteira do convênio 27/12 as 09:30

