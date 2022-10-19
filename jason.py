"""
Json-Javascript object notation
API-são meios de comunicação entre os serviços de empresas e terceiros(nós, desenvolvedores)
ret=json.dumps(['produto',{'playstation 4':('2TB',2340)}])
print(type(ret))
print(ret)


import json
class gato:
    def __init__(self,nome,raca):
        self.__nome=nome
        self.__raca=raca
    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca

g=gato('felix','viralata')
ret=json.dumps(g.__dic
"""
import pickle
class gato:
    def __init__(self,nome,raca):
        self.__nome=nome
        self.__raca=raca
    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca
g=gato('felix','viralata')
g2=gato('simba','civil')
with open('animais2.pickle','wb') as arquivo:
    ret=pickle.dump((g,g2),arquivo)
with open('animais2.pickle','rb') as arquivo2:
    ret1,ret2=pickle.load(arquivo2)
    print(ret1)
    print(ret1.nome)
    print(ret2)
    print(ret2.nome)







