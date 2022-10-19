"""Métodos mágicos
    def __repr__(self):
        return self.__titulo
"""
class livro:
    def __init__(self,autor,titulo,paginas):
        self.__autor=autor
        self.__titulo=titulo
        self.__paginas=paginas
    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'
    def __str__(self):
        return self.__titulo
    def __len__(self):
        return self.__paginas
    def __add__(self, other):
        return f'{self}-{other}'
    def __del__(self):
        print('um objeto livro foi deletado da memória')
livro1=livro('Pedro','a arte de ser civil',254)
livro2=livro('joão','grande vai mamar',46)
print(livro1)
print(livro2)
print(len(livro1))
print(len(livro2))
print(livro1+livro2)




