"""
Manipulando data e hora

import datetime
#inicio=datetime.datetime.now()
#print(inicio)
#replace para alterar horário
nascimento=input('informe a sua data de nascimento ')
nascimento=nascimento.split('/')
nascimento=datetime.datetime(int(nascimento[2]),int(nascimento[1]),int(nascimento[0]))
print(nascimento)
print(nascimento.year)
print(nascimento.day)
"""
import datas
import jsonpickle
#inicio=datas.datas.now()
#print(inicio)
#replace para alterar horário
nascimento=input('informe a sua data de nascimento ')
nascimento=nascimento.split('/')
nascimento=datas.datas(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
with open('datas.pickle','w') as arquivo:
    dados=jsonpickle.encode(nascimento)
    arquivo.write(dados)
with open('datas.pickle','r') as arquivo2:
    arq=arquivo2.read()
    dados1=jsonpickle.decode(arq)
    print(dados1.year)
    print(dados1.month)
    print(dados1.day)