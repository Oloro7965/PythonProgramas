"""
Pickle
A função do pickle é transformar um objeto python em binário e vice-versa
Esses processos são chamados de serialização e deserialização, respectivamente

simba=cachorro('simba')
civil=gato('civil')
with open('animais.pickle','wb') as arquivo:
    pickle.dump((simba,civil),arquivo)
"""
import pickle
class animal:
    def __init__(self,nome):
        self.__nome=nome
    @property
    def nome(self):
        return self.__nome
    def comer(self):
        print(f'{self.nome} está comendo')
class gato(animal):
    def __init__(self,nome):
        super().__init__(nome)
    def mia(self):
        print(f'{self.nome} está miando')
class cachorro(animal):
    def __init__(self,nome):
        super().__init__(nome)
    def latir(self):
        print(f'{self.nome} está latindo ')
simba=cachorro('simba')
producao=gato('produção')
with open('animais3.pickle','wb') as arquivo:
    pickle.dump((simba,producao),arquivo)
with open('animais3.pickle','rb') as arquivo2:
    cao,gatuno=pickle.load(arquivo2)
    print(f'o nome do cachorro é {cao.nome}')
    cao.latir()
    print(f'o nome do gato é {gatuno.nome}')
    gatuno.mia()
