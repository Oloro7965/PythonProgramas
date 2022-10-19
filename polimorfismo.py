class animal(object):
    def __init__(self,nome):
        self.__nome=nome
    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse método')
    def comer(self):
        print(f'{self.__nome} está comendo')
class cachorro(animal):
    def __init__(self,nome):
        super().__init__(nome)
    def falar(self):
        print(f'o {self._animal__nome} está latindo')
class gato(animal):
    def __init__(self,nome):
        super().__init__(nome)
    def falar(self):
       print(f'o {self._animal__nome} está miando')
class rato(animal):
    def __init__(self,nome):
        super().__init__(nome)
    def falar(self):
        print(f'{self._animal__nome} fala algo')
felix=gato('felix')
felix.falar()
felix.comer()
simba=cachorro('simba')
simba.comer()
simba.falar()
mickey=rato('mickey')
mickey.comer()
mickey.falar()


