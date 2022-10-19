"""Métodos mágicos
    def __repr__(self):
        return self.__titulo
"""
class moto:
    def __init__(self,marca,modelo,cor,marcha):
        self.__marca=marca
        self.__modelo=modelo
        self.__cor=cor
        self.__marcha=marcha
    def __str__(self):
        self.__marca=str(input('digite a marca '))
        self.__modelo=str(input('digite o modelo '))
        self.__cor=str(input('digite a cor '))
        self.__marcha=int(input('digite a marcha atual '))
        return f'{self.__marca}\n{self.__modelo}\n{self.__cor}\n{self.__marcha}'
    def imprimir(self):
        if self.__marcha==0:
            self.__marcha='neutro'
        if self.__marcha==1:
            self.__marcha='primeira'
        if self.__marcha==2:
            self.__marcha='segunda'
        return f'modelo-{self.__modelo}\nmarca-{self.__marca}\ncor-{self.__cor}\nmarcha-{self.__marcha}'
moto1=moto('','','',0)
print(moto1)




